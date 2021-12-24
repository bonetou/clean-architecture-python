from dataclasses import dataclass

from src.domain.school.student import Student
from src.domain.school.student_builder import StudentBuilder


@dataclass
class EnrollStudentDto:
    name: str
    cpf: str
    email: str

    def create_student(self) -> Student:
        sb = StudentBuilder()
        student = (
            sb.
            with_name_cpf_email(
                self.name, 
                self.cpf, 
                self.email
            )
            .build()
        )
        return student
            