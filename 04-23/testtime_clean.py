from datetime import datetime,tzinfo,timedelta

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

t = datetime.now()
t = t.replace(tzinfo=Zone(-3,False,'GMT'))

print "Hora local: "
print t

timezones = range(-12,12)
for x in timezones:
    print t.astimezone(Zone(x,False,'GMT'))