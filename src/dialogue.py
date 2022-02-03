import pygame



class DialogBox:
    X_POSITION = 60
    Y_POSITION = 470
    def __init__(self):
        self.box = pygame.image.load('../dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (700, 100))
        self.texts = []
        self.text_index = 0
        self.reading = False
        self.lettre_index = 0
        self.font = pygame.font.Font("../dialogs/dialog_font.ttf", 20)

    def execute(self, dialog = []):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
    def render(self, screen):
        if self.reading:
            self.lettre_index +=1
            if self.lettre_index >= len(self.texts[self.text_index]):
                self.lettre_index = self.lettre_index
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.lettre_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 60, self.Y_POSITION + 30))

    def next_text(self):
        self.text_index += 1
        self.lettre_index = 0
        if self.text_index >= len(self.texts):
            self.reading = False
