def test(value, *year, name='Арман', **years):
    print('тип', type(years))
    print('Аргумент:', years)
    for key, value in years.items():
        print(key, value)
    print(year)

test(43, 1, 9, 8, 0, name='Арман', num=26, month='november')


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))
