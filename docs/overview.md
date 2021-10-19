Overview
===========

Sportsipy covers Soccer, MLB, NBA, NFL, NHL, NCAAF, and NCAAB. This document serves as a brief overview of what Sportsipy has to offer. The great thing about Sportsipy that should be known right off the bat is that virtually any sport-related statistic for these leagues, teams, and players can be found. You can use the search box on this site https://sportsipy.readthedocs.io/en/latest/index.html to find the exact command for whatever you are looking for!

Team - (Soccer, MLB/NBA/NFL/NHL/NCAAF/NCAAB)

The Team module is used to grab high-level stats and information for a specific team. Each Team instance can be used to access the Schedule and Roster classes.

Available attributes - team abbreivation, team name, average age, games played (season), team total stats, rank, wins, losses.

Schedule - (Soccer, MLB/NBA/NFL/NHL/NCAAF/NCAAB)

The Schedule module can be used to iterate over all games in a team's schedule to get high-level game information such as the date, score, result, and more.

Available attributes (per game) - Boxscore class, other high level information not in boxscore such as game #, overtime (yes/no), etc.

Roster - (Soccer, MLB/NBA/NFL/NHL/NCAAF/NCAAB)

The Roster module contains detailed player information for every player on a team's roster, allowing each player to be queried by either their name or their unique player ID. You can obtain statistics for any stat available (i.e. goals, shots, assists, playtime). 

Available attributes - See Player module

Boxscore - (MLB/NBA/NFL/NHL/NCAAF/NCAAB)

The Boxscore module can be used to grab information from a specific game. The Boxscore can be easily queried by passing a boxscore's URI on sports-reference.com which can be retrieved from the Schedule class.

Available attributes are - arena, attendance, date, duration, and game stats relative to the sport.

You can also access the Player module from within the Boxscore module to get the player specific stats for that game.

Player - (MLB/NBA/NFL/NHL/NCAAF/NCAAB)

The Player module contains player information and stats for all seasons. Given a player ID you can capture all relevant stats and information like name, team, height/weight, career stats, single-season stats, and much more. This class can also be found within the Roster module and Boxscore module.

Available attributes are - player stats (career, single season, single game, etc.)
