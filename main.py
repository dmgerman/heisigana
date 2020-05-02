#!/usr/bin/python
# coding: utf8
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import importlib
import sys

from anki.hooks import addHook

from heisigana import config, jpParser

conf = config.Config()

#ANKI SPECIFIC
def add_heisigana(selectedNotes):

    mw.checkpoint("Heisigana Definitions")
    mw.progress.start()
    destField = conf.heisiganaDstField
    for currentSelectedNote in selectedNotes:
        note = mw.col.getNote(currentSelectedNote)
        # skip if it does not have the destination field
        if not destField in note:
            continue

        # find the first field in the source fields
        # and then use it... the break will guarantee
        # we only do it once..
        # ugly... in wonder how to do it better...
        # map/filter/take(1)

        for f in conf.heisiganaSrcFields:
            if not f in note:
                continue;

            srcTxt = mw.col.media.strip(note[f])
            if len(srcTxt) == 0:
                continue;

            #we will do this only once

            current = note[destField]

            # if not empty, do only if overwrite
            # otherwise skip note
            if len(current) > 0 and (not conf.overwrite):
                break

            h = jpParser.do_heisigana(srcTxt)

            if h != current:
                note[destField] =h
                note.flush()

            break

    mw.progress.finish()
    mw.reset()

def setupMenu(browser):
    action = QAction("Bulk Add Heisigana", browser)
    action.triggered.connect(lambda: add_heisigana(browser.selectedNotes()))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(action)
    browser.form.menuEdit.addSeparator()

addHook("browser.setupMenus", setupMenu)
