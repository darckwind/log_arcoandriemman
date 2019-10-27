import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
from sympy import *



class main :

    @staticmethod
    def nice():
        x, y, z = symbols('x y z')
        init_printing(use_unicode=True)
        rango_1 = float(input("rango 1: "))
        rango_2 = float(input("rango 2: "))
        resolution = int(input("resolucion: "))
        print("formula")
        function = input()

        results=[]
        value_x = []
        value_y = []
        cosa = ((rango_2 - rango_1) / resolution)


        for x_n in np.arange(rango_1,rango_2, cosa):
            cosa2 = (rango_1 + (((rango_2 - rango_1) / 2 * resolution) * (2*x_n - 1)))
            value_y.append(cosa * sympify(function).evalf(subs={x: cosa2}))
            #value_y.append(sympify("x**2").evalf(subs={x: x_n}))

        for y_n in np.arange(rango_1,rango_2, cosa):
            value_x.append(y_n)

        print(value_x,value_y)

        fig = plt.figure()
        ax = SubplotZero(fig,111)
        fig.add_subplot(ax)

        for direction in ["xzero","yzero"]:
            ax.axis[direction].set_axisline_style("-|>")
            ax.axis[direction].set_visible(True)

        for direction in ["left","right","bottom","top"]:
            ax.axis[direction].set_visible(False)

        ax.y(value_x, value_y)
        plt.savefig('foo.svg')


if __name__ == '__main__':
    main.nice()