#!/usr/bin/env python3
"""Defines the League class to store Team instances."""
import json
from models.twitter_list import TwitterList

team_urls = {
    "Los Angeles Angels":    "http://m.angels.mlb.com/ana/roster/40-man/",
    "Houston Astros":        "http://m.astros.mlb.com/hou/roster/40-man/",
    "Oakland Athletics":     "http://m.athletics.mlb.com/oak/roster/40-man/",
    "Toronto Blue Jays":     "http://m.bluejays.mlb.com/tor/roster/40-man/",
    "Atlanta Braves":        "http://m.braves.mlb.com/atl/roster/40-man/",
    "Milwaukee Brewers":     "http://m.brewers.mlb.com/mil/roster/40-man/",
    "St. Louis Cardinals":   "http://m.cardinals.mlb.com/stl/roster/40-man/",
    "Chicago Cubs":          "http://m.cubs.mlb.com/chc/roster/40-man/",
    "Arizona Diamondbacks":  "http://m.dbacks.mlb.com/ari/roster/40-man/",
    "Los Angeles Dodgers":   "http://m.dodgers.mlb.com/la/roster/40-man/",
    "San Francisco Giants":  "http://m.giants.mlb.com/sf/roster/40-man/",
    "Cleveland Indians":     "http://m.indians.mlb.com/cle/roster/40-man/",
    "Seattle Mariners":      "http://m.mariners.mlb.com/sea/roster/40-man/",
    "Miami Marlins":         "http://m.marlins.mlb.com/mia/roster/40-man/",
    "New York Mets":         "http://m.mets.mlb.com/nym/roster/40-man/",
    "Washington Nationals":  "http://m.nationals.mlb.com/was/roster/40-man/",
    "Baltimore Orioles":     "http://m.orioles.mlb.com/bal/roster/40-man/",
    "San Diego Padres":      "http://m.padres.mlb.com/sd/roster/40-man/",
    "Philadelphia Phillies": "http://m.phillies.mlb.com/phi/roster/40-man/",
    "Pittsburgh Pirates":    "http://m.pirates.mlb.com/pit/roster/40-man/",
    "Texas Rangers":         "http://m.rangers.mlb.com/tex/roster/40-man/",
    "Tampa Bay Rays":        "http://m.rays.mlb.com/tb/roster/40-man/",
    "Cincinatti Reds":       "http://m.reds.mlb.com/cin/roster/40-man/",
    "Boston Red Sox":        "http://m.redsox.mlb.com/bos/roster/40-man/",
    "Colorado Rockies":      "http://m.rockies.mlb.com/col/roster/40-man/",
    "Kansas City Royals":    "http://m.royals.mlb.com/kc/roster/40-man/",
    "Detroit Tigers":        "http://m.tigers.mlb.com/det/roster/40-man/",
    "Minnesota Twins":       "http://m.twins.mlb.com/min/roster/40-man/",
    "Chicago White Sox":     "http://m.whitesox.mlb.com/cws/roster/40-man/",
    "New York Yankees":      "http://m.yankees.mlb.com/nyy/roster/40-man/"
}

team_routes = {
    "angels": "Los Angeles Angels",
    "astros": "Houston Astros",
    "athletics": "Oakland Athletics",
    "blue-jays": "Toronto Blue Jays",
    "braves": "Atlanta Braves",
    "brewers": "Milwaukee Brewers",
    "cardinals": "St. Louis Cardinals",
    "cubs": "Chicago Cubs",
    "diamondbacks": "Arizona Diamondbacks",
    "dodgers": "Los Angeles Dodgers",
    "giants": "San Francisco Giants",
    "indians": "Cleveland Indians",
    "mariners": "Seattle Mariners",
    "marlins": "Miami Marlins",
    "mets": "New York Mets",
    "nationals": "Washington Nationals",
    "orioles": "Baltimore Orioles",
    "padres": "San Diego Padres",
    "phillies": "Philadelphia Phillies",
    "pirates": "Pittsburgh Pirates",
    "rangers": "Texas Rangers",
    "rays": "Tampa Bay Rays",
    "reds": "Cincinatti Reds",
    "red-sox": "Boston Red Sox",
    "rockies": "Colorado Rockies",
    "royals": "Kansas City Royals",
    "tigers": "Detroit Tigers",
    "twins": "Minnesota Twins",
    "white-sox": "Chicago White Sox",
    "yankees": "New York Yankees"
}


class League:
    """Stores all 30 Team instances.
    
    Attributes:
        __file_path (str): The name of the file to save teams to.
        __teams (dict): A dictionary of instantiated teams.
    """

    __file_path = "league.json"
    __teams = {}

    def save(self):
        """Serialize __teams to the JSON file __file_path."""
        d = {t: self.__teams[t].to_dict() for t in self.__teams.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __teams, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for t in json.load(f).values():
                    self.__teams[t.get("name")] = TwitterList(**t)
        except FileNotFoundError:
            pass 
    
    def get(self, name):
        """Retrieves a given team."""
        return self.__teams.get(team_routes[name])
