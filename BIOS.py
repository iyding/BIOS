from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
import time

path = '/Users/thompsonblade/Documents/Chromedriver/chromedriver'

driver = webdriver.Chrome()

class Roster:
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link
        self.driver.get(self.link)
        time.sleep(0.5)
        links = driver.find_elements("tag name", "a")
        roster_links = [link.get_attribute("href") for link in links if link.get_attribute("href") != None and link.get_attribute("href").split("/")[-1] == "roster"]
        self.roster_links = roster_links



yale_roster = Roster(driver, "https://yalebulldogs.com/")
print(yale_roster.roster_links)

class Player:
    def __init__(self, name, height, year, highschool, hometown):
        self.name = name
        self.year = year
        self.hometown = hometown
        self.highschool = highschool
        self.height = height
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Team:
    def __init__(self, roster_link):
        self.roster_link = roster_link
        self.players = []
        self.team_name = roster_link.split("/")[-1]

    def scrape(self):
        driver.get(self.roster_link)
        time.sleep(0.5)
        people = driver.find_element(By.CLASS_NAME, "sidearm-roster-players")
        people_links = people.find_elements("tag name", "a")
        people_href = [people.get_attribute("href") for people in people_links if people.get_attribute("href") != None]
        for people in people_href:
            driver.get(people)
            time.sleep(1)
            name = driver.find_element(By.CLASS_NAME, "sidearm-roster-player-first-name").text + " " + driver.find_element(By.CLASS_NAME, "sidearm-roster-player-last-name").text
            info = driver.find_element(By.CLASS_NAME,"flex flex-item-1 row flex-wrap")
            vals = info.find_elements("tag name","dd")
            info_str = [val.text for val in vals]
            player = Player(name, info_str[0], info_str[1], info_str[2], info_str[3])
            self.players.append(player)

wbb = Team("https://yalebulldogs.com/sports/womens-basketball/roster")

wbb.scrape()

print(wbb.team_name)

print(wbb.players)

