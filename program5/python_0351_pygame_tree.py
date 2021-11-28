import pygame


class PyGameTree:

    def __init__(self):

        # Step 1) prepare pygame screen
        self.screen_width = 800
        self.screen_height = 600
        self.screen_size = self.screen_width, self.screen_height
        pygame.display.set_mode(self.screen_size)

        # Step 2) set title
        pygame.display.set_caption("Green Tree")


    def begin(self):

        # Step 1) init pygame
        pygame.init()




if __name__ == '__main__':
    game = PyGameTree()
    game.begin()