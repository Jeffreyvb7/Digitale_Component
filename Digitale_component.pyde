import game_combat

def setup():
    global screen_1, screen_2, screen_3, screen_4, screen_bg, env, battlebutton, battlebutton_pressed, current_button_img
    screen_1 = loadImage("Screen-1-1000x600.jpg")
    screen_2 = loadImage("Screen-2-1000x600.jpg")
    screen_3 = loadImage("Screen-3-1000x600.jpg")
    screen_4 = loadImage("Screen-4-1000x600.jpg")
    screen_bg = loadImage("Bg-Screen.jpg")
    env = 0
    
    battlebutton = loadImage('battle-button.png')
    battlebutton_pressed = loadImage('battle-button-pressed.png')
    current_button_img = battlebutton
    
    size(1000, 600)


def draw():    
    global env
    background(screen_bg)
    print(env)
        
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
        game_combat.draw(battlebutton, battlebutton_pressed, current_button_img)
    elif env == 2:
        None
        
def mousePressed():
    global env
    ## Temporary back button
    if overCircle(width*0.05, height*0.075, 50):
        env = 0
    
    game_combat.mousePressed(battlebutton, battlebutton_pressed, current_button_img);
    
    if mouseButton == LEFT and env == 0:
        if 339 < mouseX < 517 and 239 < mouseY < 324:
            env = 1
            background(screen_bg)
        elif 533 < mouseX < 712 and 342 < mouseY < 431:
            background(screen_bg)
        elif 729 < mouseX < 907 and 450 < mouseY < 563:
            exit()
    
def overCircle(x, y, diameter):
    disX = x - mouseX
    disY = y - mouseY
    if (sqrt(sq(disX) + sq(disY)) < diameter/2 ):
        return True
    else:
        return False
