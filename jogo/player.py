import pygame


class Player:
    def __init__(self, x, y, w, h, id):
        self.id = id
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 3
        self.is_dead = False

    def setAll(self, model):
        self.x = model.x
        self.y = model.y
        self.width = model.width
        self.height = model.height
        self.rect = (model.x, model.y, model.width, model.height)
        self.vel = model.vel
        self.is_dead = model.is_dead
        self.id = model.id

    def draw(self, window, color):
        pygame.draw.rect(window, color, self.rect)

    def move(self, has_game_started, board_top_left, board_top_right, board_bottom_left, board_bottom_right, win_w, win_h):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if has_game_started:
                if self.x > board_top_left[0]:
                    self.x -= self.vel
            else:
                if self.x > 0:
                    self.x -= self.vel

        if keys[pygame.K_UP]:
            if has_game_started:
                if self.y > board_top_left[1]:
                    self.y -= self.vel
            else:
                if self.y > 0:
                    self.y -= self.vel

        if keys[pygame.K_RIGHT]:
            if has_game_started:
                if self.x < board_top_right[0] - self.width:
                    self.x += self.vel
            else:
                if self.x < win_w - self.width:
                    self.x += self.vel

        if keys[pygame.K_DOWN]:
            if has_game_started:
                if self.y < board_bottom_left[1] - self.height:
                    self.y += self.vel
            else:
                if self.y < win_h - self.height:
                    self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


