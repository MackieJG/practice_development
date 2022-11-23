from modules.football_team import *

team1 = Team("Saint Anthony", "Davie Weir", True)
team2 = Team("Rosyth", "Alex Rae", True)
team3 = Team("Govan", "Bob Malcolm", False)
team4 = Team("Rutherglen", "Barry Ferguson", False)

teams = [team1, team2, team3, team4]

def add_new_team(team):
    teams.append(team)