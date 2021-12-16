import re
from dataclasses import dataclass

from src.school.exceptions.cpf_not_valid import CPFNotValid


@dataclass
class CPF:
    number: str

    def __post_init__(self):
        if self._is_number_null() or not self._is_number_valid():
            raise CPFNotValid

    def _is_number_null(self):
        return self.number is None

    def _is_number_valid(self):
        return re.match(r"^(\d{3}.){2}\d{3}-\d{2}$", self.number)
