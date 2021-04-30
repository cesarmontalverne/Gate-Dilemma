#game.py, cesar godoy
import pygame, gamebox, random
def And(inputs):
    for item in inputs:
        if item==0:
            return 0
    return 1
def Or(inputs):
    for item in inputs:
        if item==1:
            return 1
    return 0
def Nand(inputs):
    return not And(inputs)
def Nor(inputs):
    return not Or(inputs)
def Xor(inputs):
    totaltrue = 0
    for item in inputs:
        if item==1:
            totaltrue+=1
    return totaltrue%2
def Xnor(inputs):
    return not Xor(inputs)

camera = gamebox.Camera(800, 600)
def restart(govalue):
    global game_on, score, timer,inputs, output,siz,vari,selected
    game_on = govalue
    score = 0
    timer = 15
    inputs = [random.randint(0, 1) for i in range(2)]
    output = random.randint(0, 1)
    siz = 2
    vari = 1
    selected = "none"
restart(0)
def startscreen():
    start_screen = gamebox.from_color(400, 300, 'white', 1000, 800)
    camera.draw(start_screen)
    camera.draw(gamebox.from_text(400, 100, 'Gate Dilemma', 60, 'black'))
    camera.draw(gamebox.from_text(400, 550, 'By: Cesar A Godoy', 20, 'black'))
    camera.draw(gamebox.from_text(400, 570, 'Uses Gamebox, by Luther Tychonievich', 15, 'black'))
    instructions = ["Choose the gate that matches the inputs and the output."
        ,"Get ","with time running out and inputs increasing:"
        , "How many points can you score?"]
    for i in range(4):
        camera.draw(gamebox.from_text(400,200+i*35,instructions[i],35,'black'))
    camera.draw(gamebox.from_text(400, 445, 'Press Spacebar to Continue', 25, 'white'))
def gameover(keys):
    global game_on,score
    camera.clear("black")
    camera.draw(gamebox.from_text(400, 100, 'Game Over', 60, 'white'))
    camera.draw(gamebox.from_text(400, 300, 'Score: '+str(score), 60, 'white'))
    camera.draw(gamebox.from_text(400, 500, "press spacebar to restart", 60, 'white'))
    if pygame.K_SPACE in keys:
        restart(1)

def play(keys):
    global score,siz,inputs,output, game_on, inputs, output, siz
    camera.draw(gamebox.from_text(200, 100, 'INPUTS', 60, 'black'))
    camera.draw(gamebox.from_text(600, 100, 'OUTPUT', 60, 'black'))
    camera.draw(gamebox.from_text(400, 60, 'score: '+str(score), 30, 'black'))
    camera.draw(gamebox.from_text(400, 30, 'timer: '+str(round(timer)), 30, 'black'))
    for i in range(siz):
        camera.draw(gamebox.from_text(200, 150 + i * 35, str(inputs[i]), 35, 'black'))
    camera.draw(gamebox.from_text(600,150,str(output),35,'black'))
    #gates
    camera.draw(gamebox.from_color(400, 400, 'black', 800, 1))
    camera.draw(gamebox.from_color(400, 500, 'black', 800, 200))
    camera.draw(gamebox.from_color(133, 450, 'white', 266, 100))
    camera.draw(gamebox.from_color(667, 450, 'white', 266, 100))
    camera.draw(gamebox.from_color(400, 550, 'white', 266, 100))
    camera.draw(gamebox.from_text(133, 450, 'AND(1)', 40, 'black'))
    camera.draw(gamebox.from_text(400, 450, 'NAND(2)', 40, 'white'))
    camera.draw(gamebox.from_text(667, 450, 'OR(3)', 40, 'black'))
    camera.draw(gamebox.from_text(133, 550, 'NOR(4)', 40, 'white'))
    camera.draw(gamebox.from_text(400, 550, 'XOR(5)', 40, 'black'))
    camera.draw(gamebox.from_text(667, 550, 'XNOR(6)', 40, 'white'))
    scores(keys,pygame.K_1, And(inputs),1)
    scores(keys,pygame.K_2, Nand(inputs),2)
    scores(keys,pygame.K_3, Or(inputs),0.5)
    scores(keys,pygame.K_4, Nor(inputs),1)
    scores(keys,pygame.K_5, Xor(inputs),3)
    scores(keys,pygame.K_6, Xnor(inputs),3)

def inandout():
    global inputs,output,siz
    siz = min(max(2, score // 5), 7)  # minimum num of inputs is 2, max is 7 and it changes every 5 times u score
    inputs = [random.randint(0, 1) for i in range(siz)]
    output = random.randint(0, 1)

def scores(keys,k,gate,points):
    global game_on,score,timer, vari
    pressed = pygame.key.get_pressed()
    if pressed[k] and timer>0 and vari:
        if gate != output:
            timer = 0
        elif gate==output:
            vari = 0
            score+=points
    if not vari and not (k in keys):
        pygame.time.delay(200)
        vari = 1
        timer = 15
        inandout()
    elif timer<=0:
        game_on = 2

def tick(keys):
    '''
    runs the game
    '''
    global game_on,timer,vari
    if(not game_on):
        startscreen()
        if pygame.K_SPACE in keys:
            game_on = 1
    elif(game_on==1):
        camera.clear("white")
        play(keys)
    elif(game_on==2):
        gameover(keys)
    timer-=0.08
    #camera.draw(gamebox.from_text(400, 300, 'vari: '+str(vari), 30, 'black'))
    camera.display()
gamebox.timer_loop(30, tick)

