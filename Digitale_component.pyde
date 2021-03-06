import game_combat
import Uitleg_1 as game_help
import grid as game_grid

def setup():
    global screen_1, screen_2, screen_3, screen_4, screen_bg, env, battlebutton, battlebutton_pressed, current_button_img
    global LTtitle, LTsubtitle, LTtext, currentScene, round_counter
    
    screen_1 = loadImage("Screen-1-1000x600.jpg")
    screen_2 = loadImage("Screen-2-1000x600.jpg")
    screen_3 = loadImage("Screen-3-1000x600.jpg")
    screen_4 = loadImage("Screen-4-1000x600.jpg")
    screen_bg = loadImage("Bg-Screen.jpg")
    env = 0
    
    battlebutton = loadImage('battle-button.png')
    battlebutton_pressed = loadImage('battle-button-pressed.png')
    current_button_img = battlebutton
    
    LTtitle = createFont('AgencyFB-Reg',30)
    LTsubtitle = createFont('AgencyFB-Reg',15)
    LTtext = createFont('AgencyFB-Reg',10)
    
    round_counter = 0
    
    size(1000, 600)
    

def draw():    
    global env
    background(screen_bg)
        
    if env == 0:
        background(screen_1)
        if 339 < mouseX < 517 and 239 < mouseY < 324:
            background(screen_2)
        elif 533 < mouseX < 712 and 342 < mouseY < 431:
            background(screen_3)
        elif 729 < mouseX < 907 and 450 < mouseY < 563:
            background(screen_4)
            
        circle(width*0.05, height*0.075, 50)

    elif env == 1:
        game_grid.draw(round_counter)
    elif env == 3:
        game_combat.draw(battlebutton, battlebutton_pressed, current_button_img)
    elif env == 2:
        game_help.draw(LTtitle, LTsubtitle, LTtext)

        
                
def mousePressed():
    global env, round_counter
    ## Temporary back button
    if overCircle(width*0.05, height*0.075, 50) and env != 3:
        env = 0
        
    if overCircle(width*0.05, height*0.075, 50) and env == 3:
        env = 1
    
    game_combat.mousePressed(battlebutton, battlebutton_pressed, current_button_img);
    game_grid.mousePressed()
    
    if mouseWithinRectangle(700, 80, 200, 80) and env == 1:
        round_counter += 1
        print(round_counter)
        
    if mouseWithinRectangle(700,500,200,40) and env == 1:
        env = 3
        
    if mouseButton == LEFT and env == 0:
        if 339 < mouseX < 517 and 239 < mouseY < 324:
            env = 1
            background(screen_bg)
        elif 533 < mouseX < 712 and 342 < mouseY < 431:
            env = 2
            background(screen_bg)
        elif 729 < mouseX < 907 and 450 < mouseY < 563:
            exit()
            
def keyPressed():
    game_help.keyPressed(LTtitle, LTsubtitle, LTtext)

def overCircle(x, y, diameter):
    disX = x - mouseX
    disY = y - mouseY
    if (sqrt(sq(disX) + sq(disY)) < diameter/2 ):
        return True
    else:
        return False
    
def mouseWithinRectangle(x, y, h, w):
    if x < mouseX < x + h and y < mouseY < y + w:
        return True
    else:
        return False
