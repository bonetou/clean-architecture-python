from dataclasses import asdict

from src.domain.school.cpf import CPF
from src.domain.school.student import Student
from src.domain.school.student_builder import StudentBuilder
from src.domain.school.student_repository import StudentRepositoryInterface
from google.cloud import firestore


class StudentRepositoryFirestore(StudentRepositoryInterface):

    def __init__(self, config):
        self.__collection = firestore.Client().collection(config.collection)

    def enroll(self, student: Student):
        self.__collection.add(
            document_id=student.cpf.number,
            document_data=asdict(student)
        )

    def get_by_cpf(self, cpf: CPF) -> Student:
        student_document = self.__collection.document(cpf.number).get()
        if not student_document.exists:
            raise Exception(f"Student with cpf {cpf.number} does not exist")
        student_document_dict = student_document.to_dict()
        return Student(
            cpf=student_document_dict.get("cpf"),
            name=student_document_dict.get("name"),
            email=student_document_dict.get("email", ""),
            phones=student_document_dict.get("phones", "")
        )

    def list_all_enrolled(self) -> list[Student]:
        students = []
        student_docs = self.__collection.stream()
        for student_doc in student_docs:
            student_document_dict = student_doc.to_dict()
            students.append(
                Student(
                    cpf=student_document_dict.get("cpf"),
                    name=student_document_dict.get("name"),
                    email=student_document_dict.get("email", ""),
                    phones=student_document_dict.get("phones", "")
                )
            )
        return students
