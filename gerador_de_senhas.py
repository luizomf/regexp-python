from random import randint, choice, shuffle


def zero_a_nove():
    return chr(randint(48, 57))


def a_a_z():
    return chr(randint(97, 122))


def A_a_Z():
    return chr(randint(65, 90))


def strange_chars():
    rand_range = [
        randint(32, 47),  # \u0020-\u002F [ -\/]
        randint(58, 64),  # \u003A-\u0040 [:-@]
        randint(91, 96),  # \u005B-\u0060 [[-`]
        randint(123, 126),  # \u007B-\u007E [{-~]
    ]

    # [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
    # [ -\/:-@[-`{-~]

    return chr(choice(rand_range))


def create_pass(
        length=12,
        upper=True,
        lower=True,
        numbers=True,
        chars=True
):
    password = []

    for i in range(length):
        if numbers:
            password.append(zero_a_nove())
        if lower:
            password.append(a_a_z())
        if upper:
            password.append(A_a_Z())
        if chars:
            password.append(strange_chars())

    password = password[:length]
    shuffle(password)
    return ''.join(password)


if __name__ == '__main__':

    print('VÁLIDAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=True,
            numbers=True
        ))
    print()

    print('SEM MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=False,
            numbers=True
        ))
    print()

    print('SEM MINÚSCULAS E NÚMEROS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    print('SEM NÚMEROS CARACTERES E MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=False,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    print('QUANTIDADE INVÁLIDA (6)')
    for i in range(5):
        print(create_pass(
            length=6,
        ))
    print()
