button_size = width/2.5
button_minus_y = height*5
button_plus_y = height*4
counter_y = height*4.55

button_att_ex = 
button_att_wa =
button_att_ta =

defending_explorer_counter = 0
defending_warrior_counter = 0
defending_tank_counter = 0

attacking_explorer_counter = 0
attacking_warrior_counter = 0
attacking_tank_counter = 0

def setup():
    size(800,600)
    windowWidth = int(round(displayWidth*0.5))
    windowHeight = int(round(displayHeight*0.5))
    print(windowHeight, windowWidth)
    

def draw():
    background(240) 
    draw_buttons()

def mousePressed():
    attackerButtons()
    defenderButtons()

# def isMouseWithinObject(x, y):
#     global button_plus_y, button_size
#     if x < mouseX < x + button_size and y < mouseY < y + button_size:
#         return True
#     else:
#         return False
    
def overCircle(x, y, diameter):
    disX = x - mouseX
    disY = y - mouseY
    if (sqrt(sq(disX) + sq(disY)) < diameter/2 ):
        return True
    else:
        return False
    
def attackerButtons():
    global attacking_explorer_counter, attacking_warrior_counter, attacking_tank_counter
    if overCircle(width*0.10, button_plus_y, button_size) and attacking_explorer_counter < 5:
        attacking_explorer_counter += 1
    if overCircle(width*0.16, button_plus_y, button_size) and attacking_warrior_counter < 5:
        attacking_warrior_counter += 1
    if overCircle(width*0.22, button_plus_y, button_size) and attacking_tank_counter < 5:
        attacking_tank_counter += 1
        
    if overCircle(width*0.10, button_minus_y, button_size) and attacking_explorer_counter > 0:
        attacking_explorer_counter -= 1
    if overCircle(width*0.16, button_minus_y, button_size) and attacking_warrior_counter > 0:
        attacking_warrior_counter -= 1
    if overCircle(width*0.22, button_minus_y, button_size) and attacking_tank_counter > 0:
        attacking_tank_counter -= 1
        
def defenderButtons():
    global defending_explorer_counter, defending_warrior_counter, defending_tank_counter
    if overCircle(width*0.78, button_plus_y, button_size) and defending_explorer_counter < 5:
        defending_explorer_counter += 1
    if overCircle(width*0.84, button_plus_y, button_size) and defending_warrior_counter < 5:
        defending_warrior_counter += 1
    if overCircle(width*0.90, button_plus_y, button_size) and defending_tank_counter < 5:
        defending_tank_counter += 1
        
    if overCircle(width*0.78, button_minus_y, button_size) and defending_explorer_counter > 0:
        defending_explorer_counter -= 1
    if overCircle(width*0.84, button_minus_y, button_size) and defending_warrior_counter > 0:
        defending_warrior_counter -= 1
    if overCircle(width*0.90, button_minus_y, button_size) and defending_tank_counter > 0:
        defending_tank_counter -= 1
        
def get_explorer_roll(x):
    explorer_rolls = []
    while x > 0:
        explorer_roll += random(1,4)
        x -= 1
    return explorer_roll
    
def get_warrior_rolls(x):
    warrior_rolls = []
    while x > 0:
        warrior_roll += random(1,6)
        x -= 1
    return warrior_roll
    
def get_tank_rolls(x):
    tank_rolls = []
    while x > 0:
        tank_rolls += random(1,8)
        x -= 1
    return tank_rolls
        
def draw_buttons():
    #LEFT SIDE
    #PLUS
    fill(255)
    circle(width*0.10, button_plus_y, button_size)
    circle(width*0.16, button_plus_y, button_size)
    circle(width*0.22, button_plus_y, button_size)
    
    #MINUS
    fill(255)
    circle(width*0.10, button_minus_y, button_size)
    circle(width*0.16, button_minus_y, button_size)
    circle(width*0.22, button_minus_y, button_size)
    
    #TEXT
    fill(0)
    textSize(25)
    textAlign(CENTER)
    #COUNTERS
    text(attacking_explorer_counter, width*0.10, counter_y)
    text(attacking_warrior_counter, width*0.16, counter_y)
    text(attacking_tank_counter, width*0.22, counter_y)
    #SYMBOLS
    textAlign(CENTER)
    text('+', width*0.10, button_plus_y+5)
    text('+', width*0.16, button_plus_y+5)
    text('+', width*0.22, button_plus_y+5)
    text('-', width*0.10, button_minus_y+5)
    text('-', width*0.16, button_minus_y+5)
    text('-', width*0.22, button_minus_y+5)
    
    #RIGHT SIDE
    #PLUS
    fill(255)
    circle(width*0.78, button_plus_y, button_size)
    circle(width*0.84, button_plus_y, button_size)
    circle(width*0.90, button_plus_y, button_size)
    
    #MINUS
    fill(255)
    circle(width*0.78, button_minus_y, button_size)
    circle(width*0.84, button_minus_y, button_size)
    circle(width*0.90, button_minus_y, button_size)

    #TEXT
    fill(0)
    textSize(25)
    textAlign(CENTER)
    #COUNTERS
    text(defending_explorer_counter, width*0.90, counter_y)
    text(defending_warrior_counter, width*0.84, counter_y)
    text(defending_tank_counter, width*0.78, counter_y)
    #SYMBOLS
    textAlign(CENTER)
    text('+', width*0.90, button_plus_y+5)
    text('+', width*0.84, button_plus_y+5)
    text('+', width*0.78, button_plus_y+5)
    text('-', width*0.90, button_minus_y+5)
    text('-', width*0.84, button_minus_y+5)
    text('-', width*0.78, button_minus_y+5)
