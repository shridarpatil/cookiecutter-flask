#!/bin/python
# -*- coding: utf-8 -*-

"""Generate token and update user token."""
from bitcoin.database.database import Database
from bitcoin.utils.exceptions import ServerError
from bitcoin.utils.unique_id import get_uuid
from flask import request


def generate_token():
    """Validate Token"""
    try:
        args = request.args.to_dict()
        email = args['email']
        token = get_uuid()
        query = """
                UPDATE `user` set token='{}' where email='{}'
            """.format(token, email)
        db = Database()
        cursor, conn = db.connect()

        cursor.execute(query)
        conn.commit()
    except Exception as e:
        raise ServerError(e.message)
    else:
        return token
