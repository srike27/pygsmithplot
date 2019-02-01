import sys
import pygame as pg
import math as m 
import matplotlib.pyplot as plt

def run_game(Zo):
    l= [[],[]]
    for i in range(100):
        a =[0.01*i],[Zo*m.tan(2*3.14*0.01*i)]
        l.append(a)
    plt.plot(l[0],l[1])
    plt.show()

if __name__ == '__main__':
    L = input('Inductance per unit meter of lossless transmission line')
    C = input('Capacitance per unit meter of lossless transmission line')
    Zo = m.sqrt(L/C)
    run_game(Zo)