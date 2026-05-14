import random # for .random()

class Matrix:
    """
    A simple Matrix class supporting basic arithmetic operations
    like addition, multiplication, and scalar operations.

    Examples:
        Creating a matrix with size (rows x cols):
            m = Matrix(2, 3)

        Creating a matrix from a list:
            m = Matrix([[1, 2], [3, 4]])

        Filling a matrix:
            m.fill(5)  # all elements become 5

        Scalar addition:
            m2 = m + 10

        Matrix addition:
            m3 = m + m2

        Scalar multiplication:
            m4 = m * 2

        Matrix multiplication:
            a = Matrix([[1, 2], [3, 4]])
            b = Matrix([[5, 6], [7, 8]])
            c = a * b

        Indexing:
            row = m[0]   # first row

        Printing:
            print(m)
    """

    def __init__(self, rows, columns=None):
        """
        Initialize a matrix.

        Args:
            rows (int or list): If int, creates a zero matrix with given rows.
                                If list, treats it as an existing matrix.
            columns (int, optional): Number of columns (required if rows is int).
        """
        if isinstance(rows, list):
            self.matrix = rows
            self.rows = len(rows)
            self.cols = len(rows[0])
        else:
            self.rows = rows
            self.cols = columns
            self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def fill(self, value=0):
        """
        Fill the entire matrix with a given value.

        Args:
            value (int or float): Value to fill the matrix with.
        """
        self.matrix = [[value for j in range(self.cols)] for i in range(self.rows)]

    def random(self, lower=0, upper=1):
        """
        Fill the entire matrix with random values

        Args:
            lower (int or float): Value greater or equal to lower
            upper (int or float): Value smaller than upper
        """
        self.matrix = [
            [random.uniform(lower, upper) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    @staticmethod
    def add(A, B):
        """
        Static method for matrix addition using operator overloading.

        Args:
            A (Matrix): First matrix
            B (Matrix): Second matrix

        Returns:
            Matrix: Result of A + B
        """
        return A + B

    @staticmethod
    def multiply(A, B):
        """
        Static method for matrix multiplication using operator overloading.

        Args:
            A (Matrix): First matrix
            B (Matrix): Second matrix

        Returns:
            Matrix: Result of A * B
        """
        return A * B

    def __add__(self, other):
        """
        Add either a scalar or another matrix.

        Args:
            other (Matrix, int, float): Value to add

        Returns:
            Matrix: Resulting matrix or NotImplemented
        """

        # if it's not a vector nor scalar
        if not isinstance(other, (Matrix, int, float)):
            return NotImplemented

        # if it's a scalar value
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + other
            return result

        # matrix-matrix addition
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Rows And Columns must be same for summation")

        result_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result_matrix

    def __mul__(self, other):
        """
        Multiply matrix with scalar or another matrix.

        Args:
            other (Matrix, int, float): Value to multiply

        Returns:
            Matrix: Resulting matrix or NotImplemented
        """

        if not isinstance(other, (Matrix, int, float)):
            return NotImplemented

        # scalar multiplication
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] * other
            return result

        # matrix multiplication validation
        if self.cols != other.rows:
            raise ValueError(
                "Rows of One matrix should be equal to other matrix column"
            )

        result = Matrix(self.rows, other.cols)  # (m × n) × (n × p) = (m × p)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def __radd__(self, other):
        """
        Right-side addition support.
        """
        return self + other

    def __rmul__(self, other):
        """
        Right-side multiplication support.
        """
        return self * other

    def __getitem__(self, index):
        """
        Allow matrix indexing like matrix[i].

        Args:
            index (int): Row index

        Returns:
            list: Row of matrix
        """
        return self.matrix[index]

    def __repr__(self):
        """
        String representation of the matrix.
        """
        return "\n".join(str(row) for row in self.matrix)

# TODO: add transpose()
