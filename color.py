import random
class Color:
    def __init__(self, r=0, g=0, b=0):
        self.rgb = [r + random.randint(0, 255),b+ random.randint(0, 255),g+ random.randint(0, 255)]

    def get(self):
        return self.rgb

    def add(self, number):
        for i in range(len(self.rgb)):
            if number > 0:
                if self.rgb[i] < 255:
                    if self.rgb[i] + number <= 255:
                        self.rgb[i] += number
                        number = 0
                    else:
                        number -= 255 - self.rgb[i]
                        self.rgb[i] += 255 - self.rgb[i]

    def set(self, number):
        self.rgb = [0, 0, 0]
        self.add(number)
