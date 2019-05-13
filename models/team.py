#!/usr/bin/env python3
"""Defines the base Team class."""
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Team:
    """Represents the Twitter handles of a 40-man MLB team roster."""

    def __init__(self, **kwargs):
        """Initialize a new Team.

        Args:
            **kwargs (any): Key/value pairs of attributes.
        """
        for key, value in kwargs.items():
            if key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

    def to_dict(self):
        """Return a dictionary representation of the Team instance."""
        d = self.__dict__.copy()
        d["updated_at"] = self.updated_at.isoformat()
        return d

    def update_roster(self):
        """Updates the Team roster."""
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        self.roster = {}
        for t in soup.find_all("tbody"):
            for player in t.find_all("a"):
                page = requests.get("{}{}".format(self.url[:-1], player["href"]))
                soup = BeautifulSoup(page.text, "html.parser")
                handle = soup.find("a", class_="twitter-follow-button")
                handle = handle["href"].split("/")[-1]
                self.roster[player.text] = "None" if handle == "mlb" else handle
