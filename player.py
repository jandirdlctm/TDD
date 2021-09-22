import random

class Player:
    def __init__(self, firstName, lastName, nationality, age):
        if isinstance(firstName, str) == False or isinstance(lastName, str) == False or isinstance(nationality, str) == False or isinstance(age, int) == False or age <= 0 :
            raise ValueError
        self.mFirstName = firstName
        self.mLastName = lastName
        self.mNationality = nationality
        self.mAge = age

    def setFirstName(self, value):
        if isinstance(value, str) == False:
            return False
        self.mFirstName = value
        return True

    def setLastName(self, value):
        if isinstance(value, str) == False:
            return False
        self.mLastName = value
        return True

    def setNationality(self, value):
        if isinstance(value, str) == False:
            return False
        self.mNationality = value
        return True

    def setAge(self, value):
        if isinstance(value, int) == False or value <= 0:
            return False
        self.mAge = value
        return True

    def getFirstName(self):
        return self.mFirstName
    
    def getLastName(self):
        return self.mLastName

    def getNationality(self):
        return self.mNationality

    def getAge(self):
        return self.mAge

    def generateID(self):
        number = random.randint(1000,9999)
        return True


    
        





class SoccerPlayer:
    def __init__(self,pace, shooting, passing, dribbling, defending, physical):
        
        if pace < 0 or pace > 100  or shooting < 0 or shooting > 100 or passing < 0 or passing > 100 or dribbling < 0 or dribbling > 100 or defending < 0 or defending > 100 or physical < 0 or physical > 100:
            raise ValueError
        self.mPace = pace
        self.mShooting = shooting
        self.mPassing = passing
        self.mDribbling = dribbling
        self.mDefending = defending
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
        self.mDefending = value
        return True

    def setPhysicality(self, value):
        if (isinstance(value, float) or isinstance(value, str) or value < 0 or value > 100):
            return False
        self.mPhysical = value
        return True

    def getPace(self):
        return self.mPace

    def getShooting(self):
        return self.mShooting

    def getPassing(self):
        return self.mPassing

    def getDribbling(self):
        return self.mDribbling
    
    def getDefending(self):
        return self.mDefending

    def getPhysicality(self):
        return self.mPhysical


