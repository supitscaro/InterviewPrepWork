# Return a function with the name of the winning team

# 0 - away team
# 1 - home team

# INPUTS/OUTPUTS
# competitions = [HTML, C#] and results = [0], away team won meaning C# won
# competitions = [C#, Python] and results = [0], away team won meaning Python won

# IMPORTANT NOTES
# only one team will win the tournament
# each time competes only once against each other
# there will always be at least two teams

# QUESTIONS
# 3 points if team wins
# 0 points if team loses
# !!!! keep track of points, whichever team has the most points wins the tournament

# GOAL
# a function that returns the name of the winner

HOME_TEAM = 1


def tournamentWinner(competitions, results):
    best_team = ""
    scores = {best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winning_team = home_team if home_team == HOME_TEAM else away_team

        updateScores(winning_team, 3, scores)

        if scores[winning_team] > scores[best_team]:
            best_team = winning_team

    return best_team


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
