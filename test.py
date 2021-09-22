import pytest
import math
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
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            assert newPlayer.setFirstName("Carlos") == True
            assert newPlayer.setFirstName(32) == False
            assert newPlayer.setFirstName(-43) == False
            assert newPlayer.setFirstName(56.0) == False
            assert newPlayer.setFirstName(-56.0) == False

        def it_sets_last_name_of_player_with_correct_value():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            assert newPlayer.setLastName("Carlos") == True
            assert newPlayer.setLastName(32) == False
            assert newPlayer.setLastName(-43) == False
            assert newPlayer.setLastName(56.0) == False
            assert newPlayer.setLastName(-56.0) == False

        def it_sets_nationality_of_player_with_correct_value():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            assert newPlayer.setLastName("Carlos") == True
            assert newPlayer.setNationality(32) == False
            assert newPlayer.setNationality(-43) == False
            assert newPlayer.setNationality(56.0) == False
            assert newPlayer.setNationality(-56.0) == False

        def it_sets_age_of_player_with_correct_value():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            assert newPlayer.setAge(45) == True
            assert newPlayer.setAge("forty") == False
            assert newPlayer.setAge(-45) == False
            assert newPlayer.setAge(45.0) == False
            assert newPlayer.setAge(-56.0) == False
            assert newPlayer.setAge(0) == False

    def describe_getters_for_all_attributes():
        
        def it_gets_all_player_attributes():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            assert newPlayer.getFirstName() == "Jandir"
            assert newPlayer.getLastName() == "Porta"
            assert newPlayer.getNationality() == "Peru"
            assert newPlayer.getAge() == 22

        def it_gets_the_id():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            expectedID = 0
            if newPlayer.generateID():
                expectedID = newPlayer.mID
            assert expectedID == newPlayer.mID


    def describe_random_id_for_player():
        def it_gives_a_random_id_for_a_player():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            assert newPlayer.generateID() == True

        def it_generates_a_four_digit_number():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            if (newPlayer.generateID()):
                listID = [int(x) for x in str(newPlayer.mID)]
                assert len(listID) == 4
    
    def describe_store_in_dictionary():
        def it_stores_as_dictionaries():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            newPlayer.generateID
            response = False
            if newPlayer.addToDict():
                response = True
            assert  response == True

        def it_sets_the_id_as_key():
            newPlayer = Player("Jandir", "Porta", "Peru", 22 )
            newPlayer.generateID
            playerDict = newPlayer.addToDict()
            id = newPlayer.mID
            response = False
            if playerDict[id]:
                response = True
            assert response == True
        
        
            
            
        
def describe_SoccerPlayer():

    @pytest.fixture
    def soccer_player():
        return SoccerPlayer(23,67,45,56,35,34)

    def describe_inheritance_from_Player_Class():
        def it_inherits_from_Player():
            newSoccerPlayer = SoccerPlayer(23,67,45,56,35,34)
            assert isinstance(newSoccerPlayer, Player) == True
    
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
            

    def describe_overall_rating():
        def it_calculates_overall_rating():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            expectedRating = (newPlayer.getPace() + newPlayer.getShooting() + newPlayer.getPassing() + newPlayer.getDribbling() + newPlayer.getDefending() + newPlayer.getPhysicality()) / 6
            assert newPlayer.getOverallRating() == expectedRating

        def it_calculates_overall_rating_as_integer():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            rating = newPlayer.getOverallRating()
            newRating = int(math.floor(rating))
            assert isinstance(newRating, int)


        def it_gives_feedback_based_on_rating():
            newPlayer = SoccerPlayer(23,67,45,56,35,34)
            # 0 - 24 = poor
            # 25 - 49 = alright
            # 50 - 75 = good
            # 75 - 100 = legendary
            rating = newPlayer.getOverallRating()
            assert newPlayer.getFeedback() == "alright"