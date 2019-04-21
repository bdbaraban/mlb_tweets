#!/usr/bin/env python3
"""Defines the Team class."""
import requests
from bs4 import BeautifulSoup


class Team:
    """Represents the Twitter handles of a 40-man MLB team roster.

    Attributes:
        __team_urls (dict): A dictionary of roster URL's for all 30 MLB teams.
    """

    __team_urls = {
        "Angels":       "http://m.angels.mlb.com/ana/roster/40-man/",
        "Astros":       "http://m.astros.mlb.com/hou/roster/40-man/",
        "Athletics":    "http://m.athletics.mlb.com/oak/roster/40-man/",
        "Blue Jays":    "http://m.bluejays.mlb.com/tor/roster/40-man/",
        "Braves":       "http://m.braves.mlb.com/atl/roster/40-man/",
        "Brewers":      "http://m.brewers.mlb.com/mil/roster/40-man/",
        "Cardinals":    "http://m.cardinals.mlb.com/stl/roster/40-man/",
        "Cubs":         "http://m.cubs.mlb.com/chc/roster/40-man/",
        "Diamondbacks": "http://m.dbacks.mlb.com/ari/roster/40-man/",
        "Dodgers":      "http://m.dodgers.mlb.com/la/roster/40-man/",
        "Giants":       "http://m.giants.mlb.com/sf/roster/40-man/",
        "Indians":      "http://m.indians.mlb.com/cle/roster/40-man/",
        "Mariners":     "http://m.mariners.mlb.com/sea/roster/40-man/",
        "Marlins":      "http://m.marlins.mlb.com/mia/roster/40-man/",
        "Mets":         "http://m.mets.mlb.com/nym/roster/40-man/",
        "Nationals":    "http://m.nationals.mlb.com/was/roster/40-man/",
        "Orioles":      "http://m.orioles.mlb.com/bal/roster/40-man/",
        "Padres":       "http://m.padres.mlb.com/sd/roster/40-man/",
        "Phillies":     "http://m.phillies.mlb.com/phi/roster/40-man/",
        "Pirates":      "http://m.pirates.mlb.com/pit/roster/40-man/",
        "Rangers":      "http://m.rangers.mlb.com/tex/roster/40-man/",
        "Rays":         "http://m.rays.mlb.com/tb/roster/40-man/",
        "Reds":         "http://m.reds.mlb.com/cin/roster/40-man/",
        "Red Sox":      "http://m.redsox.mlb.com/bos/roster/40-man/",
        "Rockies":      "http://m.rockies.mlb.com/col/roster/40-man/",
        "Royals":       "http://m.royals.mlb.com/kc/roster/40-man/",
        "Tigers":       "http://m.tigers.mlb.com/det/roster/40-man/",
        "Twins":        "http://m.twins.mlb.com/min/roster/40-man/",
        "White Sox":    "http://m.whitesox.mlb.com/cws/roster/40-man/",
        "Yankees":      "http://m.yankees.mlb.com/nyy/roster/40-man/"
    }

    def __init__(self, team):
        """Initializes a new Team.

        team (str): The MLB team name.
        """
        self.team_url = Team.__team_urls[team]
        self.scrape_roster()
        self.scrape_handles()

    def scrape_roster(self):
        """Scrapes the player URL pages of the team roster."""
        page = requests.get(self.team_url)
        soup = BeautifulSoup(page.text, "html.parser")
        self.roster = []
        for t in soup.find_all("tbody"):
            [self.roster.append(player["href"]) for player in t.find_all("a")]

    def scrape_handles(self):
        """Scrapes the player Twitter handles of the team roster."""
        self.handles = []
        for player in self.roster:
            player_url = "{}{}".format(self.team_url[:-1], player)
            page = requests.get(player_url)
            soup = BeautifulSoup(page.text, "html.parser")

            handle = soup.find("a", class_="twitter-follow-button")
            handle = handle["href"].split("/")[-1][1:]
            if handle != "lb":
                self.handles.append(handle)
