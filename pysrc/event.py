#!/usr/bin/python
import track
import car

class Event(object):

        def __init__(self, c, t):
                self.eventtrack = track.Track("TestTrack.trk")
                self.eventcar = car.Car("86_trueno")
                print self.eventtrack

        def start(self):
                for n in range(0, self.eventtrack.getTrackLength()):
                        if self.eventtrack.getSegmentParam(n, 'type') == 'S':
                                self.straight(self.eventtrack.
                                              getSegmentParam(n, 'length'))
                        elif trackelement[0] == 'R':
                                pass
                        elif trackelement[0] == 'L':
                                pass




        def straight(self, length):
                l = 0.0;
                while l < length:
                        l = self.eventcar.accelerateStraight(l)
                        print "Length passed = %f" % l
