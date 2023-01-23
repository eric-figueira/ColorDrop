import pygame


width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Player:

    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = width // 2 - self.width
        self.y = height // 2 - self.height
        self.color = (255,0,0)
        self.vel = 0.5
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)



def drawWindow(win, player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = Player()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        drawWindow(win, p)

main()