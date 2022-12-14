# Guido van Rossum <guido@python.org>

def step2_umbrella():
    print('Дождь пошел и зонтик пригодился!')


def step2_no_umbrella():
    print('Дождь не пошел и зонтик не пригодился!')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()