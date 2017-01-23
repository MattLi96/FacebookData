"""Use for getting username from userid"""
import re

import requests
from bs4 import BeautifulSoup


# helper function to extract a uid when in the format uid@facebook.com (or whenever uid is just the starting numbers)
def extract_uid(string):
    return re.search("[0-9]+", string).group(0)


class UsernameFinder:
    def __init__(self):
        # dictionary from uid to username, some id's have to be initialized
        self.uid_to_name = {

        }
        self.unknown = set()  # uid we weren't able to get a username for

    # get the username from uid
    def get_username(self, uid):
        if uid in self.uid_to_name:  # check if we already know it
            return self.uid_to_name[uid]

        res = requests.get("https://www.facebook.com/" + uid)
        soup = BeautifulSoup(res.text, 'html.parser')
        name_element = soup.find(id="fb-timeline-cover-name")
        if name_element is None:  # unable to find a name
            name = uid
            self.unknown.add(uid)
        else:
            name = name_element.contents[0].strip()
        self.uid_to_name[uid] = name
        return name
