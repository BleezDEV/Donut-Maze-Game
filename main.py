#Donut Maze by @BleezDEV for 20 Second Game Jam 2022
import turtle
import random
import time
import sys
import winsound

#set recursion limit
sys.setrecursionlimit(10**6)

#setup window
wn = turtle.Screen()
wn.title('Donut Maze')
wn.setup(height=500, width=500)
wn.bgcolor('black')
wn.register_shape('Donut Maze Title Screen.gif')
wn.register_shape('Blocks for Donut Maze.gif')
wn.register_shape('Donut Maze Sprite Idle.gif')
wn.register_shape('Donut Maze Sprite Idle Left.gif')
wn.register_shape('Donut Maze Sprite Right 1.gif')
wn.register_shape('Donut Maze Sprite Right 2.gif')
wn.register_shape('Donut Maze Sprite Left 1.gif')
wn.register_shape('Donut Maze Sprite Left 2.gif')
wn.register_shape('donut.gif')
wn.register_shape('Game Over.gif')
wn.tracer(0)

#title screen
title = turtle.Turtle()
title.speed('fastest')
title.shape('Donut Maze Title Screen.gif')
title.penup()
wn.update()
winsound.PlaySound('gamestart.wav', winsound.SND_ASYNC)
time.sleep(5)
title.hideturtle()
wn.update()
winsound.PlaySound('backgroundtheme.wav', winsound.SND_LOOP + winsound.SND_ASYNC)

#create score and time
score = 0
gameTime = 20
scorePen = turtle.Turtle()
scorePen.speed('fastest')
scorePen.color('red')
scorePen.hideturtle()
scorePen.penup()
scorePen.setpos(-180, 170)
scorePen.write(f'SCORE: {score}              TIME: {gameTime}', font=('Arial', 20))

#create map array, hashtag represents blocks, and spaces represent empty area
maps = [(
  '#######'
  '#   # #'
  '#  #  #'
  '#     #'
  '##  # #'
  '#  #  #'
  '#######'
), (
  '#######'
  '#  #  #'
  '##  # #'
  '#   # #'
  '#  #  #'
  '#     #'
  '#######'
), (
  '#######'
  '#  #  #'
  '##   ##'
  '# #   #'
  '#  #  #'
  '#     #'
  '#######'
)]

map = maps[random.randint(0, 2)]

#create a variable used in the loop that you can change(represents how many columns in each row in map)
mapLength = 7

#create a variable used to setup screen, how many rows in the map
mapHeight = 7

#create counts for loop to space out blocks in each row and column
countX = 0
countY = 0

blocks = []

#draw game map
for row in map:
  for column in row:
    if column == '#':
      #create block as turtle
      newBlock = turtle.Turtle()
      newBlock.shape('Blocks for Donut Maze.gif')
      newBlock.speed('fastest')
      newBlock.penup()
      
      #change this value below to add space between blocks in map
      countX += 50

      #create variable for amount of blocks before moving on to next row (countX * (mapLength + 1))
      blockFull = 400

      #if a row has been mapped out, move on to next row by decreasing initial y value(move down) and reset x value
      if (countX%int(blockFull)) == 0:
        countX = 50
        countY += 50
        newBlock.setpos(-205+(countX), 130-countY)
        
      #otherwise keep adding to current row
      else:
        newBlock.setpos(-205+(countX), 130-countY)

      blocks.append(newBlock)
    #just make a space if there is empty space in map
    else:
      countX += 50

#create useful collision detection function for later
def isCollision(obj1, obj2):
  if obj1.distance(obj2) < 40:
    return True

#create player sprite
player = turtle.Turtle()
player.penup()
player.shape('Donut Maze Sprite Idle.gif')
player.setpos(0, -20)

#player movement functions
def left():
  if random.randint(1, 2) == 2:
    player.shape('Donut Maze Sprite Left 1.gif')
  else:
    player.shape('Donut Maze Sprite Left 2.gif')

  wn.update()
  player.seth(180)
  player.forward(10)
  #player.shape('Donut Maze Sprite Idle Left.gif')
  wn.update()

def right():
  if random.randint(1, 2) == 2:
    player.shape('Donut Maze Sprite Right 2.gif')
  else:
    player.shape('Donut Maze Sprite Right 1.gif') 
  
  wn.update()
  player.seth(0)
  player.forward(10)
  #player.shape('Donut Maze Sprite Idle.gif')
  wn.update()

def down():
  if random.randint(1, 2) == 2:
    player.shape('Donut Maze Sprite Right 2.gif')
  else:
    player.shape('Donut Maze Sprite Right 1.gif') 

  wn.update()
  player.seth(270)
  player.forward(10)
  #player.shape('Donut Maze Sprite Idle.gif')
  wn.update()

def up():
  if random.randint(1, 2) == 2:
    player.shape('Donut Maze Sprite Right 2.gif')
  else:
    player.shape('Donut Maze Sprite Right 1.gif') 

  wn.update()
  player.seth(90)
  player.forward(10)
  #player.shape('Donut Maze Sprite Idle.gif')
  wn.update()

#create donut / game objective
donut = turtle.Turtle()
donut.speed('fastest')
donut.shape('donut.gif')
donut.penup()

#create function that spawns donut to new random location
def newDonut():
  donut.hideturtle()
  #donut.setpos(random.randint(-190, 100), random.randint(-100, 100))
  for block in blocks:
    while isCollision(block, donut) or isCollision(player, donut):
      randomBlock = blocks[random.randint(7, 23)]
      x = randomBlock.xcor()
      y = randomBlock.ycor()
      donut.setpos(x, y)
      donut.seth(donut.towards(0, 0))
      donut.forward(50)
  
  donut.showturtle()

#get new donut every game
newDonut()

#create frame variable to keep track of frames
frame = 0

#create game over screen
gameOver = turtle.Turtle()
gameOver.speed('fastest')
gameOver.penup()
gameOver.shape('Game Over.gif')
gameOver.hideturtle()

#main loop
while True:
  newGame = False

  #set up framerate
  time.sleep(1./90)
  frame += 1

  #subtract 1 from time after 60 frames (1 second)
  if frame%60 == 0:
    frame = 0
    gameTime -= 1
    scorePen.undo()
    scorePen.setpos(-180, 170)
    scorePen.write(f'SCORE: {score}              TIME: {gameTime}', font=('Arial', 20))
    wn.update()

    #check if time reached 0 (game over)
    if gameTime == 0:
      gameOver.setpos(0, 0)
      gameOver.showturtle()
      scorePen.undo()
      scorePen.setpos(-150, -50)
      scorePen.write(f'YOU GOT {score} DONUTS.', font=('Arial', 20, 'bold'))
      wn.update()
      winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
      time.sleep(10)
      wn.bye()
      
  #check if collision between player and block in maze
  for block in blocks:
    if isCollision(block, player):
      player.backward(10)
      wn.update()

  if player.xcor() > 150 or player.xcor() < -150 or player.ycor() > 100 or player.ycor() < -200:
    player.setpos(0, 0)

  #check if collision between player and donut in maze
  if isCollision(player, donut):
    score += 1
    newDonut()
    scorePen.undo()
    scorePen.setpos(-180, 170)
    scorePen.write(f'SCORE: {score}              TIME: {gameTime}', font=('Arial', 20))

  #player keybinds
  wn.listen()
  wn.onkeypress(left, 'a')
  wn.onkeypress(right, 'd')
  wn.onkeypress(up, 'w')
  wn.onkeypress(down, 's')

  wn.update()
