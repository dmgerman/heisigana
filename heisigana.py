# coding: utf8
import re, os
from . import jpParser
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

#parserObj = parser.Parser()
source_directory = os.path.join(os.path.dirname(__file__),'data')

def extractKanjiFromElement(org):
    regex = ".*?【(.*?)】"
    matchObj = re.match(regex, org)
    if matchObj == None:
        return None
    else:
        returnValue = matchObj.group(1)

    #If more than one kanji, ex(内・家) for うち
    #return an array of kanji, It seems like the "・" character doesnt work with regex?
    #Currently only handles two different words, like うち -> 家 and 内 works
    matchObj = re.search("・", returnValue)
    if matchObj != None: #Multiple kanji found
        matchObj = re.match("(.*?)・(.*?) ", returnValue+" ")
        if matchObj != None:
            returnValue = []
            returnValue.append(matchObj.group(1))
            returnValue.append(matchObj.group(2))
    return returnValue
