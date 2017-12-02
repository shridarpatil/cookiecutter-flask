#!/bin/python
# -*- coding: utf-8 -*-

"""Respponse"""
from flask import jsonify


def send_exception_response(
    payload, message, success=False, response_type='Error'
):
    """
    Send Exception response

    :param payload: response data
    :param messae: response message
    :param success: response success status
    :param response_type: response type valid optioons success or error
    """
    response = dict(payload or ())
    response['data'] = []
    response['message'] = message
    response['success'] = success
    response['type'] = response_type
    return response


def send_response(
    data=[], message='Success', success=True,
    response_type='Success', payload=None, status_code=200
):
    """
    Send Exception response

    :param payload: response data
    :param messae: response message
    :param success: response success status
    :param response_type: response type valid optioons success or error
    """
    response = dict(payload or ())
    response['data'] = data
    response['message'] = message
    response['success'] = success
    response['type'] = response_type
    return jsonify(response), status_code
