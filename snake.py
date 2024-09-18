import turtle, random
foodbit = turtle.Turtle()
score = 0
pcount = 0

'''
implemented 1,2,3,4,5,6, and 7:
(score output, full functioning pause and unpause option, the ability to choose if the player wants an enemy snake or not, 
general aesthetic imrpovements, an option to change the color of the player snake, and a celebratory random color change every time the player gets 5 points
'''

class Food:
    '''
    Purpose: To construct a food object that a snake can eat in order to grow segments and gain points

    Instance variables: self.x: the food object's x coordinate  
                        self.y: the food object's y coordinate
                        self.color = the food object's color 

    Methods: __init__ = a constructor to initialize self.color, self.x, self.y, and to create the "foodbit" turtle and to place it randomly
            new_pos = a method that will place the food object in a new, random location somewhere on the game map, ensuring it doesn't spawn in a snake
    '''
    def __init__(self,x,y,color):
        self.color = color
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        foodbit.speed(0)
        foodbit.fillcolor(self.color)
        foodbit.shape("circle")
        foodbit.shapesize(1.5,1.5)
        foodbit.penup()
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        foodbit.setx(self.x)
        foodbit.sety(self.y)

    def new_pos(self,food,segments):
        '''
        5: food pellets will not spawn in snake(s)
        '''
        free = True
        segx = []
        segy = []
        
        for i in range(len(segments)):
            segx.append(segments[i].xcor())
            segy.append(segments[i].ycor())
        
        while free:
            self.x = 15 + 30*random.randint(0,19)
            self.y = 15 + 30*random.randint(0,19)
            for i in range(len(segx)):
                if segx[i] == self.x and segy[i] == self.y:
                    self.x = 15 + 30*random.randint(0,19)
                    self.y = 15 + 30*random.randint(0,19)
                    free = True
                else:
                    free = False
        foodbit.setx(self.x)
        foodbit.sety(self.y)

class Enemy:
    '''
    1: Add an enemy snake controlled by the computer that's a different color
    '''


    '''
    Purpose: To construct an enemy snake object to act as a challenge for the player

    Instance variables: self.x: the enemy snake object's head's x coordinate  
                        self.y: the enemy snake object's y coordinate
                        self.color = the enemy snake object's color 
                        self.rival = a boolean declaring if there will or not be a "rival" to play against
                        self.alive = a boolean declaring if the enemy snake object is alive or not
                        self.segments = a list containing all of the enemy snake's segments (turtles)
                        self.vx = the velocity of the enemy snake object with respect to the x axis
                        self.vy = the velocity of the enemy snake object with respect to the y axis
                        self.p_count = the current amount of times "p" has been pressed to gauge if the game should pause or unpause

    Methods: __init__ = a constructor to initialize self.rival, and if self.rival == True: self.alive, self.x, self.y, self.color, self.segments. self.vx, self.vy, and self.p_count. It also calls the grow method
            grow = a method that will create a segment turtle object and add it to the self.segments list
            move = a method that, if self.rival == True, will dictate how the enemy snake should move in order to get to a food object.
                   It also checks if the head of the enemy snake object is on a foodbit, causing the grow method to be called. Lastly, it makes each of the segment turtle objects follow the path of the segment infront of them.
            
    '''
    def __init__(self, x, y, color, rival):
        self.rival = rival
        if self.rival:
            self.alive = True
            self.x = x
            self.y = y
            self.color = color
            self.segments = []
            self.grow()
            self.vx = 15
            self.vy = 0
            self.p_count = 0

    def grow(self):
        if self.rival:
            head = turtle.Turtle()
            head.speed(0)
            head.fillcolor(self.color)
            head.shape("square")
            head.shapesize(1.5,1.5)
            head.penup()
            head.setx(self.x)
            head.sety(self.y)
            (self.segments).append(head)

    def move(self, food):
        global score

        if self.rival:
            if pcount % 2 == 0 and self.alive:
                if food.x < self.x and abs(self.x - food.x) >= 15:
                    self.x -= 30
                elif food.x > self.x and abs(self.x - food.x) >= 15:
                    self.x += 30
                else:
                    if food.y < self.y and abs(self.y - food.y) >= 15:
                        self.y -= 30
                    elif food.y > self.y and abs(self.x - food.x) >= 15:
                        self.y += 30
                    else:
                        self.y += 30

                if self.x == food.x and self.y == food.y:
                    self.grow()
                    food.new_pos(foodbit,self.segments)

                if len(self.segments) > 1 and self.p_count % 2 == 0:
                    for i in range(len(self.segments)-1,0,-1):
                        self.segments[i].setx(self.segments[i-1].xcor())
                        self.segments[i].sety(self.segments[i-1].ycor())

                (self.segments[0]).setx(self.x)
                (self.segments[0]).sety(self.y)

class Snake:
    '''
    Purpose: To construct a snake object for the player to control

    Instance variables: self.x: the snake object's head's x coordinate  
                        self.y: the snake object's y coordinate
                        self.color = the snake object's color 
                        self.segments = a list containing all of the snake's segments (turtles)
                        self.vx = the velocity of the snake object with respect to the x axis
                        self.vy = the velocity of the snake object with respect to the y axis
                        self.gameover = a boolean declaring if the game has been lost or not
                        self.move_logx = a list containing all moves made by the player in the x direction
                        self.move_logy = a list containing all moves made by the player in the y direction
                        self.p_count = the current amount of times "p" has been pressed to gauge if the game should pause or unpause

    Methods: __init__ = a constructor to initialize self.x, self.y, self.color, self.segments, self.vx, self.vy, self.gameover, self.move_logx, self.move_logy, and self.p_count. It also calls the grow method
            grow = a method that will create a segment turtle object and add it to the self.segments list
            move = a method that will alter self.x and self.y given a player's directional input. It also checks for several game over conditions, and makes each of the segment turtle objects follow the path of the segment infront of them.
                   It also checks if the head of the snake object is on a foodbit, causing the grow method to happen. Lastly, it makes each of the segment turtle objects follow the path of the segment infront of them.
            go_down = a method that will set self.vx to 0 and self.vy to -30
            go_up = a method that will set self.vx to 0 and self.vy to 30
            go_left = a method that will set self.vx to -30 and self.vy to 0
            go_right = a method that will set self.vx to 30 and self.vy to 0
            pause = a method that will freeze the player snake object, and if there is one, the enemy snake object as well.
            restart = a method that will restart the game
    '''
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.grow()
        self.vx = 30
        self.vy = 0
        self.gameover = False
        self.move_logx = []
        self.move_logy = []
        self.p_count = 0

    def grow(self):
        global score
        '''
        7. score counter that will be outputted at end of game and a temporary "party" mode every time the player scores 5 points
        '''
        score += 1
        colors = ["red","yellow","orange","green","pink","black","grey","white"]
        if score % 6 == 0:
            for i in range(len(self.segments)):
                self.segments[i].fillcolor(random.choice(colors))
        else:
            for i in range(len(self.segments)):
                self.segments[i].fillcolor(self.color)

        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape("square")
        head.shapesize(1.5,1.5)
        head.penup()
        head.setx(self.x)
        head.sety(self.y)
        (self.segments).append(head)
    
    def move(self, food, enemy_segments=None):
        global pcount
        self.x += self.vx
        self.y += self.vy

        if self.x == food.x and self.y == food.y:
            self.grow()
            food.new_pos(foodbit,self.segments)
        
        if self.segments[0].xcor() < 0 or self.segments[0].xcor() > 600:
            foodbit.hideturtle()
            turtle.penup()
            turtle.goto(300,600)
            turtle.pendown()
            self.gameover = True
            
        if self.segments[0].ycor() < 0 or self.segments[0].ycor() > 600:
            foodbit.hideturtle()
            turtle.penup()
            turtle.goto(300,600)
            turtle.pendown()
            self.gameover = True

        if len(self.segments) > 1 and pcount % 2 == 0:
            for i in range(len(self.segments)-1,0,-1):
                self.segments[i].setx(self.segments[i-1].xcor())
                self.segments[i].sety(self.segments[i-1].ycor())

        (self.segments[0]).setx(self.x)
        (self.segments[0]).sety(self.y)

        if pcount % 2 == 0:
            for i in range(1,len(self.segments)):
                if self.segments[i].xcor() == self.segments[0].xcor() and self.segments[i].ycor() == self.segments[0].ycor():
                    turtle.penup()
                    turtle.goto(300,600)
                    turtle.pendown()
                    self.gameover = True
            if enemy_segments != None:
                for i in range(0,len(enemy_segments)):
                    if enemy_segments[i].xcor() == self.segments[0].xcor() and enemy_segments[i].ycor() == self.segments[0].ycor():
                        foodbit.hideturtle()
                        turtle.penup()
                        turtle.goto(300,600)
                        turtle.pendown()
                        self.gameover = True

    '''
    2: no direction reversal (the following 4 methods)
    '''
    def go_down(self):
        global pcount
        if self.vy != 30:
            if pcount % 2 == 0:
                self.vx = 0
                self.vy = -30
                self.move_logx.append(self.vx)
                self.move_logy.append(self.vy)
    
    def go_up(self):
        global pcount
        if self.vy != -30:
            if pcount % 2 == 0:
                self.vx = 0
                self.vy = 30
                self.move_logx.append(self.vx)
                self.move_logy.append(self.vy)
    
    def go_left(self):
        global pcount
        if self.vx != 30:
            if pcount % 2 == 0:
                self.vx = -30
                self.vy = 0
                self.move_logx.append(self.vx)
                self.move_logy.append(self.vy)

    def go_right(self):
        global pcount
        if self.vx != -30:
            if pcount % 2 == 0:
                self.vx = 30
                self.vy = 0
                self.move_logx.append(self.vx)
                self.move_logy.append(self.vy)

    '''
    7: pause/unpause option
    '''
    def pause(self):
        global pcount
        pcount += 1
        if pcount % 2 != 0:
            self.vx = 0
            self.vy = 0
            turtle.penup()
            turtle.goto(300,600)
            turtle.pendown()
            turtle.write("PAUSED",False, align='center',font=("arial", 40, "normal"))
        else:
            turtle.undo()
            self.vx = self.move_logx[-1]
            self.vy = self.move_logy[-1]

    '''
    3: Allow the user to restart the game by pressing the 'R' key
    '''
    def restart(self):
        if self.gameover:
            self.reset = True
            turtle.undo()
            turtle.undo()
            Menu()

    '''
    7: option to change color of player's snake
    '''
    def change_color(self):
        colors = ["red","yellow","orange","green","pink","black","grey","white"]
        self.color = random.choice(colors)
        for i in range(len(self.segments)):
            self.segments[i].fillcolor(self.color)
          
class Game:
    '''
    Purpose: to start the game of snake

    Instance Variables: self.retry: a boolean declaring if the game being created is created by the snake class' restart method
                        self.speed: the speed of the game
                        self.rival: a boolean declaring if the is or is not an enemy snake to be added to the game
                        self.player a snake object to be controlled by the player
                        self.food: a food object to be (hopefully) collected by the player's snake
                        self.enemy: an enemy snake object to challenge the player

    Methods: __init__: a constructor to intialize self.retry, self.speed, self.rival, self.player, self.food, and self.enemy as well as to set up onkeypress functions
            gameloop: a method that will continuously run the game automatically 
    '''
    def __init__(self,retry,speed,rival):
        self.retry = retry
        self.speed = speed
        self.rival = rival
        if self.retry == False:
            for i in range(4):
                turtle.forward(600)
                turtle.left(90)
                
        self.player = Snake(315, 315, "green")
        self.food = Food(250,250,"red")
        self.enemy = Enemy(255,255,"blue",self.rival)
        foodbit.showturtle()
        self.gameloop()

        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.player.restart,"r")
        turtle.onkeypress(self.player.pause, "p")
        turtle.onkeypress(self.player.change_color, "x")
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if (self.player).gameover == False:
            if self.rival:
                self.enemy.move(self.food)
                self.player.move(self.food,self.enemy.segments)
            else:
                self.player.move(self.food)
            turtle.ontimer(self.gameloop, self.speed)
            turtle.update()
        else:
            global score
            turtle.write(("       Game Over \n          Score: {} \n Press 'r' to try again".format(score-1)), False, align='center',font=("arial", 15, "normal"))
            if self.rival:
                for i in range(len(self.enemy.segments)):
                    self.enemy.segments[i].setx(-1000)
            for i in range(len(self.player.segments)):
                self.player.segments[i].setx(-1000)

            turtle.update()
            score = 0

class Menu2:
    '''
    Purpose: to create a menu object to describe the choice of having an enemy snake or not to the player.

    Instance Variable(s): self.speed: the speed of the game
                          self.menu2: a menu object representing the second menu the player will see

    Methods: __init__: a constructor to initialize self.speed, self.menu2, and to draw the self.menu2 turtle as well as to set up onkeypress functions
            yes: a method that will create a game with an enemy snake
            no: a method that will create a game without an enemy snake
    '''
    def __init__(self,speed):
        self.speed = speed

        self.menu2 = turtle.Turtle()
        self.menu2.penup()
        self.menu2.goto(300,315)
        self.menu2.pendown()
        self.menu2.color("blue")
        self.menu2.write("Do you want an enemy snake?: \n                 1: Yes \n                 2: No", False, align ="center", font=("arial", 28, "normal"))
        self.menu2.penup()
        turtle.onkeypress(self.yes, '1')
        turtle.onkeypress(self.no, '2')
        turtle.listen()
        turtle.mainloop()

    def yes(self):
        self.menu2.clear()
        self.menu2.hideturtle()
        Game(False, self.speed, True)

    def no(self):
        self.menu2.clear()
        self.menu2.hideturtle()
        Game(False, self.speed, False)

class Menu:
    '''
    6: Multiple speeds
    '''

    '''
    Purpose: to create a menu object to welcome the player and to describe the choices of speeds for the game to run at 

    Instance Variable(s): self.menu: a turtle object representing the first menu the player will see

    Methods: __init__: a constructor to initialize self.menu, and to draw the self.menu turtle object as well as to set up onkeypress functions
            slow: a method that will cause the game to update every 300 ms
            medium: a method that will cause the game to update every 200 ms
            fast: a method that will cause the game to update every 100 ms
    '''
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        '''
        4: Optimize the game speed
        '''
        turtle.tracer(0, 0)
        turtle.speed(0)

        self.menu = turtle.Turtle()
        self.menu.penup()
        self.menu.goto(300,315)
        self.menu.pendown()
        self.menu.color("blue")
        self.menu.write("****************SNAKE GAME**************** \n--------------------------------------------------------- \n                       Select a speed: \n                       1: slow \n                       2: medium \n                       3:fast \n \n \n -press 'p' at anytime to pause or unpause- \n -press 'x' at anytime to change your color- \n               -Made with love by LIN-", False, align ="center", font=("arial", 25, "normal"))

        self.menu.penup()
        turtle.onkeypress(self.slow, '1')
        turtle.onkeypress(self.medium, '2')
        turtle.onkeypress(self.fast, '3')
        turtle.listen()
        turtle.mainloop()

    def slow(self):
        self.menu.clear()
        self.menu.hideturtle()
        Menu2(300)

    def medium(self):
        self.menu.clear()
        self.menu.hideturtle()
        Menu2(200)

    def fast(self):
        self.menu.clear()
        self.menu.hideturtle()
        Menu2(100)

Menu()
turtle.done()
