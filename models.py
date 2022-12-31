import random
import settings
import game_exceptions

"""
class Enemy:
Атрибути класу - level, lives.
Конструктор приймає тільки аргумент level. 
Кількість життів = рівень противника
"""
class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = settings.PLAYER_LEVEL

    @staticmethod
    def select_attack():
        return random.randint(1, 3)
    """
    select_attack(): повертає випадкове число від 1 до 3
    """
    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.EnemyDown
        """
        decrease_lives(self): зменшує кількість життів на 1. 
        Коли життів стає 0, викликає виняток EnemyDown.
        """
class Player:
    def __init__(self, name, lives, score=0, allowed_attacks=None):
        self.name = name
        self.lives = lives
        self.score = 0
        self.allowed_attacks = allowed_attacks
        self.level = settings.PLAYER_LEVEL
        """
        class Player:
Атрибути: name, lives, score, allowed_attacks.
Конструктор приймає ім'я гравця.
Кількість життів отримується з settings.
Рахунок дорівнює нулю.
        """
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
        """
        статичний fight(attack, defense) - повертає результат атаки/захисту:
        0 нічия
-1 aтака/захист невдалі.
1 атака/захист вдалі.
        """
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
        """
        attack(self, enemy_obj)
отримує input (1, 2, 3) від користувача;
обирає атаку противника з об'екту enemy_obj;
викликає метод fight();
Якщо результат 0 - вивести "It's a draw!"
Якщо 1 = "You attacked successfully!" та зменшує кількість життів противника на 1;
Якщо -1 = "You missed!"
        """
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
        """
        defence(self, enemy_obj) - такий самий, як метод attack(), 
        тільки в метод fight першим передається атака противника,
        та при вдалій атаці противника викликається метод decrease_lives гравця.

        """
    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.GameOver(f'{self.name} score: {self.score}')
        file = open('scores.txt', 'a+')
        file.write(f'Name: {self.name} |score: {self.score}\n')
        file.read()
        file.close()
        """
        decrease_lives(self) - те саме, що і Enemy.decrease_lives(),
         викликає виняток GameOver.
        """