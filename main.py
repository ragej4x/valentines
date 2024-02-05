import pygame as pg
pg.init()

window = pg.display.set_mode((1024,620))
pg.display.set_caption("LOMIII")

#++++
class main_class():
    def __init__(self) -> None:
        self.btn1_x = 0
        self.btn1_y = 0

        self.sad_list = []
        self.love_list = []
        self.love_frame = 0
        self.sad_frame = 0

        self.love = False
        self.sad = False

        self.res = 2

        for num in range(1, 4):
            self.love_image = pg.image.load(f"data/anim/love_frame ({num}).png")
            self.love_image = pg.transform.scale(self.love_image, (self.love_image.get_width()//self.res,self.love_image.get_height()//self.res))
            self.love_list.append(self.love_image)

        for num in range(1, 16):
            self.sad_image = pg.image.load(f"data/anim/sad_frame ({num}).png")
            self.sad_image = pg.transform.scale(self.sad_image, (self.sad_image.get_width()//self.res,self.sad_image.get_height()//self.res))
            self.sad_list.append(self.sad_image)


    def animate_love(self):
        
        window.blit(self.love_list[int(self.love_frame)], (410,100))
        
        self.love_frame += 00.02
        if self.love_frame > 3:
            self.love_frame = 0
        
        print(self.love_frame
              )

    def animate_sad(self):

        window.blit(self.sad_list[int(self.sad_frame)], (410,100))
        
        self.sad_frame += 00.02
        if self.sad_frame > 16:
            self.sad_frame = 0

    def update(self):
        pass        

main = main_class()

def event_handler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    pg.display.flip()


while True:
    window.fill((30,30,30))
    mp = pg.mouse.get_pos()
    mc = pg.mouse.get_pressed()

    #CALL
    #main.animate_love()
    main.animate_sad()

    event_handler()