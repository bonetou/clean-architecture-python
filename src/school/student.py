from src.school.cpf import CPF
from src.school.email import Email
from typing import List

from src.school.phone import Phone


class Student:
    def __init__(self, cpf: CPF, name: str, email: Email) -> None:
        self._cpf: CPF = cpf
        self._name: str = name
        self._email: Email = email
        self._phones: List[Phone] = []

    def add_phone(self, phone: Phone):
        self._phones.append(phone)
