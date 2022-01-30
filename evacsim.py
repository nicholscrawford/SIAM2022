timestep = 5

class path:
    
    #len is in km, speedlim is in km/hr, out is an object that can accept people (has acceptperson() method, yay for python ambiguity)
    def __init__(self, len, speedlim, out, location):
        self._len = len
        self._speedlim = speedlim
        minutesonroad = (len / speedlim) * 60
        timestepsonroad = minutesonroad/timestep
        self._peoplearr = [0] * round(timestepsonroad+ 0.5)
        self.location = location
        
        self._out = out
        capacityperkm = (speedlim*(3.0/3600.0)+4.5e-3)**-1
        self._capacityperelement = int(capacityperkm * (len / self._peoplearr.__len__()) )
        
    def timestep(self):
        i = len(self._peoplearr) - 1
        
        #Try and move the people out at the end
        for j in range(self._peoplearr[i]):
            if self._out.accept() == True:
                self._peoplearr[i] -= 1
        i -= 1
        
        #Try to drive foreward.
        while i >= 0:
            self._driveforeward(i)
            i -= 1
        
    def _driveforeward(self, i):
        for i in range(self._peoplearr[i]):
            if self._peoplearr[i+1] <= self._capacityperelement:
                self._peoplearr[i] -= 1
                self._peoplearr[i+1] += 1
        
    #Returns true if person is accepted.
    def accept(self):
        if(self._peoplearr[0] >= self._capacityperelement):
            return False
        else:
            self._peoplearr[0] += 1
            return True
        
    def isempty(self):
        total = 0
        for x in self._peoplearr:
            total += x
            
        return total <= 0
        
        
class neighborhood:
    #Rate people leave, in fraction per timestep.
    leavingrates = [.10, .2, .3, .2, .15, .05]
    
    def __init__(self, numpeople, out):
        self._numpeopleleft = numpeople
        self._out = out
        
        self._stepssinceevac = 0
        
        self._leavingpertimestep = []
        for x in neighborhood.leavingrates:
            self._leavingpertimestep.append(int(x * numpeople + 0.5))
        
        #People who are trying to leave but are blocked by traffic.
        self._numpeoplequeued  = 0
        
    def timestep(self):
        #If there are people who haven't left their homes yet
        if self._stepssinceevac < len(self._leavingpertimestep):
            
            #Each person tries to get on the road, if not queues.
            for x in range(self._leavingpertimestep[self._stepssinceevac]):
                if(self._out.accept() == True):
                    self._numpeopleleft -= 1
                else:
                    self._numpeoplequeued += 1
                self._leavingpertimestep[self._stepssinceevac] -= 1
                
        #People queued try to leave
        for x in range(self._numpeoplequeued):
            if(self._out.accept() == True):
                self._numpeoplequeued -= 1
                self._numpeopleleft -= 1
                    
        self._stepssinceevac += 1
                    
    
    def isempty(self):
        return self._numpeopleleft <= 0
        
        
class evaczone:
    def __init__(self):
        self.numevacuated = 0
    
    def accept(self):
        self.numevacuated += 1
        return True
    
    
