from src.school.email import Email
from src.school.exceptions.email_address_not_valid import EmailAddressNotValid
import pytest


def test_should_create_valid_email():
    valid_email = Email("valid_email@gmail.com")
    assert valid_email.address == "valid_email@gmail.com"


def test_should_not_create_invalid_email():
    invalid_emails = [None, "", "invalid_email"]
    for invalid_email in invalid_emails:
        with pytest.raises(EmailAddressNotValid):
            Email(invalid_email)
