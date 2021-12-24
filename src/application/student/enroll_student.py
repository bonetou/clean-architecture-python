from src.application.student.enroll_student_dto import EnrollStudentDto
from src.domain.school.student_repository import StudentRepositoryInterface

class EnrollStudent:
    def __init__(self, repository: StudentRepositoryInterface):
        self._repository = repository

    def execute(self, data: EnrollStudentDto):
        student = data.create_student()
        self._repository.enroll(student)