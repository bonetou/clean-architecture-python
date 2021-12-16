from src.school.student import Student


class Indication:
    def __init__(self, nominating: Student, nominated: Student):
        self._nominating: Student = nominating
        self._nominated: Student = nominated
