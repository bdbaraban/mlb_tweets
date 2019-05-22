<h1 align="center">MLB Tweets :baseball:</h1>
<p align="center">
  An MLB Twitter lists website featuring Twitter lists for all 30 MLB teams.
</p>

<p align="center">
  <img src="https://github.com/bdbaraban/twenty_timer/blob/master/screenshots/home.png"
   alt="Home screen screenshot"
  />
</p>

## Description :speech_balloon:

MLB Tweets runs on a Python Flask app serving HTML static content using Jinja2.

### Back-End :electric_plug:

* [mlbtweets.py](./mlbtweets.py): Entry point of the Flask app.
* [models/team.py](./models/team.py): Class representing an MLB Team:
  * `name`: Team name
  * `url`: URL of team's active 40-main roster (on [mlb.com](./mlb.com))
  * `handle`: Team's official Twitter handle.
  * `roster`: Key/value pairs of team player names/Twitter handles.
  * `list_id`: Team's Twitter list ID (owned by yours truly).
  * `embed`: URL of team's Twitter list to embed in HTML.
  * `updated_at`: Time of team's last roster update.
* [models/league.py](./models/league.py): Class to store all Team instances:
  * `__teams`: Key/value pairs of Team names/Team instances.
* [models/standings.py](./models/standings.py): Class to represent league standings. (Temporary - planned phase-out, will soon be converting to handling standings dynamically using jQuery)
  * `__standings`: Key/value pairs of MLB divisions/ordered list of team standings.

## Front-End :high_brightness:

* [static/templates/home.html](./static/templates/home.html): HTML for home page.
* [static/templates/about.html](./static/templates/about.html): HTML for about page.
* [static/templates/home.html](./static/templates/home.html): Generic HTML template for a team page.
* [static/styles](./static/styles): Folder of CSS3 styling.
* [static/scripts/scrollbar.js](./static/scripts/scrollbar.js): Sidebar scrolling.

## Development :computer:

MLB Tweets is a work-in-progress - more to come soon!
* Dynamic handling of standings updates on front-end using jQuery.
* Design improvements.
* Deployment.

## Author :black_nib:

* __Brennan D Baraban__ <[bdbaraban](https://github.com/bdbaraban)>

## License :lock:

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.