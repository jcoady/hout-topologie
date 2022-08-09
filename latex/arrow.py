#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:39:28 2022

@author: windhoos
"""

from vpython import vector,cylinder,cone, compound, quad, vertex, text
import numpy as np
from math import sqrt,pi
from latex import config as cfg

def build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case):
    a=direction(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return a

def origin(O):
    xp = cylinder(pos=O, axis=vector(1,0,0), radius=10, color=vector(1,0,0), length=50)
    Ox=O+vector(50,0,0)
    xc = cone(pos=Ox, axis=vector(1,0,0),radius=20, color=vector(1,0,0), length = 20)
    xt = text(text='x', pos = xc.pos + xc.axis +vector(10,0,0),align='center', color=vector(1,0,0), axis=vector(1,0,0), height = 20)
    #xas = compound([xp, xc, xt])
    #xas.axis = vector(1,0,0)
    
    yp = cylinder(pos=O, axis=vector(0,1,0), radius=10, color=vector(0,1,0), length=50)
    Oy=O+vector(0,50,0)
    yc = cone(pos=Oy, axis=vector(0,1,0),radius=20, color=vector(0,1,0), length = 20)
    yt = text(text='y', pos = yc.pos + yc.axis +vector(0,10,0),align='center', color=vector(0,1,0),axis=vector(0,1,0),  height = 20)
    #yas = compound([yp, yc, yt])
    #yas.axis = vector(0,1,0)
    
    zp = cylinder(pos=O, axis=vector(0,0,1), radius=10, color=vector(0,0,1), length=50)
    Oz=O+vector(0,0,50)
    zc = cone(pos=Oz, axis=vector(0,0,1),radius=20, color=vector(0,0,1), length = 20)
    zt = text(text='z', pos = zc.pos + zc.axis +vector(0,0,10),align='center', axis=vector(0,0,1), color=vector(0,0,1), height = 20)
    #zas = compound([zp, zc, zt])
    #zas.axis = vector(0,0,1)

def direction(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case):
    if case == 1:#(z0 == z1 and z0==z2 and y1 == y2 and x0 == x1 and y0 < y1):
        vrichting = vector(1,0,0)
        a=arrow1(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case==21:#(z0 == z1 and z0==z2 and y1 == y2 and x0 == x1 and y0 > y1):
        vrichting = vector(-1,0,0)
        a=arrow21(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 22:#(y0 == y1 and y0==y2 and z1 == z2 and x0 == x1 and z0 > z1):
        vrichting = vector(-1,0,0)
        a=arrow22(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 3: #(y0 == y1 and y0==y2 and z1 == z2 and x0 == x1 and z0 < z1):
        vrichting = vector(0,0,1)
        a=arrow3(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 5: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(0,0,1)
        a=arrow5(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 6: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(0,0,1)
        a=arrow6(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 8: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(0,0,1)
        a=arrow8(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 9: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(0,0,-1)
        a=arrow9(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 10: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(-1,0,0)
        a=arrow10(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 111: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(1,0,0)
        a=arrow111(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case == 112: #(z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        vrichting = vector(0,0,-1)
        a=arrow112(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    
def arrow1(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    '''
    if x0 != x1:
        x_old=cfg.step1_camera[0]
        y_old=cfg.step1_camera[1]
        z_old=cfg.step1_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step1_camera[0]=x_new
        cfg.step1_camera[1]=y_new
        cfg.step1_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step1_camera[0]
        y_old=cfg.step1_camera[1]
        z_old=cfg.step1_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step1_camera[0]=x_new
        cfg.step1_camera[1]=y_new
        cfg.step1_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step1_camera[0]
        y_old=cfg.step1_camera[1]
        z_old=cfg.step1_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step1_camera[0]=x_new
        cfg.step1_camera[1]=y_new
        cfg.step1_camera[2]=z_new
    '''
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=-1*head_length*uv[0]
    y1e=-1*head_length*uv[1]
    z1e=-1*head_length*uv[2]
    
    x2e=1*head_length*uv[0]
    y2e=1*head_length*uv[1]
    z2e=1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x1e,y1e,z1e), radius=head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2-x2e,y2-y2e,z2-z2e), axis=vector(x2e,y2e,z2e), radius=head_thickness, color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue), radius = body_thickness )

    t=text(text=f'{dtot} cm', pos= body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0) ,axis = vrichting, align='center', height=3*thickness, color=vector(red,green,blue))
    t.rotate(angle=pi, axis=vector(0,1,0),origin=body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y0,z0+thickness), color=vector(red,green,blue))
    va2=vertex(pos=vector(x2,y0,z0-thickness), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2,y2+thickness*2,z2-thickness), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2,y2+thickness*2,z2+thickness), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x1,y0,z0+thickness), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x1,y0,z0-thickness), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1,y1+thickness*2,z1-thickness), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1,y1+thickness*2,z1+thickness), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])
    
    cfg.step1_ycam.append(body.pos.y)
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    return arrow
    
def arrow21(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    '''
    if x0 != x1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    '''
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=-1*head_length*uv[0]
    y1e=-1*head_length*uv[1]
    z1e=-1*head_length*uv[2]
    
    x2e=1*head_length*uv[0]
    y2e=1*head_length*uv[1]
    z2e=1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x1e,y1e,z1e), radius=head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2-x2e,y2-y2e,z2-z2e), axis=vector(x2e,y2e,z2e), radius=head_thickness, color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue), radius = body_thickness )

    t=text(text=f'{dtot} cm', pos= body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0) ,axis=vrichting,align='center', height=3*thickness, color=vector(red,green,blue))
    t.rotate(angle=pi, axis=vector(0,1,0),origin=body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y0,z0+thickness), color=vector(red,green,blue))
    va2=vertex(pos=vector(x2,y0,z0-thickness), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2,y2+thickness*2,z2-thickness), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2,y2+thickness*2,z2+thickness), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x1,y0,z0+thickness), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x1,y0,z0-thickness), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1,y1+thickness*2,z1-thickness), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1,y1+thickness*2,z1+thickness), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])
    
    cfg.step2_ycam.append(body.pos.y)
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    return arrow

def arrow22(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    '''
    if x0 != x1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    '''
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1,y1+2*head_thickness,z1), axis=vector(x1e,y1e,z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2-2*head_thickness,z2), axis=vector(x2e,y2e,z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    #body=cylinder(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue), radius = body_thickness )

    t=text(text=f'{dtot} cm', pos= head.pos+vector(0,thickness*(1+2/3),0) ,axis=vrichting,align='center', height=3*thickness, color=vector(red,green,blue))
    t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y2,z0+thickness), color=vector(red,green,blue))
    va2=vertex(pos=vector(x2,y2,z0-thickness), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2+thickness*2,y2,z2-thickness), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2+thickness*2,y2,z2+thickness), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x1,y0,z0+thickness), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x1,y0,z0-thickness), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1+thickness*2,y1,z1-thickness), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1+thickness*2,y1,z1+thickness), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, tail,slaba,slabb,t])
    
    cfg.step2_xcam.append(head.pos.x)
    
    return arrow

def arrow3(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    '''
    if x0 != x1:
        x_old=cfg.step3_camera[0]
        y_old=cfg.step3_camera[1]
        z_old=cfg.step3_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step3_camera[0]=x_new
        cfg.step3_camera[1]=y_new
        cfg.step3_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step3_camera[0]
        y_old=cfg.step3_camera[1]
        z_old=cfg.step3_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step3_camera[0]=x_new
        cfg.step3_camera[1]=y_new
        cfg.step3_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step3_camera[0]
        y_old=cfg.step3_camera[1]
        z_old=cfg.step3_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step3_camera[0]=x_new
        cfg.step3_camera[1]=y_new
        cfg.step3_camera[2]=z_new
    '''
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,z1-2*head_thickness), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    t=text(text=f'{dtot} cm', pos=head.pos+head.axis*0.2+vector(0,thickness*(2.5),0) ,axis = vrichting, align='left', height=3*thickness, color=vector(red,green,blue))
    t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2+thickness,y0,z2), color=vector(red,green,blue))
    va2=vertex(pos=vector(x2-thickness,y0,z2), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2-thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2+thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x1+thickness,y0,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x1-thickness,y0,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1-thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1+thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step3_ycam.append(body.pos.y)
    
    return arrow

def arrow5(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    '''
    if x0 != x1:
        x_old=cfg.step3_camera[0]
        y_old=cfg.step3_camera[1]
        z_old=cfg.step3_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step3_camera[0]=x_new
        cfg.step3_camera[1]=y_new
        cfg.step3_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step3_camera[0]
        y_old=cfg.step3_camera[1]
        z_old=cfg.step3_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step3_camera[0]=x_new
        cfg.step3_camera[1]=y_new
        cfg.step3_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step3_camera[0]
        y_old=cfg.step3_camera[1]
        z_old=cfg.step3_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step3_camera[0]=x_new
        cfg.step3_camera[1]=y_new
        cfg.step3_camera[2]=z_new
    '''
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    #head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    #tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,tail.pos.z+2*head_length), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    #t_invisible=text(text=f'{dtot} cm', pos=body.pos+vector(-body.pos.x*2,0,-body.pos.z/2) ,axis = vrichting, up=vector(1,0,0), align='center', height=3*thickness, color=vector(1,1,1))
    t=text(text=f'{dtot} cm', pos=body.pos+vector(thickness*2.5,0,0) ,axis = vrichting, up=vector(1,0,0), align='center', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x0-thickness,y0+thickness*2,z2), color=vector(red,green,blue))
    va2=vertex(pos=vector(x0-thickness,y0-thickness*2,z2), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2+thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2+thickness,y2+thickness*2,z2), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0-thickness,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0-thickness,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1+thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1+thickness,y1+thickness*2,z1), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step5_xcam.append(body.pos.x)

    
    return arrow

def arrow6(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''

    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    #head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    #tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,tail.pos.z+2*head_length), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    #t_invisible=text(text=f'{dtot} cm', pos=body.pos+vector(-body.pos.x*2,0,-body.pos.z/2) ,axis = vrichting, up=vector(1,0,0), align='center', height=3*thickness, color=vector(1,1,1))
    t=text(text=f'{dtot} cm', pos=body.pos+vector(thickness*2.5,0,0) ,axis = vrichting, up=vector(1,0,0), align='center', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x0-thickness,y0+thickness*2,z2), color=vector(red,green,blue))
    va2=vertex(pos=vector(x0-thickness,y0-thickness*2,z2), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2+thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2+thickness,y2+thickness*2,z2), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0-thickness,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0-thickness,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1+thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1+thickness,y1+thickness*2,z1), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step6_xcam.append(body.pos.x)
    
    return arrow

def arrow8(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''

    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    #head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    #tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,head.pos.z), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    #t_invisible=text(text=f'{dtot} cm', pos=body.pos+vector(-body.pos.x*2,0,-body.pos.z/2) ,axis = vrichting, up=vector(1,0,0), align='center', height=3*thickness, color=vector(1,1,1))
    t=text(text=f'{dtot} cm', pos=body.pos+vector(thickness*2.5,0,-body.length) ,axis = vrichting, up=vector(1,0,0), align='left', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x0-thickness,y0+thickness*2,z2), color=vector(red,green,blue))
    va2=vertex(pos=vector(x0-thickness,y0-thickness*2,z2), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2+thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2+thickness,y2+thickness*2,z2), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0-thickness,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0-thickness,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1+thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1+thickness,y1+thickness*2,z1), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step8_xcam.append(body.pos.x)
    
    return arrow

def arrow9(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''

    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    #head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    #tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    head=cone(pos=vector(x1,y1,z1-2*head_thickness), axis=vector(x1e,y1e,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2,z2+2*head_thickness), axis=vector(x2e,y2e,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,head.pos.z), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    #t_invisible=text(text=f'{dtot} cm', pos=body.pos+vector(-body.pos.x*2,0,-body.pos.z/2) ,axis = vrichting, up=vector(1,0,0), align='center', height=3*thickness, color=vector(1,1,1))
    t=text(text=f'{dtot} cm', pos=body.pos+vector(thickness*2.5,0,-body.length) ,axis = vrichting, up=vector(1,0,0), align='right', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x0-thickness,y0+thickness*2,z2), color=vector(red,green,blue))
    va2=vertex(pos=vector(x0-thickness,y0-thickness*2,z2), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2+thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2+thickness,y2+thickness*2,z2), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0-thickness,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0-thickness,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1+thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1+thickness,y1+thickness*2,z1), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step9_xcam.append(body.pos.x)
    
    return arrow

def arrow10(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''

    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1-2*head_thickness,y1,z1), axis=vector(-x1e,y1e,z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2+2*head_thickness,y2,z2), axis=vector(-x2e,y2e,z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(head.pos.x,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=head.pos.x-tail.pos.x , radius = body_thickness )
    #body=cylinder(pos=vector(head.pos.x,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    t=text(text=f'{dtot} cm', pos=body.pos+vector(0,0,thickness*2.5) , axis = vrichting, up=vector(0,0,1), align='left', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y0+thickness*2,z0), color=vector(red,green,blue))
    va2=vertex(pos=vector(x2,y0-thickness*2,z0), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2,y2-thickness*2,z2-thickness), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2,y2+thickness*2,z2-thickness), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1,y1-thickness*2,z1-thickness), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1,y1+thickness*2,z1-thickness), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step10_zcam.append(body.pos.x)
    
    return arrow



def arrow111(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z   || 2   
            |    ||
            |    || 1
            |____//___x
            /   //    
           /   //
          / y //0
    '''

    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1-2*head_thickness,y1,z1), axis=vector(x1e,y1e,z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2+2*head_thickness,y2,z2), axis=vector(x2e,y2e,z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(head.pos.x,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=head.pos.x-tail.pos.x , radius = body_thickness )
    #body=cylinder(pos=vector(head.pos.x,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    t=text(text=f'{dtot} cm', pos=body.pos+vector(0,0,thickness*2.5) , axis = vrichting, up=vector(0,0,1), align='right', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=head.pos+0.5*head.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y0+thickness*2,z0), color=vector(red,green,blue))
    va2=vertex(pos=vector(x2,y0-thickness*2,z0), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2,y2-thickness*2,z2+thickness), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2,y2+thickness*2,z2+thickness), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1,y1-thickness*2,z1+thickness), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1,y1+thickness*2,z1+thickness), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step11_zcam.append(body.pos.z)
    
    return arrow

def arrow112(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):

    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    x2e=-1*head_length*uv[0]
    y2e=-1*head_length*uv[1]
    z2e=-1*head_length*uv[2]
    
    red,green,blue = 0.75,0.1,0.1
    
    head=cone(pos=vector(x1,y1,z1+2*head_thickness), axis=vector(0,0,-z1e), radius=head_thickness,length=2*head_thickness, color=vector(red,green,blue))
    tail=cone(pos=vector(x2,y2,z2-2*head_thickness), axis=vector(0,0,-z2e), radius=head_thickness,length=2*head_thickness,color=vector(red,green,blue))
    body=cylinder(pos=vector(tail.pos.x,tail.pos.y,tail.pos.z), axis=vector(0,0,z2-z1-z2e+z1e), color=vector(red,green,blue),length=head.pos.z-tail.pos.z , radius = body_thickness )
    #body=cylinder(pos=vector(head.pos.x,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,green,blue),length=z1-z2-2*head_length , radius = body_thickness )
    t=text(text=f'{dtot} cm', pos=head.pos+vector(-thickness*2.5,0,0) , axis = -vrichting, up=vector(-1,0,0), align='left', height=3*thickness, color=vector(red,green,blue))
    #t.rotate(angle=pi, axis=vector(0,1,0),origin=tail.pos+0.5*tail.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x0+thickness,y0+thickness*2,z2), color=vector(red,green,blue))
    va2=vertex(pos=vector(x0+thickness,y0-thickness*2,z2), color=vector(red,green,blue))
    va3=vertex(pos=vector(x2-thickness,y2-thickness*2,z2), color=vector(red,green,blue))
    va4=vertex(pos=vector(x2-thickness,y2+thickness*2,z2), color=vector(red,green,blue))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x0+thickness,y0+thickness*2,z0), color=vector(red,green,blue))
    vb2=vertex(pos=vector(x0+thickness,y0-thickness*2,z0), color=vector(red,green,blue))
    vb3=vertex(pos=vector(x1-thickness,y1-thickness*2,z1), color=vector(red,green,blue))
    vb4=vertex(pos=vector(x1-thickness,y1+thickness*2,z1), color=vector(red,green,blue))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    
    cfg.step11_xcam.append(body.pos.x)
    
    return arrow

def pointer(x0,y0,z0,x1,y1,z1):
    #print('pointer')
    #print(x0,y0,z0,x1,y1,z1)
    
    '''
    0    1
    <-----
    
    '''
    
    dx=x1-x0
    dy=y1-y0
    dz=z1-z0
    
    dtot=sqrt(dx**2+dy**2+dz**2)
    
    r_cone=dtot/7.5
    
    green=0.75
    
    head=cone(length=abs(dtot)*1/3 ,     radius=r_cone*2, color=vector(0,green,0), pos=vector(abs(dtot)*2/3,0,0), axis=vector(1,0,0))
    body=cylinder(length=abs(dtot)*2/3 , radius=r_cone  , color=vector(0,green,0), pos=vector(0,0,0),             axis=vector(1,0,0))
    arrow=compound([head,body])
    arrow.pos=vector(x0,y0,z0)+vector(dx/2,dy/2,dz/2)
    arrow.axis=vector(dx,dy,dz)
    
    return arrow