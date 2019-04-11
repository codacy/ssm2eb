
#!/usr/bin/env python
import codecs

from setuptools import setup, find_packages

dependencies = ['boto3>=1.9.75', 'PyYAML>=3.13']

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


setup(
    name='ssm2eb',
    version=open('VERSION').read(),
    description='A simple tool to get ssm parameters to an .ebextensions file',
    long_description=open('README.rst').read(),
    url='https://github.com/codacy/ssm2eb',
    author='Codacy',
    author_email='team@codacy.com',
    scripts=['bin/ssm2eb'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    install_requires=dependencies,
    include_package_data=True
)