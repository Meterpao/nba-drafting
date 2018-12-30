from get_html import get_html
from bs4 import BeautifulSoup
from bs4 import Comment
from collections import namedtuple

TEAM_STATS_PAGE = "https://www.basketball-reference.com/leagues/NBA_2019.html#all_team-stats-base"
Team_Info = namedtuple('Team_Info', ['name', 'points', 'threes', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers'], verbose=False)

def calculate_team_rois():
	"""
		For each team, calculate the ROI - return on investment. For each team, calculate the number of 
		fantasy points they generate, and divide by the sum of the salaries of each player on the team.
	"""
	html = get_html(TEAM_STATS_PAGE)
	soup = BeautifulSoup(html, "html.parser")

	win_pct_dict = find_team_win_pct(soup)
	team_info_dict = scrape_team_info(soup)

	for team,wp in win_pct_dict.items():
		current_team_info = team_info_dict[team]
		current_team_fps = calc_team_fps(current_team_info)
		print("Team: %s \t Win Pct: %s \t Total FPS: %s" %(team, str(wp), str(current_team_fps)))

def find_team_win_pct(html_soup):
	"""
		Given the bsoup of the html page from the TEAM_STATS_PAGE, returns a dictionary
		of (team name, win %), (key, value) pairs
	"""
	html_soup_body = html_soup.body
	win_pct_dict = {}
	
	west_div = html_soup_body.find('div', id='all_confs_standings_W')
	east_div = html_soup_body.find('div', id='all_confs_standings_E')

	for div in [west_div, east_div]:
		table = div.find('table')
		table_body = table.find('tbody')
		
		for row in table_body.find_all('tr'):
			team_name_row = row.find('a')
			team_name = team_name_row.text
			win_loss_pct_row = row.find('td', attrs={'data-stat': 'win_loss_pct'})
			win_loss_pct = float(win_loss_pct_row.text)
			win_pct_dict[team_name] = win_loss_pct

	return win_pct_dict

def scrape_team_info(soup):
	"""
		Given the bsoup body of the html page from the TEAM_STATS_PAGE, returns a dictionary
		of (team name, total fps), (key, value) pairs
	"""
	team_stats_div = soup.find('div', id='all_team-stats-base')
	
	# table is hidden in a comment, need to extract the comment then turn the comment into 
	# a BS object
	comment = team_stats_div.find(string=lambda text:isinstance(text,Comment))
	newsoup = BeautifulSoup(comment, 'html.parser')
	table = newsoup.find('table')
	table_body = table.find('tbody')
	all_teams_info = {}

	for row in table_body.find_all('tr'):

		### below is hard-coded...
		team_name = row.find('td', attrs={'data-stat': 'team_name'}).text
		points = int(row.find('td', attrs={'data-stat': 'pts'}).text)
		threes = int(row.find('td', attrs={'data-stat': 'fg3'}).text)
		rebounds = int(row.find('td', attrs={'data-stat': 'trb'}).text)
		assists = int(row.find('td', attrs={'data-stat': 'ast'}).text)
		steals = int(row.find('td', attrs={'data-stat': 'stl'}).text)
		blocks = int(row.find('td', attrs={'data-stat': 'blk'}).text)
		turnovers = int(row.find('td', attrs={'data-stat': 'tov'}).text)
		# missing double-doubles
		# missing triple-doubles...
		
		team_info = Team_Info(team_name, points, threes, rebounds, assists, steals, blocks, turnovers)
		all_teams_info[team_name] = team_info

	return all_teams_info

def calc_team_fps(team_info_struct):
	"""
		Given a struct of team info (all stats besides double-doubles and triple-doubles), calculate
		said team's total fantasy points generated.
	"""
	points = 	team_info_struct.points * 1 
	+ team_info_struct.threes * 0.5
	+ team_info_struct.rebounds * 1.25
	+ team_info_struct.assists * 1.5
	+ team_info_struct.steals * 2
	+ team_info_struct.blocks * 2
	- team_info_struct.turnovers * 0.5

	return points 

calculate_team_rois()