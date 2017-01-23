"""Use for getting username from userid"""
import copy
import re

import requests
from bs4 import BeautifulSoup

try:  # Try to import a UID_MAP, if one does not exist then simply set to default of empty
    from UidMap import UID_MAP
except ImportError:
    UID_MAP = {}
try:  # Try to import a NAME_MAP, if one does not exist then simply set to default of empty
    from UidMap import NAME_MAP
except ImportError:
    NAME_MAP = {}


# helper function to extract a uid when in the format uid@facebook.com (or whenever uid is just the starting numbers)
def extract_uid(string):
    return re.search("[0-9]+", string).group(0)


class UsernameFinder:
    def __init__(self):
        # dictionary from uid to username, some id's have to be initialized
        self.uid_to_name = copy.copy(UID_MAP)
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


finder = UsernameFinder()
nickname_to_name = {}
for real_name, nicknames in NAME_MAP.items():
    for nickname in nicknames:
        nickname_to_name[nickname] = real_name


# gets the username for a string
def get_username(string):
    name = finder.get_username(extract_uid(string)) if "@facebook" in string else string
    if name in nickname_to_name:
        return nickname_to_name[name]
    return name
