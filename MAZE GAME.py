print('Using the arrow keys, move to the blue coloured treasures, in order to colour the whole maze. BEWARE OF OBSTACLES! Hope you enjoy! :)')
import turtle
import math #importing modules
import random
wn=turtle.Screen()
wn.bgcolor("Black")
wn.title("Maze Game")#initializing the screen
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")#creating pen for walls
        self.color("white")
        self.penup()
        self.speed(0)#animation speed

class Pen1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")#creating pen for coloured walls
        self.penup()
        self.speed(0)#animation speed

class Player(turtle.Turtle):#creating class for player
    def __init__(self):#allows the class to initialize attributes of the object
        turtle.Turtle.__init__(self)
        self.shape("circle")#creating player
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gem=0

#initializing movement to players   
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() +24
        if (move_to_x,move_to_y) not in walls:#prevents collision with walls of the maze
            self.goto(move_to_x,move_to_y)
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() -24
        if (move_to_x,move_to_y) not in walls:#prevents collision with walls of the maze
            self.goto(move_to_x,move_to_y)
    def go_left(self):
        move_to_x = player.xcor() -24
        move_to_y = player.ycor() 
        if (move_to_x,move_to_y) not in walls:#prevents collision with walls of the maze
            self.goto(move_to_x,move_to_y)
    def go_right(self):
        move_to_x = player.xcor() +24
        move_to_y = player.ycor() 
        if (move_to_x,move_to_y) not in walls:#prevents collision with walls of the maze
            self.goto(move_to_x,move_to_y)

    def is_collision(self, other):#defining collision 
        a=self.xcor() - other.xcor()#equations to detect collision
        b=self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:#condition for collision
            return True
        else:
            return False

        
class Treasure(turtle.Turtle):#creating treasure
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gem = 100
        self.goto(x,y)#coordinates of treasures

    def destroy(self):#dissapearance of treasure after collision
        self.goto(200000,200000)
        player.goto(0,144)
        self.hideturtle()

class Obstacle(turtle.Turtle):#creating obstacles 
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color('red')
        self.penup()
        self.speed(0)
        self.goto(x,y)#coordinates of obstacles
        self.direction = random.choice(['left','right'])#direction of movement of obstacles
    def move(self):#defining movement of obstacles
        if self.direction=='left':
            dx=-24
            dy=0
            self.shape('triangle')
        elif self.direction=='right':
            dx = 24
            dy=0
            self.shape('triangle')
        else:
            dx=0
            dy=0

        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy

        if (move_to_x,move_to_y) not in walls:#prevents collision with walls
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(['left','right'])
#movement per millisecond
            turtle.ontimer(self.move, t=random.randint(100,300))
#creating the maze in the form of a list
levels = [""]
level_1 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"x   xxx    x   x  xxx   x",
"x  x t x  x x x xx   x  x",
"x xo    xx   xxxx     x x",
"xx       xxxxxxx       xx",
"xx  xx      p     xx   xx",
"xx  xx            xx   xx",
"xx       xx    x       xx",
"xx      x x    xxo     xx",
"x x    x  x    x x t  x x",
"x  xxxx   x    x  xxxx  x",
"xx x x x xx    xx x x x x",
"x x x x x        x xtx xx",
"xo                      x",
"xx  xxx  xx    xx  xxx xx",
"x xx   xx x    x x   tx x",
"x x     x x    x xo     x",
"xx                     xx",
"xx x x             x x xx",
"xx xxx    xxxxxx   xxx xx",
"xx       x      x      xx",
"x xo    x  x   x x    x x",
"x  x t x    x x   x  x  x",
"x   xxx      x     xx   x",
"xxxxxxxxxxxxxxxxxxxxxxxxx" 
]

treasures = []#list for treasures required for appending
obstacles=[]#list for obstacles required for appending
levels.append(level_1)
character=""
def setup_maze(level_1):#function to set up the maze
    for y in range(len(level_1)):
        for x in range(len(level_1[y])):
            character = level_1[y][x]
            screen_x = -288 + (x * 24)#x-axis
            screen_y = 288 - (y * 24)#y-axis
            if character == "x":
                pen.goto(screen_x, screen_y)#walls at specific coordinates
                pen.stamp()
                walls.append((screen_x, screen_y))#appending to walls list in order to prevent collision
            if character == 'p':
                player.goto(screen_x, screen_y)#getting coordinates of player
            if character == 't':
                treasures.append(Treasure(screen_x, screen_y))#getting coordinates of treasure
            if character == 'y':#recolouring of maze
                pen1.goto(screen_x,screen_y)
                pen1.stamp()
                walls.append((screen_x,screen_y))
            if character == 'o':#obstacles
                obstacles.append(Obstacle(screen_x,screen_y))

pen = Pen()#association with respective functions and objects
player=Player()
walls=[]#walls list
pen1=Pen1()


setup_maze(levels[1])


turtle.listen()#connecting the keyboard to the code
turtle.onkey(player.go_left,"Left")#left arrow key 
turtle.onkey(player.go_right,"Right")#right arrow key
turtle.onkey(player.go_up,"Up")#up arrow key
turtle.onkey(player.go_down,"Down")#down arrow key



wn.tracer(2)#turns turtle animation off and sets a delay for updating the screen
q=4
count=0
while True:#game loop
    for treasure in treasures:#checking for treasure
        if player.is_collision(treasure):#checking for collision with treasure
            count+=1
            player.gem+= treasure.gem#collecting gems
            print("Player gems: {}".format(player.gem))#printing gem count on idle
            #loop to recolour the maze
            for i in range(len(level_1)):
                str1=""
                for j in range(len(level_1[i])):
                    if i <= q:
                        if level_1[i][j]=='x':
                            str1+='y'
                        elif level_1[i][j]=='t':
                            str1+='y'
                        elif level_1[i][j]=='o':
                            str1+=' '
                        elif level_1[i][j]==' ':
                            str1+=' '
                        elif level_1[i][j]=='p':
                            str1+='p'
                    elif i > q:
                        if level_1[i][j]=='o':
                            str1+=' '
                        else:
                            str1+=level_1[i][j]
                level_1[i]=str1
            setup_maze(level_1)
            q+=5
    for obstacle in obstacles:#loop for movement of obstacles
        turtle.ontimer(obstacle.move, t=200)
        if player.is_collision(obstacle):
            player.goto(0,144)
    
    if count==5:#end of game
        print("Game over, hope you liked it!")#printing on idle
        text = turtle.Turtle()
        text.speed(1)
        text.color("white")
        text.penup()
        text.setposition(-50, 50)
        text.write("GAME OVER",font=("Helvetica", 50, "normal"))#printing on turtle screen
        wn.delay(9)#delay text on the turtle screen
        text.hideturtle()
        turtle.bye()#exitting turtle
    wn.update()#updating turtle screen
turtle.done()
'''
HOPE YOU ENJOYED THE GAME! :)
'''
