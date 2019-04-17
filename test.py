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

def getinter(x1,y1,r1,x2,y2,r2):
	A = 2*(x2 - x1)
	B = 2*(y2 - y1)
	C = x1**2 - x2**2 + y1**2 -y2**2 + r2**2 - r1**2
	if A == 0:
		ya = -C/B
		xa = x1 - m.sqrt(r1**2 - (ya - y1)**2)
	else:
		aa = 0
		bb = 0
		cc = 0
		aa = aa + B**2/(A**2)
		bb = bb + 2*B*C/(A**2)
		cc = cc + C**2/(A**2)
		bb = 2*B*x1/A + bb
		cc = cc + 2*C*x1/A + x1**2
		aa = aa + 1
		bb = bb - 2*y1
		cc = cc + y1**2 - r1**2
		ya = -bb+m.sqrt(bb*bb-4*aa*cc);
		if ya <= 0.0001:
			ya = -bb-m.sqrt(bb*bb-4*aa*cc);
		ya = ya/(2 * aa);
		xa = (-C - B*ya)/A
	# print (xa-x1)**2 + (ya-y1)**2 - r1**2, "error"
	return xa,ya


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
            # print i,rx,ry,rR
            pg.draw.circle(screen, [0,0,0],disptf(rx,ry),rR,1)
            #pg.draw.circle(screen, [10,10,200],disptf(-rx,ry),rR,1)
            font = pg.font.Font('freesansbold.ttf',10)
            txtsf, txtre = text_objects(str(round(200.0/(rR),2)),font)
            txtre.center = disptf(rx-rR,5)
            screen.blit(txtsf,txtre)
            rx,ry,rR = getRxy(1/i)
            pg.draw.circle(screen, [0,0,0],disptf(rx,ry),rR,1)
            #pg.draw.circle(screen, [10,10,200],disptf(-rx,ry),rR,1)
            font = pg.font.Font('freesansbold.ttf',10)
            txtsf, txtre = text_objects(str(round(200.0/(rR),2)),font)
            txtre.center = disptf(rx-rR,5)
            screen.blit(txtsf,txtre)
            i = i+1.0
        i = 1.0
        while(i<10):
            xx,xy,xR = getXxy(1/i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
            #pg.draw.circle(screen, [10,10,200],disptf(-xx,xy),xR,1)
            xx,xy,xR = getXxy(-1/i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
            #pg.draw.circle(screen, [10,10,200],disptf(-xx,xy),abs(xR),1)
            xx,xy,xR = getXxy(i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
            #pg.draw.circle(screen, [10,10,200],disptf(-xx,xy),abs(xR),1)
            xx,xy,xR = getXxy(-i)
            pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
            #pg.draw.circle(screen, [10,10,200],disptf(-xx,xy),abs(xR),1)
            i = i+1.0
        xx,xy,xR = getXxy(0.66)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
        xx,xy,xR = getXxy(-0.66)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
        xx,xy,xR = getXxy(1.5)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),xR,1)
        xx,xy,xR = getXxy(-1.5)
        pg.draw.circle(screen, [0,0,0],disptf(xx,xy),abs(xR),1)
        rx,ry,rR = getRxy(1.0)
        # print rx,ry,rR
        for i in range(1,10):
            xx,xy,xR = getXxy(i * 1.0)
            x1 = rx * 1.0
            y1 = ry * 1.0
            r1 = rR * 1.0
            x2 = xx * 1.0
            y2 = xy * 1.0
            r2 = xR * 1.0
            font = pg.font.Font('freesansbold.ttf',10)
            txtsf, txtre = text_objects(str(round(i,2)),font)
            iX1,iY1 = getinter(x1,y1,r1,x2,y2,r2)            	
            txtre.center = disptf(iX1,iY1)
            screen.blit(txtsf,txtre)
            xx,xy,xR = getXxy(1/(i * 1.0))
            x1 = rx * 1.0
            y1 = ry * 1.0
            r1 = rR * 1.0
            x2 = xx * 1.0
            y2 = xy * 1.0
            r2 = xR * 1.0
            font = pg.font.Font('freesansbold.ttf',10)
            txtsf, txtre = text_objects(str(round(1/(i*1.0),2)),font)
            iX1,iY1 = getinter(x1,y1,r1,x2,y2,r2)            	
            txtre.center = disptf(iX1,iY1)
            screen.blit(txtsf,txtre)
            xx,xy,xR = getXxy(-i * 1.0)
            x1 = rx * 1.0
            y1 = ry * 1.0
            r1 = rR * 1.0
            x2 = xx * 1.0
            y2 = xy * 1.0
            r2 = xR * 1.0
            font = pg.font.Font('freesansbold.ttf',10)
            txtsf, txtre = text_objects(str(round(-i * 1.0,2)),font)
            iX1,iY1 = getinter(x1,y1,r1,x2,y2,r2)            	
            txtre.center = disptf(iX1,iY1)
            screen.blit(txtsf,txtre)
            xx,xy,xR = getXxy(-1/(i * 1.0))
            x1 = rx * 1.0
            y1 = ry * 1.0
            r1 = rR * 1.0
            x2 = xx * 1.0
            y2 = xy * 1.0
            r2 = xR * 1.0
            font = pg.font.Font('freesansbold.ttf',10)
            txtsf, txtre = text_objects(str(round(-1/(i * 1.0),2)),font)
            iX1,iY1 = getinter(x1,y1,r1,x2,y2,r2)            	
            txtre.center = disptf(iX1,iY1)
            screen.blit(txtsf,txtre)
            # print x2,y2,r2,iX1,iY1
            # i = i+1.0
            

        pg.draw.circle(screen, [255,0,0],disptf(X1,Y1),10,0)
        pg.draw.circle(screen, [255,0,0],disptf(X2,Y2),10,0)
        pg.draw.circle(screen, [0,0,255],disptf(-X1,-Y1),10,0)
        pg.draw.circle(screen, [0,0,255],disptf(-X2,-Y2),10,0)
        pg.display.flip()
        clock.tick(60)

def text_objects(text,font):
    txtsurf = font.render(text,True,(255,0,0))
    return txtsurf, txtsurf.get_rect()

if __name__ == '__main__':
    reZl = input('Enter Load impedance real part ')
    imZl = input('Enter Load Impedance Imaginary part ')
    L = input('Enter Inductance per unit meter of lossless transmission line ')
    C = input('Enter Capacitance per unit meter of lossless transmission line ')
    Zo = m.sqrt(L/C)
    reZn = reZl/Zo
    imZn = imZl/Zo
    run_game(reZn,imZn)
