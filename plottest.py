import sys
import pygame as pg
import math as m 
import matplotlib.pyplot as plt

def run_game(Zo):
    l= []
    r = []
    for i in range(26):
        l.append(i*0.01)
    for i in range(26):
        r.append(Zo*m.tan(2*3.14*i*0.01))
    #for i in range(100):
    #    a =[i,i]
    #    l.append(a)
    plt.plot(l,r)
    plt.show()

if __name__ == '__main__':
    Zo =1
    run_game(Zo)