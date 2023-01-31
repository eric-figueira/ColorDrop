import pygame


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 3

    def setAll(self, model):
        self.x = model.x
        self.y = model.y
        self.width = model.width
        self.height = model.height
        self.rect = (model.x, model.y, model.width, model.height)
        self.vel = model.vel

    def draw(self, window, color):
        pygame.draw.rect(window, color, self.rect)

    def move(self, has_game_started, board_top_left, board_top_right, board_bottom_left, board_bottom_right):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_LEFT]:
        #
        #     # Cannot enter the board if the game isn't started
        #     # Cannot leave the "map"
        #     if 0 < self.x:
        #         # Cannot leave the board if the game is started
        #         if has_game_started:
        #             if board_top_left[0] < self.x < board_bottom_left[0] - self.height and self.y > board_top_left[1]:
        #                 self.x -= self.vel
        #         # else?
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


