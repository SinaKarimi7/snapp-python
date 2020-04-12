class Character:
    def __init__(self, name):
        self.name = name
        self.position = {}
        pass

    def move(self, x, y):
        self.position['x'] = x
        self.position['y'] = y

class Human(Character):
    def move(self, x, y):
        print("I'm moving")
        super().move(x, y)

class Bird(Character):
    def move(self, x, y):
        print("I'm flying")
        super().move(x, y)

class Engine:
    def move_character(self, character, x, y):
        character.move(x, y)