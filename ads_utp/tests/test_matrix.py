import pytest
from data_structures.matrix import Matrix


def test_matrix_initialization():
    """Test successful initialization and dimension validation."""
    m = Matrix([[1, 2], [3, 4]])
    assert m.rows == 2
    assert m.cols == 2
    assert m.data == [[1, 2], [3, 4]]

    with pytest.raises(ValueError):
        Matrix([[1, 2], [3]])  # Unequal row lengths


def test_matrix_str():
    """Test string representation of matrix."""
    m = Matrix([[1, 2], [3, 4]])
    assert str(m) == "1\t2\n3\t4"


def test_matrix_addition():
    """Test element-wise addition of two matrices."""
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1 + m2
    assert result.data == [[6, 8], [10, 12]]

    with pytest.raises(ValueError):
        m1 + Matrix([[1, 2, 3], [4, 5, 6]])  # Shape mismatch


def test_matrix_subtraction():
    """Test element-wise subtraction of two matrices."""
    m1 = Matrix([[5, 6], [7, 8]])
    m2 = Matrix([[1, 2], [3, 4]])
    result = m1 - m2
    assert result.data == [[4, 4], [4, 4]]

    with pytest.raises(ValueError):
        m1 - Matrix([[1, 2, 3], [4, 5, 6]])  # Shape mismatch

def test_matrix_scalar_multiplication():
    """Test scalar multiplication."""
    m = Matrix([[1, 2], [3, 4]])
    result = m * 3
    assert result.data == [[3, 6], [9, 12]]

def test_matrix_multiplication():
    """Test matrix multiplication with another matrix."""
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[2, 0], [1, 2]])
    result = m1 * m2
    assert result.data == [[4, 4], [10, 8]]

    with pytest.raises(ValueError):
        m1 * Matrix([[1], [2], [3]])  # Incompatible dimensions

def test_matrix_transpose():
    """Test matrix transposition."""
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    result = m.transpose()
    assert result.data == [[1, 4], [2, 5], [3, 6]]

def test_matrix_to_list():
    """Test conversion to native Python list."""
    m = Matrix([[1, 2], [3, 4]])
    result = m.to_list()
    assert result == [[1, 2], [3, 4]]
    assert result is not m.data  # Ensure it's a deep copy


if __name__ == "__main__":
    pytest.main()
