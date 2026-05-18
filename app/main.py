class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # 1. Заменили первый цикл на красивый генератор списков в одну строку
    person_list = [Person(p["name"], p["age"]) for p in people]

    # 2. Перебираем людей для связывания браков
    for married in people:
        current_person = Person.people[married["name"]]

        # Используем .get() для безопасного поиска жены
        wife_name = married.get("wife")
        if wife_name:
            current_person.wife = Person.people[wife_name]

        # Используем .get() для безопасного поиска мужа
        husband_name = married.get("husband")
        if husband_name:
            current_person.husband = Person.people[husband_name]

    return person_list

    return person_list
