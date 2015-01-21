# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_template as template, redirect, HTTPError
from bottle.ext import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker

from ..models import engine
from ..models.users import User


# User application
user_app = Bottle()

# Bottle Plugin
SQLAlchemyBase = declarative_base()
SQLAlchemyBase.metadata.create_all(engine)
plugin = sqlalchemy.Plugin(
    engine,
    SQLAlchemyBase.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)
user_app.install(plugin)


@user_app.route('/')
def index(db):
    users = db.query(User)
    return template("user.html", users=users)


@user_app.route('/:name')
def user(db, name):
    user = db.query(User).filter_by(name=name).first()
    if user:
        return template("user_view.html", user=user)
    return HTTPError(404, 'User not found.')


@user_app.route('/add')
def add(db):
    fake = Faker()
    db.add(User(fake.user_name(), fullname=fake.name(), password=fake.sha1()))
    redirect("/user/")
