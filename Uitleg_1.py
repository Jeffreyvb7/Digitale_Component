currentScene = 'Uitleg1'

def draw(LTtitle, LTsubtitle, LTtext):
    global currentScene
    if currentScene == 'Uitleg1':
        uitleg_1(LTtitle, LTsubtitle, LTtext)
    else:
        uitleg_2(LTtitle, LTsubtitle, LTtext)

def keyPressed(LTtitle, LTsubtitle, LTtext):  
    global currentScene
    if key == ' ':
        if currentScene == 'Uitleg1':
            currentScene = 'Uitleg2'
        else:
            currentScene = 'Uitleg1'
    
def uitleg_1(LTtitle, LTsubtitle, LTtext):
    textAlign(LEFT)
    textFont(LTtitle)
    fill(255)
    text("Spelregels",250,50)
    
    textFont(LTsubtitle)
    text("Het doel van het spel", 250, 80)
    text("Voorbereiding van het spel", 250, 110)
    text("Kaarten",250,180)
    text("Spelersbeurt",250,270)
    text("1.  Kaarten ruilen met andere spelers",250,330)
    text("2.  Je huidige kaarten ruilen voor nieuwe kaarten",250,390)
    text("3.  Je huidige kaarten spelen",250,430)
   
    textFont(LTtext)
    text("De speler die als laatste overblijft met zijn troepen is de winnaar van het spel.", 250,90)
    text("Elke speler krijgt 1 brandstof bron, 1 grondstof bron en krijgt 3 verkenners. Elke speler legt zijn brandstof ", 250,120)
    text("bron op het gebied van zijn rechterbuurman en zijn grondstof bron op het gebied van zijn linker ",250,130)
    text("buurman. Tussen de bronnen moeten minimaal 2 vakjes tussen zitten. De drie verkenners zet hij op",250,140)
    text("zijn eigen hoek neer. ",250,150)
    text("De speelkaarten worden geschud en elke speler krijgt 7 kaarten. ",250,160)
    text("In het spel zijn er 3 verschillende kaarten.",250,190)
    text("    -   Brandstof kaarten",250,200)
    text("    -   Blueprint kaarten",250,210)
    text("    -   Grondstof kaarten",250,220)
    text("De brandstof kaarten zijn voor het verplaatsen van de troepen. De grondstof en de blueprint kaarten",250,240)
    text("zijn voor het maken van troepen.",250,250)
    text("Als je aan de beurt bent, kan je verschillende zetten doen.",250,280)
    text("    1.  Kaarten ruilen met andere spelers.",250,290)
    text("    2.  Je huidige kaarten ruilen voor nieuwe kaarten.",250,300)
    text("    3.  Je huidige kaarten spelen.",250,310)
    text("Aan het begin van je beurt kan je met een andere speler van kaarten ruilen. Je mag zelf bepalen",250,340)
    text("welke kaarten je wilt ruilen en welke kaarten je er voor terug wilt hebben. Als de andere speler", 250,350)
    text("akkoord gaat met de ruil, dan leg je de kaarten die je van hem gekregen hebt voor je op de tafel neer.",250,360)
    text("De kaarten die voor je op tafel liggen mag je spelen wanneer je wilt.",250,370)
    text("Aan het begin van je beurt kan je er voor kiezen om je huidige 7 kaarten die je in je handen hebt te",250,400)
    text("ruilen met 7 nieuwe kaarten. Deze nieuwe kaarten pak je van de stapel.",250,410)
    text("Aan het begin van je beurt begin je altijd met 7 kaarten in je handen. Per beurt mag je alle 7  kaarten ",250,440)
    text("die je in je handen hebt wegspelen. De kaarten die je voor je op tafel hebt liggen mag je daarnaast",250,450)
    text("ook nog eens wegspelen.",250,460)
    

    fill(0)
    rect(365,520,210,50)
    fill(250)
    rect(370,525,200,40)
    fill(0)
    textFont(LTsubtitle)
    text("Press space for next",400,550)
    
    fill(255)
    circle(width*0.05, height*0.075, 50)
    
def uitleg_2(LTtitle, LTsubtitle, LTtext):
    fill(255)
    textFont(LTtitle)
    text("Spelregels",250,50)
    
    textFont(LTsubtitle)
    text("Wanneer mag je kaarten voor je op tafel leggen?",250,80)
    text("Het verkrijgen van nieuwe troepen",250,140)
    text("Het lopen van de troepen",250,220)
    text("Het einde van het spel",250,290)
    text("Aanval en verdediging",250,350)
    
    textFont(LTtext)
    text("De kaarten die je krijgt aan het begin van de dingen krijgt aan het begin van je beurt leg je voor je",250,90)
    text("neer op de tafel. De kaarten die je krijgt van een andere speler tijdens de ruil leg je ook voor je neer",250,100)
    text("op de tafel. En de resource kaarten die je krijgt van het midden van het bord die leg je ook voor je op",250,110)
    text("de tafel.",250,120)
    text("Wanneer een speler aan de beurt is, kan hij nieuwe troepen maken. Dit kan hij doen door het",250,150)
    text("volgende kaarten te spelen:",250,160)
    text("    -  1 blueprint + 1 grondstof = 1 verkenner",250,180)
    text("    -  1 blueprint + 2 grondstoffen = 1 krijger",250,190)
    text("    -  1 blueprint + 3 grondstoffen =  1 tank",250,200)
    text("Voor elke brandstofkaart mag een troep een bepaald aantal stappen lopen. De verkenners mogen 3",250,230)
    text("stappen, de krijgers mogen 2 stappen en de tank mogen er maar 1. In het spel mogen er troepen",250,240)
    text("gestapeld worden, er mogen maximaal 5 troepen op elkaar gezet worden. Als er in een leger",250,250)
    text("meerdere troepen zitten, mag dit leger het aantal stappen zetten van het sterkste troep die in dat",250,260)
    text("leger zit.",250,270)
    text("Na een bepaald aantal rondes word het speelveld van het bord steeds kleiner. Je mag zelf afspreken",250,300)
    text("na hoeveel rondes het bordspel steeds kleiner wordt. In de eerste ronde worden de buitenste 2",250,310)
    text("randen van het bord bestormt. Hierdoor kan je ook geen troepen meer maken. Vanaf nu gaat de",250,320)
    text("storm steeds 1 vakje per ronde naar het midden toe.",250,330)
    text("Voor het vechten werken we met dobbelstenen. Voor elke troep heb je een aparte dobbelsteen.",250,360)
    text("    -  Verkenner = 1 t/m 4 dobbelsteen",250,380)
    text("    -  Krijger = 1 t/m 6 dobbelsteen",250,390)
    text("    -  Tank = 1 t/m 8 dobbelsteen",250,400)
    text("Dus stel je hebt 2 verkenners, 1 krijger en 2 tanks. Dan pak je 2 keer: 1 t/m 4 dobbelsteen, 1 keer: 1",250,420)
    text("t/m 6 dobbelsteen en 2 keer de 1 t/m 8 dobbelsteen.",250,430)
    text("Voor het gevecht gooi je je de dobbelstenen. Deze dobbelstenen leg je van hoog naar laag neer. Deze",250,440)
    text("dobbelstenen vergelijk je met de tegenstander. De hoogste van jouw vergelijk je met de hoogste met",250,450)
    text("de tegenstander. En zo vergelijk je elke dobbelsteen met je tegenstander tot je bij de laatste (laagste)",250,460)
    text("dobbelsteen bent. De verdediger heeft in het gevecht het voordeel. Als de dobbelstenen gelijk aan",250,470)
    text("elkaar zijn wint de verdediger. Je blijft dit doen tot een persoon geen troepen meer heeft.",250,480)
    
    fill(0)
    rect(365,520,210,50)
    fill(250)
    rect(370,525,200,40)
    fill(0)
    textFont(LTsubtitle)
    text("Press space for previous",390,550)
