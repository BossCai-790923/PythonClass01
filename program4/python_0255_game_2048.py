import random



class Game2048:

    def __init__(self):
        self.grid = []
        for i in range(4):
            self.grid.append(['_'] * 4)

        self.generate_number()
        self.generate_number()
        self.print_me()




    @staticmethod
    def merge_number(*row):

        pass








    def up(self):


        # handle the 1st column: self.grid[0,0], self.grid[1,0], self.grid[2,0], self.grid[3,0]
        # handle the 2nd column: self.grid[0,1], self.grid[1,1], self.grid[2,1], self.grid[3,1]
        # handle the 3rd column: self.grid[0,2], self.grid[1,2], self.grid[2,2], self.grid[3,2]
        # handle the 4th column: self.grid[0,3], self.grid[1,3], self.grid[2,3], self.grid[3,3]

        for y in range(4):

            # handle self.grid[0,y], self.grid[1,y], self.grid[2,y], self.grid[3,y]
            if self.grid[0,y] == '_' and self.grid[1,y] == '_' and self.grid[2,y] == '_' and self.grid[3,y] == '_':
                continue

            self.grid[0,y], self.grid[1,y], self.grid[2,y], self.grid[3,y] = Game2048.merge_number(self.grid[0,y], self.grid[1,y], self.grid[2,y], self.grid[3,y])






        self.print_me()







    def down(self):
        self.print_me()

    def left(self):
        self.print_me()

    def right(self):
        self.print_me()




    def print_me(self):
        print('---------------------')
        for line in self.grid:
            print(*line)



    def generate_number(self):
        '''
        Game starts with 2 random numbers ( being 2 or 4) at random position.
        After each user's move, a new random number (being 2 or 4) will appear in a random position.
        '''
        new_number = random.randint(1, 2) * 2 # random.randint(1, 2) generates either 1 or 2
        x, y = self.generate_random_available_position()
        self.grid[x][y] = new_number



    def generate_random_available_position(self):
        x = random.randint(0, 3)
        y = random.randint(0, 3)

        while self.grid[x][y] != '_':
            x = random.randint(0, 3)
            y = random.randint(0, 3)

        return x, y


# MAIN PROGRAM BEGIN ==============================


if __name__ == '__main__':

    game = Game2048()

    while True:

        action = input("Action: ")

        if 'up' == action or 'w' == action:
            game.up()

        elif 'down' == action or 's' == action:
            game.down()

        elif 'left' == action or 'a' == action:
            game.left()

        elif 'right' == action or 'd' == action:
            game.right()

        else:
            print("Unrecognized operation!")