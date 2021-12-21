from dataclasses import dataclass, field

from src.domain.school.cpf import CPF
from src.domain.school.email import Email
from typing import List

from src.domain.school.phone import Phone


@dataclass
class Student:
    cpf: CPF
    name: str
    email: Email
    phones: List[Phone] = field(default_factory=list)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def get_cpf(self) -> CPF:
        return self.cpf

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> Email:
        return self.email

    def get_phones(self) -> List[Phone]:
        return self.phones
