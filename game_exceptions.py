class ValueError(Exception):
    pass


class KeyboardInterrupt(Exception):
    pass


class GameOver(Exception):
    """
    клас GameOver - унаслідований від Exception.
    В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню
    """


class EnemyDown(Exception):
    pass