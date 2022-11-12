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


def l_order(a, n):
    count = 0
    for i in range(n):
        j = i + i * n
        print("i =", i)
        # print("n * n - (2 + i) * n - i + 1 =", n * n - (2 + i) * n - i + 1)
        # print("j =", j)
        # print()
        while j < n * n - n - i + 1:
            print("j =",j, " & n * n - n - i + 1 = ",n * n - n - i + 1)
            if j 
            # print("n * n - (2 + i) * n + i + 1 =", n * n - (2 + i) * n + i + 1)
            # print()
            if a[j + i * n] <= a[j + (i + 1) * n]:
                count += 1
                print("done:", a[j], " <= ", a[j + n])
                print()
            else:
                print("false:", a[j], " > ", a[j + n])
            j += n
        # if count !=  n - i - 1:
        #     print("for i =", i, " return 0")
        #     return 0
        # else:
        #     print("for i =", i, "count = 0")
        #     count = 0
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