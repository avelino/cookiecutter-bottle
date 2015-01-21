# -*- coding: utf-8 -*-
from sqlalchemy import create_engine


engine = create_engine('sqlite:///:memory:', echo=True)
