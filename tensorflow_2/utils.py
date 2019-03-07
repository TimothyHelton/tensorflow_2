#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Package Utilities

"""
import logging
import os
from pathlib import Path
import re


def format_logger() -> logging.Logger:
    """Format the logger."""
    log_format = ('%(asctime)s  %(levelname)8s  -> %(name)s <- '
                  '(line: %(lineno)d) %(message)s\n')
    date_format = '%m/%d/%Y %I:%M:%S'
    logging.basicConfig(format=log_format, datefmt=date_format,
                        level=logging.INFO)
    return logging.getLogger(__name__)


def package_dir() -> Path:
    """Return package root directory."""
    return Path(__file__).parents[1]


def project_vars():
    """Load project specific environment variables."""
    with open(Path('envfile'), 'r') as f:
        txt = f.read()
    env_vars = re.findall(r'export\s(.*)=(.*)', txt)
    for name, value in env_vars:
        os.environ[name] = value


if __name__ == '__main__':
    pass

