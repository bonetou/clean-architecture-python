from src.domain.school.phone import Phone
from src.domain.school.exceptions.phone import NumberIsNotValid, DDDIsNotValid, DDDOrNumberIsNull

import pytest


def test_should_create_valid_phone():
    valid_ddd = "51"
    valid_number = "982317300"
    valid_phone = Phone(ddd=valid_ddd, number=valid_number)
    assert valid_phone.ddd == valid_ddd
    assert valid_phone.number == valid_number


def test_should_not_create_phone_with_null_ddd():
    with pytest.raises(DDDOrNumberIsNull):
        Phone(ddd=None, number="123")


def test_should_not_create_phone_with_null_number():
    with pytest.raises(DDDOrNumberIsNull):
        Phone(ddd="51", number=None)


def test_should_not_create_phone_with_invalid_ddd():
    invalid_ddds = ["", "123"]
    for invalid_ddd in invalid_ddds:
        with pytest.raises(DDDIsNotValid):
            Phone(ddd=invalid_ddd, number="123456789")


def test_should_not_create_phone_with_invalid_number():
    invalid_numbers = ["", "123"]
    for invalid_number in invalid_numbers:
        with pytest.raises(NumberIsNotValid):
            Phone(ddd="51", number=invalid_number)
