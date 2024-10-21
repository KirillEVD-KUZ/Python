# Сумма всех чисел до n

def sum_sequence(n):
    if n > 0:
        return n + sum_sequence(n - 1)
    else:
        return 0


# print(sum_sequence(10))

def print_sequence(n):
    if n > 0:
        print(n, end=' ')
        print_sequence(n - 1)


print_sequence(10)