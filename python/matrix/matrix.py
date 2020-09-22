from typing import List


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.__storage: List[List[int]] = [
            [int(num) for num in row.split(" ")] for row in matrix_string.split("\n")
        ]

    def row(self, index: int) -> List[int]:
        """
        Returns a given row in the matrix.
        """
        return self.__storage[index - 1]

    def column(self, index: int) -> List[int]:
        """
        Returns a given column in the matrix
        """
        return [row[index - 1] for row in self.__storage]
