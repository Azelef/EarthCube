from random import *
from math import *
#This file assumes that you have already generated an elevation map

def elev(lat,lon):#Obtain an elevation from coordinates
    return elevMap[int(lat+89+0.5)][int(lon+179+0.5)]

def ll(v):#Compute the latitude and longitude of a point expressesed as a vector
    lat=180*asin(v[0]/sqrt(sum([v[i]**2 for i in range(3)])))/pi
    lon=180*acos(v[1]/sqrt(v[1]**2+v[2]**2))/pi
    if v[2]<0:
        lon*=-1
    return [lat,lon]

def norm(v):#Return a normalized version of vector v
    n=sqrt(sum([v[i]**2 for i in range(3)]))
    return [v[i]/n for i in range(3)]

def fois(v,f):
    return [v[i]*f for i in range(3)]

def hCube(cube):#Obtain the elevation of the lowest vertex of a cube
    h=10000
    for v in cube:
        h=min(h,alt(v[0],v[1]))
    return h

def dispCube(cube,res):#Display a cube on a map
    for i in range(89,-90,-res):
        s=""
        for j in range(-170,181,res):
            bon=False
            for c in cube:
                if (c[0]-i)**2+(c[1]-j)**2<50:
                    s+="X"
                    bon=True
            if not bon:
                if alt(i,j)>0:
                    s+="#"
                else:
                    s+=" "
        print(s)

def dispMap(res):#Display a map of the world
    for i in range(89,-90,-res):
        s=""
        for j in range(-170,181,res):
            if alt(i,j)>0:
                s+="#"
            else:
                s+=" "
        print(s)

record=-3000
recordCube=[]
for n in range(1000000):
    a=norm([random() for i in range(3)])
    b=[random() for i in range(3)]
    avb=norm([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-b[0]*a[1]])
    avb2=norm([a[1]*avb[2]-a[2]*avb[1],a[2]*avb[0]-a[0]*avb[2],a[0]*avb[1]-avb[0]*a[1]])
    cube=[]
    pm={-1,1}
    for i in pm:
        for j in pm:
            for k in pm:
                v=[fois(a,i)[l]+fois(avb,j)[l]+fois(avb2,k)[l] for l in range(3)]
                cube.append(ll(v))
    if hCube(cube)>record:
        recordCube=cube
        record=hCube(cube)
        dispCube(cube,5)
        print(hCube(cube))
