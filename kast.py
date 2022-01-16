#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:38:23 2021

@author: windhoos
"""
from math import degrees,radians,sin,cos,tan,floor
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.axes as a
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection#, Line3DCollection

#from matplotlib.collections import LineCollection
#from matplotlib.colors import ListedColormap, BoundaryNorm

def input_data():
    global breedte_kast,hoogte_kast,diepte_kast,breedte_plank,lengte_plank,dikte_plank,niveaus,tussenschot,plankhoogte,hoogte_voet
    indeling_correct = False
    while indeling_correct == False:
        breedte_kast=230 #float(input('Wat is de breedte van de kast in cm? '))
        voetjes=str('JA') #str(input('heeft de kast pootjes? [y/n] '))
        if voetjes == ('ja' or 'JA') or ('Ja' or 'YES') or ('yes' or 'Yes') or ('j' or 'y'):
            hoogte_voet = 10 #float(input('Hoe hoog zijn de pootjes in cm? '))
        else:
            hoogte_voet = 0.
        hoogte_kast=250 #float(input('Wat is de hoogte van de kast in cm? '))
        hoogte_kast=hoogte_kast-hoogte_voet
        diepte_kast=50 #float(input('Wat is de diepte van de kast in cm? '))
        breedte_plank=20 #float(input('Wat is de breedte van de plank in cm? '))
        lengte_plank=450 #float(input('Wat is de lengte van de plank in cm? '))
        dikte_plank=3.2 #float(input('Wat is de dikte van de plank in cm? '))
        niveaus=1 #int(input('Hoeveel niveaus wil je ? '))
        tussenschot = 1 #int(input('Hoeveel tussenschotten wil je ? '))
        if hoogte_kast > lengte_plank:
            print('De kast is hoger dan de hoogte van de plank dat is niet mogelijk!')
            print('Voer de waarden opnieuw in.')
        if breedte_kast > lengte_plank:
            print('De kast is breder dan de hoogte van de plank dat is niet mogelijk!')
            print('Voer de waarden opnieuw in.')
        else:
            indeling_correct = True
    plankhoogte=[]
    htot=0
    indeling_correct = False
    while indeling_correct == False:
        for niveau in range(niveaus):
            #print('Er zijn %d niveaus ' % (niveaus))
            if niveau == 0:
                afstand=30# int(input('Wat is de afstand van bodem tot plank %d in cm? ' % (niveau+1)))
                plankhoogte.append(afstand+dikte_plank)
                htot=htot+plankhoogte[niveau]
                print('Er is nu afstand %.1f cm van onder en nog %.1f cm vrije ruimte er boven' % (htot, hoogte_kast-htot-dikte_plank))
            else:
                afstand=30 #float(input('Wat is de afstand tussen plank %d en plank %d in cm? ' % (niveau,niveau+1)))
                if afstand != 0:  
                    plankhoogte.append(afstand+dikte_plank)
                    htot=htot+plankhoogte[niveau]
                print('Er is nu afstand %.1f cm van onder en nog %.1f cm vrije ruimte tot boven' % (htot, hoogte_kast-htot-dikte_plank))
        print('Het volgende is nu bekend van de indeling van de kast')
        print('Er zijn %d niveaus in de kast' % (niveaus+1))
        for niveau in range(niveaus):
            if niveau == 0:
                print('De afstand tot de grond tot de bovenkant van plank 1 is: %.1f cm' % (plankhoogte[niveau]))
            else:
                print('De afstand van plank %s tot plank %s is %.1f cm' % (niveau,niveau+1,plankhoogte[niveau]))
                if niveau == niveaus-1:
                    print('De afstand van de bovenkant van de bovenste plank tot de onderkant van de bovenplank van de kast is %.1f cm' % (hoogte_kast-dikte_plank-htot))
        check='ja' #raw_input('Ben je tevreden met deze waarden ? [Ja/Nee] ')
        if check == ('ja' or 'JA') or ('Ja' or 'YES') or ('yes' or 'Yes') or ('j' or 'y'):
            indeling_correct = True
        print('')
            
class plank:
    def __init__(self,lengte,breedte,dikte):
        self.breedte=breedte
        self.lengte=lengte
        self.dikte=dikte
        self.aantal=0.
    
        self.matrix_base=0.
        self.vlakken_base=0.
        self.amax=0.
        
        self.matrix3=0.
        self.matrix4=0.
        
        self.matrix_nieuw=0.
        self.vlakken_nieuw=0.
    
        breedte=self.breedte
        lengte=self.lengte
        dikte=self.dikte
        
        
        '''
               z|_x
                \y
         
          ____________
         3\           \2
         4\___________\1
          |___________|
         7\           \6
         8\___________\5
        '''
        
        #p0=[0.,0.,0.] #xyz
        #p1=[ lengte/2., dikte/2., breedte/2.]
        #p2=[ lengte/2.,-dikte/2., breedte/2.]
        #p3=[-lengte/2.,-dikte/2., breedte/2.]
        #p4=[-lengte/2., dikte/2., breedte/2.]
        #5=[ lengte/2., dikte/2.,-breedte/2.]
        #p6=[ lengte/2.,-dikte/2.,-breedte/2.]
        #p7=[-lengte/2.,-dikte/2.,-breedte/2.]
        #8=[-lengte/2., dikte/2.,-breedte/2.]
        
        p1=[ lengte/2., breedte/2., dikte/2.]
        p2=[ lengte/2.,-breedte/2., dikte/2.]
        p3=[-lengte/2.,-breedte/2., dikte/2.]
        p4=[-lengte/2., breedte/2., dikte/2.]
        p5=[ lengte/2., breedte/2.,-dikte/2.]
        p6=[ lengte/2.,-breedte/2.,-dikte/2.]
        p7=[-lengte/2.,-breedte/2.,-dikte/2.]
        p8=[-lengte/2., breedte/2.,-dikte/2.]
        
        self.matrix_base = np.matrix([p1,p2,p3,p4,p5,p6,p7,p8])
        self.matrix_nieuw = self.matrix_base
        self.amax=np.amax(self.matrix_base)
        
        v1=[p1,p2,p3,p4]
        v2=[p5,p6,p7,p8]
        v3=[p1,p2,p6,p5]
        v4=[p2,p3,p7,p6]
        v5=[p4,p3,p7,p8]
        v6=[p1,p4,p8,p5]
        
        self.vlakken_base = np.array([v1,v2,v3,v4,v5,v6])
        self.vlakken_nieuw = self.vlakken_base
        
        self.matrix3=self.matrix_nieuw
        self.vorm4_matrix()
        
    def plank_zagen(self, lengte, breedte, dikte):
        if breedte > self.breedte:
            print('test1')
            exit()
        if lengte > self.lengte:
            exit()
            print('test2')
        if dikte > self.dikte:
            exit()
            print('test3')
        #p0=[0.,0.,0.] #xyz
        p1=[ lengte/2., breedte/2., dikte/2.]
        p2=[ lengte/2.,-breedte/2., dikte/2.]
        p3=[-lengte/2.,-breedte/2., dikte/2.]
        p4=[-lengte/2., breedte/2., dikte/2.]
        p5=[ lengte/2., breedte/2.,-dikte/2.]
        p6=[ lengte/2.,-breedte/2.,-dikte/2.]
        p7=[-lengte/2.,-breedte/2.,-dikte/2.]
        p8=[-lengte/2., breedte/2.,-dikte/2.]
        
        self.breedte=breedte
        self.lengte=lengte
        self.dikte=dikte
        
        self.matrix_nieuw = np.matrix([p1,p2,p3,p4,p5,p6,p7,p8])
        self.amax=np.amax(self.matrix_nieuw)
        self.vlakken_maken(self.matrix_nieuw)
        self.matrix3 = self.matrix_nieuw
    
    '''
    def plank_vlakken(self):
        a=1
        b=2
        c=6
        d=5
        a=a-1
        b=b-1
        c=c-1
        d=d-1
        p1=self.matrix_nieuw[a]
        p2=self.matrix_nieuw[b]
        p3=self.matrix_nieuw[c]
        p4=self.matrix_nieuw[d]
        angle=45
        p1,p2,p3,p4=self.hoeken_zagen(p1, p2, p3, p4, angle)
        self.matrix_nieuw[a]=p1
        self.matrix_nieuw[b]=p2
        self.matrix_nieuw[c]=p3
        self.matrix_nieuw[d]=p4
    
    def hoeken_zagen(self, p1, p2, p3, p4, angle):
        angle=radians(angle)
        
        # p2-----p1
        # |      |
        # |      |
        # p3-----p4
        
        

        p1=p1.tolist() #hoofd node
        p2=p2.tolist() #hoofd node
        p3=p3.tolist()
        p4=p4.tolist()
        
        dx=abs(p1[0][0]-p2[0][0])
        dy=abs(p1[0][1]-p2[0][1])
        dz=abs(p1[0][2]-p2[0][2])
        
        #print(dx,dy,dz)
        
        #breedte = (dx**2 + dy**2 + dz**2)**(1/2.)
        
        dx=abs(p2[0][0]-p3[0][0])
        dy=abs(p2[0][1]-p3[0][1])
        dz=abs(p2[0][2]-p3[0][2])
        
        
        hoogte = (dx**2 + dy**2 + dz**2)**(1/2.)
        
        if dx != 0:
            p3n=[p3[0][0],p3[0][1]-hoogte*tan(angle),p3[0][2]]
            p4n=[p4[0][0],p4[0][1]-hoogte*tan(angle),p4[0][2]]
        if dy != 0:
            p3n=[p3[0][0],p3[0][1],p3[0][2]-hoogte*tan(angle)]
            p4n=[p4[0][0],p4[0][1],p4[0][2]-hoogte*tan(angle)]
        if dz != 0:
            p3n=[p3[0][0]-hoogte*tan(angle),p3[0][1],p3[0][2]]
            p4n=[p4[0][0]-hoogte*tan(angle),p4[0][1],p4[0][2]]
       
        return np.matrix(p1),np.matrix(p2),np.matrix(p3n),np.matrix(p4n)
    '''            
        
    def vlakken_maken(self,matrix):
        matrix=np.array(matrix)
        p=[]
        for i in range(len(matrix)):
            p.append(matrix[i])
        
        v1=[p[0],p[1],p[2],p[3]]
        v2=[p[4],p[5],p[6],p[7]]
        v3=[p[0],p[1],p[5],p[4]]
        v4=[p[1],p[2],p[6],p[5]]
        v5=[p[3],p[2],p[6],p[7]]
        v6=[p[0],p[3],p[7],p[4]]
        
        self.vlakken_nieuw = np.array([v1,v2,v3,v4,v5,v6])
        
    def plot(self,punten,vlakken):
        #points=self.punten_base
        #edges=self.vlakken_base
        fig = plt.figure(dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
        faces.set_facecolor((0.45,0.1,0,1))

        ax.add_collection3d(faces)
    
        #cmap = plt.cm.hsv
        #norm = plt.Normalize(vmin=1, vmax=8)
        #z = np.array([1,2,3,4,5,6,7,8])

        #ax.scatter(punten[:,0], punten[:,1], punten[:,2], alpha=1 ,c = cmap(norm(z)) , marker='o')
        #ax.scatter(punten[:,0], punten[:,1], punten[:,2], alpha=1 ,c = 'black' , marker='o')
            
        plt.title('Balk')
        ax.autoscale(False)
        #ax.set_aspect('auto')
        ax.view_init(45, 45)
        ax.set_xlabel('x-as (lengte) %s cm' % self.lengte)
        ax.set_ylabel('y-as (breedte) %s cm' % self.breedte)
        ax.set_zlabel('z-as (dikte) %s cm' % self.dikte)
        ax.set_xlim(-self.amax*1.1, self.amax*1.1)
        ax.set_ylim(-self.amax*1.1, self.amax*1.1)
        ax.set_zlim(-self.amax*1.1, self.amax*1.1)
        plt.tight_layout()
        plt.show()
        plt.clf()
        
    def vorm4_matrix(self):
        self.matrix4=np.insert(self.matrix3, 3, 1, axis=1)
        #return matrix4
        
    def vorm3_matrix(self):
        self.matrix3 = np.delete(self.matrix4, 3, 1)
        #return matrix3
        
    def rotatieX(self,deg):
        rad=radians(deg)
        c = np.cos(rad)
        s = np.sin(rad)
        R=np.array([[1, 0, 0, 0],
                     [0, c,-s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])
        self.matrix4=self.matrix4*R
        #return R
        
    def rotatieY(self,deg):
        rad=radians(deg)
        c = np.cos(rad)
        s = np.sin(rad)
        R=np.array([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]])
        self.matrix4=self.matrix4*R
        #return R

    def rotatieZ(self,deg):
        rad=radians(deg)
        c = np.cos(rad)
        s = np.sin(rad)
        R=np.array([[c,-s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
        self.matrix4=self.matrix4*R
        #return R
    
    def translatie(self,dx=0, dy=0, dz=0):
        U=np.array([[1,0,0,0],
                   [0,1,0,0],
                   [0,0,1,0],
                   [dx,dy,dz,1]])
        self.matrix4=self.matrix4*U
        #return U
    
    def schaal(self,sx=1, sy=1, sz=1):
        S=np.array([[sx, 0,  0,  0],
                    [0,  sy, 0,  0],
                    [0,  0,  sz, 0],
                    [0,  0,  0,  1]])
        self.matrix4=self.matrix4*S
        #return S
    
    def transformatie(self,Rx,Ry,Rz,dx,dy,dz,sx,sy,sz):
        self.vorm4_matrix()
        self.rotatieX(Rx)
        self.rotatieY(Ry)
        self.rotatieZ(Rz)
        self.translatie(dx,dy,dz)
        self.schaal(sx,sy,sz)
        self.vorm3_matrix()
        self.matrix_nieuw=self.matrix3
        self.vlakken_maken(self.matrix_nieuw)
        #self.plot(self.matrix_nieuw,self.vlakken_nieuw)
        
    def balk(self):
        return self.vlakken_nieuw
        
def multiplot(breedte,hoogte,diepte,amax,Balken,Voeten):
    
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    for voet in range(len(Voeten)):
        vlakken = Voeten[voet]
        #print('balk: '+str(balk+1))
        #print(vlakken[balk])
        faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
        faces.set_facecolor((0.45,0.1,0,1))
        ax.add_collection3d(faces)
        #print('')
    
    for balk in range(len(Balken)):
        vlakken = Balken[balk]
        #print('balk: '+str(balk+1))
        #print(vlakken[balk])
        faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
        faces.set_facecolor((0.45,0.1,0,1))
        ax.add_collection3d(faces)
        #print('')
    
    plt.title('Kast assembly')
    ax.autoscale(True)
    ax.set_aspect('auto')
    ax.view_init(45, 45)
    #ax.view_init(0, 0)
    ax.set_xlabel('x-as - %s cm' % int(breedte))
    ax.set_ylabel('y-as - %s cm' % int(diepte))
    ax.set_zlabel('z-as - %s cm' % int(hoogte))
    ax.set_xlim(-amax*1.1/2., amax*1.1/2.)
    ax.set_ylim(-amax*1.1/2., amax*1.1/2.)
    ax.set_zlim(0., amax*1.1/2.)
    plt.tight_layout()
    print('kast assembly')
    plt.show()
    plt.clf()
    
def voeten():
    Voeten=[]
    #bereken hoeveelheid voeten
    voet_extra=0
    if breedte_kast >= 150:
        for i in range(int(breedte_kast/150)):
            voet_extra=voet_extra+1
            
    v=hoogte_voet

    #voet1
    v1=plank(v,v,v)
    v1.aantal=4+voet_extra
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.,diepte_kast/2.-v/2.,v/2.
    sx,sy,sz=1,1,1
    v1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet1=v1.balk()
    Voeten.append(voet1)
    
    #voet2
    v2=plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.,-diepte_kast/2.+v/2.,v/2.
    sx,sy,sz=1,1,1
    v2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet2=v2.balk()
    Voeten.append(voet2)
    
    #voet3
    v3=plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=-breedte_kast/2.+v/2.,-diepte_kast/2.+v/2.,v/2.
    sx,sy,sz=1,1,1
    v3.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet3=v3.balk()
    Voeten.append(voet3)
    
    #voet4
    v4=plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=-breedte_kast/2.+v/2.,diepte_kast/2.-v/2.,v/2.
    sx,sy,sz=1,1,1
    v4.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet4=v4.balk()
    Voeten.append(voet4)
    
    if voet_extra > 0:
        for voet in range(voet_extra):
            ve1=plank(v,v,v)
            rx,ry,rz=0,0,0
            if voet_extra == 1:
                ve1=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=0.
                uy=diepte_kast/2.-v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
            elif voet_extra == 2:
                ve1=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=breedte_kast/6.
                uy=diepte_kast/2.-v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
                ve1=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=-breedte_kast/6.
                uy=diepte_kast/2.-v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
            elif voet_extra >= 3:
                ve1=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=0
                uy=diepte_kast/2.-v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
                ve1=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=breedte_kast/4.
                uy=diepte_kast/2.-v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
                ve1=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=-breedte_kast/4.
                uy=diepte_kast/2.-v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
            
            ve2=plank(v,v,v)
            rx,ry,rz=0,0,0
            if voet_extra == 1:
                ve2=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=0.
                uy=-diepte_kast/2.+v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete2=ve2.balk()
                Voeten.append(voete2)
            elif voet_extra == 2:
                ve2=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=breedte_kast/6.
                uy=-diepte_kast/2.+v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete2=ve2.balk()
                Voeten.append(voete2)
                
                ve2=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=-breedte_kast/6.
                uy=-diepte_kast/2.+v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete2=ve2.balk()
                Voeten.append(voete2)
                
            elif voet_extra >= 3:
                ve2=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=0.
                uy=-diepte_kast/2.+v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete2=ve2.balk()
                Voeten.append(voete2)
                
                ve2=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=breedte_kast/4.
                uy=-diepte_kast/2.+v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete2=ve2.balk()
                Voeten.append(voete2)
                
                ve2=plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=-breedte_kast/4.
                uy=-diepte_kast/2.+v/2.
                uz=v/2.
                sx,sy,sz=1,1,1
                ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete2=ve2.balk()
                Voeten.append(voete2)
    
    return Voeten

def onderstel():
    Breedtes=[]
    Balken=[]
    
    d=float(diepte_kast)
    b=float(breedte_plank)
    
    fractie_planken=d/b
    hele_planken=int(floor(fractie_planken))
    over=fractie_planken-hele_planken

    print(d,b,fractie_planken,hele_planken,over)
    
    if ((over > 0.0) and (hele_planken > 1)):
        hele_planken=hele_planken-1
        for planken in range(hele_planken):
            Breedtes.append(b)
        over=(b*(over+1.)/2.)
        Breedtes.append(over)
        Breedtes.append(over)
    else:
        for planken in range(hele_planken):
            Breedtes.append(b)
    
    uy=diepte_kast/2.-Breedtes[planken]/2.    
    for planken in range(len(Breedtes)):
        p=plank(lengte_plank,breedte_plank,dikte_plank)
        p.plank_zagen(breedte_kast,Breedtes[planken],dikte_plank)
        rx,ry,rz=0,0,0
        ux=0
        if planken >= 1:
            uy = uy - Breedtes[planken]/2. - Breedtes[planken-1]/2.
        uz=hoogte_voet+dikte_plank/2.
        sx,sy,sz=1,1,1
        p.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=p.balk()
        Balken.append(balk)
        
        print(planken)
    return Balken

def main():
    input_data()
    
    Voeten=voeten()
    Onderstel=onderstel()
    
    #plotten
    amax=max(breedte_kast,hoogte_kast,diepte_kast)

    multiplot(breedte_kast,hoogte_kast,diepte_kast,amax,Onderstel,Voeten)
main()