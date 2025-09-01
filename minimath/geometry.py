from typing import List, Union
from .constants import Constants

class Geometry(Constants):  # Inheriting from Constants to access pi() directly
    def distance(self, p1: List[float], p2: List[float]) -> float:
        """
        Calculates the Euclidean distance between two points in a multidimensional space.

        Arguments:
        p1 -- Coordinates of the first point (list of floats or ints)
        p2 -- Coordinates of the second point (list of floats or ints)

        Returns:
        float -- The Euclidean distance between points p1 and p2.

        Example:
        ```py
        >>> geometry = Geometry()
        >>> geometry.distance([1, 2], [4, 6])
        5.0
        ```
        """
        if len(p1) != len(p2):
            raise ValueError("Points must have the same dimension.")

        result = 0
        for i in range(len(p1)):
            result += (p1[i] - p2[i]) ** 2
        return result ** 0.5

    def triangle_area(self, a: float, b: float, c: float) -> Union[float, str]:
        """
        Calculates the area of a triangle given the lengths of its three sides using Heron's formula.

        Arguments:
        a -- Length of the first side (float)
        b -- Length of the second side (float)
        c -- Length of the third side (float)

        Returns:
        float -- The area of the triangle if the sides form a valid triangle.
        str -- An error message if the sides do not form a valid triangle.

        Example:
        ```py
        >>> geometry = Geometry()
        >>> geometry.triangle_area(3, 4, 5)
        6.0
        ```
        """
        # Check if the sides form a valid triangle (triangle inequality theorem)
        if a + b <= c or b + c <= a or a + c <= b:
            return "Invalid triangle sides"

        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def circle_area(self, r: float) -> Union[float, str]:
        """
        Calculates the area of a circle given its radius.

        Arguments:
        r -- The radius of the circle (float)

        Returns:
        float -- The area of the circle.

        Example:
        ```py
        >>> geometry = Geometry()
        >>> geometry.circle_area(5)
        78.53981633974483
        ```
        """
        if r < 0:
            return "Radius cannot be negative."

        return self.pi() * (r ** 2)
