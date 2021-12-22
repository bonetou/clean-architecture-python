from src.application.indication.send_email_indication import SendEmailIndicationInterface
from src.domain.school.student import Student


class SendEmailIndication(SendEmailIndicationInterface):

    def sendTo(self, nominating: Student):
        # implementation of send email
        print(f"Email sent to {nominating.get_name()} with email {nominating.get_email().get_email()}")
