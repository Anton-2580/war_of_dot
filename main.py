import pygame


class Game:
    def __init__(self):
        pygame.init()

        info = pygame.display.Info()
        print(info)
        pygame.display.set_mode((info.current_w - 100, info.current_h - 100), pygame.RESIZABLE)
        self.size = self.width, self.height = pygame.display.get_window_size()

    def resize(self):
        self.size = self.width, self.height = pygame.display.get_window_size()

    def update(self):
        ...

    def start(self):
        while True:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT: return pygame.quit()
                    case pygame.WINDOWSIZECHANGED: self.resize()
                    case pygame.MOUSEBUTTONUP: pos_click = event.pos

            self.update()


if __name__ == "__main__":
    game = Game()
    game.start()
