#!/bin/python
# -*- coding: utf-8 -*-

"""{{cookiecutter.repo_name}} Server."""
import os

from flask import Flask
from flask import jsonify
from flask import request

from {{cookiecutter.repo_name}}.logger.logger import get_logger
from {{cookiecutter.repo_name}}.utils.exceptions import BadRequest
from {{cookiecutter.repo_name}}.utils.exceptions import ResourceNotFound
from {{cookiecutter.repo_name}}.utils.exceptions import AccessDenied
from {{cookiecutter.repo_name}}.utils.exceptions import ServerError
from {{cookiecutter.repo_name}}.utils.exceptions import DuplicateEntry

from {{cookiecutter.repo_name}}.utils.log_client import LogClient
from {{cookiecutter.repo_name}}.utils.register_route import register_routes
from {{cookiecutter.repo_name}}.utils.validate_token import validate_token
from {{cookiecutter.repo_name}}.utils.generate_token import generate_token


logger = get_logger()

app = Flask(__name__)

register_routes(app)


@app.errorhandler(AccessDenied)
def access_denied(error):
    """Handle Error."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(BadRequest)
def bad_request(error):
    """Handle Error."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(ResourceNotFound)
def resource_not_found(error):
    """Handle Error."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(DuplicateEntry)
def duplicate_entry(error):
    """Handle Error."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 error."""
    return jsonify({
        'message': 'This page does not exist',
        'status': 'Error',
        'success': False,
        'data': []
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 404 error."""
    return jsonify({
        'message': 'Method Not Allowed',
        'status': 'Error',
        'success': False,
        'data': []
    }), 405


@app.errorhandler(ServerError)
def server_error(error):
    """Handle 404 error."""
    return jsonify({
        'message': 'Server Error',
        'status': 'Error',
        'success': False,
        'data': []
    }), 500


@app.before_request
def before_request():
    """Log client Details."""
    LogClient(request)
    try:
        endpoint = request.endpoint

        if ['login', 'registration'] not in endpoint:
            token = request.headers.get('token')
            validate_token(token)
    except Exception:
        pass

        # validate_roles(token, endpoint)


@app.after_request
def after_request(response):
    """Add token to response headers."""
    status = response.status
    if status[0] == '2':
        # new_token = generate_token()
        token = request.headers.get('token', generate_token())

        # update_token(cursor, connection, token, new_token)
        response.headers["token"] = token

    return response


if __name__ == "__main__":
    app.run(
        debug=os.getenv("debug_mode", False),
        port=os.getenv("port", 60003),
        host='127.0.1.1'
    )
