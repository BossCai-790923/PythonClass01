import math

import pygame
import random

class PyGameTree:

    def __init__(self):

        # Step 1) prepare pygame screen
        self.screen_width = 800
        self.screen_height = 600
        self.screen_size = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.screen_size)

        # Step 2) set title
        pygame.display.set_caption("Green Tree")


    def begin(self):

        # Step 1) init pygame
        pygame.init()

        # Step 2) draw the tree
        root_x = self.screen_width / 2
        root_y = self.screen_height - 10
        line_segment_angle = -90

        self.draw_line_segment(root_x, root_y, line_segment_angle, 12)
        # the function is a recursive function, so we pass in depth param - 12

        pygame.display.update()




    def draw_line_segment(self, x1, y1, theta, depth):
        '''
        x1, y1: line segment start point coordinates
        theta: line segment angle
        depth: recursive call repeat time param
        '''

        # base case
        if depth <= 0:
            return

        '''
        math.radians(theta) -> convert degree to radians, so that we calculate cos(theta) & sin(theta)
        When we first time call the function, theta is -90
        
        cos(-90) = 0
        sin(-90) = -1
        
        The value is too small, so we need to amplify it
        
        So we: * depth * rand_length
        '''
        rand_length = random.randint(1, 10)
        x2 = x1 + int(math.cos(math.radians(theta)) * depth * rand_length)
        y2 = y1 + int(math.sin(math.radians(theta)) * depth * rand_length)


        '''
        The color is represented in the RGB format
        Hence, (0, 255, 0) means green. (255, 0, 0) means red.
        '''

        if(depth < 5):
            color = (0, 255, 0) # green
        else:
            color = (255, 255, 255) # white

        pygame.draw.line(self.screen, color, (x1,y1), (x2,y2), 2)

        # Finally, there is a recursive call
        rand_angle = random.randint(10, 20)
        self.draw_line_segment(x2, y2, theta - rand_angle, depth - 1)
        self.draw_line_segment(x2, y2, theta + rand_angle, depth - 1)




if __name__ == '__main__':
    game = PyGameTree()
    game.begin()