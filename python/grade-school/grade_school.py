import bisect
from collections import defaultdict


class School:
    def __init__(self):
        self._enrollment = defaultdict(list)

    def add_student(self, name: str, grade: int):
        """
        Enroll a student in our school
        """
        bisect.insort_right(self._enrollment[grade], name)

    def roster(self):
        """
        Return a list of all students enrolled in the school
        """
        return [
            student
            for grade, students in sorted(self._enrollment.items(), key=lambda x: x[0])
            for student in students
        ]

    def grade(self, grade_number: int):
        """
        Return all the students of a particular grade
        """
        return self._enrollment.get(grade_number, [])

