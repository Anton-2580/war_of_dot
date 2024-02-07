import pygame
import math
import numpy as np


class Game:
    def __init__(self):
        pygame.init()

        info = pygame.display.Info()
        self.display = pygame.display.set_mode((info.current_w - 100, info.current_h - 100), pygame.RESIZABLE)
        self.size = self.width, self.height = pygame.display.get_window_size()

        self.count_cell_in_row = 10
        self.cell_size = self.width / self.count_cell_in_row

        self.field = np.zeros((math.ceil(self.height / self.cell_size) + 1, self.count_cell_in_row + 1))

    def resize(self):
        self.size = self.width, self.height = pygame.display.get_window_size()
        self.cell_size = self.width / self.count_cell_in_row

        if self.field.size / self.count_cell_in_row < self.height / self.cell_size:
            self.field.resize((math.ceil(self.height / self.cell_size) + 1, self.count_cell_in_row + 1), refcheck=False)

    def paint_cell(self, event_click):
        if not event_click:
            return

        pos = event_click.pos
        x, y = round(pos[0] / self.cell_size), round(pos[1] / self.cell_size)

        self.field[y][x] = 1

    def draw_field(self):
        self.display.fill((255, 255, 255))
        for x in range(self.count_cell_in_row):
            pygame.draw.line(self.display, (0, 0, 200), (x * self.cell_size, 0), (x * self.cell_size, self.height))

        for y in range(math.ceil(self.height / self.cell_size)):
            pygame.draw.line(self.display, (0, 0, 200), (0, y * self.cell_size), (self.width, y * self.cell_size))

    def start(self):
        while True:
            event_click = None
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT: return pygame.quit()
                    case pygame.WINDOWSIZECHANGED: self.resize()
                    case pygame.MOUSEBUTTONUP: event_click = event

            self.draw_field()
            self.paint_cell(event_click)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.start()
