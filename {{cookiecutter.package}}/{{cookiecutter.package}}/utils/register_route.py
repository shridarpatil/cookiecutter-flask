#!/bin/python
# -*- coding: utf-8 -*-

"""Bitcoin Price Trigers."""
from {{cookiecutter.package}}.api.login.login import login
from {{cookiecutter.package}}.api.registration.registration import registration


def register_routes(app):
    """Register Routes"""
    app.register_blueprint(login)
    app.register_blueprint(registration)
