from math import *
import matplotlib.pyplot as plt

eq=input("Enter equation (dy/dx = f(x,y)) : ")

def f(x,y):
    return eval(eq)


def heun(x0,y0,x,h,a1=0.5,a2=0.5,p1=1,q1=1):

    x_values=[x0]
    y_values=[y0]

    while x0<x:

        k1=f(x0,y0)

        k2=f(x0+p1*h, y0+q1*k1*h)

        y0=y0+h*(a1*k1+a2*k2)

        x0=x0+h

        x_values.append(x0)
        y_values.append(y0)

        print("By Heun's method approximate solution at x = ", x0, " is ", y0)

    return x_values,y_values


def midpoint(x0,y0,x,h,a1=0,a2=1,p1=0.5,q1=0.5):

    x_values=[x0]
    y_values=[y0]

    while x0<x:

        k1=f(x0,y0)

        k2=f(x0+p1*h, y0+q1*k1*h)

        y0=y0+h*(a1*k1+a2*k2)

        x0=x0+h

        x_values.append(x0)
        y_values.append(y0)

        print("By Midpoint method approximate solution at x = ", x0, " is ", y0)

    return x_values,y_values


def ralston(x0,y0,x,h,a1=1/3,a2=2/3,p1=3/4,q1=3/4):

    x_values=[x0]
    y_values=[y0]

    while x0<x:

        k1=f(x0,y0)

        k2=f(x0+p1*h, y0+q1*k1*h)

        y0=y0+h*(a1*k1+a2*k2)

        x0=x0+h

        x_values.append(x0)
        y_values.append(y0)

        print("By Ralston method approximate solution at x = ", x0, " is ", y0)

    return x_values,y_values


x0=float(input("Enter x0 : "))
y0=float(input("Enter y0 : "))
x=float(input("Enter x : "))
h=float(input("Enter step size h : "))


print("\nHeun Method:")
x_heun,y_heun=heun(x0,y0,x,h)


print("\nMidpoint Method:")
x_midpoint,y_midpoint=midpoint(x0,y0,x,h)


print("\nRalston Method:")
x_ralston,y_ralston=ralston(x0,y0,x,h)


# Graph

plt.plot(x_heun,y_heun,label="Heun")
plt.plot(x_midpoint,y_midpoint,label="Midpoint")
plt.plot(x_ralston,y_ralston,label="Ralston")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison of Runge-Kutta 2nd Order Methods")

plt.legend()
plt.grid()

plt.show() 
# import matplotlib.pyplot as plt

# h = [30, 60, 120, 240, 480]

# theta = [648.21, 649.91, 651.35, 584.27, -393.87]

# plt.plot(h, theta, marker='D')

# plt.xlabel("Step size, h")
# plt.ylabel("Temperature, θ(480)")
# plt.title("Effect of step size in Heun's method")

# plt.grid()

# plt.show()