#!/usr/bin/env python3

import sys
import argparse
import yaml
import boto3

SSM_CLIENT = boto3.client('ssm')


def get_ssm_data(parameter, env):
    """ Get data for placeholder variable from SSM

    :param parameter: parameter dictionary with "option_name" and "path"
    :param env: environment name to be prepended to the
    :return: dictionary with the "parameter_name" and "value" obtained from SSM

    """
    name = parameter["option_name"]
    required = True
    if "required" in parameter:
        if parameter["required"] in [True, False]:
            required = parameter["required"]
        else:
            print("ERROR: \"required\" for '%s' should be \"true\" or \"false\". Falling back to default (true)" %
                  name, file=sys.stderr)

    path = "/%s%s" % (env, parameter["path"]) if env else parameter["path"]

    print("Getting '%s'..." % path, file=sys.stderr, end='', flush=True)
    try:
        response = SSM_CLIENT.get_parameter(Name=path)
        value = response["Parameter"]["Value"]
        print("OK", file=sys.stderr)
        return dict(option_name=name, value=value)
    except SSM_CLIENT.exceptions.ParameterNotFound as e:
        if required:
            raise e
        else:
            print("NON REQUIRED, NOT FOUND IN SSM. SKIPPING", file=sys.stderr)
    return None


def set_ssm_data(parameter, env):
    """ Set SSM parameter

    If type is not set then it is assumed to be a string.
    If value is not set then it is read form stdin


    :param parameter: parameter dictionary with "path", "name", and parameterally "type" and value"
    :param env: environment name to be prepended to the
    :return: response from ssm

    """

    path = "/%s%s" % (env, parameter["path"]) if env else parameter["path"]
    desc = parameter["option_name"].replace("_", "").lower(
    ) if "description" not in parameter else parameter["description"]
    typ = "String" if "type" not in parameter else parameter["type"]
    value = input("Input value for '%s' (%s):" %
                  (desc, path)) if "value" not in parameter else parameter["value"]
    if not value:
        print("Skipping...")
    else:
        print("Setting '%s'..." % path, file=sys.stderr)
        response = SSM_CLIENT.put_parameter(
            Name=path, Description=desc, Value=value, Type=typ, Overwrite=True)
        print(response)
        return response

def get_data(key, data, default=list()):
    """ Safely get the value of a key

    :param key: key to the data of interest
    :param data: dictionary holding the data
    :param default: what to return if the key is missing or empty
    :return: the value for `key` of default
    """

    if key in data:
        if data[key] is None:
            return default
        else:
            return data[key]
    else:
        return default


def main():
    parser = argparse.ArgumentParser(
        description='Get or set SSM parameters and generate environment \
                     variables file for ebextensions')
    parser.add_argument('--input', '-i', dest='input',
                        help='input template environment variables config')
    parser.add_argument('--output', '-o', dest='output',
                        help='input template environment variables config')
    parser.add_argument('--environment', '-e', dest='env',
                        help='environment name used as prefix for the ssm parameters (e.g. codacy)')
    parser.add_argument('--mode', '-m', dest='mode', default='get', choices=['set', 'get'],
                        help='enable set or get mode (default is get)')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if not args.input:
        print("Missing mandatory argument: `--input / -i`")
        sys.exit(1)

    template_data = yaml.load(open(args.input, 'r'))
    config_data = dict(option_settings=list())

    if args.mode == 'get':
        for par in get_data("component", template_data) + get_data("external", template_data):
            try:
                param = get_ssm_data(par, args.env)
                if param:
                    config_data["option_settings"].append(param)
            except SSM_CLIENT.exceptions.ParameterNotFound:
                print("ERROR: REQUIRED PARAMETER NOT FOUND IN SSM", file=sys.stderr)
                sys.exit(1)

        if len(config_data["option_settings"]) > 0:
            if args.output:
                yaml.dump(config_data, open(args.output, 'w'),
                          default_flow_style=False)
            else:
                yaml.dump(config_data, sys.stdout, default_flow_style=False)

    elif args.mode == 'set':
        for par in get_data("component", template_data):
            set_ssm_data(par, args.env)

if __name__ == '__main__':
    main()
