#!/usr/bin/env python3
"""Defines the Team subclass."""
import json
import models
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Team:
    """Represents the roster and Twitter list for a given team.

    Attributes:
        name (str): The Team name.
        url (str): The URL of the Team's 40-man roster.
        handle (str): The Team Twitter handle.
        roster (dict): Key/value pairs of players/Twitter handles.
        list_id (str): The Team's Twitter list ID.
        embed (str): The embedded link for the Team's Twitter list.
        updated_at (datetime): The time of last update.
    """

    name = ""
    url = ""
    handle = ""
    roster = ""
    list_id = ""
    embed = ""
    updated_at = datetime

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
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
        except Exception:
            return

        updated = {}
        for t in soup.find_all("tbody"):
            for p in t.find_all("a"):
                if p.text in self.roster.keys():
                    updated[p.text] = self.roster[p.text]
                    continue
                try:
                    page = requests.get("{}{}".format(self.url[:-1], p["href"]))
                    soup = BeautifulSoup(page.text, "html.parser")
                    handle = soup.find("a", class_="twitter-follow-button")
                    handle = handle["href"].split("/")[-1]
                    updated[p.text] = "None" if handle == "mlb" else handle
                except Exception:
                    continue
        self.roster = updated

    def update_list(self, oauth):
        """Updates the Team Twitter list.

        Attributes:
            oauth (OAuth1Session): The Twitter user-auth session.
        """
        url = "https://api.twitter.com/1.1/lists/members.json"
        params = {
            "list_id": self.list_id,
            "count": 41
        }
        try:
            r = oauth.get(url, params=params).json()
        except Exception:
            return

        current_members = set()
        for u in r.get("users"):
            if u.get("screen_name").lower() != self.handle.lower():
                current_members.add(u.get("screen_name").lower())
        updated_members = set()
        for h in self.roster.values():
            if h != "None":
                updated_members.add(h[1:].lower())
        to_delete = current_members - updated_members
        to_add = updated_members - current_members

        if len(to_delete) > 0:
            url = "https://api.twitter.com/1.1/lists/members/destroy_all.json"
            params["screen_name"] = ",".join(to_delete)
            oauth.post(url, params=params)

        if len(to_add) > 0:
            url = "https://api.twitter.com/1.1/lists/members/create_all.json"
            params["screen_name"] = ",".join(to_add)
            oauth.post(url, params=params)
