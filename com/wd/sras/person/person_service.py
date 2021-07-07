from com.wd.sras.person import person_repository, person_entity
from com.wd.sras.person.person_entity import Person
from com.wd.sras.util import controller_util


def __check_person_exist(person_id: int):
    if person_repository.exist(person_id)[0] is 0:
        controller_util.abort_json("Person with ID {id} not found".format(id=person_id), 404)


def create_person(person: Person):
    person_entity.validate_person_fields(person)
    return person_entity.tuple_to_entity(person_repository.create(person.name, person.age))


def get_persons():
    persons = person_repository.get_all()
    response = []
    for person in persons:
        response.append(person_entity.tuple_to_entity(person))
    return response


def get_person(person_id: int):
    return person_entity.tuple_to_entity(person_repository.get(person_id))


def update_person(person_id: int, person: Person):
    person_entity.validate_person_fields(person)
    __check_person_exist(person_id)
    return person_entity.tuple_to_entity(person_repository.update(person_id, person.name, person.age))


def delete(person_id: int):
    __check_person_exist(person_id)
    person_repository.delete(person_id)
