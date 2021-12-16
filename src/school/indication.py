from src.school.student import Student
from datetime import datetime


class Indication:
    def __init__(self, nominating: Student, nominated: Student):
        self._nominating: Student = nominating
        self._nominated: Student = nominated
        self._indication_date: datetime = datetime.now()

    def get_nominating(self):
        return self._nominating

    def get_nominated(self):
        return self._nominated

    def get_indication_date(self):
        return self._indication_date
