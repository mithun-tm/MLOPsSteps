#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Mithun T M",
    author_email='mithuntm@alumni.iitm.ac.in',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Steps in MLOPs ",
    entry_points={
        'console_scripts': [
            'src=src.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='src',
    name='src',
    packages=find_packages(include=['src', 'src.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mithun-tm/src',
    version='0.1.0',
    zip_safe=False,
)
