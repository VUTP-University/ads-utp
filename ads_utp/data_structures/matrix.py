class Matrix:
    """
    Represents a 2D matrix and supports basic matrix operations.

    Attributes:
        data (list of list of numbers): The matrix elements.
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
    """

    def __init__(self, data):
        """
        Initializes a Matrix instance with the given 2D list.

        Args:
            data (list of list of numbers): 2D list representing matrix values.

        Raises:
            ValueError: If rows are not of equal length.
        """
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same number of columns.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])


    def __str__(self):
        """Returns a string representation of the matrix."""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


    def __add__(self, other):
        """
        Adds two matrices of the same dimensions.

        Args:
            other (Matrix): Another matrix to add.

        Returns:
            Matrix: A new matrix representing the result.

        Raises:
            ValueError: If dimensions don't match.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)


    def __sub__(self, other):
            """
            Subtracts another matrix from the current one.

            Args:
                other (Matrix): The matrix to subtract.

            Returns:
                Matrix: Result of the subtraction.

            Raises:
                ValueError: If dimensions don't match.
            """
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrices must have the same dimensions for subtraction.")

            result = [
                [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)


    def __mul__(self, other):
        """
        Multiplies the matrix with another matrix or a scalar.

        Args:
            other (Matrix or int or float): The matrix or scalar to multiply by.

        Returns:
            Matrix: Resulting matrix after multiplication.

        Raises:
            ValueError: If dimensions are incompatible for matrix multiplication.
        """
        if isinstance(other, (int, float)):
            # Scalar multiplication
            result = [
                [self.data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Incompatible dimensions for matrix multiplication.")
            result = [
                [
                    sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    for j in range(other.cols)
                ]
                for i in range(self.rows)
            ]
            return Matrix(result)
        else:
            raise TypeError("Unsupported type for multiplication.")


    def transpose(self):
        """
        Returns the transpose of the matrix.

        Returns:
            Matrix: The transposed matrix.
        """
        transposed = [
            [self.data[i][j] for i in range(self.rows)]
            for j in range(self.cols)
        ]
        return Matrix(transposed)


    def to_list(self):
        """
        Converts the matrix to a native Python list.

        Returns:
            list of list: Matrix data as nested lists.
        """
        return [row[:] for row in self.data]
