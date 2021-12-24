from src.domain.school.cpf import CPF
from src.domain.school.email import Email
from src.application.student.enroll_student import EnrollStudent
from src.application.student.enroll_student_dto import EnrollStudentDto
from src.infrastructure.school.student_repository_memory import StudentRepositoryMemory


def test_student_should_be_enrolled():
    repository = StudentRepositoryMemory()
    use_case = EnrollStudent(repository)
    student_data = EnrollStudentDto(
        name="Teste",
        cpf="870.521.292-51",
        email="teste@gmail.com",
    )
    use_case.execute(student_data)
    student_saved = repository.get_by_cpf(CPF("870.521.292-51"))
    assert student_saved.get_cpf() == CPF("870.521.292-51")
    assert student_saved.get_name() == "Teste"
    assert student_saved.get_email() == Email("teste@gmail.com")
