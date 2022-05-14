import random
import turtle

# Responsible for give util features
class Get_Utils():
    # get a random number in x axys
    def get_random_x(self):
        return random.randint(-380, 380)
    # get a random number in y axys
    def get_random_y(self):
        return random.randint(300, 400)
        # get a random number to turtle speed
    def get_random_speed(self):
        return random.randint(1, 4)
        # get a font givin the font size
    def get_font(self, font_size):
        return ("Courier", font_size, "normal")

# Responsible to show score on screen    
class Score_Board(Get_Utils):
    def __init__(self):
        self._pen = turtle.Turtle()
    # create score board
    def show_score (self, score):
        self._pen = turtle.Turtle()        
        self._pen.hideturtle()
        self._pen.speed(0)
        self._pen.shape("square")
        self._pen.color("white")
        self._pen.penup()
        self._pen.goto(-200 , 260)
        self._pen.write("Score = {}".format(score), align= "center", font = self.get_font(16))
    # clear score board 
    def dismiss_pen(self):
        self._pen.clear()

# Responsible to manipulate score
class Score_Points:
    # start score
    def __init__(self):
        self.score = 0
    # decrease score 
    def decrease_score(self):
        self.score -= 10
    # increase score
    def increase_score(self):
        self.score += 10
    # give score    
    def get_score(self):
        return self.score

# Responsible to create screen
class Screen():
    # Start screen
    def __init__(self) :
        self.screen = turtle.Screen()
        self.screen.title("Greed")
        self.screen.bgcolor("black")
        self.screen.setup(width= 800, height=600)
        self.screen.tracer(0)
        self.screen.register_shape("bucket.gif")
        self.screen.register_shape("gem.gif")
        self.screen.register_shape("rock.gif")
    # Get screen
    def get_screen(self):
        return self.screen

# Responsible to create player
class Player():
    # Initialize Player
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.speed(0)
        self.player.shape("bucket.gif")
        self.player.color("white")
        self.player.penup()
        self.player.goto(0, -250)
    # Get player
    def get_player(self):
        return self.player

# Responsible to create Rocks
class Rocks(Get_Utils):
    _rocks = []
    # Instance Rocks
    def __init__(self):
        for _ in range(15):
            rock = turtle.Turtle()
            rock.speed(self.get_random_speed())
            rock.shape("rock.gif")
            rock.color("red")
            rock.penup()
            rock.goto(100, 250)
            rock.speed = 0
            self._rocks.append(rock)
    # Get rocks
    def get_rocks(self):
        return self._rocks

class Gems(Get_Utils):
    _gems = []

    # Instance Gems
    def __init__(self):        
        for _ in range(20):
            gem = turtle.Turtle()
            gem.speed(self.get_random_speed())
            gem.shape("gem.gif")
            gem.color("blue")
            gem.penup()
            gem.goto(-100, 250)
            gem.speed = random.randint(1, 4)
            self._gems.append(gem)
    # Get Gems
    def get_gems(self):
        return self._gems

# Responsible to manage the game
class GreenGame(Get_Utils):
    # Initialize the game
    def __init__(self):
        self.screen = Screen().get_screen()
        self.player = Player().get_player()
        self.rocks = Rocks().get_rocks()
        self.gems = Gems().get_gems()
        self.score = Score_Points()
        self.score_board = Score_Board()
        self.score_board.show_score(self.score.get_score())
        self.main_looping()

    # set movement player to left
    def go_left(self):
        self.player.backward(10)
    # set movement player to right
    def go_right(self):
        self.player.forward(10)
    # Set binding keys on game
    def set_binding(self):
        self.screen.listen()
        self.screen.onkeypress(self.go_left, "Left")
        self.screen.onkeypress(self.go_right, "Right")
    # Start the game
    def main_looping(self):
        self.set_binding()
        while True:
            self.screen.update()    
            self.set_rocks_moves()
            self.set_gems_moves()            
            if self.score.get_score() >= 200:
                self.screen.clear()
                self.final_message("You Win!")

        self.screen.get_screen().mainloop()
    # Set movement on rocks
    def set_rocks_moves(self):
        for rock in self.rocks:
            y = rock.ycor()
            y -= 3
            rock.sety(y)

            if y < -300:
                x = self.get_random_x()
                y = self.get_random_y()
                rock.goto(x, y)
            
            if rock.distance(self.player) < 35:        
                x = self.get_random_x()
                y = self.get_random_y()
                rock.goto(x, y)
                self.score.decrease_score()
                self.score_board.dismiss_pen()
                self.score_board.show_score(self.score.get_score())
    
    # Set movement on gems
    def set_gems_moves(self):
        for gem in self.gems:
            y = gem.ycor()
            y -= 3
            gem.sety(y)

            if y < -300:
                x = self.get_random_x()
                y = self.get_random_y()
                gem.goto(x, y)
            
            if gem.distance(self.player) < 35:        
                x = self.get_random_x()
                y = self.get_random_y()
                gem.goto(x, y)
                self.score.increase_score()
                self.score_board.dismiss_pen()
                self.score_board.show_score(self.score.get_score())

    # show final message
    def final_message(self, text):
        message = turtle.Turtle()
        message.hideturtle()
        message.speed(0)
        message.shape("square")
        message.color("black")
        message.penup()
        message.goto(0 , 0)
        message.write("{}".format(text), align= "center", font = self.get_font(42))


def main():
    GreenGame()

main()

