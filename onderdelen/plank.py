#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from math import radians
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class plank:
    def __init__(self,lengte,breedte,dikte):
        self.breedte=breedte
        self.lengte=lengte
        self.dikte=dikte
        #self.aantal=0.
    
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