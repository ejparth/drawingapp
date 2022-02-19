# drawing app on turtle library
import turtle as tim

# listen method starts the interface to start listening to event keys mode
tim.listen()


def move_ahead():
    tim.forward(10)


def move_back():
    tim.backward(10)


def move_cClock():
    tim.circle(10, 10, 10)


def move_Clock():
    tim.circle(-10, 10, 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Higher level functions "Calling a function from the onkey function

tim.onkey(move_ahead, "w")
tim.onkey(move_back, "s")
tim.onkey(move_cClock, "a")
tim.onkey(move_Clock, "d")

tim.onkey(clear, "c")
screen = tim.Screen()
screen.exitonclick()
