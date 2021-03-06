import pygame


pygame.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    pygame.quit()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.txt_surface = FONT.render(self.text, True, self.color)
                else:
                    self.text += event.unicode
                    self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def openBox():
    clock = pygame.time.Clock()
    Text_box = InputBox(100, 100, 140, 32, 'Do You Want To Play Another Maze?(y/n)')
    input_box = InputBox(100, 300, 140, 32)
    boxes = [Text_box, input_box]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            input_box.handle_event(event)
        try:
            for box in boxes:
                box.update()

            screen.fill((30, 30, 30))
            for box in boxes:
                box.draw(screen)

            pygame.display.flip()
            clock.tick(30)
        except:
            return input_box.text