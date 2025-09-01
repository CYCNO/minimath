from typing import Union, List

class Basic:
    def add(self, *args: Union[int, float]) -> Union[int, float]:
        """
        Takes any number of arguments (integers or floats) and returns their sum.

        Arguments:
        *args -- any number of numerical values (int or float)

        Returns:
        int or float -- the sum of all input numbers

        Example:
        ```py
        >>> mm.add(134, 323.5, 45, 1, -343.2, 34)
        194.3
        ```
        """
        return sum(args)

    def multiply(self, *args: Union[int, float]) -> Union[int, float]:
        """
        Multiplies any number of arguments (integers or floats) and returns the product.

        Arguments:
        *args -- any number of numerical values (int or float)

        Returns:
        int or float -- the product of all input numbers

        Example:
        ```py
        >>> mm.multiply(2, 3.5, 4)
        28.0
        ```
        """
        result = 1
        for num in args:
            result *= num
        return result

    def fibonacci(self, n: int) -> List[Union[int, float]]:
        """
        Generates the first 'n' Fibonacci numbers (integers or floats).

        Arguments:
        n -- the number of Fibonacci numbers to generate (int)

        Returns:
        List[Union[int, float]] -- a list containing the first 'n' Fibonacci numbers

        Example:
        ```py
        >>> mm.fibonacci(5)
        [0, 1, 1, 2, 3]
        ```
        """
        result = []
        a, b = 0, 1
        for i in range(n):
            result.append(a)
            a, b = b, a + b
        return result

    def is_prime(self, n: Union[int, float]) -> bool:
        """
        Checks if the given number 'n' is prime (only integers are prime).

        Arguments:
        n -- the number to check for primality (int or float)

        Returns:
        bool -- True if 'n' is prime, False otherwise

        Example:
        ```py
        >>> mm.is_prime(7)
        True
        >>> mm.is_prime(7.5)
        False
        ```
        """
        if isinstance(n, float):
            return False  # Only integers can be prime
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n)):
            if n % i == 0:
                return False
        return True

    def factorial(self, n: int) -> int:
        """
        Computes the factorial of a given number 'n'.

        Arguments:
        n -- the number to compute the factorial for (int)

        Returns:
        int -- the factorial of 'n'

        Example:
        ```py
        >>> mm.factorial(5)
        120
        ```
        """
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def primes_upto(self, n: int) -> List[int]:
        """
        Finds all prime numbers up to 'n'.

        Arguments:
        n -- the upper limit up to which primes are to be found (int)

        Returns:
        List[int] -- a list of all primes less than or equal to 'n'

        Example:
        ```py
        >>> mm.prime_upto(10)
        [2, 3, 5, 7]
        ```
        """
        primes = []
        for i in range(2, n + 1):
            if self.is_prime(i):
                primes.append(i)
        return primes

    def factors(self, n: Union[int, float]) -> List[Union[int, float]]:
        """
        Finds all factors of a given number 'n'.

        Arguments:
        n -- the number to find factors for (int or float)

        Returns:
        List[Union[int, float]] -- a list of factors of 'n'

        Example:
        ```py
        >>> mm.factors(28)
        [1, 2, 4, 7, 14, 28]
        >>> mm.factors(28.0)
        [1.0, 2.0, 4.0, 7.0, 14.0, 28.0]
        ```
        """
        factors = []
        for i in range(1, int(n) + 1):  # Treating 'n' as an integer for factor calculation
            if n % i == 0:
                factors.append(i)
        return factors

    def gcd(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Finds the greatest common divisor (GCD) of two numbers 'a' and 'b'.

        Arguments:
        a, b -- the two numbers to find the GCD of (int or float)

        Returns:
        int or float -- the GCD of 'a' and 'b'

        Example:
        ```py
        >>> mm.gcd(28, 35)
        7
        >>> mm.gcd(28.0, 35.0)
        7.0
        ```
        """
        a, b = max(a, b), min(a, b)
        while b != 0:
            rem = a % b
            a, b = b, rem
        return a

    def lcm(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Finds the least common multiple (LCM) of two numbers 'a' and 'b'.

        Arguments:
        a, b -- the two numbers to find the LCM of (int or float)

        Returns:
        int or float -- the LCM of 'a' and 'b'

        Example:
        ```py
        >>> mm.lcm(4, 6)
        12
        >>> mm.lcm(4.5, 6.5)
        29.25
        ```
        """
        return int((a * b) / self.gcd(a, b))

    def max(self, *args: Union[int, float]) -> Union[int, float]:
        """
        Finds the maximum value from a list of numbers.

        Arguments:
        *args -- any number of numerical values (int or float)

        Returns:
        int or float -- the maximum value

        Example:
        ```py
        >>> mm.max(1, 4.5, 2, 7.3)
        7.3
        ```
        """
        return max(args)

    def min(self, *args: Union[int, float]) -> Union[int, float]:
        """
        Finds the minimum value from a list of numbers.

        Arguments:
        *args -- any number of numerical values (int or float)

        Returns:
        int or float -- the minimum value

        Example:
        ```py
        >>> mm.min(1, 4.5, 2, 7.3)
        1
        ```
        """
        return min(args)

    def sum_upto(self, n: Union[int, float]) -> Union[int, float]:
        """
        Calculates the sum of integers from 1 to 'n'.

        Arguments:
        n -- the number up to which the sum is to be calculated (int or float)

        Returns:
        int or float -- the sum of integers from 1 to 'n'

        Example:
        ```py
        >>> mm.sum_upto(5)
        15
        >>> mm.sum_upto(5.5)
        15.5
        ```
        """
        return n * (1 + n) / 2

    def nCr(self, n: int, r: int) -> Union[int, float]:
        """
        Calculates the number of combinations of 'n' items taken 'r' at a time.

        Arguments:
        n -- the total number of items (int)
        r -- the number of items to choose (int)

        Returns:
        int or float -- the number of combinations (n choose r)

        Example:
        ```py
        >>> mm.nCr(5, 2)
        10
        ```
        """
        return self.factorial(n) / (self.factorial(r) * self.factorial(n - r))

    def nPr(self, n: int, r: int) -> Union[int, float]:
        """
        Calculates the number of permutations of 'n' items taken 'r' at a time.

        Arguments:
        n -- the total number of items (int)
        r -- the number of items to arrange (int)

        Returns:
        int or float -- the number of permutations (n permute r)

        Example:
        ```py
        >>> mm.nPr(5, 2)
        20
        ```
        """
        return self.factorial(n) / self.factorial(n - r)
