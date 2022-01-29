timestep = 5

class path:
    capacityperkm = 1000
    
    #len is in km, speedlim is in km/hr, out is an object that can accept people (has acceptperson() method, yay for python ambiguity)
    def __init__(self, len, speedlim, out):
        self._len = len
        self._speedlim = speedlim
        minutesonroad = (len / speedlim) * 60
        timestepsonroad = minutesonroad/timestep
        self._peoplearr = [0] * int(timestepsonroad+ 0.5)
        
        self._out = out
        self._capacityperelement = int(path.capacityperkm * (len / len(self._peoplearr)) )
        
    def timestep(self):
        i = len(self._peoplearr) - 1
        
        #Try and move the people out at the end
        for i in range(self._peoplearr[i]):
            if self._out.acceptperson() == True:
                self._peoplearr[i] -= 1
        i -= 1
        
        #Try to drive foreward.
        while i >= 0:
            self._driveforeward(i)
            i += 1
        
    def _driveforeward(self, i):
        for i in range(self._peoplearr[i]):
            if self._peoplearr[i+1] <= self._capacityperelement:
                self._peoplearr[i] -= 1
                self._peoplearr[i+1] += 1
        
    #Returns true if person is accepted.
    def _acceptperson(self):
        if(self._peoplearr[0] >= self._capacityperelement):
            return False
        else:
            self._peoplearr[0] += 1
            return True
        