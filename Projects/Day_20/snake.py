from turtle import Turtle
import random

X_INIT = random.randint(-240,240)
Y_INIT = random.randint(-280,280)
MOVE_DISTANCE = 20
# STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
STARTING_POSITION = [(X_INIT,Y_INIT), (X_INIT-20,Y_INIT), (X_INIT-40,Y_INIT)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments = [Turtle(shape="square") for _ in range(3)]
        for segment in self.segments:
            segment.color("white")
            segment.penup()
            segment.goto(STARTING_POSITION[self.segments.index(segment)])
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)