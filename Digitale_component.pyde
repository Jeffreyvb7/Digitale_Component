app_width = 800
app_height = 600

button_att_ex = app_width*0.10
button_att_wa = app_width*0.16
button_att_ta = app_width*0.22

button_def_ex = app_width*0.78
button_def_wa = app_width*0.84
button_def_ta = app_width*0.90

button_size = app_width/18
button_minus_y = app_height*0.85
button_plus_y = app_height*0.70
counter_y = app_height*0.785

defending_explorer_counter = 0
defending_warrior_counter = 0
defending_tank_counter = 0

attacking_explorer_counter = 0
attacking_warrior_counter = 0
attacking_tank_counter = 0

def setup():
    size(app_width, app_height)

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

# Detects if mouse is over the buttons
def overCircle(x, y, diameter):
    disX = x - mouseX
    disY = y - mouseY
    if (sqrt(sq(disX) + sq(disY)) < diameter/2 ):
        return True
    else:
        return False
    
# Controls the buttons for the attacking player
def attackerButtons():
    global attacking_explorer_counter, attacking_warrior_counter, attacking_tank_counter, button_att_ex, button_att_wa, button_att_ta
    if overCircle(button_att_ex, button_plus_y, button_size) and attacking_explorer_counter < 5:
        attacking_explorer_counter += 1
    if overCircle(button_att_wa, button_plus_y, button_size) and attacking_warrior_counter < 5:
        attacking_warrior_counter += 1
    if overCircle(button_att_ta, button_plus_y, button_size) and attacking_tank_counter < 5:
        attacking_tank_counter += 1
        
    if overCircle(button_att_ex, button_minus_y, button_size) and attacking_explorer_counter > 0:
        attacking_explorer_counter -= 1
    if overCircle(button_att_wa, button_minus_y, button_size) and attacking_warrior_counter > 0:
        attacking_warrior_counter -= 1
    if overCircle(button_att_ta, button_minus_y, button_size) and attacking_tank_counter > 0:
        attacking_tank_counter -= 1

# Controls the buttons for the defending player    
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
 
# Gets the rolls for explorer ships
def get_explorer_roll(x):
    explorer_rolls = []
    while x > 0:
        explorer_roll += random(1,4)
        x -= 1
    return explorer_roll
   
# Gets the rolls for warrior ships
def get_warrior_rolls(x):
    warrior_rolls = []
    while x > 0:
        warrior_roll += random(1,6)
        x -= 1
    return warrior_roll

# Gets the rolls for tank ships
def get_tank_rolls(x):
    tank_rolls = []
    while x > 0:
        tank_rolls += random(1,8)
        x -= 1
    return tank_rolls

# Draws the layout for the buttons and counters
def draw_buttons():
    global button_att_ex, button_att_wa, button_att_ta, button_def_ex, button_def_wa, button_def_ta
    #LEFT SIDE
    #PLUS
    fill(255)
    circle(button_att_ex, button_plus_y, button_size)
    circle(button_att_wa, button_plus_y, button_size)
    circle(button_att_ta, button_plus_y, button_size)
    
    #MINUS
    fill(255)
    circle(button_att_ex, button_minus_y, button_size)
    circle(button_att_wa, button_minus_y, button_size)
    circle(button_att_ta, button_minus_y, button_size)
    
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
    text('+', button_att_ex, button_plus_y+5)
    text('+', button_att_wa, button_plus_y+5)
    text('+', button_att_ta, button_plus_y+5)
    text('-', button_att_ex, button_minus_y+5)
    text('-', button_att_wa, button_minus_y+5)
    text('-', button_att_ta, button_minus_y+5)
    
    #RIGHT SIDE
    #PLUS
    fill(255)
    circle(button_def_ex, button_plus_y, button_size)
    circle(button_def_wa, button_plus_y, button_size)
    circle(button_def_ta, button_plus_y, button_size)
    
    #MINUS
    fill(255)
    circle(button_def_ex, button_minus_y, button_size)
    circle(button_def_wa, button_minus_y, button_size)
    circle(button_def_ta, button_minus_y, button_size)

    #TEXT
    fill(0)
    textSize(25)
    textAlign(CENTER)
    #COUNTERS
    text(defending_explorer_counter, button_def_ex, counter_y)
    text(defending_warrior_counter, button_def_wa, counter_y)
    text(defending_tank_counter, button_def_ta, counter_y)
    #SYMBOLS
    textAlign(CENTER)
    text('+', button_def_ex, button_plus_y+5)
    text('+', button_def_wa, button_plus_y+5)
    text('+', button_def_ta, button_plus_y+5)
    text('-', button_def_ex, button_minus_y+5)
    text('-', button_def_wa, button_minus_y+5)
    text('-', button_def_ta, button_minus_y+5)
