from com.wd.sras.person import person_controller, person_repository

if __name__ == "__main__":
    person_repository.init()
    person_controller.app.run(debug=False)
