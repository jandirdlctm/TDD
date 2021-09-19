class SoccerPlayer:
    def __init__(self,pace, shooting, passing, dribbling, defending, physical):
        if pace < 0 or shooting < 0 or passing < 0 or dribbling < 0 or defending < 0 or physical < 0:
            raise ValueError
        self.mPace = pace
        self.mShooting = shooting
        self.mPassing = passing
        self.mDribbling = dribbling
        self.mDeffending = defending
        self.mPhysical = physical
