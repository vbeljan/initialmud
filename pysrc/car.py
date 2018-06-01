#!/usr/bin/python

import xml.etree.cElementTree as et
from lxml import objectify
from constants import imud

class Car(object):

    def __init__(self, name):

        self.cardata = objectify.fromstring(self.parseCar(name))
        self.initGearbox()

        self.speed = 0.0
        self.angle = 0.0

        FrontSurface = self.cardata.width * self.cardata.height
        self.drag = 0.5 * FrontSurface * imud.AIRDENS * self.cardata.drag

        self.gear = 0

    def test():
        cardata = parseCar("86_trueno")
        getName(cardata)

    def parseCar(self, name):
        path = "../res/cars/" + name + ".xml"
        f = open(path, 'r')
        carstr = f.read()
        f.close()
        return carstr

    def initGearbox(self):
        self.geardict = {}
        gbox = et.parse('../res/parts/gearbox/86_5_speed.xml')
        root = gbox.getroot()
        self.ratio = root.find('ratio')

##======================================================================
## GETTERS & SETTERS
##======================================================================

    def getDesc(self, param):
        return cardata.findtext(param)

    def getNum(self, param):
        vs = self.cardata.findtext(param)
        print param
        print vs
        if vs == None:
            print "fetching numeral parameter failed \n"

        return float(vs)

    def getParam(self, param):
        vs = self.cardata.find('gear1')



##======================================================================
## DRIVING IMPLEMENTATION
##======================================================================

    def accelerateStraight(self, s1):
        v1 = self.speed  #0.1 | 40,773937978
        Cdrag = self.drag #0.4389
        Crr = self.cardata.drag * 30 #13.167

        Fdrag = Cdrag * v1  #0.004389 | 729,677402603
        Frr = Crr * v1 #1.3167 | 536.870441356
        Fdrive = (self.cardata.engine.hp) * 1.30 * 3.1 * self.gearselect() * self.cardata.gearbox.powerloss / imud.WHEEL
        print "Fdrive = %.5f" % Fdrive
        print "Distance = %.5f" % s1
        print "Speed = %.5f" % v1
        print "Resistance = %.5f" % Frr
        print "Drag = %.5f" % Fdrag
        print "Gear = %i" % self.gear
        print "\n"

        Fu = Fdrive - Fdrag - Frr #89482.663551 | 928,088952916
        a = Fu / self.cardata.mass #81.347875955 | 0,84371723
        v2 = v1 + imud.TIMEFRAME * a #40,773937978 | 41,195796593

        self.speed = v2
        return s1 + imud.TIMEFRAME * v2 #20,386968989 | 40,984867285

    def getBrakingPoint(self, distanceOfStraight, turnRadiusMid):
        pass


##======================================================================
## DRIVING HELPERS
##======================================================================

    def lateralForce(self, turnRadius):
        delta = math.acos(self.cardata.length / turnRadius)
        turnAngle = 90 - delta
        Fz = imud.CT * delta
        return Fz

    def tractionForce(self):
        nm = self.cardata.engine.hp * 745.7 * imud.TIMEFRAME #177,61215145 idealno
        #nm = 0.001 * imud.TIMEFRAME * self.hp #
        rnm = nm - nm * self.cardata.gearbox.powerloss
        Ft = rnm  / imud.WHEEL
        return float(Ft)

    def gearselect(self):
        #here be dragons
        if self.speed > float(self.ratio[self.gear].get('top')):
            self.gear += 1

        return float(self.ratio[self.gear].get('r'))
