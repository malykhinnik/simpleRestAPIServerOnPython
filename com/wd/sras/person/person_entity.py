from com.wd.sras.util import controller_util
from flask.json import JSONEncoder


class Person:
    def __init__(self, name, age, id=None):
        self.name = name
        self.age = age
        self.id = id


class PersonJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {
                'id': obj.id,
                'name': obj.name,
                'age': obj.age,
            }
        return super(PersonJSONEncoder, self).default(obj)


def validate_person_fields(person: Person):
    if person is None:
        controller_util.abort_json("Person is required", 400)
    elif person.name is None:
        controller_util.abort_json("Person name is required", 400)
    elif person.age is None:
        controller_util.abort_json("Person age is required", 400)


def tuple_to_entity(person):
    if person is not None:
        return Person(person[0], person[1], person[2])
    else:
        return None
