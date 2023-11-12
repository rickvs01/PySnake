from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        random_x = random.randint(-710, 710)
        random_y = random.randint(-460, 460)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-710, 710)
        random_y = random.randint(-460, 460)
        self.goto(random_x, random_y)
