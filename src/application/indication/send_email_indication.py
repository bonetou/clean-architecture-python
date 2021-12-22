from abc import ABC, abstractmethod
from src.domain.school.student import Student


class SendEmailIndicationInterface(ABC):

    @abstractmethod
    def sendTo(self, nominating: Student):
        pass
