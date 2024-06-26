# importing Operating system
import os


class SparseMatrix:
    """A class to represent a sparse matrix and perform basic operations on it."""

    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        """
        Initialize the SparseMatrix.

        Args:
        - file_path (str): Path to the file containing the sparse matrix data.
        - num_rows (int): Number of rows in the sparse matrix.
        - num_cols (int): Number of columns in the sparse matrix.
        """
        if file_path:
            self.load_from_file(file_path)
        else:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.elements = {}

    def load_from_file(self, file_path):
        """
        Load the sparse matrix from a file.

        Args:
        - file_path (str): Path to the file containing the sparse matrix data.
        """
        self.elements = {}
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.num_rows = 0
            self.num_cols = 0
            for line in lines[2:]:
                if line.strip() == "":
                    continue
                try:
                    row, col, value = self.parse_line(line.strip())
                    self.num_rows = max(self.num_rows, row + 1)
                    self.num_cols = max(self.num_cols, col + 1)
                    self.elements[(row, col)] = value
                except ValueError as e:
                    raise ValueError(f"Input file has wrong format: {e}")

    def parse_line(self, line):
        """
        Parse a line from the file containing the sparse matrix data.

        Args:
        - line (str): A line from the file containing the sparse matrix data.

        Returns:
        - tuple: A tuple containing the row, column, and value from the line.
        """
        if not (line.startswith('(') and line.endswith(')')):
            raise ValueError("Line must start with '(' and end with ')'")
        line = line[1:-1]  # Remove parentheses
        parts = line.split(',')
        if len(parts) != 3:
            raise ValueError(
                "Line must contain exactly three comma-separated values")
        return int(parts[0]), int(parts[1]), int(parts[2])

    def get_element(self, row, col):
        """
        Get the value at the specified row and column in the sparse matrix.

        Args:
        - row (int): The row index.
        - col (int): The column index.

        Returns:
        - int: The value at the specified row and column.
        """
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        """
        Set the value at the specified row and column in the sparse matrix.

        Args:
        - row (int): The row index.
        - col (int): The column index.
        - value (int): The value to set.
        """
        if row >= self.num_rows or col >= self.num_cols:
            raise IndexError("Index out of bounds")
        self.elements[(row, col)] = value

    def __add__(self, other):
        """
        Add two sparse matrices.

        Args:
        - other (SparseMatrix): The other sparse matrix to add.

        Returns:
        - SparseMatrix: The result of adding the two matrices.
        """
        result = SparseMatrix(num_rows=max(
            self.num_rows, other.num_rows), num_cols=max(self.num_cols, other.num_cols))
        for key, value in self.elements.items():
            result.set_element(*key, value)
        for key, value in other.elements.items():
            result.set_element(*key, result.get_element(*key) + value)
        return result

    def __sub__(self, other):
        """
        Subtract one sparse matrix from another.

        Args:
        - other (SparseMatrix): The other sparse matrix to subtract.

        Returns:
        - SparseMatrix: The result of subtracting the second matrix from the first.
        """
        result = SparseMatrix(num_rows=max(
            self.num_rows, other.num_rows), num_cols=max(self.num_cols, other.num_cols))
        for key, value in self.elements.items():
            result.set_element(*key, value)
        for key, value in other.elements.items():
            result.set_element(*key, result.get_element(*key) - value)
        return result

    def __mul__(self, other):
        """
        Multiply two sparse matrices.

        Args:
        - other (SparseMatrix): The other sparse matrix to multiply.

        Returns:
        - SparseMatrix: The result of multiplying the two matrices.
        """
        if self.num_cols != other.num_rows:
            raise ValueError(
                "Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                sum_value = 0
                for k in range(self.num_cols):
                    sum_value += self.get_element(i, k) * \
                        other.get_element(k, j)
                if sum_value != 0:
                    result.set_element(i, j,)

# importing Operating system


class SparseMatrix:
    """A class to represent a sparse matrix and perform basic operations on it."""

    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        """
        Initialize the SparseMatrix.

        Args:
        - file_path (str): Path to the file containing the sparse matrix data.
        - num_rows (int): Number of rows in the sparse matrix.
        - num_cols (int): Number of columns in the sparse matrix.
        """
        if file_path:
            self.load_from_file(file_path)
        else:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.elements = {}

    def load_from_file(self, file_path):
        """
        Load the sparse matrix from a file.

        Args:
        - file_path (str): Path to the file containing the sparse matrix data.
        """
        self.elements = {}
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.num_rows = 0
            self.num_cols = 0
            for line in lines[2:]:
                if line.strip() == "":
                    continue
                try:
                    row, col, value = self.parse_line(line.strip())
                    self.num_rows = max(self.num_rows, row + 1)
                    self.num_cols = max(self.num_cols, col + 1)
                    self.elements[(row, col)] = value
                except ValueError as e:
                    raise ValueError(f"Input file has wrong format: {e}")

    def parse_line(self, line):
        """
        Parse a line from the file containing the sparse matrix data.

        Args:
        - line (str): A line from the file containing the sparse matrix data.

        Returns:
        - tuple: A tuple containing the row, column, and value from the line.
        """
        if not (line.startswith('(') and line.endswith(')')):
            raise ValueError("Line must start with '(' and end with ')'")
        line = line[1:-1]  # Remove parentheses
        parts = line.split(',')
        if len(parts) != 3:
            raise ValueError(
                "Line must contain exactly three comma-separated values")
        return int(parts[0]), int(parts[1]), int(parts[2])

    def get_element(self, row, col):
        """
        Get the value at the specified row and column in the sparse matrix.

        Args:
        - row (int): The row index.
        - col (int): The column index.

        Returns:
        - int: The value at the specified row and column.
        """
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        """
        Set the value at the specified row and column in the sparse matrix.

        Args:
        - row (int): The row index.
        - col (int): The column index.
        - value (int): The value to set.
        """
        if row >= self.num_rows or col >= self.num_cols:
            raise IndexError("Index out of bounds")
        self.elements[(row, col)] = value

    def __add__(self, other):
        """
        Add two sparse matrices.

        Args:
        - other (SparseMatrix): The other sparse matrix to add.

        Returns:
        - SparseMatrix: The result of adding the two matrices.
        """
        result = SparseMatrix(num_rows=max(
            self.num_rows, other.num_rows), num_cols=max(self.num_cols, other.num_cols))
        for key, value in self.elements.items():
            result.set_element(*key, value)
        for key, value in other.elements.items():
            result.set_element(*key, result.get_element(*key) + value)
        return result

    def __sub__(self, other):
        """
        Subtract one sparse matrix from another.

        Args:
        - other (SparseMatrix): The other sparse matrix to subtract.

        Returns:
        - SparseMatrix: The result of subtracting the second matrix from the first.
        """
        result = SparseMatrix(num_rows=max(
            self.num_rows, other.num_rows), num_cols=max(self.num_cols, other.num_cols))
        for key, value in self.elements.items():
            result.set_element(*key, value)
        for key, value in other.elements.items():
            result.set_element(*key, result.get_element(*key) - value)
        return result

    def __mul__(self, other):
        """
        Multiply two sparse matrices.

        Args:
        - other (SparseMatrix): The other sparse matrix to multiply.

        Returns:
        - SparseMatrix: The result of multiplying the two matrices.
        """
        if self.num_cols != other.num_rows:
            raise ValueError(
                "Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                sum_value = 0
                for k in range(self.num_cols):
                    sum_value += self.get_element(i, k) * \
                        other.get_element(k, j)
                if sum_value != 0:
                    result.set_element(i, j, result.set_element(i, j, sum_value))
        return result

    def __repr__(self):
        """
        Return a string representation of the sparse matrix.

        Returns:
        - str: A string representation of the sparse matrix.
        """
        result=f"SparseMatrix(num_rows={self.num_rows}, num_cols={
                              self.num_cols})\n"
        for (row, col), value in self.elements.items():
            result += f"({row}, {col}, {value})\n"
        return result

def main():
    base_dir=os.path.dirname(os.path.abspath(__file__))
    input_dir=os.path.abspath(os.path.join(
        base_dir, '..', '..', 'sample_inputs'))
    output_dir=os.path.abspath(os.path.join(
        base_dir, '..', '..', 'sample_results'))

    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")
    if not os.path.exists(output_dir):
        raise FileNotFoundError(
            f"Output directory does not exist: {output_dir}")

    print(f"Base directory: {base_dir}")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")

    matrix1_file=os.path.join(input_dir, 'matrix1.txt')
    matrix2_file=os.path.join(input_dir, 'matrix2.txt')

    try:
        matrix1=SparseMatrix(file_path=matrix1_file)
        matrix2=SparseMatrix(file_path=matrix2_file)
    except ValueError as e:
        print(f"Error loading matrices: {e}")
        return

    operation=input("Select operation (add, sub, mul): ").strip().lower()
    if operation == 'add':
        result=matrix1 + matrix2
    elif operation == 'sub':
        result=matrix1 - matrix2
    elif operation == 'mul':
        result=matrix1 * matrix2
    else:
        print("Invalid operation")
        return

    output_file=os.path.join(output_dir, 'result.txt')
    with open(output_file, 'w') as file:
        file.write(f"rows={result.num_rows}\n")
        file.write(f"cols={result.num_cols}\n")
        for (row, col), value in result.elements.items():
            file.write(f"({row}, {col}, {value})\n")

    print(f"Result saved to {output_file}")


if __name__ == '__main__':
    main()
