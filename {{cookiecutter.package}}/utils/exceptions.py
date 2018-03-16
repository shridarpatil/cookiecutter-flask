#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Exceptions to be raised by every other sub-package"""

__all__ = ['{{cookiecutter.package}}Exception', 'ResourceNotFound']


class {{cookiecutter.package}}BaseException(Exception):
    """Base exception for crux utils."""

    pass


class ResourceNotFound({{cookiecutter.package}}BaseException):
    """Resource not found exception"""

    def __init__(
        self, message='Resource Not Found', status_code=404, payload=None
    ):
        """Initialise."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """To dict."""
        response = dict(self.payload or ())
        response['message'] = self.message
        response['success'] = False
        response['type'] = 'Error'
        response['data'] = ''
        return response


class DuplicateEntry({{cookiecutter.package}}BaseException):
    """Mysql DuplicateEntry Error"""

    def __init__(
        self, message='Duplicate Entry', status_code=409, payload=None
    ):
        """Initialise."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """To dict."""
        response = dict(self.payload or ())
        response['message'] = self.message
        response['success'] = False
        response['type'] = 'Warning'
        response['data'] = ''
        return response


class BadRequest(Exception):
    """Invalid Usage."""

    def __init__(
        self, message='Bad Request', status_code=400, payload=None
    ):
        """Initialise."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """To dict."""
        response = dict(self.payload or ())
        response['message'] = self.message
        response['success'] = False
        response['type'] = 'Error'
        response['data'] = ''
        return response


class AccessDenied(Exception):
    """Invalid Usage."""

    def __init__(
        self, message='Access Denied', status_code=403, payload=None
    ):
        """Initialise."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """To dict."""
        response = dict(self.payload or ())
        response['message'] = self.message
        response['success'] = False
        response['type'] = 'Error'
        response['data'] = ''
        return response


class ServerError(Exception):
    """Invalid Usage."""

    def __init__(
        self, message='Server Error', status_code=500, payload=None
    ):
        """Initialise."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """To dict."""
        response = dict(self.payload or ())
        response['message'] = self.message
        response['success'] = False
        response['type'] = 'Error'
        response['data'] = ''
        return response
