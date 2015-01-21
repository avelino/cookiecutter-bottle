# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_template as template, redirect
from bottle.ext import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..models import engine
from ..models.entities import User


# Example application
example_app = Bottle()

# Bottle Plugin
SQLAlchemyBase = declarative_base()
create_session = sessionmaker(bind=engine)
SQLAlchemyBase.metadata.create_all(engine)
plugin = sqlalchemy.Plugin(
    engine,
    SQLAlchemyBase.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False,
    create_session=create_session
)
example_app.install(plugin)


@example_app.route('/')
def index(db):
    users = db.query(User)
    return template("example.html", var="123", users=users)


@example_app.route('/add')
def add(db):
    db.add(User("bottle", fullname="Bottle web framework", password=123))
    redirect("/example/")
