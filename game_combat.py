import battle

app_width = 1000
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

survived_explorers = 0
survived_warriors = 0
survived_tanks = 0

winner_string = ''

def setup():
    global backgroundimg, battlebutton, battlebutton_pressed, current_button_img
    size(app_width, app_height)
    
    battlebutton = loadImage('battle-button.png')
    battlebutton_pressed = loadImage('battle-button-pressed.png')
    current_button_img = battlebutton

def draw(battlebutton, battlebutton_pressed, current_button_img):
    draw_buttons(battlebutton, battlebutton_pressed, current_button_img)

          
def mousePressed(battlebutton, battlebutton_pressed, current_button_img):
    global winner_string
    attackerButtons()
    defenderButtons()
        
    if isMouseWithinFightButton(width*0.5 - width*0.1, height*0.85, width*0.2, 55): 
        current_button_img = battlebutton_pressed
        def_rolls_counter = [defending_explorer_counter, defending_warrior_counter, defending_tank_counter]
        att_rolls_counter = [attacking_explorer_counter, attacking_warrior_counter, attacking_tank_counter]
        
        winning_rolls = battle.combat(att_rolls_counter, def_rolls_counter)
        
        if winning_rolls == 0:
            winner_string = 'Both teams lose'
        elif winning_rolls[0] == 'defending':
            winner_string = 'Defending wins'
            return_survived_ships(winning_rolls)
        elif winning_rolls[0] == 'attacking':
            winner_string = 'Attacking wins'
            return_survived_ships(winning_rolls)
        

def return_survived_ships(winning_rolls):
    global survived_explorers, survived_warriors, survived_tanks
    survived_explorers = 0
    survived_warriors = 0 
    survived_tanks = 0
    for roll in winning_rolls[1]:
        x = roll // 10
        if x == 1:
            survived_explorers += 1
        elif x == 2:
            survived_warriors += 1
        elif x == 3:
            survived_tanks += 1


def isMouseWithinFightButton(x, y, h, w):
    global button_plus_y, button_size
    if x < mouseX < x + h and y < mouseY < y + w:
        return True
    else:
        return False

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
    global attacking_explorer_counter, attacking_warrior_counter, attacking_tank_counter
    total = attacking_explorer_counter + attacking_warrior_counter + attacking_tank_counter
    
    if overCircle(button_att_ex, button_plus_y, button_size) and attacking_explorer_counter < 5 and total < 5:
        attacking_explorer_counter += 1
    if overCircle(button_att_wa, button_plus_y, button_size) and attacking_warrior_counter < 5 and total < 5:
        attacking_warrior_counter += 1
    if overCircle(button_att_ta, button_plus_y, button_size) and attacking_tank_counter < 5 and total < 5:
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
    total = defending_explorer_counter + defending_warrior_counter + defending_tank_counter 
    
    if overCircle(width*0.78, button_plus_y, button_size) and defending_explorer_counter < 5 and total < 5:
        defending_explorer_counter += 1
    if overCircle(width*0.84, button_plus_y, button_size) and defending_warrior_counter < 5 and total < 5:
        defending_warrior_counter += 1
    if overCircle(width*0.90, button_plus_y, button_size) and defending_tank_counter < 5 and total < 5:
        defending_tank_counter += 1
        
    if overCircle(width*0.78, button_minus_y, button_size) and defending_explorer_counter > 0:
        defending_explorer_counter -= 1
    if overCircle(width*0.84, button_minus_y, button_size) and defending_warrior_counter > 0:
        defending_warrior_counter -= 1
    if overCircle(width*0.90, button_minus_y, button_size) and defending_tank_counter > 0:
        defending_tank_counter -= 1

# Draws the layout for the buttons and counters
def draw_buttons(battlebutton, battlebutton_pressed, current_button_img):
    global button_att_ex, button_att_wa, button_att_ta, button_def_ex, button_def_wa, button_def_ta, winner_string
    
    textSize(50)
    textAlign(CENTER)
    fill(255)
    text(winner_string,width*0.5, height*0.2)
    if winner_string != '':
        textSize(30)
        text('Survived ships', width*0.5, height*0.3)
        textSize(25)
        textAlign(LEFT)
        text('Explorers: ', width*0.4, height*0.4)
        text(survived_explorers, width*0.55, height*0.4)
        text('Warriors: ', width*0.4, height*0.5)
        text(survived_warriors, width*0.55, height*0.5)
        text('Tanks: ', width*0.4, height*0.6)
        text(survived_tanks, width*0.55, height*0.6)

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
    fill(255)
    textSize(25)
    textAlign(CENTER)
    text('Attacking team', app_width*0.16, button_plus_y-100)
    text('E', button_att_ex, button_plus_y-50)
    text('W', button_att_wa, button_plus_y-50)
    text('T', button_att_ta, button_plus_y-50)

    #COUNTERS
    text(attacking_explorer_counter, width*0.10, counter_y)
    text(attacking_warrior_counter, width*0.16, counter_y)
    text(attacking_tank_counter, width*0.22, counter_y)
    #SYMBOLS
    textAlign(CENTER)
    fill(0)
    text('+', button_att_ex, button_plus_y+5)
    text('+', button_att_wa, button_plus_y+5)
    text('+', button_att_ta, button_plus_y+5)
    text('-', button_att_ex, button_minus_y+5)
    text('-', button_att_wa, button_minus_y+5)
    text('-', button_att_ta, button_minus_y+5)
    
    #RIGHT SIDE
    fill(255)
    text('Defending team', app_width*0.84, button_plus_y-100)
    text('E', button_def_ex, button_plus_y-50)
    text('W', button_def_wa, button_plus_y-50)
    text('T', button_def_ta, button_plus_y-50)
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
    fill(255)
    textSize(25)
    textAlign(CENTER)
    #COUNTERS
    text(defending_explorer_counter, button_def_ex, counter_y)
    text(defending_warrior_counter, button_def_wa, counter_y)
    text(defending_tank_counter, button_def_ta, counter_y)
    #SYMBOLS
    textAlign(CENTER)
    fill(0)
    text('+', button_def_ex, button_plus_y+5)
    text('+', button_def_wa, button_plus_y+5)
    text('+', button_def_ta, button_plus_y+5)
    text('-', button_def_ex, button_minus_y+5)
    text('-', button_def_wa, button_minus_y+5)
    text('-', button_def_ta, button_minus_y+5)
    
    current_button_img.resize(int(width*0.2), int(55))
    fill(255)
    rect(width*0.5 - width*0.1, height*0.85, width*0.2, 55);
    image(current_button_img, width*0.4, height*0.85)
    circle(width*0.05, height*0.075, 50)
