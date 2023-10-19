# я не фанат Бангладеша, ноо...

# 1
upper = 8
lower = 8

print('1. Флаг Бангладеша:')
for line in range(8):
    print(u"\u001b[42m")

print(u"\u001b[42m                                                \u001b[41m                              \u001b[42m")
print(u"\u001b[42m                                            \u001b[41m                                      \u001b["
      u"42m")
print(u"\u001b[42m                                     \u001b[41m                                                    "
      u"\u001b[42m")
print(u"\u001b[42m                                \u001b[41m                                                          "
      u"     \u001b[42m")
print(u"\u001b[42m                             \u001b[41m                                                             "
      u"         \u001b[42m")
print(u"\u001b[42m                           \u001b[41m                                                               "
      u"           \u001b[42m")
print(u"\u001b[42m                          \u001b[41m                                                                "
      u"            \u001b[42m")
print(u"\u001b[42m                         \u001b[41m                                                                 "
      u"             \u001b[42m")
print(u"\u001b[42m                       \u001b[41m                                                                   "
      u"               \u001b[42m")
print(u"\u001b[42m                      \u001b[41m                                                                    "
      u"                \u001b[42m")
print(u"\u001b[42m                      \u001b[41m                                                                    "
      u"                \u001b[42m")
print(u"\u001b[42m                      \u001b[41m                                                                    "
      u"                \u001b[42m")
print(u"\u001b[42m                      \u001b[41m                                                                    "
      u"                \u001b[42m")
print(u"\u001b[42m                       \u001b[41m                                                                   "
      u"               \u001b[42m")
print(u"\u001b[42m                         \u001b[41m                                                                 "
      u"             \u001b[42m")
print(u"\u001b[42m                          \u001b[41m                                                                "
      u"            \u001b[42m")
print(u"\u001b[42m                           \u001b[41m                                                               "
      u"           \u001b[42m")
print(u"\u001b[42m                             \u001b[41m                                                             "
      u"         \u001b[42m")
print(u"\u001b[42m                                \u001b[41m                                                          "
      u"     \u001b[42m")
print(u"\u001b[42m                                     \u001b[41m                                                    "
      u"\u001b[42m")
print(u"\u001b[42m                                            \u001b[41m                                      \u001b["
      u"42m")
print(u"\u001b[42m                                                \u001b[41m                              \u001b[42m")

for line in range(8):
    print(u"\u001b[42m")
print(u"\u001b[0m\n\n")
# 2
print('2. Узор b:')
multiplier = 10

print()
print()
print(u"\u001b[40m          \u001b[47m      " * multiplier)
print(u"\u001b[40m  \u001b[47m      \u001b[40m  \u001b[47m      " * multiplier)
print(u"\u001b[40m  \u001b[47m  \u001b[40m      \u001b[47m      " * multiplier)
print(u"\u001b[40m  \u001b[47m  \u001b[40m  \u001b[47m          " * multiplier)
print(u"\u001b[40m  \u001b[47m  \u001b[40m            \u001b[47m" * multiplier)
print(u"\u001b[0m\n\n")

# 3
print('3. График')
coordinates = [(2 * x + 3) for x in range(9, 0, -1)]
max_coord = max(coordinates)
len_coordinates = len(coordinates)

ordinate = '|'
abscissa = '_'
step = ' ' * (len_coordinates - 1)
point = '*'

for line in range(max_coord, 0, -1):
    if line == 1:
        print(f'{ordinate}{abscissa * len_coordinates}')
    elif line not in coordinates:
        print(ordinate)
    else:
        print(f'{ordinate}{step}{point}')
        step = step[:-1]

# 4
print('4. Диаграмма процентного соотношения суммы модуля первых 125 чисел и вторых 125 чисел по отношению к общей '
      'сумме:')

shkala = '|'

with open('sequence.txt') as file:
    dataFile = file.readlines()
    dataFile = [float(line.rstrip()) for line in dataFile]
    first = 0
    second = 0
    allsum = 0
    for num in dataFile[0:125]:
        first += abs(num)
    for num in dataFile[126:250]:
        second += abs(num)
    for num in dataFile:
        allsum += abs(num)
    per_one = round((first / allsum) * 100)
    per_two = round((second / allsum) * 100)
    x = u"\u001b[40m    \u001b[0m"
    y = u"\u001b[47m    \u001b[0m"
    for line in range(100, -1, -1):
        if per_one >= line and per_two >= line:
            print(shkala + x + y)
        elif per_one >= line > per_two:
            print(shkala + x)
        elif per_two >= line > per_one:
            print(shkala + '    ' + y)
        else:
            print(shkala)


