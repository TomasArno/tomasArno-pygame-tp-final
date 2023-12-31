import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class Button(Widget):
    def __init__(
        self,
        master,
        x=0,
        y=0,
        w=200,
        h=50,
        color_background=C_GREEN,
        color_border=C_RED,
        image_background=None,
        is_active=True,
        text=None,
        font="Arial",
        font_size=14,
        font_color=C_BLUE,
        on_click=None,
        on_click_param=None,
    ):
        super().__init__(
            master,
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
        )

        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.render()

    def inactive(self):
        self.is_active = False

    def update(self, lista_eventos):
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.slave_rect_collide.collidepoint(evento.pos):
                    if self.on_click:
                        self.on_click(self.on_click_param)

        self.render()

    def render(self):
        super().render()
        if self.state == M_STATE_HOVER:  # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD)
        elif self.state == M_STATE_CLICK:  # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB)
