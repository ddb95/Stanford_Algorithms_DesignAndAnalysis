from math import ceil, floor


def karatsuba(number1, number2):
    if number1 < 10 and number2 < 10:
        return number1 * number2

    n1 = ceil(max(floor(len(list(str(number1))) / 2), floor(len(list(str(number2))) / 2)))
    m_x = floor(number1 / (10 ** n1))
    m_y = floor(number1 % (10 ** n1))
    n_x = floor(number2 / (10 ** n1))
    n_y = floor(number2 % (10 ** n1))
    a = karatsuba(m_x, n_x)
    b = karatsuba(m_y, n_y)
    e = karatsuba(m_x + m_y, n_x + n_y) - a - b
    return int((a * (10 ** (n1 * 2))) + (e * (10 ** n1)) + b)


if __name__ == "__main__":
    n1 = int(input('Enter the first number '))
    n2 = int(input('Enter the second number '))
    print(karatsuba(n1, n2))
