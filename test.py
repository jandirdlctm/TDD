import pytest
from player import SoccerPlayer
todo = pytest.mark.skip(reason='todo: pending spec')


def describe_SoccerPlayer():

    @pytest.fixture
    def soccer_player():
        return SoccerPlayer(23,67,45,56,35,34)
    
    def describe_initializer_of_soccer_player():
        def it_assigns_all_six_attributes():
                newPlayer = SoccerPlayer(23,67,45,56,35,34)
                assert newPlayer.mPace == 23
                assert newPlayer.mShooting == 67
                assert newPlayer.mPassing == 45
                assert newPlayer.mDribbling == 56
                assert newPlayer.mDeffending == 35
                assert newPlayer.mPhysical == 34

        def it_rejects_less_than_zero_values_for_attributes():
            # newPlayer = SoccerPlayer(-23,67,45,-56,35,34)
            with pytest.raises(ValueError):
                SoccerPlayer(-23,67,45,-56,35,34)
        
        def it_rejects_over_100_values():
            with pytest.raises(ValueError):
                SoccerPlayer(102,100,120, 130, 40,20)

        def it_constructs_the_object():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            assert isinstance(newPlayer, SoccerPlayer) 
    
    def describe_set_attributes_of_soccer_Player():
        def it_sets_for_all_six_attributes():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            newPace = 45
            newShooting = 56
            newPassing = 67
            newDribbling = 56
            newDefending = 67
            newPhysicality = 78
            assert newPlayer.setPace(newPace) == True
            assert newPlayer.setShooting(newShooting) == True
            assert newPlayer.setPassing(newPassing) == True
            assert newPlayer.setDribbling(newDribbling) == True
            assert newPlayer.setDefending(newDefending) == True
            assert newPlayer.setPhysicality(newPhysicality) == True
        