# Write a simple Rest API server.
1. There will only one resource in the API server: Persons with ID and two attributes: "name" and "age"
2. Please use SQLite DB to store the data in the API
3. API response / errors will be in JSON
4. The API will support GET, POST, PUT, DELETE operations:
   1. GET api/persons
      - Will return list of all persons
   2. GET api/persons/3
      - Will return list of all persons
   3. POST api/persons
      -  Will return single person with id 3
      -  Will return 404 error in case there is no person with id 3
   4. PUT api/persons/2
      -  Will validate that a body with name and age was given and if not return error.
      -  Will return the inserted person (include the new id)
   5. DELETE api/persons/4
5. Please use a well-known Python framework, such as Cherypy, Flask, FastAPI .
6. Please include tests in your solution.
