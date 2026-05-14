app.background = fill='silver'

import time
time = time.perf_counter()
#gradient('Orange', 'Red', start='top')
#sound('cmu://1204766/46781422/Yakuza+0+OST+-+54+Fiercest+Warrior+ver+0.mp3') ROBOT BOSS 1
#sound('cmu://1204766/46833344/Limbus+Company+-+Canto+V+Boss+1+Battle+Theme.mp3') MISSILE BOSS 2
#sound('cmu://1204766/46833449/Limbus+Company+OST+-+Middle+Finger+Sanjou.mp3') SNAKE BOSS 3
#sound('cmu://1204766/46833481/[+Lobotoapp.MissileYCorporation+OST+]+-+Second+Warning.mp3') AMALGAMATION BOSS  (FINAL)
#sound('cmu://1204766/46984121/Shun+Akiyama+(秋山+駿)+-+Baka+Mitai+(馬鹿みたい)+Lyrics+(RomajiKanjiEng+Trans)+Yakuza+5+(龍が如く)+OST+(1).mp3')
#sound('cmu://1204766/46985822/Yakuza_+Like+A+Dragon+-+Baka+Mitai+(I've+Been+a+Fool)+(English).mp3')
#^WINNING SCREEN SONG
app.stepsPerSecond = 60
app.steps = 0
app.stepHeight = 250

Background = Group(
    Image('cmu://1204766/46767736/hq720.Png', 0, 0, width=600, height=400),
    Rect(0, 0, 400, 400, fill=gradient('grey', 'white', start='top'), opacity=40)
)

Boss = Group(
    Image('cmu://1204779/46774386/bigkillerrobot.png', -200, 400, width=800, height=800),
    Image('cmu://1204779/46774443/bigkillerrobothand.png', -20, 675, width=100, height=100)
    )

Hand = Group(
    Image('cmu://1204779/46774480/bigkillerrobothandR.png', 310, 665, width=100, height=110)
    )

Boss2 = Group(
    Image('cmu://1204779/46795527/Untitled+design.png', 400, 217, width=150, height=160)
    )

Boss3 = Group(
    Image('cmu://1204779/46853931/2cd7434e-d342-4c0a-9093-c749b1b0da5e.png', 300, 405, height=200, width=90)
    )

#rotate_Boss3 = Boss3.rotate(45, 200, 200)

player = Group( 
    Image('cmu://1204766/46765880/bobogbobng.png', 190, 295, width= 34, height=55)
    )

shield = Group (
    Oval(180, 322.5, 10, 35, fill='blue')
    )

player.dy = 0
player.isJumping = False
player.hit  = False
player.tooHigh = False

floor = Group(
    Rect(-3, 350, 410, 50, fill=rgb(35, 35, 35))
)

Rect(300, 25, 100, 50, fill='lightGrey', border='dimGrey', borderWidth=2)

Pillar = Group(
    Rect(200, -400, 40, 400, fill=gradient('white', 'red', 'red', 'white', start='left')),
    Polygon(210, 0, 195, 0, 185, -20, fill='red'),
    Polygon(230, 0, 245, 0, 255, -20, fill='red'),
    Rect(200, -400, 40, 400, fill='red', opacity=30)
    )
    
outsideBlock = Rect(410, 200, 20, 20)

Warning = Group(
    Rect(20, 20, 300, 50, fill=None, border='red', borderWidth=3),
    Label('ORBITAL STRIKE INBOUND!!', 170, 45, size=17, fill='yellow', font='orbitron')
    )
    
music = Sound('cmu://1204766/46781422/Yakuza+0+OST+-+54+Fiercest+Warrior+ver+0.mp3')
blocks = Group()
meteor = Group()
LaserL = Group()
LaserR = Group()
Missile = Group()
groundBlocks = Group()
groundBlocks.dy = 0

bossWarning = Group(
    Image('cmu://1204779/46774186/PSD603.jpg', 0, 10, width=200, height=20),
    Image('cmu://1204779/46774186/PSD603.jpg', 200, 10, width=200, height=20),
    Image('cmu://1204779/46774186/PSD603.jpg', 0, 370, width=200, height=20),
    Image('cmu://1204779/46774186/PSD603.jpg', 200, 370, width=200, height=20)
    )

lava = Group(
    Rect(0, 400, 400, 400, fill=gradient('red', 'orange', start='top'), opacity=90),
    Rect(0, 395, 400, 10, fill=gradient('lightYellow', 'yellow', 'white', start='top'), opacity=70)
    )

time1 = Label(0, 350, 50, fill='dimGrey', size=30, font='orbitron')

conveyer1 = Group(
    Rect(0, 350, 400, 50, fill='darkGrey'),
    Line(0, 375, 400, 375, fill='grey', lineWidth=48, dashes=(2, 25))
    )
conveyer2 = Group(
    Rect(-400, 350, 400, 50, fill='darkGrey'),
    Line(-400, 375, 0, 375, fill='grey', lineWidth=48, dashes=(2, 25))
    )


transition = Group(
    Rect(0, 0, 400, 400, opacity=0)
    )    
    

instructions = Group(
    Image('cmu://1204766/46768858/ab6e6f39240d7dc6387a0f2e0efc148e.png', -400, 0, width=801, height=404),
    #Rect(0, 0, 400, 400, fill=app.background),
    #Label('Hold the right and left keys to move', 200, 150, size=20),
    #Label('Avoid getting hit by blocks', 200, 200, size=20),
    Label('PRESS SPACE', 83, 250, size=19, font='orbitron', fill='white')
    )

    
def gameOver():
    #Rect(60, 70, 280, 150, fill='black')
    Rect(0, 0, 400, 400, fill='red', opacity=25)
    Image('cmu://1204779/46835910/cdccbdf4-14e1-4696-9328-b2b87424f0df.png', 0, 0, height=400, width=400)
    #Label('Combusted instantly.', 200, 120, size=30, fill='White')
    #Label('time1: ' + str(time1.value) + ' seconds', 200, 200, size=20, fill='White')
    app.stop()

def makeBlock():
    x = randrange(0, 390)
    y = (-1) * 15
    newBlock = Group(
        Image('cmu://1204779/46835549/6061515b-be14-4c56-ac54-b6c7c9ba16ba.png',x + 5, y, width=25, height=45, opacity=55)
    )
    blocks.add(newBlock)
    
def makeBoss():
    size = 30
    x = randrange(0, 390)
    y = (-1) * size - 50
    color = 'red'
    newBoss = Group(
        Rect(x + 5, y, size - 10, size, fill=color, border='black'),
        Rect(x, y + 5, size, size - 10, fill=color, border='black'),
        Rect(x + 3, y + 3, size - 6, size - 6, fill=color)
        )
    meteor.add(newBoss)
    
def makeLaserL():
    newLaserL = Group (
        Oval(450, 325, 50, 20, fill=gradient('white', 'red', 'white', start='top'))
        )
    LaserL.add(newLaserL)
    
def makeLaserR():
    newLaserR = Group(
        Oval(-50, 325, 50, 20, fill=gradient('white', 'red', 'white', start='top'))
        )
    LaserR.add(newLaserR)
    
def makeMissile():
    x = randrange(320, 350)
    newMissile = Group (
        Image('cmu://1204779/46795710/Untitled+design+1.png', x, 300, width=25, height=40)
        )
    
    rotate_img = Missile.rotate(135, Missile.centerX, Missile.centerY)
    Missile.add(newMissile)


def meteorWarning(x):
    Rect(x, 0, 15, 40, fill=gradient('red', 'white', start=top))
    
def checkHitsFallingBlock():
    for block in blocks:
        if (player.hitsShape(block) == True):
            return True
    return False
    
def onKeyPress(key):
    # Starts the jumping animation.
    if ((key == '') and (player.isJumping == False)):
        player.isJumping = True
        player.dy = -3

    if (key == 'space'):
        instructions.visible = False
        Pillar.visible = False
        Warning.visible = False
        bossWarning.visible = False
        shield.visible = False
        conveyer1.visible = False
        
def onKeyHold(keys):
    # Moves the players.
    if ('right' in keys):
        player.centerX += 4
        shield.centerX = player.centerX +20
        shield.centerX += 4
    elif ('left' in keys):
        player.centerX -= 4
        shield.centerX = player.centerX -20
        shield.centerX -= 4
        
    if ('right' in keys and 'up' in keys):
        player.centerX += 10
        shield.centerX += 10
    elif ('left' in keys and 'up' in keys):
        player.centerX -= 10
        shield.centerX -= 10
        

    # Wraparound.
    if (player.centerX >= 400):
        player.centerX = 400
    elif (player.centerX <= 0):
        player.centerX = 0
        
    # Moves the lava.
    if ('z' in keys and 'x' in keys):
        lava.centerY += 0.5


def onStep():
    # If the instructions are visible, don't do the rest of onStep.
    if (instructions.visible == True):
        return None
        
        #make block outside of screen for pillar to follow

    #Boss 1 (create a pause value to pause the music at 150, everytime1 i do this i break the game somehow... lol)
    if (time1.value >=10):
      if (time1.value == 10):
          music.play(loop=False)
      elif (time1.value >=70):
        music.play(loop=False)
    if (time1.value >= 5 and time1.value <= 10):
        bossWarning.visible = True
    if (time1.value >= 10 and time1.value <= 40):
        bossWarning.visible = False
        Boss.centerY -= 1.25
        if (Boss.centerY <= 400):
            Boss.centerY = 400
        if (Boss.centerY <= 400 and time1.value <= 90):
            Hand.centerY = 325
        if (time1.value <= 90 and time1.value >= 10):
            shield.visble = True
            LaserL.centerX -= 4
            LaserR.centerX += 4
            if (app.steps % 100 == 0):
                rand = randrange(0, 5)
                if (rand == 3):
                    makeLaserL()
            if (app.steps % 100 == 0):
                rand = randrange(0, 2)
                if (rand == 1):
                    makeLaserR()
    if (time1.value >= 105 and time1.value <= 120):
        shield.visible = False
        Boss.centerY += 2
        if (Boss.centerY == 800):
            Boss.centerY = 800
            
    if (time1.value >= 99 and time1.value <= 100):
        Hand.centerY -= 3
    if (time1.value >= 100):
        Hand.centerY += 6
        
    if (time1.value >= 10):
        shield.visible = True
    if (LaserL.hitsShape(shield) == True):
        LaserL.centerX = 500000
        LaserL.centerY = 325
    if (LaserR.hitsShape(shield) == True):
        LaserR.centerX = -500000
        LaserR.centerY = 325
        
    if (time1.value >= 102):
        Hand.centerY = 665
        
    if (time1.value == 100):
        transition.opacity = 50
    if (time1.value == 101):
        transition.opacity = 100
    if (time1.value == 110):
        transition.opacity = 50
    if (time1.value == 111):
        transition.opacity = 0
        
                    
    #hazard 1, falling debris
    if (time1.value >= 120):
        meteor.centerY += 6
    if (time1.value >= 120 and time1.value <= 150):
        if (app.steps % 30 == 0):
            rand = randrange(0, 2)
            if (rand == 1):
                makeBoss()

                
    #boss 2
    if (time1.value >=180):
      if (time1.value == 180):
          music.play(loop=True)
      elif (time1.value >=240):
          music.play(loop=False)
    if (time1.value >= 170):
        bossWarning.visible = True
    if (time1.value >= 170):
        bossWarning.visible = False
    
    if (time1.value >= 180):
        Boss2.centerX -= 1.75
        if (Boss2.centerX <= 325):
            Boss2.centerX = 325
        if (time1.value >= 180 and time1.value <= 240):
            if (app.steps % 110 == 0):
                rand = randrange(0, 2)
                if (rand == 1):
                    makeMissile()
            Missilex = randrange(3,4)
            MissileY = randrange(4,5)
            bounce = Group()
            bounce = 0
            if (bounce.value <= 5):
                if (Missile.centerX <= 10):
                    Missilex = Missilex * (-1)
                    bounce += 1
                    rotate_img = Missile.rotate(270, Missile.centerX, Missile.centerY)
                if (Missile.centerY <= 10):
                    MissileY = MissileY * (-1)
                    bounce += 1
                    rotate_img = Missile.rotate(270, Missile.centerX, Missile.centerY)
                if (Missile.centerX >= 390):
                    Missilex = Missilex * (-1)
                    bounce += 1
                    rotate_img = Missile.rotate(270, Missile.centerX, Missile.centerY)
                if (Missile.centerY >= 390):
                    MissileY = MissileY * (-1)
                    bounce += 1
                    rotate_img = Missile.rotate(270, Missile.centerX, Missile.centerY)
                Missile.centerX -= Missilex
                Missile.centerY -= MissileY
                #time1.wait=(0.0001)
                #time.sleep=(0.00001)
                #Copyimport time, 
                #time.sleep(2.5)
    if (time1.value >= 240):
        Boss2.centerX += 3
        Missile.visible = True
        if (Boss2.centerX == 425):
            Boss2.centerX = 425
    
    
    
    #Hazard 2, conveyer belt
    if (time1.value >= 270 and time1.value <= 285):
        conveyer1.centerX += 0.75
        conveyer2.centerX += 0.75
        if (conveyer1.centerX >= 600):
            conveyer1.centerX = -200
        if (conveyer2.centerX >= 600):
            conveyer2.centerX = -200
        player.centerX += 0.75
    if (time1.value >= 285 and time1.value <= 300):
        conveyer1.centerX -= 0.75
        conveyer2.centerX -= 0.75
        if (conveyer1.centerX <= -200):
            conveyer1.centerX = 600
        if (conveyer2.centerX <= -200):
            conveyer2.centerX = 600
        player.centerX -= 0.75



    #boss 3, snake
    if (time1.value >= 330):
        Boss3.centerY -= 4
        if (Boss3.centerY <= 255):
            Boss3.centerY = 255
     
                   
    #hazard 3
    if (time1.value == 415):
        Warning.visible = True
    elif (time1.value == 420):
        Warning.visible = False
    if (time1.value >= 420):
        if (time1.value <=450):
            Pillar.visible = True
            if (Pillar.centerY <= 190):
                Pillar.centerY += 11
            if (Pillar.centerX >= outsideBlock.centerX):
                Pillar.centerX -= 0.24
                if (Pillar.centerX <= 100):
                    outsideBlock.centerX = 420
            if (Pillar.centerX <= outsideBlock.centerX):
                Pillar.centerX += 0.24
                if (Pillar.centerX >= 300):
                    outsideBlock.centerX = -20
        else:
            Pillar.centerX = -200

        
        
    #boss 4, final boss, amalgamation
    
        

    
    if (player.hitsShape(Pillar) == True):
        gameOver()
    if (player.hitsShape(LaserL) == True):
        gameOver()
    if (player.hitsShape(LaserR) == True):
        gameOver()
    if (player.hitsShape(meteor) == True):
        gameOver()
    if (player.hitsShape(Missile) == True):
        gameOver()
    if (player.hitsShape(Boss3) == True):
        gameOver()
    
    app.steps += 1
    time1.value = int(lava.top - player.bottom - 45) #int(lava.top - player.bottom - 45)

    lava.centerY += 0.01 #0.01 default speed
  

    # Creates new blocks. #Change % to 100 to slow block spawn
    if (time1.value >= 115):
        if (app.steps % 30 == 0):
            rand = randrange(0, 2)
            if (rand == 1):
                makeBlock()
    if (time1.value >= 120):
        if (app.steps % 50 == 0):
            rand = randrange(0, 2)
            if (rand == 1):
                makeBlock()
    if (time1.value >= 129):
        if (app.steps % 200 == 0):
            rand = randrange(0, 2)
            if (rand == 1):
                makeBlock()    
    if (time1.value >= 160):
        if (app.steps % 100 == 0):
            rand = randrange(0, 2)
            if (rand == 1):
                makeBlock() 
    if (time1.value >= 185):
        if (app.steps % 10000000000 == 0):
            rand = randrange(0, 2)
            if (rand == 1):
                makeBlock()


    # Jumping animation.
    # Moves the screen down if the player gets high enough.
    if ((app.stepHeight - player.bottom > 5) and (player.tooHigh == False)):
        groundBlocks.dy = 10
        player.tooHigh = True

    if (groundBlocks.dy > 0):
        groundBlocks.centerY += groundBlocks.dy
        floor.centerY += groundBlocks.dy
        lava.centerY += groundBlocks.dy
        groundBlocks.dy = 0

    # Moves all the blocks down.
    for block in blocks:
        if (block.hitsShape(player) == True):
            gameOver()

        if ((block.bottom <= floor.bottom) and
            (groundBlocks.hitsShape(block) == False)):
            block.centerY += 4
        else:
            blocks.remove(block)
            groundBlocks.add(block)

        # Removes any blocks that have fallen off the canvas.
        if (block.top >= 320):
            blocks.remove(block)

    # Removes any blocks that have landed on the ground and are below the canvas.
    for block in groundBlocks:
        if (block.top >= 400):
            groundBlocks.remove(block)
