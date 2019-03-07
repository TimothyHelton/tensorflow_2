#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Database Module

"""
import os

import pandas as pd
import sqlalchemy as sa
from sqlalchemy.sql import select

from .utils import format_logger, project_vars


logger = format_logger


class Connect:
    """
    Database Connection Class

    :Attributes:

    - **conn**: *Connection* SQLAlchemy connection object
    - **db_name**: *str* database name
    - **dialect**: *str* SQLAlchemy dialect
    - **driver**: *str* SQLAlchemy driver \
        (if None the default value will be used)
    - **engine**: *Engine* SQLAlchemy engine object
    - **host**: *str* database host
    - **meta**: *MetaData* A collection of *Table* objects and their \
        associated child objects
    - **password**: *str* database password
    - **port**: *int* database port
    - **tables**: *list* tables in database
    - **user**: *str* username
    """
    def __init__(self):
        project_vars()
        self.dialect = 'postgresql'
        self.driver = None
        self.db_name = os.environ['POSTGRES_DB']
        self.host = 'tensorflow_2_postgres'
        self.meta = sa.MetaData()
        self.password = os.environ['POSTGRES_PASSWORD']
        self.port = 5432
        self.user = os.environ['POSTGRES_USER']

        self.dialect = (f'{self.dialect}+{self.driver}' if self.driver
                        else self.dialect)
        self.engine = sa.create_engine(
            f'{self.dialect}://{self.user}:{self.password}'
            f'@{self.host}:{self.port}/{self.db_name}'
        )
        self.conn = self.engine.connect()
        self.tables = self.engine.table_names()

    def __repr__(self) -> str:
        return (f'<{type(self).__name__}('
                f'user={os.environ["POSTGRES_USER"]}, '
                f'database={os.environ["POSTGRES_DB"]}'
                f')')


class User(Connect):
    """
    User Tables

    :Attributes:

    - **df**: *DataFrame* table with all user data
    - **user_df**: *DataFrame* table with base user information
    - **pref_df**: *DataFrame* table with user preferences
    """
    def __init__(self):
        super(User, self).__init__()
        self._user = sa.Table(
            'user', self.meta,
            sa.Column('user_id', sa.Integer, primary_key=True),
            sa.Column('User_name', sa.String(16), nullable=False),
            sa.Column('email_address', sa.String(60), key='email'),
            sa.Column('password', sa.String(20), nullable=False)
        )
        self._pref = sa.Table(
            'user_pref', self.meta,
            sa.Column('pref_id', sa.Integer, primary_key=True),
            sa.Column('user_id', sa.Integer, sa.ForeignKey("user.user_id"),
                      nullable=False),
            sa.Column('pref_name', sa.String(40), nullable=False),
            sa.Column('pref_value', sa.String(100))
        )
        self.meta.create_all(self.engine)
        
        self._user_df = pd.read_sql(select([self._user]), self.engine)
        self._pref_df = pd.read_sql(select([self._pref]), self.engine)

    @property
    def df(self):
        return pd.merge(self._user_df, self._pref_df, on='user_id')

    @property
    def pref_df(self):
        return self._pref_df

    @property
    def user_df(self):
        return self._user_df


if __name__ == '__main__':
    pass
