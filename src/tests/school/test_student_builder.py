from src.domain.school.cpf import CPF
from src.domain.school.email import Email
from src.domain.school.phone import Phone
from src.domain.school.student_builder import StudentBuilder


def test_create_student():
    name = "boneto"
    cpf = "888.111.231-02"
    email = "boneto@yahoo.com.br"
    ddd_1 = "51"
    number_1 = "123456789"
    ddd_2 = "51"
    number_2 = "12345678"
    student_builder = StudentBuilder()
    student = (
        student_builder
    ).with_name_cpf_email(
        name=name,
        cpf=cpf,
        email=email,
    ).with_phone(
        phone_ddd=ddd_1, 
        phone_number=number_1,
    ).with_phone(
        phone_ddd=ddd_2,
        phone_number=number_2,
    ).build()
    assert student.get_cpf() == CPF(cpf)
    assert student.get_email() == Email(email)
    assert student.get_name() == name
    assert student.get_phones() == [Phone(ddd_1, number_1), Phone(ddd_2, number_2)]