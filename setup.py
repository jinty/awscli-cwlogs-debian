#!/usr/bin/env python
import sys
from setuptools import setup, find_packages, Command
import cwlogs

requires = ['awscli==1.7.27',
            'six>=1.1.0',
            'python-dateutil>=2.1']

cmdclass = dict()
try:
    import cwlogs_setup_targets
    cmdclass = cwlogs_setup_targets.cmdclass
except:
    pass

setup(
    name='awscli-cwlogs',
    version=cwlogs.__version__,
    description='AWSCLI CloudWatch Logs plugin',
    long_description=open('README.rst').read(),
    author='Amazon',
    url='http://aws.amazon.com/cli/',
    packages=find_packages('.', exclude=['tests*']),
    package_dir={'cwlogs': 'cwlogs'},
    package_data={'cwlogs': ['examples/*/*.rst',
                             'examples/*/*/*.rst']},
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
    cmdclass=cmdclass,
)