####################################################################################################
# Задача №1 Игра "Камень, Ножницы, Бумага, Ящерица, Спок"
# rock paper scissors lizard spock
####################################################################################################
import random
####################################################################################################
CONFIRMATION = ['Y', 'N']
SHAPE = ['rock', 'lizard', 'spock', 'scissors', 'paper']
####################################################################################################


def determining_the_winner(shape_input):
    shape_rand = random.choice(SHAPE)
    if (SHAPE[SHAPE.index(shape_input) - 4] == shape_rand or
            SHAPE[SHAPE.index(shape_input) - 2] == shape_rand):
        print(f'Player: {shape_input}')
        print(f'Computer: {shape_rand}')
        print('Player WIN!')
    elif (SHAPE[SHAPE.index(shape_rand) - 4] == shape_input or
            SHAPE[SHAPE.index(shape_rand) - 2] == shape_input):
        print(f'Player: {shape_input}')
        print(f'Computer: {shape_rand}')
        print('Computer WIN!')
    else:
        print(f'Player: {shape_input}')
        print(f'Computer: {shape_rand}')
        print('Draw game')


def checking_input(data_check):
    user_input = ''
    while not (user_input in data_check):
        if data_check == SHAPE:
            print('Your choice (rock paper scissors lizard spock)?')
            user_input = input()
        else:
            user_input = input('Repeat (Y/N)')
        if user_input == '':
            print('Invalid input "Not entered"')
        elif not (user_input in data_check):
            print(f'Invalid input "{user_input}"')
    return user_input


if __name__ == '__main__':
    continue_game = 'Y'
    while continue_game == 'Y':
        determining_the_winner(checking_input(SHAPE))
        continue_game = checking_input(CONFIRMATION)
