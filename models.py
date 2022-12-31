import random
import settings
import game_exceptions

class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = settings.PLAYER_LEVEL

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.EnemyDown

class Player:
    def __init__(self, name, lives, score=0, allowed_attacks=None):
        self.name = name
        self.lives = lives
        self.score = 0
        self.allowed_attacks = allowed_attacks
        self.level = settings.PLAYER_LEVEL

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        if attack == 1 and defense == 2:
            return 1
        if attack == 1 and defense == 3:
            return -1
        if attack == 2 and defense == 3:
            return 1
        if attack == 2 and defense == 1:
            return -1
        if attack == 3 and defense == 1:
            return 1
        if attack == 3 and defense == 2:
            return -1

    @staticmethod
    def usr_input_num():
        flag = True
        while flag:
            usr_input = input('Select to Use: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE : ')
            if len(usr_input) == 1 and usr_input in '123':
                flag = False
                return int(usr_input)
            else:
                print("The input must be from numbers and result from 1 to 3!")

    def attack(self, enemy_obj):
        attack = self.usr_input_num()
        attack_res = self.fight(attack, enemy_obj)
        if attack_res == 0:
            print('It`s a draw!')
            print("--------------------------------------------------------------")
        elif attack_res == 1:
            print('You attacked successfully!')
            print("--------------------------------------------------------------")
            self.score += 1
            return False
        elif attack_res == -1:
            print('Your attack not successful!')
            print("--------------------------------------------------------------")

    def defence(self, enemy_obj):
        defence = self.usr_input_num()
        defence_res = self.fight(enemy_obj, defence)
        if defence_res == 0:
            print('It`s a draw!')
            print("-------------------------------------------------------------")
        elif defence_res == 1:
            print('Enemy attack successfully!')
            print("-------------------------------------------------------------")
            self.decrease_lives()
        elif defence_res == -1:
            print('Enemy attack is not successful!')
            print("-------------------------------------------------------------")

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.GameOver(f'{self.name} score: {self.score}')
        file = open('scores.txt', 'a+')
        file.write(f'Name: {self.name} |score: {self.score}\n')
        file.read()
        file.close()
