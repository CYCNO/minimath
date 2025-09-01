class Algebra:
    def quadratic_roots(self, a: float, b: float, c: float):
        """
        Solves the quadratic equation ax^2 + bx + c = 0 and returns the roots.

        Arguments:
        a -- the coefficient of x^2 (float)
        b -- the coefficient of x (float)
        c -- the constant term (float)

        Returns:
        A list containing the two roots (if real), or a string indicating no real roots.

        Example:
        ```py
        >>> algebra = Algebra()
        >>> algebra.quadratic_roots(1, -3, 2)
        [2.0, 1.0]

        >>> algebra.quadratic_roots(1, 2, 5)
        "No real roots"
        ```
        """
        if a == 0:
            return "Not a quadratic equation (a cannot be 0)"

        determinant = b**2 - 4*a*c

        if determinant < 0:
            return "No real roots"

        # Calculate the two roots using the quadratic formula
        root1 = (-b + determinant**0.5) / (2 * a)
        root2 = (-b - determinant**0.5) / (2 * a)

        return [root1, root2]
