from typing import TypeAlias, Optional

Matrix: TypeAlias = list[list[int | float]]


def has_same_column_size(matrix: Matrix) -> None:
    """Avoid matrices that has not same number of column in each row
    ex: [[1, 2, 3], [1, 2]] this matrix is not valid

    Args:
        m (Matrix): matrix to check

    Raises:
        ValueError: Matrix has not same number of column in each row

    """
    first_row_len = len(matrix[0])
    if not all([len(row) == first_row_len for row in matrix]):
        raise ValueError("Matrix has not the same number of column in each row")


def rows_equal(m1: Matrix, m2: Matrix) -> None:
    """Check that matrices have the same number of rows

    Args:
        m1 (Matrix): matrix to check
        m2 (Matrix): matrix to check

    Raises:
        ValueError: Matrices have not the same number of rows
    """
    if not len(m1) == len(m2):
        raise ValueError("Matrices have not the same number of rows")


def columns_equal(m1: Matrix, m2: Matrix) -> None:
    """Check that matrices have same number of columns

    Args:
        m1 (Matrix): matrix to check
        m2 (Matrix): matrix to Check

    Raises:
        ValueError: Matrices have not the same number of columns
    """
    if not [len(row) for row in m1] == [len(row) for row in m2]:
        raise ValueError("Matrices have not the same number of columns")


def can_add_matrices(m1: Matrix, m2: Matrix) -> None:
    """Check that we can add the two matrices

    Args:
        m1 (Matrix):
        m2 (Matrix):
        
    Raises:
        ValueError: if matrices don't respect matrix add constraints
    """
    try:
        has_same_column_size(m1)
        has_same_column_size(m2)
        rows_equal(m1, m2)
        columns_equal(m1, m2)
    except ValueError as e:
        print(e)
        exit()


def add_matrices(m1: Matrix, m2: Matrix) -> Optional[Matrix]:
    """Add two matrices

    Args:
        m1 (Matrix):
        m2 (Matrix):

    Raises:
        ValueError: if matrices don't respect matrix add constraints

    Returns:
        Matrix: new matrix which is the sum of the two given matrices
    """
    can_add_matrices(m1, m2)

    return [[n1 + n2 for n1, n2 in zip(row1, row2)] for row1, row2 in zip(m1, m2)]


def show_matrix(matrix: Optional[Matrix]) -> None:
    if matrix is None:
        return

    max_nb: str = str(max([max(row) for row in matrix]))
    space = "".join([" " for _ in max_nb]) + " "

    for row in matrix:
        print("|" + space[:-1], end="")
        for row_nb in row:
            print(row_nb, end=space[: len(space) - len(str(row_nb))])
        print("|")


if "__main__" == __name__:
    m1: Matrix = [[1, 2, 3], [3, 7, 3]]
    m2: Matrix = [[6, 4, 2], [3, 1, 0]]

    show_matrix(add_matrices(m1, m2))

    m1: Matrix = [[-9, 2], [4, 0]]
    m2: Matrix = [[6, 4, 2], [3, 10, 0]]
    show_matrix(add_matrices(m1, m2))  # raise value error
