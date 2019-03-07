#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from codecs import open
from pathlib import Path
import re

from setuptools import setup, find_packages


with open('tensorflow_2/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

here = Path(__file__).absolute().parent
with open(here / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tensorflow_2',
    version=version,
    description='Modules related to EnterDescriptionHere',
    author='EnterAuthorName',
    author_email='EnterAuthorEmail',
    license='BSD',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
        ],
    keywords='EnterKeywordsHere',
    packages=find_packages(exclude=[
        'data',
        'docker',
        'docs',
        'notebooks',
        'wheels',
        '*tests',
        ]
    ),
    install_requires=[
        'click',
        ],
    extras_require={
        'build': ['setuptools', 'wheel'],
        'data': ['cufflinks', 'matplotlib', 'pandas'],
        'database': ['psycopg2', 'sqlalchemy'],
        'docs': ['sphinx', 'sphinx_rtd_theme'],
        'notebook': ['jupyter', 'jupyterlab'],
        'profile': ['memory_profiler', 'snakeviz'],
        'test': ['pytest', 'pytest-pep8'],
        },
    package_dir={'tensorflow_2': 'tensorflow_2'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'count=tensorflow_2.cli:count',
        ]
    }
)


if __name__ == '__main__':
    pass
