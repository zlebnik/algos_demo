# Задача: "Комбинации"
# На вход подается строка из нажатий на клавиатуру телефона (цифровую)
# На выходе ожидается весь набор возможных выходных строк,
# которые можно было набрать такой комбинацией цифр
# Пример:
# 34
# dg
# dh
# di
# eg
# eh
# ei
# fg
# fh
# fi

nmbs = [
    [],
    [],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z'],
]

# 3, 4
#

def get_combinations(lst):
    i, rest = lst[0], lst[1:]

    if not rest:
        return nmbs[i]

    return [
        el + x
            for x in get_combinations(rest)
                for el in nmbs[i]
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keys = '347'
    print(' '.join((get_combinations([
        int(x) for x in keys
    ]))))

