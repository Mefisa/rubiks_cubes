# we have 6 colours in a rubik's cube and we
# can represent each colour as a number

from enum import Enum
import colorama
from colorama import Fore

class Colour(Enum):
    WHITE = "WHITE"
    ORANGE = "ORANGE"
    GREEN = "GREEN"
    RED = "RED"
    YELLOW = "YELLOW"
    BLUE = "BLUE"

class Direction(Enum):
    CLOCKWISE = "CLOCKWISE"
    COUNTER_CLOCKWISE = "COUNTER CLOCKWISE"

face0 = [[Colour.WHITE, Colour.WHITE],
        [Colour.WHITE, Colour.WHITE]]

face1 = [[Colour.ORANGE, Colour.ORANGE],
        [Colour.ORANGE, Colour.ORANGE]]

face2 = [[Colour.GREEN, Colour.GREEN],
        [Colour.GREEN, Colour.GREEN]]

face3 = [[Colour.RED, Colour.RED],
        [Colour.RED, Colour.RED]]

face4 = [[Colour.YELLOW, Colour.YELLOW],
        [Colour.YELLOW, Colour.YELLOW]]

face5 = [[Colour.BLUE, Colour.BLUE],
        [Colour.BLUE, Colour.BLUE]]

class Cube:
    def __init__(self):
        self.cube = [list(face0), list(face1), list(face2), list(face3), list(face4), list(face5)]
    
    def display(self, face_number):
        print("------------------")
        for row in self.cube[face_number]:
            print(f"| {row[0].value} | {row[1].value} |")
            print("------------------")

    def _rotate_face(self, direction, face):
        print(f"[INFO] Rotating face {face} in direction {direction.value}")
        # this function rotates the face in the given direction AS IF we were looking at the face
        if direction == Direction.CLOCKWISE:
            old_face = self.cube[face]
            new_face = [[old_face[1][0], old_face[0][0]], [old_face[1][1], old_face[0][1]]]
            self.cube[face] = new_face
        else:
            old_face = self.cube[face]
            new_face = [[old_face[0][1], old_face[1][1]], [old_face[0][0], old_face[1][0]]]
            self.cube[face] = new_face

    def _switch_columns(self, faces, column):
        print(f"[INFO] Rotating {faces} in column {column}")
        # this function switches the columns of the faces in order
        # i.e the column on faces[0] is written on to faces[1] and the column on faces[1] are written on to faces[2]
        temp_col = [self.cube[faces[-1]][0][column], self.cube[faces[-1]][1][column]]
        for i in range(4):
            starting_face = self.cube[faces[i]]
            face_column = [starting_face[0][column], starting_face[1][column]]
            starting_face[0][column] = temp_col[0]
            starting_face[1][column] = temp_col[1]
            temp_col = face_column
    
    def right(self):
        # rotate face 3 clockwise
        self._rotate_face(Direction.CLOCKWISE, 3)
        # rotate columns
        self._switch_columns([2,0,5,4], 1)
    
    def right_prime(self):
        # turn right 3 times
        self.right()
        self.right()
        self.right()

    def left(self):
        # rotate face 1 clockwise
        self._rotate_face(Direction.CLOCKWISE, 1)
        # rotate columns
        self._switch_columns([2, 4, 5, 0], 0)
    
    def left_prime(self):
        self.left()
        self.left()
        self.left()

    def up(self):
        # rotate face 0 clockwise
        self._rotate_face(Direction.CLOCKWISE, 0)

cube = Cube()
cube.left_prime()
cube.display(2)
cube.display(0)
cube.display(5)
cube.display(4)


