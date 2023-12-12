import pygame

class Button:
    def __init__(self, x, y, image, width, height):
        self.image = image
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def isOver(self, pos):
        if self.rect.collidepoint(pos):
            return True

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect.size = self.image.get_size()
        return False

def main():
    pygame.init()
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Projectile Motion')
    background = pygame.image.load("background.png")
    button_img = pygame.image.load("login.png")
    button1 = pygame.image.load("signup.png")
    button2 = pygame.image.load("options.png")
    button_x = 50
    button_y = 200
    login_button = Button(button_x, button_y, button_img, 500, 100 )
    signup_button = Button(button_x + 650, button_y, button1, 500, 100)
    options_button = Button(button_x + 350, button_y + 150, button2,500,100)
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.isOver(pos):
                    open_new_window()  
                if signup_button.isOver(pos):
                    open_new_window()  
                if options_button.isOver(pos):
                    open_new_window()  

        screen.blit(background, (0, 0))
        login_button.draw(screen)
        signup_button.draw(screen)
        options_button.draw(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
