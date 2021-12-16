import re
from dataclasses import dataclass
from src.school.exceptions.phone import DDDOrNumberIsNull, NumberIsNotValid, DDDIsNotValid


@dataclass
class Phone:
    ddd: str
    number: str

    def __post_init__(self):
        if self._is_ddd_null() or self._is_number_null():
            raise DDDOrNumberIsNull

        if not self._is_ddd_valid():
            raise DDDIsNotValid

        if not self._is_number_valid():
            raise NumberIsNotValid

    def _is_ddd_null(self):
        return self.ddd is None

    def _is_number_null(self):
        return self.number is None

    def _is_ddd_valid(self):
        return len(self.ddd) == 2

    def _is_number_valid(self):
        return re.match("\\d{8}|\\d{9}", self.number)
