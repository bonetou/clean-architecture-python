import pytest

from src.school.cpf import CPF
from src.school.exceptions.cpf_not_valid import CPFNotValid


def test_should_create_valid_cpf():
    valid_cpf = CPF("870.521.292-51")
    assert valid_cpf.number == "870.521.292-51"


def test_should_not_create_invalid_cpf():
    invalid_cpfs = [None, "", "123456789"]
    for invalid_cpf in invalid_cpfs:
        with pytest.raises(CPFNotValid):
            CPF(invalid_cpf)
