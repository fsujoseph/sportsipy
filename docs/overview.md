Overview
===========

Sportsipy is currently available for Soccer, MLB, NBA, NFL, NHL, NCAAF, and NCAAB. This document serves as a brief overview of what Sportsipy has to offer. The great thing about Sportsipy is that almost any sport-related statistic for these teams and players can be found. You can use the search box in the [documentation](http://sportsipy.readthedocs.io/en/latest) to track down what you are looking for.

Shown below, each module is covered at a high level. The listed available attributes aren't all encompasing, they are meant to give a general idea of what each module has to offer.

Team
--------

The Team module is used to grab high-level stats and information for a specific team. Each Team instance can be used to access the Schedule and Roster classes.

Available attributes - team abbreivation, team name, average age, games played (season), team total stats, rank, wins, losses.

Supported sports - Soccer, MLB/NBA/NFL/NHL/NCAAF/NCAAB

Schedule
--------

The Schedule module can be used to iterate over all games in a team's schedule to get high-level game information such as the date, score, result, and more.

Available attributes (per game) - Boxscore class, other high level information not in boxscore such as game #, overtime (yes/no)

Supported sports - Soccer, MLB/NBA/NFL/NHL/NCAAF/NCAAB

Roster
--------

The Roster module contains detailed player information for every player on a team's roster, allowing each player to be queried by either their name or their unique player ID. You can obtain statistics for any stat available (i.e. goals, shots, assists, playtime). 

Available attributes - See Player module

Supported sports - Soccer, MLB/NBA/NFL/NHL/NCAAF/NCAAB

Boxscore
--------

The Boxscore module can be used to grab information from a specific game. The Boxscore can be easily queried by passing a boxscore's URI on sports-reference.com which can be retrieved from the Schedule class.

Available attributes are - arena, attendance, date, duration, and game stats relative to the sport.

You can also access the Player module from within the Boxscore module to get the player specific stats for that game.

Supported sports - MLB/NBA/NFL/NHL/NCAAF/NCAAB

Player
--------

The Player module contains player information and stats for all seasons. Given a player ID you can capture all relevant stats and information like name, team, height/weight, career stats, single-season stats, and much more. This class can also be found within the Roster module and Boxscore module.

Available attributes are - player stats (career, single season, single game, etc.)

Supported sports - MLB/NBA/NFL/NHL/NCAAF/NCAAB

Conferences
--------

The Conference module allows conferences to be pulled for any season. Accessing the class properties exposes various dictionaries containing the team and conference abbreviations as well as other information.

Available attributes - conferences, Teams class

Supported sports - NCAAF/NCAAB

Rankings
--------

The Rankings module can be used to easily query the NCAA Men's Division-I Football rankings published by the Associated Press on a week-by-week basis. Different formats can be referenced, ranging from a lightweight dictionary of the most recent rankings containing only the team abbreviation and rank, to a much larger dictionary of all rankings for an entire season with results including full team name and abbreviation, current rank, week number, previous rank, and movement.

Available attributes - current, complete (by week)

Supported sports - NCAAF/NCAAB
