#!/usr/bin/env python3
"""Defines the League class to store Team instances."""
import json
from datetime import datetime
from models.team import Team
from requests_oauthlib import OAuth1Session


class League:
    """Stores all 30 Team instances.

    Attributes:
        __teams (dict): A dictionary of instantiated teams.
    """

    __teams = {}

    def save(self):
        """Serialize __teams to the JSON file __file_path."""
        d = {t: self.__teams[t].to_dict() for t in self.__teams.keys()}
        with open("league.json", "w", encoding="utf-8") as f:
            json.dump(d, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __teams, if it exists."""
        try:
            with open("league.json", "r", encoding="utf-8") as f:
                self.__teams = {k: Team(**v) for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass

    def get(self, name):
        """Retrieves a given team."""
        return self.__teams.get(name)

    def update(self):
        """Updates the Twitter lists of all 30 teams."""
        with open("auth.json", "r", encoding="utf-8") as f:
            auth = json.load(f)
            client_key = auth.get("client_key")
            client_secret = auth.get("client_secret")
            resource_owner_key = auth.get("resource_owner_key")
            resource_owner_secret = auth.get("resource_owner_secret")
        oauth = OAuth1Session(client_key,
                              client_secret=client_secret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret)

        for team in self.__teams.values():
            team.update_roster()
            team.update_list(oauth)
            team.updated_at = datetime.today()
        self.save()
