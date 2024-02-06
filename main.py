import pygame as pg
import random 
pg.init()

window = pg.display.set_mode((1024,620))
pg.display.set_caption("LOMIII")
clock = pg.time.Clock()
cursor = pg.image.load("data/cursor.png")

#++++
class main_class():
    def __init__(self) -> None:
        self.button_image = pg.image.load("data/button.png")
        self.btn1_x = window.get_width()//3
        self.btn1_y = window.get_height()//1.5

        self.btn2_x = window.get_width()//1.7
        self.btn2_y = window.get_height()//1.5


        self.sad_list = []
        self.love_list = []
        self.love_frame = 0
        self.sad_frame = 0

        self.love = False
        self.sad = False


        self.res = 2

        for num in range(1, 4):
            self.love_image = pg.image.load(f"data/anim/love_frame ({num}).png")
            self.love_image = pg.transform.scale(self.love_image, (self.love_image.get_width()// 3 ,self.love_image.get_height()//3))
            self.love_list.append(self.love_image)

        for num in range(1, 16):
            self.sad_image = pg.image.load(f"data/anim/sad_frame ({num}).png")
            self.sad_image = pg.transform.scale(self.sad_image, (self.sad_image.get_width()//self.res,self.sad_image.get_height()//self.res))
            self.sad_list.append(self.sad_image)



    def update(self):
        self.love_image_rect = self.love_image.get_rect(x=(430),y=(100))
        self.sad_image_rect = self.sad_image.get_rect(x=(430),y=(100))

        font = pg.font.Font("data/font.ttf", 40)

        yes = font.render("YES :>", True, (255,255,255))
        no = font.render("NO :<", True, (255,255,255))

        def animate_love():
            window.blit(self.love_list[int(self.love_frame)], (430,100))
            
            self.love_frame += 00.1
            if self.love_frame > 3:
                self.love_frame = 0
            
            print(self.love_frame
                )

        def animate_sad():

            window.blit(self.sad_list[int(self.sad_frame)], (430,100))
            
            self.sad_frame += 00.1
            if self.sad_frame > 15:
                self.sad_frame = 0

        self.button_yes = self.button_image.get_rect(topleft=(self.btn1_x,self.btn1_y))

        self.button_no = self.button_image.get_rect(topleft=(self.btn2_x,self.btn2_y))

        self.mouse_rect = cursor.get_rect(x=(mp[0]),y=(mp[1]))

        window.blit(self.button_image,(self.button_yes.x , self.button_yes.y))
        window.blit(yes,(self.btn1_x + 15,self.btn1_y))

        window.blit(self.button_image,(self.button_no.x , self.button_no.y))
        window.blit(no,(self.btn2_x + 20,self.btn2_y))

        if self.mouse_rect.colliderect(self.button_no) and mc[0] == True:
            self.sad = True
            self.love = False
            self.btn2_x = random.randint(0,window.get_width() - 100)
            self.btn2_y = random.randint(0,window.get_height() - 100)

        if self.mouse_rect.colliderect(self.button_yes):
            self.love = True
            self.sad = False


        if self.love_image_rect.colliderect(self.button_no) or self.button_yes.colliderect(self.button_no):
            self.btn2_x = random.randint(0,window.get_width() - 100)
            self.btn2_y = random.randint(0,window.get_height() - 100)

        if self.love == True:
            animate_love()

        if self.sad == True:
            animate_sad()
            

main = main_class()

def event_handler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    pg.display.flip()
    clock.tick(60)

while True:
    window.fill((30,30,30))
    pg.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    mp = pg.mouse.get_pos()
    mc = pg.mouse.get_pressed()

    #CALL
    #main.animate_love()
    main.update()
    window.blit(cursor,(mp[0],mp[1]))
    event_handler()