from typing import List
from src.domain.school.cpf import CPF
from src.domain.school.exceptions.student_not_found import StudentNotFoundException
from src.domain.school.student import Student
from src.domain.school.student_repository import StudentRepositoryInterface


class StudentRepositoryMemory(StudentRepositoryInterface):
    def __init__(self):
        self._students_list: List[Student] = []

    def enroll(self, student: Student):
        self._students_list.append(student)

    def get_by_cpf(self, cpf: CPF) -> Student:
        student = list(
            filter(lambda student: student.cpf == cpf, self._students_list)
        )
        if len(student) == 0:
            raise StudentNotFoundException()
        return student[0]
        
    def list_all_enrolled(self) -> list[Student]:
        return self._students_list
