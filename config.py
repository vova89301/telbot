""" This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/."""
import pymysql


TOKEN = '5345687927:AAGH72AwcfWPRrYottvv3YRj6zuvcBtQW8c'
STARTMSG = "Hi, i am translator bot. I use google python and google API. To change lang use /choose"
CHOSEMSG = "Choose lang"
LANGUES = ['ru', 'de', 'en']
LANGDICT = {
    'ru': 'Russian',
    'de': 'Deutch',
    'en': 'English'
}



mydb = pymysql.connect(
    host="db4free.net",
    user="rootadmain",
    passwd="fuckfuck",
    database="youtubebase2"
)
