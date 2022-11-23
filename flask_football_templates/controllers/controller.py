from flask import render_template, request
from app import app
from modules.teams_list import teams, add_new_team
from modules.football_team import Team

@app.route("/teams")
def teams_list():
    return render_template('index.html', title='Team', teams=teams)

@app.route("/teams", methods=['Post'])
def add_team():
    team_club = request.form["club"] 
    team_manager = request.form["title"]
    new_team = Team(club=team_club, manager=team_manager, dues_paid=True)
    add_new_team(new_team)

    return render_template('index.html', title='Team', teams=teams)