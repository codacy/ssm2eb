.. image:: https://api.codacy.com/project/badge/Grade/f557a65b337b45a5977533f6ba82492b
   :target: https://www.codacy.com?utm_source=github.com&utm_medium=referral&utm_content=codacy/ssm2eb&utm_campaign=Badge_Grade

.. image:: https://circleci.com/gh/codacy/ssm2eb.svg?style=svg&circle-token=58eb00693898fe2f4d7d7e475d3d7eeb0bf60c16
    :target: https://circleci.com/gh/codacy/ssm2eb

.. image:: https://pypip.in/v/ssm2eb/badge.svg
    :target: https://pypi.org/project/ssm2eb/
    :alt: Latest PyPI version

======
SSM2EB
======

A simple tool to get ssm parameters to an .ebextensions file.

-----
Usage
-----

Create a template like the one in `<example/template.yaml>`_.

^^^^^^^^^^^^^^^^^^^^^^^^
Example:
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ ssm2eb -i example/template.yaml -o .ebextensions/env_variables.config

^^^^^^^^^^^^^^^^^^^^^^^^
Help:
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ ssm2eb -h
    usage: ssm2eb [-h] [--input INPUT] [--output OUTPUT]
    [--environment ENV] [--mode {set,get}]

    Get or set SSM parameters and generate environment variables file for
    ebextensions

    optional arguments:
      -h, --help            show this help message and exit
      --input INPUT, -i INPUT
                            input template environment variables config
      --output OUTPUT, -o OUTPUT
                            input template environment variables config
      --environment ENV, -e ENV
                            environment name used as prefix for the
                            ssm parameters (e.g. codacy)
      --mode {set,get}, -m {set,get}
                            enable set or get mode (default is get)
    usage: ssm2eb [-h] [--input INPUT] [--output OUTPUT]
    [--environment ENV] [--mode {set,get}]

---------------
What is Codacy?
---------------

`Codacy <https://www.codacy.com/>`__ is an Automated Code Review Tool
that monitors your technical debt, helps you improve your code quality,
teaches best practices to your developers, and helps you save time in
Code Reviews.

^^^^^^^^^^^^^^^^^^^^^^^^
Among Codacy’s features:
^^^^^^^^^^^^^^^^^^^^^^^^

-  Identify new Static Analysis issues
-  Commit and Pull Request Analysis with GitHub, BitBucket/Stash, GitLab
   (and also direct git repositories)
-  Auto-comments on Commits and Pull Requests
-  Integrations with Slack, HipChat, Jira, YouTrack
-  Track issues in Code Style, Security, Error Proneness, Performance,
   Unused Code and other categories

Codacy also helps keep track of Code Coverage, Code Duplication, and
Code Complexity.

Codacy supports PHP, Python, Ruby, Java, JavaScript, and Scala, among
others.

^^^^^^^^^^^^^^^^^^^^
Free for Open Source
^^^^^^^^^^^^^^^^^^^^


Codacy is free for Open Source projects.
