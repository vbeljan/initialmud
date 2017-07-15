#!/usr/bin/python

class Track:

    def __init__(self, name):
        track = []

        path = "../res/tracks/" + name
        trackfile = open(path, 'r')
        tlines = trackfile.readlines()

        for tline in tlines:
            tsplit = tline.split(',')

            track.append(tuple(tsplit))
        print "track element tuple"
        print track

        self.track = track

######################################################################
#### GETTERS AND SETTERS
######################################################################

    def getSegment(self, num):
        if isinstance(num, (int,long)):
            return self.track[num]
        else:
            print "Track.getSegment: invalid parameter type"

    def getSegmentParam(self, num, param):
        if not isinstance(num, (int,long)):
            print "Track.getSegmentParam: invalid parameter type(s)"

        segment = self.track[num]
        params = {'type' : 0,
                  'length' : 1,
                  }

        tuplekey = params[param]
        value = segment[tuplekey]

        if tuplekey > 0:
            return float(value)
        else:
            return value

    def getTrackLength(self):
        return len(self.track)
