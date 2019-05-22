import json
from models.league import League
from models.standings import Standings

league = League()
league.reload()
standings = Standings()
standings.reload()
