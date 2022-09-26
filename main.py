from turtle import *
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

# Declarando el objeto "pantalla"
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Declarando los objetos visibles en el juego (puntuacion, raquetas, pelota)
sleep_time = 0.1
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Creando el movimiento de los objetos con las teclas
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Mientras el juego esté activo
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Rebotar de la parte superior e inferior
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectar la colision con la raqueta derecha
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Puntos para cada lado
    if ball.xcor() > 390:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
