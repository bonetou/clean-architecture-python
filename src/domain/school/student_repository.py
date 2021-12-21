from abc import abstractmethod, ABC
from src.domain.school.cpf import CPF
from src.domain.school.student import Student


class StudentRepositoryInterface(ABC):
    @abstractmethod
    def enroll(self, student: Student):
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: CPF) -> Student:
        pass

    @abstractmethod
    def list_all_enrolled(self) -> list[Student]:
        pass
