# Первое решение
import random
my_list = [random.randint(1, 21) for i in range(10)]
print(my_list)
smallest = my_list[0] 
smallest_index = 0 # Объявляем перменные для маленького значения и его индекса
for ind, item in enumerate(my_list): # Пробегаемся по списку сразу с индексами
    if item < smallest:
        smallest = item
        smallest_index = ind # Сохраняем индексы чисел, меньших чем текущее
for i in range(smallest_index):
    my_list[i] = 0
print(my_list)


# Второе решение, чуть более питоновское
my_list2 = [random.randint(1, 21) for i in range(10)]
print(my_list2)
for i in range(my_list2.index(min(my_list2))):
    my_list2[i] = 0
print(my_list2)

# Про способы заполнения массива

# Мне показалось, что все ответы подходят
# поэтому я реализую все заполнения здесь

# ПО ФОРМУЛЕ: скажем что i-ый эелмент массива это i**2 
formula_list = [i**2 for i in range(10)]
print(f"Список заданный формулой: {formula_list}")

# ЦИКЛОМ WHILE
while_list = []
x = 0
while x < 10:
    while_list.append(random.randint(1, 5))
    x+=1
print(f"Список заполенный циклом while: {formula_list}")

# СЛУЧАЙНЫМИ ЧИСЛАМИ
random_list = [random.randint(1, 100) for i in range(10)]

# С КЛАВИАТУРЫ
while True:
    try:
        keyboard_list1 = [int(input("Введите число: ")) for i in range(10)]# На разных строках
    except ValueError:
        print("Вы ввели не число")
        continue
    break

while True:
    try:
        keyboard_list2 = [int(i) for i in input().split()]# На одной строке через пробел
    except ValueError:
        print("Вы ввели не число")
        continue
    break

print(f"Список заполенный с клавиатуры в несколько строк: {keyboard_list1}")
print(f"Список заполенный с клавиатуры в одну строк: {keyboard_list2}")

# Присвоение значений
values_list = []
values_list[0] = 8
values_list[1] = 8
values_list[2] = 0
values_list[3] = 0
values_list[4] = 5
values_list[5] = 5
values_list[6] = 5
values_list[7] = 3
values_list[8] = 5
values_list[9] = 3
values_list[10] = 5
print(f"Список заполенный по значениям {values_list}")

# Циклом FOR 
for_list = []
for i in range(10):
    for_list[i] = 2
print(f"Список заполенный FOR {for_list}")

# Вещественными числами

float_list = [3.1, 1.5, 6.7, 5.6, 7.8, 9.0, 4.20, 6.9, 14.88]