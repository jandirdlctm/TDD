import pytest
from player import SoccerPlayer
from player import Player
todo = pytest.mark.skip(reason='todo: pending spec')


def describe_Player():
    # def describe_Player_Constructor():
    def it_assigns_all_four_attributes():
        newPlayer = Player("Jandir", "Porta", "Peru", 22 )
        assert newPlayer.mFirstName == "Jandir"
        assert newPlayer.mLastName == "Porta"
        assert newPlayer.mNationality == "Peru"
        assert newPlayer.mAge == 22

    def it_rejects_all_incorrect_data_types_for_first_name():
        with pytest.raises(ValueError):
            Player(34, "Porta", "Peru", 22)
        with pytest.raises(ValueError):
            Player(-33, "Porta", "Peru", 22)
        with pytest.raises(ValueError):
            Player(33.0, "Porta", "Peru", 22)
        with pytest.raises(ValueError):
            Player(-33.0, "Porta", "Peru", 22)    
        

    def it_rejects_all_incorrect_data_types_for_last_name():
        with pytest.raises(ValueError):
            Player("Jandir", 68, "Peru", 22)
        with pytest.raises(ValueError):
            Player("Jandir", -78, "Peru", 22)
        with pytest.raises(ValueError):
            Player("Jandir", 89.0, "Peru", 22)
        with pytest.raises(ValueError):
            Player("Jandir", -79.0, "Peru", 22)

    def it_rejects_all_incorrect_data_types_for_nationality():
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", 56, 22 )
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", -56, 22 )
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", 86.0, 22 )
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", -56.0, 22 )

    def it_rejects_all_incorrect_data_types_for_age():
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", "Peru", "twenty")
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", "Peru", -23)
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", "Peru", 25.0)
        with pytest.raises(ValueError):
            Player("Jandir", "Porta", "Peru", 0)

    def describe_setters_for_player_class():
        def it_sets_first_name_of_player_with_correct_value():
            newPlayer = newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            newPlayer.setFirstName("Carlos") == True
            newPlayer.setFirstName(32) == False
            
                


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
                assert newPlayer.mDefending == 35
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
        
        def it_sets_rejects_negative_values():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            newPace = -45
            newShooting = -56
            newPassing = -67
            newDribbling = -56
            newDefending = -67
            newPhysicality = -78
            assert newPlayer.setPace(newPace) == False
            assert newPlayer.setShooting(newShooting) == False
            assert newPlayer.setPassing(newPassing) == False
            assert newPlayer.setDribbling(newDribbling) == False
            assert newPlayer.setDefending(newDefending) == False
            assert newPlayer.setPhysicality(newPhysicality) == False

        def it_rejects_set_string_values():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            newPace = "forty"
            newShooting = "forty"
            newPassing = "forty"
            newDribbling = "forty"
            newDefending = "forty"
            newPhysicality = "forty"
            assert newPlayer.setPace(newPace) == False
            assert newPlayer.setShooting(newShooting) == False
            assert newPlayer.setPassing(newPassing) == False
            assert newPlayer.setDribbling(newDribbling) == False
            assert newPlayer.setDefending(newDefending) == False
            assert newPlayer.setPhysicality(newPhysicality) == False

        def it_rejects_set_floating_values():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            newPace = 80.0
            newShooting = 80.0
            newPassing = 80.0
            newDribbling = 80.0
            newDefending = 80.0
            newPhysicality = 80.0
            assert newPlayer.setPace(newPace) == False
            assert newPlayer.setShooting(newShooting) == False
            assert newPlayer.setPassing(newPassing) == False
            assert newPlayer.setDribbling(newDribbling) == False
            assert newPlayer.setDefending(newDefending) == False
            assert newPlayer.setPhysicality(newPhysicality) == False

        def it_rejects_set_over_limit():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            newValue = 110
            assert newPlayer.setPace(newValue) == False
            assert newPlayer.setShooting(newValue) == False
            assert newPlayer.setPassing(newValue) == False
            assert newPlayer.setDribbling(newValue) == False
            assert newPlayer.setDefending(newValue) == False
            assert newPlayer.setPhysicality(newValue) == False

    def describe_get_attributes_of_soccer_Player():

        def it_gets_the_correct_value_for_all_attributes():
            newPlayer = SoccerPlayer(23,67,45,56,35,34) 
            assert newPlayer.getPace() == 23
            assert newPlayer.getShooting() == 67
            assert newPlayer.getPassing() == 45
            assert newPlayer.getDribbling() == 56
            assert newPlayer.getDefending() == 35
            assert newPlayer.getPhysicality() == 34  
            

