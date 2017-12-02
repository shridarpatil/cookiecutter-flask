#!/bin/python
# -*- coding: utf-8 -*-

"""Bitcoin Price Trigers."""
from bitcoin.api.login.login import login
from bitcoin.api.registration.registration import registration


def register_routes(app):
    """Register Routes"""
    app.register_blueprint(login)
    app.register_blueprint(registration)
