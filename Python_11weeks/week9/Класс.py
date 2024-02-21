from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, a, b):
        self.matrix1 = a
        self.matrix2 = b


class Matrix:
    def transposed(x):
        ag = []
        for i in range(len(x.list_new[0])):
            ag.append([])
        for i in range(len(x.list_new[0])):
            for u in x.list_new:
                ag[i].append(u[i])
        return Matrix(ag)

    def transpose(self):
        ag = []
        for i in range(len(self.list_new[0])):
            ag.append([])
        for i in range(len(self.list_new[0])):
            for u in self.list_new:
                ag[i].append(u[i])
        self.list_new = ag
        return Matrix(ag)

    def __init__(self, matrix):
        self.list_new = deepcopy(matrix)

    def __str__(self):
        all_str = ''
        for elem in self.list_new:
            all_str += '\t'.join(map(str, elem)) + '\n'
        return all_str[:-1]

    def size(self):
        return len(self.list_new), len(self.list_new[0])

    def __add__(self, other):
        w = len(self.list_new)
        ww = len(self.list_new[0])
        if w == len(other.list_new) and ww == len(other.list_new[0]):
            aa = ''
            p = 0
            o = -1
            for i in self.list_new:
                k = 0
                p += 1
                o += 1
                for u in i:
                    aa += str(u + other.list_new[o][k])
                    k += 1
                    if k < len(i):
                        aa += '\t'
                if p < len(self.list_new):
                    aa += '\n'
            return aa
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        new_input_list = []
        for i in range(len(self.list_new)):
            line = [j * other for j in self.list_new[i]]
            new_input_list.append(line)
        return Matrix(new_input_list)

    def __rmul__(other, self):
        new_input_list = []
        for i in range(len(other.list_new)):
            line = [j * self for j in other.list_new[i]]
            new_input_list.append(line)
        return Matrix(new_input_list)


exec(stdin.read())
