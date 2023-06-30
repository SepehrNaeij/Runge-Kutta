import turtle

def runge_kutta(f, x0, y0, a, b, h, n, xn):
    """
    Implementation of the Runge-Kutta 4th order method.

    Parameters:
    - f: The function f(x, y) defining the differential equation dy/dx = f(x, y)
    - x0: The initial value of x
    - y0: The initial value of y corresponding to x0
    - a: the exponent of x
    - b: the exponent of y
    - h: The step size
    - n: The number of iterations
    - xn: The final result

    Returns:
    - List containing the values of x and y at each iteration
    """
    
    main_n  = int(xn/(y0/n))
    x_values = [x0]
    y_values = [y0]

    for i in range(main_n):
        x = x_values[-1]
        y = y_values[-1]

        k1 = h * f(a, b, x, y)
        k2 = h * f(a, b, x + h/2, y + k1/2)
        k3 = h * f(a, b, x + h/2, y + k2/2)
        k4 = h * f(a, b, x + h, y + k3)

        next_x = x + h
        next_y = y + (k1 + 2*k2 + 2*k3 + k4)/6

        x_values.append(next_x)
        y_values.append(next_y)
    print("k1 = " + str(k1) + "\nk2 = " + str(k2) + "\nk3 = " + str(k3) + "\nk4 = " + str(k4))
    return x_values, y_values


# Example usage:
def f(a ,b ,x, y):
    """
    Example function f(x, y) defining the differential equation dy/dx = f(x, y).
    Modify this function according to your specific problem.
    """
    return x**a + y**b


# getting input

print("The exponent of x:")
a = int(input())  # the exponent of x
print("The exponent of y:")
b = int(input())  # the exponent of y

print("x0:")
x0 = float(input())  # initial value of x
print("y0:")
y0 = float(input())  # initial value of y
print("h:")
h = float(input())  # step size
print("n:")
n = int(input())  # number of iterations
print("xn:")
xn = float(input())  # value of final xn

x_values, y_values = runge_kutta(f, x0, y0, a, b, h, n, xn)

# Print the result
main_n  = int(xn/(y0/n))
i = -1
for x, y in zip(x_values, y_values):
    i+=1
    if ( i == main_n):
        print(f"x = {x:.2f}, y = {y:.5f}")
        main_x = f"{x:.2f}"
        main_y = f"{y:.2f}"
print("Which it means f(" + main_x +") = " + main_y)  
 
# Drawing the 2D diagrams with the elements of x and y     
# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()

# Draw x-axis
t.penup()
t.goto(-400, 0)
t.pendown()
t.forward(750)
t.stamp()

# Draw y-axis
t.penup()
t.goto(0, -300)
t.setheading(90)
t.pendown()
t.forward(550)
t.stamp()

# Label x-axis
t.penup()
t.color("red")
t.goto(370, -20)
t.pendown()
t.write("X", align="center", font=("Arial", 16, "bold"))
t.penup()
t.color("blue")
t.goto(200*float(main_x), -20)
t.pendown()
t.write(main_x, align="center", font=("Arial", 10))

# Label y-axis
t.penup()
t.color("red")
t.goto(-20, 250)
t.pendown()
t.write("Y", align="center", font=("Arial", 16, "bold"))
t.penup()
t.color("blue")
t.goto(-20, 25*float(main_y))
t.pendown()
t.write(main_y, align="center", font=("Arial", 10))

# Connect the x and y value together
t.penup()
t.goto(200*float(main_x), 0)
t.pendown()
#t.left(90)
t.forward(10 + 25*float(main_y))
t.pendown()

t.penup()
t.goto(0, 25*float(main_y) + 10)
t.right(90)
t.pendown()
t.forward(200*float(main_x))
t.pendown()

t.penup()
t.goto(200*float(main_x), 25*float(main_y) + 5)
t.pendown()
t.penup()
t.fillcolor("yellow") 
t.begin_fill() 
t.circle(5,360,5)
t.end_fill() 
t.pendown()


# Hide the turtle
t.hideturtle()

# Exit on click
screen.exitonclick()
     
