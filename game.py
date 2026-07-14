class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        i = 0
        for _ in range(10):
            total += self.rolls[i] + self.rolls[i + 1]
            i += 2
        return total
