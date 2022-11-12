def define_matrix(SInputFile):  # заполнение массива числами из файла

    a = []
    isf = 0
    try:
        with open(SInputFile) as f:
            while True:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                if isf == 0:
                    n = int(s[0])
                    isf += 1

                for i in range(0, len(s)):
                    if isf == 1:
                        isf += 1
                        continue
                    a.append(int(s[i]))

    except ValueError:
        print("Error: bad value.")
        f.close()
        return [-1, 0]

    except FileNotFoundError:
        print("Error: file not found.")
        return [-1, 0]

    if isf == 0:
        print("Error: file is empty.")
        return[-1, 0]

    if n == 0:
        print("Error: n = 0.")
        return [-1, n]

    if len(a) == 0:
        print("Error: matrix is empty.")
        return [-1, n]

    if (len(a) % (n * n)) != 0:
        print("Error: matrix not squared.")
        return [-1, n]

    if n * n != len(a):
        print("Error: no correct data - n * n != len(a)")
        return [-1, n]

    return [a, n]


def print_matrix(a, n):

    for i in range(len(a)):
        print(a[i], end = " ")
        if (i + 1) % n == 0:
            print()


def l_order(a, n):  # чтобы понять, упорядочены ли строки, сравним их попарно

    for i in range(n - 1):  # берём i-ую строку (на последней итерации сравниваем предпоследнюю и последнюю строки)
        for j in range(i * n, i * n + n - 1, 1):  # и сравниваем каждый j-ый элемент i-ой и i+1 строк
            if a[j] < a[j + n]:  # если елемент i-ой строки меньше эл-та i+1 строки
                break  # значит, строки i и i+1 упорядочены по возрастанию
            elif a[j] == a[j + n]:  # если эл-ты в строках одинаковые
                continue  # переходим к следующей итерации
            elif a[j] > a[j + 1]:  # если элемент i-ой строки больше эл-та i+1
                return 0  # значит, эти 2 строки упорядочены по убыванию, возращаем ноль

    return 1
def main():

    [arr, n] = define_matrix("1.txt")

    if not isinstance(arr, int):
        print("-------------------")
        print("The original array:")
        print_matrix(arr, n)
        print("-------------------")

        if l_order(arr, n) == 1:
            print("Lexicografic order.")
        elif l_order(arr, n) == 0:
            print("No lexicografic order.")

    return 0


main()