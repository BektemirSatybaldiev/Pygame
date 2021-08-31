<<<<<<< HEAD
import pygame, os

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх по оси Y"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю красиво"""
        pygame.draw.rect(self.screen, self.color, self.rect)

=======
import pygame, os

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх по оси Y"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю красиво"""
        pygame.draw.rect(self.screen, self.color, self.rect)

>>>>>>> cf059a02c6da10d8f4d4a86e869e4d0ce6164e43
