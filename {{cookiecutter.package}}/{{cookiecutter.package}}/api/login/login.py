"""Login Api"""
from . import login
from flask import request

from {{cookiecutter.package}}.database.database import Database
from {{cookiecutter.package}}.utils.response import send_response
from {{cookiecutter.package}}.utils.exceptions import BadRequest
from {{cookiecutter.package}}.utils.exceptions import ResourceNotFound


@login.route('/login', methods=['GET'])
def _login():
    """Login"""
    from server import logger
    logger.info("Running _login")
    logger.info("Request {}".format(request.args.to_dict()))
    bag = {
        "query_params": request.args.to_dict(),
        "response_body": {},
    }

    validate_query_params(bag)
    db = Database()
    cursor, conn = db.connect()
    sql = """select email, id, name, phone from user where email='{}'
        and password='{}'
        """.format(
        request.args['email'], request.args['password']
    )
    cursor.execute(sql)
    data = cursor.fetchone()
    db.close()
    if not data:
        raise ResourceNotFound()

    return send_response(data)


def validate_query_params(bag):
    """
    Validate query params

    :param bag:
    """
    query_params = bag.get('query_params')
    response_body = bag.get('response_body', {})
    email = query_params.get('email', None)
    password = query_params.get('password', None)

    if not email:
        response_body['email'] = "Email Id not found"

    if not password:
        response_body['password'] = "Password not found"

    if response_body:
        raise BadRequest(response_body)
