#!/usr/bin/env python3
"""Defines the Twitter List subclass of the base Team class."""
import base64
import os
import requests
from models.team import Team

lists = {
    "Los Angeles Angels":    "https://twitter.com/bdov_/lists/mlbt-angels",
    "Houston Astros":        "https://twitter.com/bdov_/lists/mlbt-astros",
    "Oakland Athletics":     "https://twitter.com/bdov_/lists/mlbt-athletics",
    "Toronto Blue Jays":     "https://twitter.com/bdov_/lists/mlbt-blue-jays",
    "Atlanta Braves":        "https://twitter.com/bdov_/lists/mlbt-braves",
    "Milwaukee Brewers":     "https://twitter.com/bdov_/lists/mlbt-brewers",
    "St. Louis Cardinals":   "https://twitter.com/bdov_/lists/mlbt-cardinals",
    "Chicago Cubs":          "https://twitter.com/bdov_/lists/mlbt-cubs",
    "Arizona Diamondbacks":  "https://twitter.com/bdov_/lists/mlbt-diamondbacks",
    "Los Angeles Dodgers":   "https://twitter.com/bdov_/lists/mlbt-dodgers",
    "San Francisco Giants":  "https://twitter.com/bdov_/lists/mlbt-giants",
    "Cleveland Indians":     "https://twitter.com/bdov_/lists/mlbt-indians",
    "Seattle Mariners":      "https://twitter.com/bdov_/lists/mlbt-mariners",
    "Miami Marlins":         "https://twitter.com/bdov_/lists/mlbt-marlins",
    "New York Mets":         "https://twitter.com/bdov_/lists/mlbt-mets",
    "Washington Nationals":  "https://twitter.com/bdov_/lists/mlbt-nationals",
    "Baltimore Orioles":     "https://twitter.com/bdov_/lists/mlbt-orioles",
    "San Diego Padres":      "https://twitter.com/bdov_/lists/mlbt-padres",
    "Philadelphia Phillies": "https://twitter.com/bdov_/lists/mlbt-phillies",
    "Pittsburgh Pirates":    "https://twitter.com/bdov_/lists/mlbt-pirates",
    "Texas Rangers":         "https://twitter.com/bdov_/lists/mlbt-rangers",
    "Tampa Bay Rays":        "https://twitter.com/bdov_/lists/mlbt-rays",
    "Cincinatti Reds":       "https://twitter.com/bdov_/lists/mlbt-reds",
    "Boston Red Sox":        "https://twitter.com/bdov_/lists/mlbt-red-sox",
    "Colorado Rockies":      "https://twitter.com/bdov_/lists/mlbt-rockies",
    "Kansas City Royals":    "https://twitter.com/bdov_/lists/mlbt-royals",
    "Detroit Tigers":        "https://twitter.com/bdov_/lists/mlbt-tigers",
    "Minnesota Twins":       "https://twitter.com/bdov_/lists/mlbt-twins",
    "Chicago White Sox":     "https://twitter.com/bdov_/lists/mlbt-white-sox",
    "New York Yankees":      "https://twitter.com/bdov_/lists/mlbt-yankees"
}

def get_bearer():
    """Get a bearer token for interacting with the Twitter API."""
    filename = "tokens.txt"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, "r", encoding="utf-8") as file:
        key = file.readline()
        secret = file.readline()

    url = "https://api.twitter.com/oauth2/token"
    token = "{}:{}".format(key, secret).encode("ascii")
    token = base64.b64encode(token).decode("utf-8")
    headers = {
        "Authorization": "Basic {}".format(token),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    payload = {"grant_type": "client_credentials"}
    r = requests.post(url, headers=headers, data=payload)
    return r.json().get("access_token")


#bearer = get_bearer()


class TwitterList(Team):
    """Represents the Twitter list for a given team."""

    def get_members(self):
        """Gets the members of the given Team list."""
        url = "https://api.twitter.com/1.1/lists/members.json"
        params = {
            "list_id": self.list_id,
        }
        self.members = requests.get(url, params=params).json()
        self.members = {u.get("screen_name") for u in self.members.get("users")}
        self.current = {handle[1:] for handle in self.roster.values()}

    def update_list(self):
        """Updates the Team Twitter list."""
        to_delete = self.members ^ current
        to_add = current ^ self.members

        url = "https://api.twitter.com/1.1/lists/members/destroy_all.json"
        params = {
            "list_id": self.list_id,
            "screen_name": ",".join(to_delete)
            }
        requests.post(url, params=params)

        url = "https://api.twitter.com/1.1/lists/members/create_all.json"
        params["screen_name"] = ",".join(to_add)
        requests.post(url, params=params)