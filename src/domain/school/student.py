from src.domain.school.cpf import CPF
from src.domain.school.email import Email
from typing import List

from src.domain.school.phone import Phone


class Student:
    def __init__(self, cpf: CPF, name: str, email: Email) -> None:
        self._cpf: CPF = cpf
        self._name: str = name
        self._email: Email = email
        self._phones: List[Phone] = []

    def add_phone(self, phone: Phone):
        self._phones.append(phone)

    def get_cpf(self) -> CPF:
        return self._cpf

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> Email:
        return self._email

    def get_phones(self) -> List[Phone]:
        return self._phones
