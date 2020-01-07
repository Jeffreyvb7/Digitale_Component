import textwrap

grid = [[0]*15 for n in range(15)]

#color 1
grid[0][0] = 1
grid[0][1] = 1
grid[1][0] = 1
grid[1][1] = 1

#color 2
grid[0][14] = 2
grid[0][13] = 2
grid[1][13] = 2
grid[1][14] = 2

#color 3
grid[14][14] = 3
grid[13][14] = 3
grid[13][13] = 3
grid[14][13] = 3

#color 4
grid[14][0] = 4
grid[13][0] = 4
grid[13][1] = 4
grid[14][1] = 4

w = 35
round_counter = 0
grid_event = []
current_event = ''
random_events = [
                "Door een ion storm zijn de communicatiesystemen van jouw schepen tijdelijk uitgeschakeld. Sla een beurt over.",
                "Je arriveert in sector Z-SEC7 en nadert een grote vijandige vloot, je hebt de keuze om of  cloaking te activeren maar het activeren van deze geavanceerde technologie kost je een beurt. Als alternatief kan je ook de tol van deze sector betalen wat 2 kaarten(uit de hand) kost.",
                "Je wordt aangevallen door een rebellen schip. De scheeps computer geeft een slagingspercentage van 63%. Rol met een d8 om je te verdedigen. Met 1-5 versla je de rebellen en pak je een kaart van de stapel. Als de rebellen jou verslaan, verlies je een kaart",
                "Je bent een achtervolgende bandit kwijt weten te raken na een lange achtervolging. Om aan de bandit te ontsnappen heb je door een asteroide ring moeten vliegen waardoor het schip schade heeft opgelopen en het al je grondstoffen in je hand kost om het te repareren.",
                "Wegens een gebrek aan olie en uranium moet de brandstofmijn naar een andere locatie worden verplaatst. Indien deze nog beschikbaar is, verplaats de brandstoftegel naar een andere locatie in jouw sector.",
                "De intergalactische reapers zijn jouw sector binnengevallen en hebben je resourcemijn gekaapt. Ze hebben de mijnwerkers gegijzeld,maar een van je vloten in de buurt heeft een reddingsmissie georganiseerd. Rol met een d6 om de missie uit te voeren. Met een 1 of een 6 faalt de missie en moet de mijn naar een ander locatie in jouw sector verplaatst worden.",
                "Onderweg naar een ver universum, benaderd een van je Motherships een verlaten satelliet observatorium. Er zijn duidelijke tekens van vernietiging en de bemanning overlegd wat ze doen. De speler kiest of zij het observatorium wil doorzoeken. Als dat zo is, rolt de speler met een d4 om de uitkomst van de missie te bepalen.",
                ]

random_event_with_coords = [
                            'Door een rondtrekkende nomaden vloot van het Imperium zijn de volgende coordinaten niet beschikbaar:',
                            'Door een grote nevelvlekken zijn  de volgende coordinaten niet beschikbaar',
                            'Wegens een onverwachte meteoren regen zijn alle troepen verwoest in de volgende coordinaten',
                            'Jullie horen door de intergalactische communicatie systemen dat er op de volgende coordinaten een asteroide is gevonden vol met grondstoffen (+1 grondstof bij het betreden van een vakje)',
                            'Jullie horen door de intergalactische communicatie systemen dat er op de volgende coordinaten een interstellaire wolk is gevonden vol met brandstof (+1 brandstof bij het betreden van een vakje)',
                            ]

c1 = color(41,31,191)
c2 = color(142,31,191)
c3 = color(16,10,100)
c4 = color(152,12,78)
danger_color = color(220,20,60)
    
def draw(round_counter):
    global c1, c2, c3, c4, font
    y = 20
    for row in grid:
        x = 100
        for col in row:
            if col == 1:
                fill(c1)
            elif col == 2:
                fill(c2)
            elif col == 3:
                fill(c3)
            elif col == 4:
                fill(c4)
            elif col == 5:
                fill(danger_color)
            else:
                fill(255)
            rect(x, y, w, w)
            x = x + w
        y = y + w
        x = 0
            
    draw_text(round_counter)
    
def mousePressed():
    global round_counter, danger_color, grid_event, random_events, current_event
    
    if mouseWithinRectangle(700, 80, 200, 80):
        round_counter += 1
        event_counter = random(1, 10)
        current_event = ''
        
        if grid_event:
            grid[grid_event[0][0]][grid_event[0][1]] = 0
            grid[grid_event[1][0]][grid_event[1][1]] = 0
            grid[grid_event[2][0]][grid_event[2][1]] = 0
            grid[grid_event[3][0]][grid_event[3][1]] = 0
            grid[grid_event[4][0]][grid_event[4][1]] = 0
            
        #Event with coords
        if  event_counter <= 3:
            event_y = int(random(2,13))
            event_x = int(random(2,13))
            event = int(random(0,len(random_event_with_coords)))

        
            grid_event = [[event_x, event_y],[event_x+1, event_y],[event_x-1, event_y],[event_x, event_y+1], [event_x, event_y-1]]
            print(grid_event[0][0])
            #plus shape
            grid[grid_event[0][0]][grid_event[0][1]] = 5
            grid[grid_event[1][0]][grid_event[1][1]] = 5
            grid[grid_event[2][0]][grid_event[2][1]] = 5
            grid[grid_event[3][0]][grid_event[3][1]] = 5
            grid[grid_event[4][0]][grid_event[4][1]] = 5
            
            current_event = random_event_with_coords[event]
            
        # #Event without coords
        if event_counter > 3 and event_counter < 5:
            event = int(random(0,len(random_events)))
            current_event = random_events[event] + ' >> Player '+str(int(random(1,4)))+ ' <<'
            
            
        
def mouseWithinRectangle(x, y, h, w):
    if x < mouseX < x + h and y < mouseY < y + w:
        return True
    else:
        return False
    
def draw_text(round_counter):
    # round counter
    textAlign(LEFT)
    fill(255)
    text('Round: ' + str(round_counter), 750, 50)
    #random button
    font = createFont('Arial',40)
    textFont(font, 25)
    fill(255,255,255)
    rect(700,80,200,80)
    fill(0)
    text('Click', 770, 130)
    fill(255)
    text('Event:', 760, 200)
    
    rect(700,500,200,40)
    fill(0)
    text('BATTLE', 750, 530)

    
    textSize(18)
    fill(255)
    text("\n".join(textwrap.wrap(current_event,40)), 650, 230)
    
    text('A', 85, 45)
    text('B', 85, 80)
    text('C', 85, 115)
    text('D', 85, 150)
    text('E', 85, 182)
    text('F', 85, 217)
    text('G', 85, 254)
    text('H', 85, 290)
    text('I', 85, 325)
    text('J', 85, 360)
    text('K', 85, 395)
    text('L', 85, 430)
    text('M', 85, 465)
    text('N', 85, 500)
    text('O', 85, 535)
    
    text('1', 111, 570)
    text('2', 146, 570)
    text('3', 181, 570)
    text('4', 216, 570)
    text('5', 251, 570)
    text('6', 286, 570)
    text('7', 321, 570)
    text('8', 356, 570)
    text('9', 391, 570)
    text('10', 421, 570)
    text('11', 458, 570)
    text('12', 492, 570)
    text('13', 525, 570)
    text('14', 562, 570)
    text('15', 596, 570)
    
    fill(255)
    circle(width*0.05, height*0.075, 50)



    
