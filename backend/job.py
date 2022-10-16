from logging import RootLogger
from mimetypes import init


class Job:
    name: str
    role: str
    deadline: str
    date: str
    status: str
    text: str
    def __init__(self, companyName, role, deadline, date, status, text):
        self.name = companyName
        self.role = role
        self.deadline = deadline
        self.date = date
        self.status = status
        self.text = text