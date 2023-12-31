import pygame
from pygame.locals import *
from constantes import *


class Widget:
    def __init__(
        self,
        master_form,
        x,
        y,
        w,
        h,
        color_background,
        color_border,
        image_background,
        is_active,
        text,
        font,
        font_size,
        font_color,
    ):
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self._text = text
        self.color_background = color_background
        self.color_border = color_border
        self.is_active = is_active

        if image_background != None:
            self.set_background_image(image_background)
        else:
            self.image_background = None

        if self._text != None:
            pygame.font.init()
            self._font_sys = pygame.font.SysFont(font, font_size)
            self._font_color = font_color

    def set_background_image(self, image_background):
        self.image_background = pygame.image.load(image_background)
        self.image_background = pygame.transform.scale(
            self.image_background, (self.w, self.h)
        ).convert_alpha()

    def render(self):
        self.slave_surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.color_background:
            self.slave_surface.fill(self.color_background)

        if self.image_background:
            self.slave_surface.blit(self.image_background, (0, 0))

        if self._text != None:
            image_text = self._font_sys.render(
                self._text, True, self._font_color, self.color_background
            )
            self.slave_surface.blit(
                image_text,
                [
                    self.slave_rect.width / 2 - image_text.get_rect().width / 2,
                    self.slave_rect.height / 2 - image_text.get_rect().height / 2,
                ],
            )

        if self.color_border:
            pygame.draw.rect(
                self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2
            )

    def update(self):
        pass

    def draw(self):
        if DEBUG:
            pygame.draw.rect(
                self.master_form.surface,
                color=(0, 255, 0),
                rect=self.slave_rect_collide,
            )
            pygame.draw.rect(
                self.master_form.surface, color=(255, 0, 0), rect=self.slave_rect
            )

        self.master_form.surface.blit(self.slave_surface, self.slave_rect)
