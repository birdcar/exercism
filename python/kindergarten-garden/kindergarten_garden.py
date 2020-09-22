from typing import Dict, List, Optional


class Garden:
    """
    Our kindergartener's garden
    """

    def __init__(
        self,
        diagram: str,
        students: Optional[List[str]] = None,
        plants: Optional[Dict[str, str]] = None,
    ):
        self._students = students or [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ]

        self._plants = plants or {
            "R": "Radishes",
            "C": "Clover",
            "G": "Grass",
            "V": "Violets",
        }

        self.student_plants = self._parse_diagram(diagram, self._students)

    def _parse_diagram(
        self, diagram: str, student_list: List[str]
    ) -> Dict[str, List[str]]:
        """
        Given a 2 row garden diagram as a string, return a dictionary
        containing the name of the student as a key and a list of that
        students plants as the value.
        """
        row_one, row_two = [
            [self._plants[p] for p in row] for row in diagram.splitlines()
        ]

        plant_lists = row_one[::2], row_one[1::2], row_two[::2], row_two[1::2]

        return {
            student: plants
            for student, *plants in zip(sorted(student_list), *plant_lists)
        }

    def plants(self, name: str) -> List[str]:
        """
        Return the list of plants in the school garden that belong
        to the named student.
        """
        return self.student_plants[name]
