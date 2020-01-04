#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from codecs import open
from pathlib import Path
from operator import itemgetter
import re
from typing import Iterable, List, Union

from setuptools import setup, find_packages


dependencies = {
    'build': {
        'setuptools',
        'wheel',
    },
    'docs': {
        'sphinx',
        'sphinx_rtd_theme',
    },
    'jupyter': {
        'jupyter',
        'jupyterlab',
    },
    'profile': {
        'memory_profiler',
        'snakeviz',
    },
    'test': {
        'Faker',
        'git-lint',
        'pytest',
        'pytest-cov',
        'pytest-pep8',
    },
}


def combine_dependencies(extras: Union[str, Iterable[str]]) -> List[str]:
    """
    Combine package dependencies.

    :param extras: key(s) from the `dependencies` dictionary
    :return: The minimum set of package dependencies contained in `extras`.
    """
    if isinstance(extras, str):
        deps = set(itemgetter(extras)(dependencies))
    else:
        deps = set().union(*itemgetter(*extras)(dependencies))
    return list(deps)


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
    keywords='TensorFlow, Training',
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
        'matplotlib',
        'numpy',
        'plotly',
    ],
    extras_require={
        'all': combine_dependencies(dependencies.keys()),
        'build': combine_dependencies(('build', 'test')),
        'docs': combine_dependencies('docs'),
        'jupyter': combine_dependencies('jupyter'),
        'profile': combine_dependencies('profile'),
        'test': combine_dependencies('test'),
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
