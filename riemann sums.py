import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.axisartist.axislines import SubplotZero
from sympy.utilities.lambdify import lambdify
import PySimpleGUI as sg


class Riemman():
    @staticmethod
    def calulitos(a_o,b_o,n_o,function):
        s_x = symbols("x")
        print("funcion a usar ---> ",function)

        np.seterr(divide='ignore', invalid='ignore')

        f = lambda x: lambdify(s_x,sympify(function),'numpy')(x)

        a = a_o
        b = b_o
        N = n_o
        n = n_o  # Use n*N+1 points to plot the function smoothly

        xe = np.linspace(a, b, N + 1)
        y = f(xe)
        X = np.linspace(a, b, n * N + 1)
        Y = f(X)
        fig = plt.figure()
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)

        for direction in ["xzero","yzero"]:
            ax.axis[direction].set_axisline_style("-|>")
            ax.axis[direction].set_visible(True)

        for direction in ["left","right","bottom","top"]:
            ax.axis[direction].set_visible(False)

        plt.subplot(1, 3, 2)
        plt.plot(X, Y, color="red")
        x_mid = (xe[:-1] + xe[1:]) / 2  # Midpoints
        y_mid = f(x_mid)
        plt.plot(x_mid,y_mid, color="red")
        plt.bar(x_mid, y_mid, width=(b - a) / N, edgecolor='b')
        plt.title('Midpoint Riemann Sum, N = {}'.format(N))

        plt.savefig('foo.png',dpi=500)
        vistas.resultado("foo.png")


class long_arc():
    @staticmethod
    def cancer_anal():
        print("asdasd")

class vistas():

    @staticmethod
    def principal():
        sg.ChangeLookAndFeel('GreenTan')
        layout = [
            [sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('formula', size=(15, 1)), sg.InputText()],
            [sg.Text('a', size=(15, 1)), sg.InputText()],
            [sg.Text('b', size=(15, 1)), sg.InputText()],
            [sg.Text('resolucion', size=(15, 1)), sg.InputText()],
            [sg.Submit("calcular")]
        ]

        window = sg.Window('Simple data entry window').Layout(layout)
        button, values = window.Read()
        window.close()
        return(values)

    @staticmethod
    def resultado(name_file):
        from PIL import Image
        rimman = Image.open(name_file)
        rimman.show()


if __name__ == '__main__':
    values = vistas.principal()
    rango_1 = float(values[1])
    rango_2 = float(values[2])
    resolution = int(values[3])
    function = values[0]

    Riemman.calulitos(rango_1,rango_2,resolution,function)
