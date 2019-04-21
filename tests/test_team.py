#!/usr/bin/env python3
import sys
from models.team import Team


if __name__ == "__main__":
    team = sys.argv[1]
    team = Team(team)
    print("{} at {}\n".format(team, team.team_url))
    print("Roster [{}]:".format(len(team.roster)))
    [print(player) for player in team.roster]
    print("")
    print("Handles [{}]:".format(len(team.handles)))
    [print(handle) for handle in team.handles]
