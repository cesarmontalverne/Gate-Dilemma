#gatedilemma.py, cesar godoy
import pygame, gamebox, random
# logic gate simulator
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
    return not(Xor(inputs))

camera = gamebox.Camera(800, 600)
def restart(govalue):
    '''
    initializes all variables necessary to start (or restart) the game from the very beginning (2 inputs and 10 time units)
    '''
    global game_on, score, timer,inputs, output,siz,vari,selected, gatetried
    game_on = govalue
    score = 0
    timer = 10
    inputs = [random.randint(0, 1) for i in range(2)]
    output = random.randint(0, 1)
    siz = 2
    vari = 1
    gatetried = 0
restart(0) #initializes the variables
def startscreen():
    '''
    just builds the start screen
    '''
    start_screen = gamebox.from_color(400, 300, 'white', 1000, 800)
    camera.draw(start_screen)
    camera.draw(gamebox.from_text(400, 100, 'Gate Dilemma', 60, 'black'))
    fin = open("score.txt","r")
    camera.draw(gamebox.from_text(400, 50, 'High Score: '+fin.readline().strip(), 30, 'black'))
    fin.close()
    camera.draw(gamebox.from_text(400, 550, 'By: Cesar A Godoy', 20, 'black'))
    camera.draw(gamebox.from_text(400, 570, 'Uses Gamebox, by Luther Tychonievich', 15, 'black'))
    instructions = ["Choose the gate that matches the inputs and the output."
        ,"The time is short and the inputs increasing", "How many points can you score?"]
    for i in range(len(instructions)):
        camera.draw(gamebox.from_text(400,200+i*35,instructions[i],35,'black'))
    camera.draw(gamebox.from_text(400, 515, 'Press Spacebar to Continue', 30, 'red'))
    camera.draw(gamebox.from_text(400, 350, "Select keys and gain points as specified:", 25, 'black'))
    gatespec = ["Gate     key#     points", "AND          1            1",
                "NAND        2            2","OR            3           1","NOR          8           2","XOR           9           3","XNOR        0            3"]
    for i in range(len(gatespec)):
        camera.draw(gamebox.from_text(400,375+i*15,gatespec[i],20,'black'))


def gameover(keys):
    '''
    deals with all the stuff that happens when the game is over. restarts all varaibles
    leading you to restart the game or to the menu, whatever you please. Shows highscores and etc
    '''
    camera.clear("black")
    camera.draw(gamebox.from_text(400, 100, 'Game Over', 65, 'white'))
    camera.draw(gamebox.from_text(400, 300, 'Score: '+str(score), 55, 'white'))
    fin = open("score.txt","r")
    highscore = int(fin.readline().strip())
    fin.close()
    camera.draw(gamebox.from_text(400, 250, 'Highscore: '+str(highscore), 55, 'white'))
    fout = open("score.txt","w")
    fout.write(str(round(max(score,highscore))))
    fout.close()
    camera.draw(gamebox.from_text(400, 550, "press spacebar to restart", 30, 'red'))
    camera.draw(gamebox.from_text(400, 515, 'Press M to go to menu', 30, 'red'))
    camera.draw(gamebox.from_text(200, 400, "inputs", 35, 'white'))
    camera.draw(gamebox.from_text(400, 400, "output", 35, 'white'))
    camera.draw(gamebox.from_text(400, 440, str(output), 30, 'white'))
    camera.draw(gamebox.from_text(600, 400, "gate tried", 35, 'white'))
    gate = ["NONE","AND","NAND","OR","NOR","XOR","XNOR"]
    camera.draw(gamebox.from_text(600, 440, gate[gatetried], 30, 'white'))
    for i in range(round(siz)):
        camera.draw(gamebox.from_text(180+i*20-(siz-2)*5, 440, str(inputs[i]), 30, 'white'))
    #camera.draw(gamebox.from_text(400, 600, "press spacebar to restart", 60, 'white'))
    if pygame.K_SPACE in keys:
        restart(1) #restarts variables and sets the page to menu
    if pygame.K_m in keys:
        restart(0)

def play():
    """
    sets playing mode. calls the relevant functions for the input section of the game
    """
    global score,siz,inputs,output, game_on, inputs, output, siz
    camera.draw(gamebox.from_text(200, 100, 'INPUTS', 60, 'black'))
    camera.draw(gamebox.from_text(600, 100, 'OUTPUT', 60, 'black'))
    camera.draw(gamebox.from_text(400, 60, 'score: '+str(score), 30, 'black'))
    camera.draw(gamebox.from_text(400, 30, 'timer: '+str(round(timer)), 30, 'black'))
    for i in range(round(siz)):
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
    scores(pygame.K_1, And(inputs),1,1)
    scores(pygame.K_2, Nand(inputs),2,2)
    scores(pygame.K_3, Or(inputs),1,3)
    scores(pygame.K_8, Nor(inputs),2,4)
    scores(pygame.K_9, Xor(inputs),3,5)
    scores(pygame.K_0, Xnor(inputs),3,6)

def inandout():
    '''
    defines inputs, the output and number of inputs
    '''
    global inputs,output,siz
    siz = min(max(2, int(score) // 5), 7)  # minimum num of inputs is 2, max is 7 and it changes every 5 times u score
    inputs = [random.randint(0, 1) for i in range(round(siz))]
    output = random.randint(0, 1)

def scores(k,gate,points,attempind):
    '''
    input section of the game. where all the user input and answer verification comes along.
    '''
    global game_on,score,timer, vari,gatetried
    pressed = pygame.key.get_pressed()
    list = [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_8,pygame.K_9]
    if pressed[k] and timer>0 and vari:
        if gate != output:
            gatetried = attempind
            timer = 0
        elif gate==output:
            vari = 0
            score+=points
            inandout()
    elif timer<=0:
        game_on = 2
    for i in range(6):
        # this loop is necessary because we need to make sure none of the keys is NOT being pressed.
        # if Im selecting XOR by pressing 9, then 1,2,3,8 and 0 are not being pressed and the condition not pressed[k] is true
        # which causes the inandout method to be called and change the inputs while you are still answering the previous question
        if not vari and not pressed[list[i]]:
            pygame.time.delay(200)
            vari = 1
            timer = max(5,10-1/(8*score))

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
        play()
        timer -= 0.08
    elif(game_on==2):
        gameover(keys)
    camera.display()
gamebox.timer_loop(30, tick)

