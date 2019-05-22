#!/usr/bin/env python3
"""Defines the Standings class for storing standings."""
import json
import requests
from datetime import datetime


class Standings():
    """Represents the MLB standings.
    
    Attributes:
        __standings (dict): Dictionary of str/lists representing MLB standings.
    """

    __standings = {}

    def save(self):
        """Saves the current standings to a storage file."""
        d = self.__standings.copy()
        d["updated_at"] = d["updated_at"].isoformat()
        with open("standings.json", "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON standings storage file to __standings."""
        with open("standings.json", "r", encoding="utf-8") as f:
            self.__standings = json.load(f)
        self.__standings["updated_at"] = datetime.strptime(
            self.__standings["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

    def get(self):
        """Return __standings."""
        return self.__standings

    def update(self):
        """Updates the standings using the erikberg.com API."""
        try:
            results = requests.get("https://erikberg.com/mlb/standings.json")
            results = results.json()
        except Exception:
            return

        codex = {
            "AL E": "AL East",
            "AL C": "AL Central",
            "AL W": "AL West",
            "NL E": "NL East",
            "NL C": "NL Central",
            "NL W": "NL West",
        }
        for team in results.get("standing"):
            if team.get("last_name") == "Diamondbacks":
                team["last_name"] = "Dbacks"
            t = {
                "rank": team.get("rank"),
                "won": team.get("won"),
                "lost": team.get("lost"),
                "last_name": team.get("last_name")
            }
            key = "{} {}".format(team.get("conference"), team.get("division"))
            self.__standings["divisions"][codex[key]][t.get("rank") - 1] = t
        self.__standings["updated_at"] = datetime.today()
        self.save()
