f = open('schedule.txt', 'r')
data = f.readlines()
f.close()

nteams = 8
teams = ['MI', 'CSK', 'DD', 'KXIP', 'KKR', 'RCB', 'RR', 'DD']
ngames = 56
ntransfers = 80
nplayers = 11

MI = 0
CSK = 0
DD = 0
KXIP = 0
KKR = 0
RCB = 0
RR = 0
DD = 0

#goal is to keep schedule team players n+n = maximum of 11.

#use free transfers + ntransfers for each game and play maximum possible players each game
