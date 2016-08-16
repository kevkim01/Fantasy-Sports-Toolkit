from bs4 import BeautifulSoup
import urllib2, sys, re

FIRST_NAME = sys.argv[1]
LAST_NAME = sys.argv[2]
FULL_NAME = FIRST_NAME + " " + LAST_NAME

RAW_BASKETBALL_STATS_BASE_URL = "http://www.basketball-reference.com"
PLAYER_INDEX_URL = RAW_BASKETBALL_STATS_BASE_URL + "/players/" + LAST_NAME[0].lower()

html = urllib2.urlopen(PLAYER_INDEX_URL).read()

soup = BeautifulSoup(html, "html.parser")

ANCHOR_TAG_CONTENT = soup.findAll('a', href = True, text = FULL_NAME)
HREF_LINK = ANCHOR_TAG_CONTENT[0]["href"]

DESIRED_PLAYER_LINK = RAW_BASKETBALL_STATS_BASE_URL + HREF_LINK

DESIRED_PLAYER_LINK_HTML = urllib2.urlopen(DESIRED_PLAYER_LINK).read()
soup_water = BeautifulSoup(DESIRED_PLAYER_LINK_HTML, "html.parser")

def printText(tags):
        for tag in tags:
                if tag.__class__ == NavigableString:
                        print tag,
                else:
                        printText(tag)
        print ""
printText(soup_water.findAll("table"))
