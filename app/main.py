class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for married in people:
        current_person = Person.people[married["name"]]
        if "wife" in married and married["wife"] is not None:
            married_obj = Person.people[married["wife"]]
            current_person.wife = married_obj
        elif "husband" in married and married["husband"] is not None:
            married_obj = Person.people[married["husband"]]
            current_person.husband = married_obj

    return person_list
