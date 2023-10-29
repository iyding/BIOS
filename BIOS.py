from selenium.webdriver.common.by import By
import time
import numpy as np
class Roster:
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link
        self.driver.get(self.link)
        time.sleep(0.5)
        links = driver.find_elements("tag name", "a")
        roster_links = [link.get_attribute("href") for link in links if link.get_attribute("href") != None and link.get_attribute("href").split("/")[-1] == "roster"]
        self.roster_links = roster_links


class Player:
    def __init__(self, name, height, year, highschool, hometown, weight):
        self.name = name
        self.year = year
        self.hometown = hometown
        self.highschool = highschool
        self.height = height
        self.weight = weight
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Team:
    def __init__(self, roster_link, driver):
        self.roster_link = roster_link
        self.players = []
        self.team_name = roster_link.split("/")[-1]
        self.driver = driver
    def scrape(self):
        self.driver.get(self.roster_link)
        time.sleep(0.5)
        people = self.driver.find_element(By.CLASS_NAME, "sidearm-roster-players")
        people_links = people.find_elements("tag name", "a")
        people_href = [people.get_attribute("href") for people in people_links if
                       people.get_attribute("href") is not None]
        people_href_filtered = [people for people in people_href if
                                people != 'https://yalebulldogs.com/sports/womens-basketball/roster#']
        people_href_dist = list(set(people_href_filtered))
        for people in people_href_dist:
            self.driver.get(people)
            time.sleep(0.5)
            header = self.driver.find_elements("tag name", "header")[1]
            names = header.find_elements("tag name", "span")
            name_text = [name.text for name in names]
            name = " ".join(name_text[-2:])
            li = header.find_element("tag name", "ul").find_elements("tag name", "li")
            val_dict = {}
            val_dict["Name"] = name
            for element in li:
                cat = element.find_element("tag name", "dt").text
                val = element.find_element("tag name", "dd").text
                if cat == "Height":
                    nums = val.split("-")
                    nums = [int(num) for num in nums]
                    feet = 12 * nums[0]
                    val = feet + nums[1]
                val_dict[cat] = val
            if "Weight" not in val_dict:
                val_dict["Weight"] = np.NaN
            player = Player(name = val_dict["Name"], weight = val_dict["Weight"], year = val_dict["Class"],
                            highschool= val_dict["Highschool"], hometown = val_dict["Hometown"], height = val_dict["Height"])
            self.players.append(player)

