import game_exceptions
import models
import settings


"""
Містить блок на перевірку імені модуля (main)
В середині if блок try/except.
try запускає функцію play()
except обробляє два винятки:
GameOver - виводить на екран повідомлення про завершення гри, 
записує результат в таблицю рекордів.
KeyboardInterrupt - pass.
finally виводить на екран "Good bye!"
"""
def exit():
    pass

def play():
    flag_name = True
    while flag_name:
        flag_name = False
        name = input('Please, enter your "name" : ')
        try:
            for i in name:
                if i.isdigit():
                    raise ValueError("The name must not numbers!")
        except ValueError:
            print("The name must not numbers!!")
            flag_name = True
    print("----------------------------------------\n"
          "May the Force be with you!\n"
          "----------------------------------------\n"
          "****************************************")
    settings.GAME_LEVEL = 1
    player = models.Player(name, settings.PLAYER_LIVES, settings.score)
    enemy = models.Enemy(settings.ENEMY_LEVEL)
    while True:
        if player.attack(enemy.select_attack()) is False:
            enemy.decrease_lives()
        print(f'Your lives {player.lives} | score {player.score}| Enemy lives: {enemy.lives}')
        player.defence(enemy.select_attack())
        print(f'Your lives {player.lives} | score {player.score}| Enemy lives: {enemy.lives}')

    game.play()

if __name__ == '__main__':
    while True:
        print("*------------Welcome to Game!----------*")
        command = input('Type "start" or "help" \nor "exit" or "show scores":')
        if command == 'help':
            print(settings.HELP_INFORMATION)
        elif command == 'start':
            break
        elif command == 'show scores':
            file = open('scores.txt', 'a+')
            file.read()
        elif command == 'exit':
            print('Good bye!!!')
            exit()
        else:
            print('Wrong command!\n'
                  'Try again')
    try:
        play()
    except game_exceptions.GameOver as err:
        print(f'Game Over!!! {err}')
    except game_exceptions.EnemyDown as e:
        print(f'Enemy down!{e}')
        settings.score +=5
        settings.GAME_LEVEL +=1
        enemy = models.Enemy(settings.ENEMY_LEVEL)
    except KeyboardInterrupt:
        print('Wrong command!\n'
              'Try again')
    finally:
        print('Good bye!!!')
