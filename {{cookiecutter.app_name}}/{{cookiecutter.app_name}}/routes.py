# -*- coding: utf-8 -*-
from bottle import Bottle

from .controllers.home import home_app
from .controllers.user import user_app


Routes = Bottle()
# App to render / (home)
Routes.merge(home_app)
# Mount other applications
Routes.mount("/user", user_app)
