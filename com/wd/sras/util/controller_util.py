from flask import abort, make_response, jsonify


def abort_json(error, code):
    return abort(make_response(jsonify(error=error), code))
