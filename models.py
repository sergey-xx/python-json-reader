from dataclasses import asdict, dataclass
from abc import ABC


@dataclass
class AbstractModel(ABC):

    id: int
    name: str

    @classmethod
    def from_dict(cls, dct):
        return cls(**dct)

    @classmethod
    def from_list(cls, lst):
        return [cls.from_dict(dct) for dct in lst]

    def to_dict(self):
        return asdict(self)


@dataclass
class Student(AbstractModel):

    room: int


@dataclass
class Room(AbstractModel):

    students: list[Student] | None = None

    def match_students(self, student_list: list[Student]):
        for student in student_list:
            if student.room == self.id:
                if not self.students:
                    self.students = [student]
                else:
                    self.students.append(student)
