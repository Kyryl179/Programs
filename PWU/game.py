import ursina as ursina
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import pygame
import tkinter
from tkinter import ttk , messagebox
pygame.init()

GAME = True

window = tkinter.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Login")
window.geometry('1000x900')
window.configure(background = "yellow");
Login_L = tkinter.Label(window ,text = "Login:").place(relx=0.375, rely=0.475, anchor=tkinter.CENTER)
Password_L = tkinter.Label(window ,text = "Password:").place(relx=0.375, rely=0.5, anchor=tkinter.CENTER)
Login_Input = tkinter.Entry(window).place(relx=0.5, rely=0.475, anchor=tkinter.CENTER)
Password_Input = tkinter.Entry(window).place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def LogIN():
    pass
def Closed():
    global GAME
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()
        GAME = False
def Pass():
    window.destroy()
bt_create = ttk.Button(window ,text="Create").place(relx=0.465, rely=0.525, anchor=tkinter.CENTER)
bt_login = ttk.Button(window ,text="Log In", command=LogIN).place(relx=0.55, rely=0.525, anchor=tkinter.CENTER)
AS_Guest = ttk.Button(window ,text="Pass for Now", command=Pass).place(relx=0.50, rely=0.555, anchor=tkinter.CENTER)
window.protocol("WM_DELETE_WINDOW", Closed)
window.mainloop()


if GAME != False:
    mw = screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("PWU")

    ############################################################

    Bground = pygame.transform.scale((pygame.image.load('.\Widgets\Pygame\Bgrounds\Menu-Bground.png')),(screen_width,screen_height))
    Play_button =  pygame.image.load('.\Widgets\Pygame\Buttons\Play-button.png')
    Play_button_X = screen_width/2-Play_button.get_width()/2
    Play_button_Y = screen_height/2-Play_button.get_height()/2
    
    
    Kanoe_Logo =  pygame.image.load('.\Widgets\Pygame\Other\Kanoe-Logo.png')
    Kanoe_Logo_X = screen_width-Kanoe_Logo.get_width()-20
    Kanoe_Logo_Y = Kanoe_Logo.get_height()+10


    ###########################################################
        
    Registration = True

    CR = 0
    CB = 0
    CG = 0

    while Registration != False:
        mw.blit(Bground,(0,0))
        mw.blit(Kanoe_Logo,(Kanoe_Logo_X,Kanoe_Logo_Y))
        mw.blit(Play_button,(Play_button_X,Play_button_Y))
        ##############
        
        if CR <= 252:
            CR += random.randint(0,3)
        else:
            CR = 1
            
        if CB <= 245:
            CB += random.randint(0,10)
        else:
            CB = 1
            
        if CG <= 250:
            CG += random.randint(0,5)
        else:
            CG = 1
            
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if Mouse_x > Play_button_X and Mouse_x < Play_button_X+Play_button.get_width() and Mouse_y>Play_button_Y and Mouse_y < Play_button_Y+Play_button.get_height():
            Play_button_Y = screen_height/2-Play_button.get_height()/2-2
        else:
            Play_button_Y = screen_height/2-Play_button.get_height()/2
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Registration = False
                GAME = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Mouse_x > Play_button_X and Mouse_x < Play_button_X+Play_button.get_width() and Mouse_y>Play_button_Y and Mouse_y < Play_button_Y+Play_button.get_height():
                    Registration = False
        pygame.draw.rect(mw, (CR,CG,CB), pygame.Rect(0, 0, screen_width, 5))
        pygame.draw.rect(mw, (CR,CG,CB), pygame.Rect(screen_width-5, 0, 5, screen_width))
        pygame.draw.rect(mw, (CR,CG,CB), pygame.Rect(0, 0, 5, screen_height))
        pygame.draw.rect(mw, (CR,CG,CB), pygame.Rect(0, screen_height-5, screen_width, 5))
        
        pygame.display.update()

    pygame.display.quit()
######################################################################


#######################################################################
if GAME != False:
    
    FirstPersonController.cursor = None
    ursina.window.size = ursina.window.fullscreen_size
    ursina.window.position = ursina.Vec2(0, 0)
    
    app = ursina.Ursina()
    class Block(ursina.Button):
        def __init__(self,model = 'cube',position = (0,0,0),color = ursina.color.white,texture = 'white_cube' ,scale = (1,1,1)):
            super().__init__(
                parent = ursina.scene,
                position = position,
                model = model,
                texture = texture,
                color = color ,
                scale = scale
            )

    def update():
        global Levl
        global Block
        global Block_5_move,Block_5_up
        #Sky.rotation_z += 5
        Rotations4 = [0,-1,-1.5,-2,-2.5,-3,-3.5,-4,-4.5,5,6,7,8,9,10,11,12,13,14,15]
        Looper = 0
        for box in Blocks:
            box.rotation_x += 5
        for block_3 in Block_3:
            block_3.rotation_z += 0.5
        for levl1 in Levl_1:
            levl1.rotation_y += 50
        for box_4 in Block_4:
            box_4.rotation_x += Rotations4[Looper]
            box_4.rotation_y += Rotations4[Looper]
            Looper+=1



        player_x,player_z,player_y = player.position


        if player_z < -10 and Levl == 1:
            player.setPos(15,15,15)
        if player_x > 12 and player_x < 20 and player_y > 135 and player_y < 138:
            Levl = 2
        if player_z < -10 and Levl == 2:
            player.setPos(15,5,137)
        if player_x > 10 and player_x < 20 and player_y > 183 and player_y < 192:
            Levl = 3
        if player_z < -10 and Levl == 3:
            player.setPos(15,10,180)
        if player_y > 280 and player_y < 290 and player_x > 10 and player_x < 18:
            Levl = 4
        if player_z < -10 and Levl == 4:
            player.position = (15,10,285)
        if player_y > 395 and player_y < 405 and player_x > 10 and player_x < 18:
            Levl = 5
        if player_z < -10 and Levl == 5:
            player.setPos(15,10,400)
        #############################################################
        #############################################################

    Admin = open('.\Widgets\Administrator.txt','r')
    Admin = Admin.read()
    if 'True' in Admin:
        def input(key):
            player_x,player_z,player_y = player.position
            global Levl
            hight = 100
            if key == '1':
                Levl = 1
                player.setPos(15,15,15)
            elif key == '2':
                Levl = 2
                player.setPos(15,5,137)
            elif key == '3':
                Levl = 3
                player.setPos(15,10,180)
            elif key == '4':
                player.position = (15,10,285)
            elif key == '5':
                player.setPos(15,10,400)      
            if key == '/':
                print(player.position)
            if key == 'g':
                player.gravity  = 0 
                player.speed = 100
                hight += 2
                player.setPos(player_x,player_y,hight)
            if key == 'h':
                hight = 100
                player.gravity = 1
                player.speed = 10



    sky_texture= ursina.load_texture("Back-ground.png")
    Sky = ursina.Sky(texture=sky_texture,rotation_x = 180)
    Levl = 1
    BColor = 1
    Blocks = []
    Levl_1 = []
    Block_3 = []
    Block_4 = []
    Block_5 = []


    for y in range(30):
        for x in range(30):
            block = Block(model = 'cube',position=(x,0,y),color=ursina.color.blue)

    for y in range(10):
        levl_1 = Block(model = 'cube',position=(15,0,y*10+35),color=ursina.color.turquoise,scale=(3,0.5,3))
        Levl_1.append(levl_1)
    levl_2_spawn = Block(model = 'cube',position=(15,3,135),color=ursina.color.yellow,scale=(5,0.5,5))
    for i in range(10):
        levl_2 = Block(model = 'Plane',position=(15,3,i*3.5+140),color=ursina.color.yellow,scale=(3,0.5,3))
        Blocks.append(levl_2)
    Platform_3 = Block(model = 'cube',position=(15,5,178),color=ursina.color.orange,scale=(10,0.5,10))
    Position3 = [14,13,14,17,12,13,14,14,12,16,13,13,17,14,13]
    for i in range(15):
        levl_3 = Block(model = 'cube',position=(Position3[i],5,188 + i * 6),color=ursina.color.orange,scale=(3,0.5,3))
        Block_3.append(levl_3)

    Platform_4 = Block(model = 'cube',position=(15,5,285),color=ursina.color.red,scale=(10,0.5,10))
    Position4 = [14,17,13,12,15,16,15,12,17,14]
    for i in range(10):
        Levl_4 = Block(model = 'cube',position=(Position4[i],5,295 + i*10),color=ursina.color.red,scale=(4,4,4))
        Block_4.append(Levl_4)

    Platform_5 = Block(model = 'cube',position=(15,5,400),color=ursina.color.black90,scale=(10,0.5,10))
    Position5 = [12,16,14,13,16,15,16,13,15,14,15,14,16,12,12,14,13,17,12,16]
    for i in range(20):
        Levl_5 = Block(model = 'sphere',position=(Position5[i],5,410 + i*5),color=ursina.color.black,scale=(1,1,1))
        Block_5.append(Levl_5)



    PLAYER_SERV = Block(model = '.\Widgets\Textures\Man.obj', position= (0,0,0),color=ursina.color.blue,scale=(0.25,0.5,0.25))


    finish_platform = Block(model = 'cube',position=(15,5,515),texture='.\Widgets\Textures\Gradient.png',scale=(15,1,15))
    finish_platform.rotation = (0,90,0)


    player = FirstPersonController()
    player.speed = 10
    player.jump_height = 7
    player.setPos(15,15,15)

    app.run()