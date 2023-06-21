from constantes import *
from auxiliar import Auxiliar


class Player:
    def __init__(
        self,
        x,
        y,
        speed_walk,
        speed_run,
        gravity,
        jump_velocity,
        frame_rate_ms,
        jump_high,
    ) -> None:
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(
            "images/caracters/stink/idle.png",
            16,
            1,
        )

        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(
            "images/caracters/stink/idle.png",
            16,
            1,
            True,
        )

        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(
            "images/caracters/stink/walk.png",
            15,
            1,
        )[:12]

        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(
            "images/caracters/stink/walk.png",
            15,
            1,
            True,
        )[:12]

        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(
            "images/caracters/stink/jump.png", 33, 1, False
        )
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(
            "images/caracters/stink/jump.png", 33, 1, True
        )

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_velocity = jump_velocity
        self.jump_high = jump_high
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time_elapsed_ms = 0
        self.frame_rate_ms = frame_rate_ms
        self.jump_starting_pos_y = 0
        self.view_direction = VIEW_DIRECTION_R
        self.is_jump = False

    def stay(self):
        if self.animation != self.stay_l and self.animation != self.stay_r:
            if self.view_direction:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l

            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def walk(self, view_direction):
        if self.view_direction != view_direction or (
            self.animation != self.walk_l and self.animation != self.walk_r
        ):
            self.frame = 0
            self.view_direction = view_direction

            if self.view_direction:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l

    def jump(self, is_jump):
        if is_jump and not self.is_jump:
            self.jump_starting_pos_y = self.rect.y

            if self.view_direction:
                self.animation = self.jump_r
                self.move_x = self.speed_walk
            else:
                self.animation = self.jump_l
                self.move_x = -self.speed_walk

            self.is_jump = True
            self.move_y = -self.jump_velocity
            self.frame = 0

        else:
            self.is_jump = False
            self.stay()

    def update_moves(self, delta_ms):
        self.time_elapsed_ms += delta_ms

        if self.time_elapsed_ms >= self.frame_rate_ms:
            self.time_elapsed_ms = 0

            # print(abs(self.jump_starting_pos_y - self.rect.y))
            # print(self.jump_starting_pos_y)
            print(
                self.rect.y
            )  # Se va a ver el resultado de la resta entre jump_velocity and self.gravity que se ejecuta constantemente

            # if abs(self.jump_starting_pos_y - self.rect.y) > 200 and self.is_jump: Que simboliza esa resta?
            if self.rect.y <= self.jump_high and self.is_jump:
                self.move_y = 0

            self.rect.x += self.move_x
            self.rect.y += self.move_y

            if self.rect.y < 500:
                self.rect.y += self.gravity

    def update_animations(self, delta_ms):
        self.time_elapsed_ms += delta_ms

        if self.time_elapsed_ms >= self.frame_rate_ms:
            self.time_elapsed_ms = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    def update(self, delta_ms):
        self.update_animations(delta_ms)
        self.update_moves(delta_ms)

    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
