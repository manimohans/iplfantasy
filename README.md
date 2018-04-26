# iplfantasy

#WORK IN PROGRESS

Problem statement:
For IPL fantasy, the total number of transfers is limited.
Hence, the user needs to optimize the usage based on number of available transfers and number of games in the schedule (remaining schedule).

The goal of this code is to achieve:
1. Play maximum number of possible players in a given game. (Minimum 4 or 5?)
2. Not over-use transfers and still stick to the limit.
3. Build a matrix that will show which team members should be taken off and which team member should be added in order to correctly utilize transfers and still play N games with maximum players possible.

e.g. at start of season, we are given with 80 transfers to use over 56 games. We manually have to look at the schedule and optimize the usage of transfers. This algorithm should automatically tell which team players to take off and which team players should be put in.

End of 56 games, 0 transfers remaining, maximum possible players should be played.
