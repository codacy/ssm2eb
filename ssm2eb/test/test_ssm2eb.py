import pytest
from moto import mock_ssm
from .. import ssm2eb
from botocore.exceptions import ClientError


mock = mock_ssm()

setup_data = [
    {'option_name': 'VARIABLE_1', 'path': '/application/VARIABLE_1',
     'value': 'value_1', 'required': True},
    {'option_name': 'VARIABLE_2', 'path': '/application/VARIABLE_2',
     'value': 'value_2', 'required': False, 'environment': 'codacy'}
]


def _create_param(param):
    full_path = param['path']
    if 'environment' in param:
        full_path = '/' + param['environment'] + param['path']
    print(full_path)
    ssm2eb.SSM_CLIENT.put_parameter(
        Name=full_path, Description="dummy description", Value=param["value"], Type="String", Overwrite=True)


def setup_module():
    """ setup any state specific to the execution of the given module."""
    mock.start()
    for t in setup_data:
        _create_param(t)


required_testdata = [
    ({'option_name': 'VARIABLE_1', 'path': '/application/VARIABLE_1',
      'required': True}, '', "value_1"),
    ({'option_name': 'VARIABLE_2', 'path': '/application/VARIABLE_2',
      'required': True}, 'codacy', "value_2"),
]


@pytest.mark.parametrize("parameter,env,expected", required_testdata)
def test_get_required_ssm_data(parameter, env, expected):
    output = ssm2eb.get_ssm_data(parameter, env)
    assert output['value'] == expected


non_existent_testdata = [
    ({'option_name': 'UNEXSITENT_VARIABLE_2', 'path': '/application/UNEXSITENT_VARIABLE',
      'required': True}, '', pytest.raises(ClientError)),
]


@pytest.mark.parametrize("parameter,env,expected", non_existent_testdata)
def test_get_non_existent_ssm_data(parameter, env, expected):
    with expected:
        ssm2eb.get_ssm_data(parameter, env)


non_required_testdata = [
    ({'option_name': 'UNEXSITENT_VARIABLE_1', 'path': '/application/VARIABLE_2',
      'required': False}, ''),
]


@pytest.mark.parametrize("parameter,env", non_required_testdata)
def test_get_non_required_ssm_data(parameter, env):
    output = ssm2eb.get_ssm_data(parameter, env)
    assert output is None


def test_get_data():
    test_dict = dict(winter="coming")
    assert isinstance(ssm2eb.get_data("fall", test_dict), list)
    assert ssm2eb.get_data("winter", test_dict) is "coming"
    assert ssm2eb.get_data("summer", test_dict, "warm") is "warm"



