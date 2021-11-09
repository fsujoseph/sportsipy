import pytest

from sportsipy.ncaab.boxscore import Boxscore
from sportsipy.ncaab.roster import Player

game = Boxscore('2020-02-24-19-florida-state')
trent_forest = Player('trent-forrest-1')


class TestBoxScore:

    def test_away_assists(self):
        assert game.away_assists == 8

    def test_away_blocks(self):
        assert game.away_blocks == 2

    def test_away_defensive_rebounds(self):
        assert game.away_defensive_rebounds == 19

    def test_away_field_goals(self):
        assert game.away_field_goals == 25

    def test_away_faield_goal_attempts(self):
        assert game.away_field_goal_attempts == 59

    def test_away_free_throw_percentage(self):
        assert game.away_free_throw_percentage == 0.857

    def test_away_offensive_rating(self):
        assert game.away_offensive_rating == 95.7

    def test_away_fouls(self):
        assert game.away_personal_fouls == 23

    def test_away_score(self):
        assert game.away_points == 67

    def test_away_ranking(self):
        assert game.away_ranking == 11

    def test_away_steals(self):
        assert game.away_steals == 1

    def test_away_three_point_field_goal_percentage(self):
        assert game.away_three_point_field_goal_percentage == 0.238

    def test_away_turnovers(self):
        assert game.away_turnovers == 13

    def test_away_wins(self):
        assert game.away_wins == 23

    def test_date(self):
        assert game.date == "February 24, 2020"
    
    def test_home_assists(self):
        assert game.home_assists == 9

    def test_home_blocks(self):
        assert game.home_blocks == 4

    def test_home_defensive_rebounds(self):
        assert game.home_defensive_rebounds == 26

    def test_home_field_goals(self):
        assert game.home_field_goals == 28

    def test_home_faield_goal_attempts(self):
        assert game.home_field_goal_attempts == 55

    def test_home_free_throw_percentage(self):
        assert game.home_free_throw_percentage == 0.778

    def test_home_offensive_rating(self):
        assert game.home_offensive_rating == 117.1

    def test_home_fouls(self):
        assert game.home_personal_fouls == 16

    def test_home_score(self):
        assert game.home_points == 82

    def test_home_ranking(self):
        assert game.home_ranking == 6

    def test_home_steals(self):
        assert game.home_steals == 7

    def test_home_three_point_field_goal_percentage(self):
        assert game.home_three_point_field_goal_percentage == 0.313

    def test_home_turnovers(self):
        assert game.home_turnovers == 11

    def test_home_wins(self):
        assert game.home_wins == 24

    def test_location(self):
        assert game.location == "Donald L. Tucker Center, Tallahassee, Florida"


class TestPlayer:

    def test_conference(self):
        assert trent_forest.blocks == 44

    def test_defensive_rebounds(self):
        assert trent_forest.defensive_rebounds == 424

    def test_field_goal_percentage(self):
        assert trent_forest.field_goal_percentage == 0.462

    def test_free_throws_made(self):
        assert trent_forest.free_throws == 336

    def test_personal_fouls(self):
        assert trent_forest.personal_fouls == 205

    def test_steals(self):
        assert trent_forest.steals == 224

    def test_three_pointers(self):
        assert trent_forest.three_pointers == 27

    def test_turnovers(self):
        assert trent_forest.turnovers == 260

    def test_usage(self):
        assert trent_forest.usage_percentage == 18.5





