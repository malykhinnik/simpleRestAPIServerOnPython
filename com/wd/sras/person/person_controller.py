from com.wd.sras.person import person_service
from com.wd.sras.person.person_entity import PersonJSONEncoder, Person
from com.wd.sras.util import controller_util
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
app.json_encoder = PersonJSONEncoder


@app.route('/api/persons', methods=['GET'])
def get_persons():
    return make_response(jsonify(person_service.get_persons()), 200)


@app.route('/api/persons/<person_id>', methods=['GET'])
def get_person(person_id):
    person = person_service.get_person(person_id)
    if person is not None:
        return make_response(jsonify(person), 200)
    else:
        return controller_util.abort_json("Person with ID {id} not found".format(id=person_id), 404)


@app.route('/api/persons', methods=['POST'])
def create_person():
    json = request.get_json()
    return make_response(jsonify(person_service.create_person(Person(json['name'], json['age']))), 200)


@app.route('/api/persons/<person_id>', methods=['PUT'])
def update_person(person_id):
    request_person = request.get_json()
    return make_response(
        jsonify(person_service.update_person(person_id, Person(request_person['name'], request_person['age']))), 200)


@app.route('/api/persons/<person_id>', methods=['DELETE'])
def delete(person_id):
    person_service.delete(person_id)
    return make_response(jsonify(), 200)
