class Matrix:

    def __init__(self, n_of_rows, n_of_columns):
        self.n_of_rows = n_of_rows
        self.n_of_columns = n_of_columns
        self.rows_list = list(range(0, n_of_rows))
        self.column_list = list(range(0, n_of_columns))
        self.matrix = self.prepare_zero_matrix()

    def __str__(self):
        matrix_print = ''
        for row in self.matrix:
            for column in row:
                matrix_print += str(column) + ' '
            matrix_print += '\n'
        return str(matrix_print)

    def prepare_zero_matrix(self):
        empty_matrix = []
        for i in range(self.n_of_rows):
            empty_matrix.append(list(map(int, '0' * self.n_of_columns)))
        return empty_matrix

    def fill_matrix(self, row_number, row):
        for i in range(len(row)):
            self.matrix[row_number][i] = row[i]


def user_menu():
    print("1. Add matrices"
          "\n2. Multiply matrix by a constant"
          "\n3. Multiply matrices"
          "\n4. Transpose matrix"
          "\n5. Calculate a determinant"
          "\n6. Inverse matrix"
          "\n0. Exit")
    user_input = int(input("Your choice: > "))
    while user_input:
        if user_input == 1:  # Add matrices

            matrix_size = list(map(int, input('Enter size of first matrix: > ').split()))
            m1 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter first matrix:')
            for n in range(matrix_size[0]):
                m1.fill_matrix(n, list(map(float, input('> ').split())))

            matrix_size = list(map(int, input('Enter size of second matrix: > ').split()))
            m2 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter second matrix:')
            for n in range(matrix_size[0]):
                m2.fill_matrix(n, list(map(float, input('> ').split())))

            m3 = Matrix(0, 0)
            m3.matrix = matrix_addition(m1, m2)
            print('The result is:')
            print(m3)

        elif user_input == 2:  # Multiply matrix by a constant

            matrix_size = list(map(int, input('Enter size of matrix: > ').split()))
            m1 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter matrix:')
            for n in range(matrix_size[0]):
                m1.fill_matrix(n, list(map(float, input('> ').split())))

            print('Enter constant: > ')
            constant = float(input())
            m2 = Matrix(0, 0)
            m2.matrix = matrix_multiplication_by_const(m1, constant)
            print('The result is:')
            print(m2)

        elif user_input == 3:  # Multiply matrices

            matrix_size = list(map(int, input('Enter size of first matrix: > ').split()))
            m1 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter first matrix:')
            for n in range(matrix_size[0]):
                m1.fill_matrix(n, list(map(float, input('> ').split())))

            matrix_size = list(map(int, input('Enter size of second matrix: > ').split()))
            m2 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter second matrix:')
            for n in range(matrix_size[0]):
                m2.fill_matrix(n, list(map(float, input('> ').split())))

            m3 = Matrix(m1.n_of_rows, m2.n_of_columns)
            m3.matrix = matrix_multiplication(m1, m2)
            print('The result is:')
            print(m3)

        elif user_input == 4:  # Transpose matrix
            print("1. Main diagonal"
                  "\n2. Side diagonal"
                  "\n3. Vertical line"
                  "\n4. Horizontal line")
            user_input = int(input("Your choice: > "))

            matrix_size = list(map(int, input('Enter size of first matrix: > ').split()))
            m1 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter first matrix:')
            for n in range(matrix_size[0]):
                m1.fill_matrix(n, list(map(float, input('> ').split())))

            m2 = Matrix(m1.n_of_rows, m1.n_of_columns)

            if user_input == 1:  # Main diagonal
                for i in range(m1.n_of_rows):
                    for j in range(m1.n_of_columns):
                        if i == j:
                            m2.matrix[i][j] = m1.matrix[i][j]
                        else:
                            m2.matrix[j][i] = m1.matrix[i][j]
                print('The result is:')
                print(m2)

            elif user_input == 2:  # Side diagonal
                for i in range(m1.n_of_rows):
                    for j in range(m1.n_of_columns):
                        m2.matrix[j][i] = m1.matrix[m1.n_of_rows - i - 1][m1.n_of_columns - j - 1]
                print('The result is:')
                print(m2)

            elif user_input == 3:  # Vertical diagonal
                for i in range(m1.n_of_rows):
                    for j in range(m1.n_of_columns):
                        m2.matrix[i][j] = m1.matrix[i][m1.n_of_columns - j - 1]
                print('The result is:')
                print(m2)

            elif user_input == 4:

                for i in range(m1.n_of_rows):
                    for j in range(m1.n_of_columns):
                        m2.matrix[i][j] = m1.matrix[m1.n_of_rows - i - 1][j]
                print('The result is:')
                print(m2)

        elif user_input == 5:  # Calculate a determinant

            matrix_size = list(map(int, input('Enter matrix size: > ').split()))
            m1 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter matrix:')
            for n in range(matrix_size[0]):
                m1.fill_matrix(n, list(map(float, input('> ').split())))

            print('The result is:')
            print(determinant(m1, m1.rows_list, m1.column_list))

        elif user_input == 6:  # Inverse matrix

            # Input Matrix:
            matrix_size = list(map(int, input('Enter size of matrix: > ').split()))
            m1 = Matrix(matrix_size[0], matrix_size[1])
            print('Enter matrix:')
            for n in range(matrix_size[0]):
                m1.fill_matrix(n, list(map(float, input('> ').split())))

            # Prepare invert of matrix determinant:
            m1_det = determinant(m1, m1.rows_list, m1.column_list)
            inv_m1_det = 1 / m1_det

            # Transpose Main Diagonal of Minors with cofactors:
            m2 = Matrix(matrix_size[0], matrix_size[1])
            m3= Matrix(matrix_size[0], matrix_size[1])
            mx = determinant(m1, m1.rows_list, m1.column_list, 'matrix')
            for n in range(matrix_size[0]):
                m2.fill_matrix(n, mx.matrix[n])

            for i in range(m3.n_of_rows):
                for j in range(m3.n_of_columns):
                    if i == j:
                        m3.matrix[i][j] = m2.matrix[i][j]
                    else:
                        m3.matrix[j][i] = m2.matrix[i][j] * ((-1) ** (2 + i + j))

            #  Calculate Inverse Matrix
            inv_matrix = matrix_multiplication_by_const(m3, inv_m1_det)
            inv_matrix_objct = Matrix(matrix_size[0], matrix_size[1])
            for n in range(matrix_size[0]):
                inv_matrix_objct.fill_matrix(n, inv_matrix[n])
            print('The result is:')
            print(inv_matrix_objct)

        print("\n1. Add matrices"
              "\n2. Multiply matrix by a constant"
              "\n3. Multiply matrices"
              "\n4. Transpose matrix"
              "\n5. Calculate a determinant"
              "\n0. Exit")
        user_input = int(input("Your choice: > "))


def matrix_addition(matrix_1, matrix_2):
    # Check if matrices are in good dimensions
    if matrix_1.n_of_rows == matrix_2.n_of_rows and matrix_1.n_of_columns == matrix_2.n_of_columns:
        matrix_3 = matrix_1.matrix.copy()
        for i in range(matrix_1.n_of_rows):
            for j in range(matrix_1.n_of_columns):
                matrix_3[i][j] += matrix_2.matrix[i][j]
        return matrix_3
    else:
        print('The operation cannot be performed.')  # Cause wrong dimensions of matrices
        return False


def matrix_multiplication_by_const(matrix_1, multiplier):
    matrix_2 = matrix_1.matrix.copy()
    for i in range(matrix_1.n_of_rows):
        for j in range(matrix_1.n_of_columns):
            matrix_2[i][j] *= multiplier
    return matrix_2


def matrix_multiplication(matrix_1, matrix_2):
    if matrix_1.n_of_columns == matrix_2.n_of_rows:  # Check if matrices are in good dimensions
        matrix_3 = []
        for i in range(matrix_1.n_of_rows):  # Making a new Matrix_3(i, m) if Matrix_1(i, j), Matrix_2(j, m)
            matrix_3.append(list(map(int, '0' * matrix_2.n_of_columns)))
        for i in range(matrix_1.n_of_rows):  # Fill new Matrix_3
            for m in range(matrix_2.n_of_columns):
                for j in range(matrix_1.n_of_columns):
                    matrix_3[i][m] += matrix_1.matrix[i][j] * matrix_2.matrix[j][m]
        return matrix_3
    print('The operation cannot be performed.')  # Cause wrong dimensions of matrices


def determinant(matrix, row_list, column_list, const_or_matrix='const'):  # i eqv m, j eqv n

    def det_minor_2_2(matrix, n_row1, n_row2, n_column1, n_column2):
        row_range = [n_row1, n_row2]
        column_range = [n_column1, n_column2]
        counter = 0
        positive = 1
        negative = 1
        for m in row_range:
            for n in column_range:
                if counter == 0 or counter == 3:
                    positive *= matrix.matrix[m][n]
                    counter += 1
                else:
                    negative *= matrix.matrix[m][n]
                    counter += 1
        return positive - negative

    if len(row_list) == 1:
        return matrix.matrix[0][0]
    if len(row_list) == 2:
        return det_minor_2_2(matrix, 0, 1, 0, 1)
    if len(row_list) == 3:
        if const_or_matrix == 'const':
            det = 0
            a = 0
            for i in column_list:
                new_c_list = column_list.copy()
                new_c_list.remove(i)
                det += matrix.matrix[row_list[0]][i] * (-1) ** (2 + a) \
                       * det_minor_2_2(matrix, row_list[1], row_list[2], new_c_list[0], new_c_list[1])
                a += 1
            return det
        else:
            mx = Matrix(len(row_list), len(column_list))
            for i in row_list:
                new_r_list = row_list.copy()
                new_r_list.remove(i)
                for j in column_list:
                    new_c_list = column_list.copy()
                    new_c_list.remove(j)
                    mx.matrix[i][j] = det_minor_2_2(matrix, new_r_list[0], new_r_list[1], new_c_list[0], new_c_list[1])
            return mx
    if len(row_list) > 3:
        if const_or_matrix == 'const':
            det = 0
            a = 0
            for i in column_list:
                new_r_list = row_list.copy()
                new_r_list.pop(0)
                new_c_list = column_list.copy()
                new_c_list.remove(i)
                det += matrix.matrix[row_list[0]][i] * (-1) ** (2 + a) * determinant(matrix, new_r_list, new_c_list)
                a += 1
            return det
        else:
            mx = Matrix(len(row_list), len(column_list))
            for i in row_list:
                new_r_list = row_list.copy()
                new_r_list.remove(i)
                for j in column_list:
                    new_c_list = column_list.copy()
                    new_c_list.remove(j)
                    mx.matrix[i][j] = determinant(matrix, new_r_list, new_c_list)
            return mx

    else:
        print('Error')


user_menu()
