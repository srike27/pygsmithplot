import sys
import pygame as pg
import math as m 

def disptf(x,y):
    yo = 400 - y
    xo = x + 400
    return xo,yo

def getRxy(r):
    x = r/(1+r)
    R = 1/(1+r)
    return int(400*x),0,int(400*R)

def getXxy(x):
    y = 1/x
    return 400,int(400*y),int(400*y)

def run_game(reZn,imZn):
    r = reZn
    x = imZn
    x1 = r/(1+r)
    y1 =0
    r1 = 1/(1+r)
    x2 =1
    y2 =1/x
    r2 =1/x

    R = m.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
    R2 = R*R
    R4 = R2*R2
    a = (r1*r1 - r2*r2) / (2 * R2)
    r2r2 = (r1*r1 - r2*r2)
    c = m.sqrt(2 * (r1*r1 + r2*r2) / R2 - (r2r2 * r2r2) / R4 - 1)

    fx = (x1+x2) / 2 + a * (x2 - x1)
    gx = c * (y2 - y1) / 2
    ix1 = fx + gx
    ix2 = fx - gx

    fy = (y1+y2) / 2 + a * (y2 - y1)
    gy = c * (x1 - x2) / 2
    iy1 = fy + gy
    iy2 = fy - gy

    X1 = int(400*ix1)
    X2 = int(400*ix2)
    Y1 =int(400*iy1)
    Y2 = int(400*iy2)


    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("first screen")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))
        pg.draw.circle(screen, [0,0,0],disptf(0,0),600,200)
        pg.draw.line(screen, (0,0,0),disptf(-400,0), disptf(400,0), 2)
        i = 1.0
        while(i<20):
            rx,ry,rR = getRxy(i)
            pg.draw.circle(screen, [0,0,0],disptf(rx,ry),rR,1)
            rx,ry,rR = getRxy(1/i)
            pg.draw.circle(screen, [0,0,0],disptf(rx,ry),rR,1)
            i = i+1.0
        i = 1.0
        while(i<10):
            xx,xy,xR = getXxy(1/i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
            xx,xy,xR = getXxy(-1/i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
            xx,xy,xR = getXxy(i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
            xx,xy,xR = getXxy(-i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
            i = i+1.0
        xx,xy,xR = getXxy(0.66)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
        xx,xy,xR = getXxy(-0.66)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
        xx,xy,xR = getXxy(1.5)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
        xx,xy,xR = getXxy(-1.5)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
        pg.draw.circle(screen, [255,0,0],disptf(X1,Y1),10,0)
        pg.draw.circle(screen, [255,0,0],disptf(X2,Y2),10,0)
        pg.draw.circle(screen, [0,0,255],disptf(-X1,-Y1),10,0)
        pg.draw.circle(screen, [0,0,255],disptf(-X2,-Y2),10,0)
        pg.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    reZl = input('Load impedance real part')
    imZl = input('Load Impedance Imaginary part')
    L = input('Inductance per unit meter of lossless transmission line')
    C = input('Capacitance per unit meter of lossless transmission line')
    Zo = m.sqrt(L/C)
    reZn = reZl/Zo
    imZn = imZl/Zo
    run_game(reZn,imZn)