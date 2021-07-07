from com.wd.sras.person import person_repository, person_service
from com.wd.sras.person.person_entity import Person
import unittest


class PersonServiceCrudTestCase(unittest.TestCase):
    testPerson1 = None
    testPerson2 = None

    def setUp(self):
        person_repository.Constant.db_name = ":memory:"
        person_repository.init()

    def test_1_create_person(self):
        request = Person("TestPerson1", 18)
        response = person_service.create_person(request)
        self.assertEqual(request.name, response.name)
        self.assertEqual(request.age, response.age)
        self.assertIsNotNone(response.id)
        PersonServiceCrudTestCase.testPerson1 = response

    def test_2_get_person(self):
        response = person_service.get_person(PersonServiceCrudTestCase.testPerson1.id)
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.id, response.id)
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.name, response.name)
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.age, response.age)
        self.assertIsNone(person_service.get_person(PersonServiceCrudTestCase.testPerson1.id + 100))

    def test_3_get_persons(self):
        response = person_service.get_persons()
        self.assertEqual(1, response.__len__())
        person_service.create_person(Person("TestPerson2", 21))
        response = person_service.get_persons()
        self.assertEqual(2, response.__len__())
        r = response[1]
        PersonServiceCrudTestCase.testPerson2 = r

    def test_4_update_person(self):
        PersonServiceCrudTestCase.testPerson1.name = "UpdatedTestPerson1"
        PersonServiceCrudTestCase.testPerson1.age = 19
        response = person_service.update_person(PersonServiceCrudTestCase.testPerson1.id,
                                                PersonServiceCrudTestCase.testPerson1)
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.id, response.id)
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.name, response.name)
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.age, response.age)

    def test_5_delete_person(self):
        person_service.delete(PersonServiceCrudTestCase.testPerson2.id)
        response = person_service.get_persons()
        self.assertEqual(1, response.__len__())
        self.assertEqual(PersonServiceCrudTestCase.testPerson1.id, response[0].id)


if __name__ == "__main__":
    unittest.main()
