import pygame

pygame.init()

win_w, win_h = 700, 500

window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Menu 0.1")

spring = pygame.transform.scale(pygame.image.load("spring.png"), (win_w, win_h))

clock = pygame.time.Clock()
FPS = 60


class Button:
    def __init__(self, x, y, w, h, image1, image2):
        self.rect = pygame.Rect(x, y, w, h)
        self.image1 = pygame.transform.scale(image1, (w, h))
        self.image2 = pygame.transform.scale(image2, (w, h))
        self.image = self.image1

    def reset(self, x, y):
        self.animate(x, y)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def animate(self, x, y):
        if self.rect.collidepoint(x, y):
            self.image = self.image2
        else:
            self.image = self.image1



play_img = pygame.image.load("Play.png")
options_img = pygame.image.load("options.png")
quit_img = pygame.image.load("Quit.png")
quit_img2 = pygame.image.load("Quit2.png")
update_img = pygame.image.load("Update.png")

click_snd = pygame.mixer.Sound("click.mp3")


btn_play = Button(win_w//2-100, (win_h-10)//5, 200, 50, play_img, play_img)
btn_options = Button(win_w//2-100, (win_h-10)//5*2, 200, 50, options_img, options_img)
btn_quit = Button(win_w//2-100, (win_h-10)//5*3, 200, 50, quit_img, quit_img2)

btn_menu = Button(win_w//2-100, (win_h-10)//2, 200, 50, update_img, update_img)
btn_menu2 = Button(0, 0, 50, 20, update_img, update_img)

game = True

screen = "menu"

while game:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if screen == "menu":
        window.blit(spring, (0, 0))
        btn_play.reset(mouse_x, mouse_y)
        btn_options.reset(mouse_x, mouse_y)
        btn_quit.reset(mouse_x, mouse_y)
        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if btn_options.rect.collidepoint(x, y):
                    click_snd.play()
                    screen = "options"
                elif btn_play.rect.collidepoint(x, y):
                    click_snd.play()
                    screen = "play"
                elif btn_quit.rect.collidepoint(x, y):
                    click_snd.play()
                    game = False

             
    elif screen == "options":
        window.blit(spring, (0, 0))
        btn_menu.reset(mouse_x, mouse_y)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if btn_menu.rect.collidepoint(x, y):
                    click_snd.play()
                    screen = "menu"


    elif screen == "play":
        window.blit(spring, (0, 0))
        btn_menu2.reset(mouse_x, mouse_y)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if btn_menu2.rect.collidepoint(x, y):
                    click_snd.play()
                    screen = "menu"


    
    pygame.display.update()
    clock.tick(FPS)