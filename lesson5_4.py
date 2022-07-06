# Пример 25
def add_numbers(first, second):
    print("add_numbers called with", first, second)
    return first + second

add_numbers(9, 10)
result = add_numbers(2, 3) - add_numbers(1, 2)
print(result)