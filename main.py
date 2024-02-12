import pygame as pg
import random
import math
import asyncio
pg.mixer.init()

pg.init()


async def main_loop():
    window = pg.display.set_mode((1024,620))
    pg.display.set_caption("LOMIII")
    icon = pg.image.load("data/ico.png")
    pg.display.set_icon(icon)
    clock = pg.time.Clock()
    cursor = pg.image.load("data/cursor.png")

    #++++
    class main_class():
        def __init__(self) -> None:
            self.rnd = 0
            self.diag = [
                "Happy Valentines Day, Will you be my Valentine?",
                "talaga ba \n Princess?",
                "ahh",
                "Di tlga?",
                "Ayaw mo ?",
                "Di mo'ko lab?",
                "Are you sure?",
                "weh",
                "Di nga ?",
                "Ahw",
                "nop",
                ":<",
                "weh",
                "tagala ba ?",
                "Sure na sure ?",
                "Sure pa sa sure????",
                "Sure pa sa sure na  \n    sure???",
                "Sure pa sa super na sure??",
                "Di ngaa talaga?",
                "meh",
                "....",
                "talaga ba ?",
                "wehh",
                "are you sure??",
                "reallyreallysuree?????",
                "sureeee?",
                "reallysure pa sa sure \n na sure??",
                "tagala ba ?",
                "Sure na sure ?",
                "Sure pa sa sure????",
                "Ayaw mo ?",
                "Di mo talaga ako lab?",
                "Are you sure?",
            ]



            self.button_image = pg.image.load("data/button.png")
            self.yes_btn_image = pg.image.load("data/yes_btn.png")
            self.diag_box = pg.image.load("data/diag_box.png")
            self.diag_box_long= pg.image.load("data/diag_box_long.png")
            self.death_s = pg.image.load("data/death.png")
            self.dim = pg.image.load("data/dim.png")
            self.btn1_x = window.get_width()//3
            self.btn1_y = window.get_height()//1.5

            self.btn2_x = window.get_width()//1.7
            self.btn2_y = window.get_height()//1.5
            
            self.get_big_int = [self.button_image.get_width(), self.button_image.get_height()]

            self.sad_list = []
            self.love_list = []
            self.love_frame = 0
            self.sad_frame = 0

            self.love = True
            self.sad = False


            self.res = 2

            self.move = [self.btn2_x, self.btn2_y]

            self.time = 0

            #particle
            self.particle = []

            for num in range(1, 4):
                self.love_image = pg.image.load(f"data/anim/love_frame ({num}).png")
                self.love_image = pg.transform.scale(self.love_image, (self.love_image.get_width()// 3 ,self.love_image.get_height()//3))
                self.love_list.append(self.love_image)

            for num in range(1, 16):
                self.sad_image = pg.image.load(f"data/anim/sad_frame ({num}).png")
                self.sad_image = pg.transform.scale(self.sad_image, (self.sad_image.get_width()//self.res,self.sad_image.get_height()//self.res))
                self.sad_list.append(self.sad_image)

            #SFX VAR
            self.vol = 100
            self.sfx_file = [
                pg.mixer.Sound("data/sfx/death_sfx.mp3"),
                pg.mixer.Sound("data/sfx/click.wav"),
                pg.mixer.Sound("data/sfx/love.wav"),
                pg.mixer.Sound("data/sfx/sad.wav"),
                ]
        
            for num in range(1,3):
                self.sfx_file[num].set_volume(self.vol)
            
        def update(self):
            def health_death_sys():
                cstm_dhs = ["AGAY","ARUY","SAKIT"]
                font = pg.font.Font("data/pricedown bl.ttf", 50)
                death_txt = font.render(f"AGAY SAKIT", True, (255,0,0))
                """
                if self.rnd == 21:
                    self.sad = True
                    window.blit(death_txt, (390, 250))
                    window.blit(self.death_s, (0,0))
                    self.time += 00.1
                    self.sfx_file[0].play()

                    if self.time >= 4:

                        for i in range(1,2):
                            window.blit(self.death_s, (0,0))
                            window.blit(self.dim, (0,0))
                            window.blit(death_txt, (390, 250))

                
                #print(self.time)

                """
            def particle_effects():
                if mc[0]:
                    
                    for i in range(1,3):
                        self.particle.append([mp[0] - random.randint(1,8), mp[1], random.randint(2,8)])
                    
                for particle in self.particle:
                    pg.draw.circle(window, (random.randint(50,200),random.randint(50,200),random.randint(50,200)), (particle[0], particle[1]),particle[2])
                    
                    particle[2] -= 0.1
                    particle[1] += particle[2]
                    particle[0] += random.randint(-3, 5)

                    if particle[2] < 0:
                        self.particle.remove(particle)


            self.love_image_rect = self.love_image.get_rect(x=(430),y=(100))
            self.sad_image_rect = self.sad_image.get_rect(x=(430),y=(100))

            font = pg.font.Font("data/font.ttf", 40)

            #yes = font.render("YES :>", True, (255,255,255))
            no = font.render("NO :<", True, (255,255,255))

            def animate_love():
                window.blit(self.love_list[int(self.love_frame)], (430,100))
                
                self.love_frame += 00.1
                if self.love_frame > 3:
                    self.love_frame = 0
                    
                #print(self.love_frame)

            def animate_sad():

                window.blit(self.sad_list[int(self.sad_frame)], (430,100))
                
                self.sad_frame += 00.1
                if self.sad_frame > 15:
                    self.sad_frame = 0

            self.button_yes = pg.Rect((self.btn1_x, self.btn1_y, self.get_big_int[0], self.get_big_int[1]))

            self.button_no = self.button_image.get_rect(topleft=(self.btn2_x,self.btn2_y))

            self.mouse_rect = cursor.get_rect(x=(mp[0]),y=(mp[1]))


            
            if self.mouse_rect.colliderect(self.button_no) and pg.event.get(pg.MOUSEBUTTONDOWN):
                self.sad = True
                self.love = False
                self.btn2_x = random.randint(0,window.get_width() - 100)
                self.btn2_y = random.randint(0,window.get_height() - 100)
                
                self.get_big_int[0] += 30
                self.get_big_int[1] += 20
                self.button_yes
                self.btn1_x -= 15
                self.btn1_y -= 15
                self.rnd += 1
                self.sfx_file[3].play()


            self.get_big = pg.transform.scale(self.yes_btn_image, (self.get_big_int[0],self.get_big_int[1]))

            window.blit(self.get_big,(self.button_yes.x , self.button_yes.y))
            #window.blit(yes,(self.btn1_x + 15,self.btn1_y))

            window.blit(self.button_image,(self.button_no.x , self.button_no.y))
            window.blit(no,(self.btn2_x + 20,self.btn2_y))
            #SMOOTHSCROLL

            """
            if self.mouse_rect.colliderect(self.button_no) and mc[0] == True:
                self.sad = True
                self.love = False
                self.move[0] = random.randint(0,window.get_width() - 100)
                self.move[1] = random.randint(0,window.get_height() - 100)

            angle = math.atan2(self.move[1] - self.btn2_y , self.move[0] - self.btn2_x)
            dx = math.cos(angle)
            dy = math.sin(angle)

            if self.button_no.x != self.move[0] or self.button_no.y != self.move[1] :
                self.btn2_x += dx * 9
            
                self.btn2_y += dy * 9

            print(self.move, self.btn2_x)
            """

            if self.mouse_rect.colliderect(self.button_yes):
                self.love = True
                self.sad = False
                if pg.event.get(pg.MOUSEBUTTONDOWN):

                    self.sfx_file[2].play()

            if pg.event.get(pg.MOUSEBUTTONDOWN):

                self.sfx_file[1].play()

            if self.love_image_rect.colliderect(self.button_no) or self.button_yes.colliderect(self.button_no) or self.diag_box.get_rect(x=330, y=10, width=self.diag_box.get_width(), height=self.diag_box.get_height()).colliderect(self.button_no) or self.diag_box_long.get_rect(x=330, y=10, width=self.diag_box_long.get_width(), height=self.diag_box_long.get_height()).colliderect(self.button_no):
                self.btn2_x = random.randint(0,window.get_width() - 80)
                self.btn2_y = random.randint(0,window.get_height() - 80)
                

            if self.love == True:
                animate_love()

            if self.sad == True:
                animate_sad()
            


            def update_diag():

                font1 = pg.font.Font("data/font.ttf", 30)
                font = pg.font.Font("data/font.ttf", 23)
                sad_diag = font.render(f"{self.diag[self.rnd]}", True, (255,255,255))
                diag_1 = font1.render(f"{self.diag[0]}", True, (200,30,30))

                #if pg.event.get(pg.MOUSEBUTTONDOWN) and self.mouse_rect.colliderect(self.button_no) == True:



                if self.rnd > len(self.diag) - 1:
                    self.rnd = 0

                #print( self.rnd)
                if self.rnd == 0:
                    window.blit(diag_1,(260,290))

                if self.rnd > 10:
                    window.blit(self.diag_box_long,(300,10))
                    window.blit(sad_diag, (310,30))

                if self.rnd < 11 and self.rnd != 0:
                    window.blit(self.diag_box,(330,10))
                    window.blit(sad_diag, (360,30))
            
            
            update_diag()
            health_death_sys()
            particle_effects()
            

            #print(clock.get_fps())
           

    main = main_class()



    def event_handler():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        pg.display.flip()
        clock.tick(60)
        

    #global window , clock, cursor, main,  mp, mc

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

        await asyncio.sleep(0)
asyncio.run(main_loop())