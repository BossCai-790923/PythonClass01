'''
Requirement:
Our next PyGame code needs to add some animation.
Let's add a bouncing ball to the PyGame screen. And we make the ball keep on bouncing and never stop.
'''

import pygame



class Ball:

    def __init__(self, screen):
        self.screen = screen
        self.ball_surface = pygame.image.load("python_0370_pygame_bouncing_ball.gif")
        '''
        Q) What is surface?
        A) In pygame, we don't say image, we say surface. All images are called surface.
        '''

        self.ball_rect = self.ball_surface.get_rect()
        '''
        Q) What is rectangle?
        A) A rectangle means a rectangle on the screen. You can move it. You can merge 2 rectangles. You can check whether 2 rectangles collide with each other.
        
        Q) How to create a rectangle? 
        A) If you have a surface, you simply call surface.get_rect(), you will get a new rectangle 
        '''

    def show(self):
        self.screen.blit(self.ball_surface, self.ball_rect)
        '''
        Q) What's blit?
        A) In pygame, we don't say : show a image on the screen.
                      we say:        blit a surface on the screen.
        Q) Where do we blit the ball surface in the screen?
           Inside the ball rectangle
        '''



class BallGame:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen_size = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.ball = Ball(self.screen)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def begin(self):
        pygame.init()
        while True:
            self.handle_events()
            self.ball.show()
            pygame.display.flip()   # flip means, refresh the screen.


if __name__ == '__main__':
    game = BallGame()
    game.begin()
