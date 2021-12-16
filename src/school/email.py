from src.school.exceptions.email_address_not_valid import EmailAddressNotValid
from dataclasses import dataclass
import re


@dataclass
class Email:
    address: str

    def __post_init__(self):
        if self._is_address_null() or not self._is_address_valid():
            raise EmailAddressNotValid

    def _is_address_null(self):
        return self.address is None

    def _is_address_valid(self):
        return re.match("^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", self.address)
