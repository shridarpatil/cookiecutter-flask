#!/bin/python
# -*- coding: utf-8 -*-

"""Registration Api"""
import pymysql

from . import registration
from flask import request

from bitcoin.database.database import Database
from bitcoin.utils.response import send_response
from bitcoin.utils.exceptions import BadRequest
from bitcoin.utils.exceptions import DuplicateEntry
from bitcoin.utils.unique_id import get_uuid


@registration.route('/registration', methods=['POST'])
def _registration():
    """Register"""
    from server import logger
    bag = {
        'request_body': request.get_json(),
        'response_body': {},
    }

    logger.info(bag)
    request_body = bag.get('request_body')
    validate_request_body(bag)
    _id = get_uuid()
    db = Database()
    try:
        cursor, conn = db.connect()
        cursor.execute(
            """insert into user(id, email, name, password, phone)
            values(%s, %s, %s, %s, %s)""",
            (
                _id, request_body['email'],
                request_body['name'], request_body['password'],
                request_body['phone']
            )
        )
    except pymysql.err.IntegrityError as e:
        logger.error(e)
        raise DuplicateEntry
    else:
        pass

    return send_response(
        data={'id': _id},
        message='Resource Created Successfully',
        status_code=201
    )


def validate_request_body(bag):
    """Validate request data"""
    request_body = bag.get('request_body')
    response_body = bag.get('response_body')

    if not request_body.get('name'):
        response_body['name'] = 'No Name'

    if not request_body.get('email'):
        response_body['email'] = 'No email'

    if not request_body.get('password'):
        response_body['password'] = 'No password'

    if not request_body.get('phone'):
        response_body['phone'] = 'No phone'

    if response_body:
        raise BadRequest(response_body)
