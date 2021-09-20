class SoccerPlayer:
    def __init__(self,pace, shooting, passing, dribbling, defending, physical):
        
        if pace < 0 or pace > 100  or shooting < 0 or shooting > 100 or passing < 0 or passing > 100 or dribbling < 0 or dribbling > 100 or defending < 0 or defending > 100 or physical < 0 or physical > 100:
            raise ValueError
        self.mPace = pace
        self.mShooting = shooting
        self.mPassing = passing
        self.mDribbling = dribbling
        self.mDeffending = defending
        self.mPhysical = physical

    def setPace(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mPace = value
        return True
    
    def setShooting(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mShooting = value
        return True

    def setPassing(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mPassing = value
        return True 

    def setDribbling(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mDribbling = value
        return True
    
    def setDefending(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mDeffending = value
        return True

    def setPhysicality(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mPhysical = value
        return True
