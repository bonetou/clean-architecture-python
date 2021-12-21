from typing import Optional

from src.domain.school.cpf import CPF
from src.domain.school.email import Email
from src.domain.school.phone import Phone
from src.domain.school.student import Student


class StudentBuilder:
    def __init__(self):
        self._student: Optional[Student] = None

    def with_name_cpf_email(self, name: str, cpf: str, email: str) -> 'StudentBuilder':
        self._student = Student(name=name, cpf=CPF(cpf), email=Email(email))
        return self

    def with_phone(self, phone_ddd: str, phone_number: str) -> 'StudentBuilder':
        self._student.add_phone(Phone(phone_ddd, phone_number))
        return self

    def build(self) -> Student:
        return self._student
