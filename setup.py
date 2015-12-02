#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'docopt'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pygrade',
    version='0.1.0',
    description="auto-grade python assignments",
    long_description=readme + '\n\n' + history,
    author="Aron Culotta",
    author_email='aronwc@gmail.com',
    url='https://github.com/aronwc/pygrade',
    packages=[
        'pygrade',
    ],
    package_dir={'pygrade':
                 'pygrade'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pygrade',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'pygrade = pygrade.pygrade:main',
            'pygrade-grade = pygrade.grade:main',
            'pygrade-cheat = pygrade.cheat:main',
        ],
    },
    test_suite='tests',
    tests_require=test_requirements
)