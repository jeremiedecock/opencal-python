#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenCAL version 3.0
# Copyright (c) 2007,2008,2010 Jérémie Decock (http://www.jdhp.org)

"""OpenCAL's main file."""

from Config import CARD_DATABASE
from Config import GUI
from Config import PKB_INTERFACE

if GUI == 'GTK':
	from GtkGUI import GUI
elif GUI == 'HILDON':
	from HildonGUI import GUI

if PKB_INTERFACE == 'minidom':
    from MinidomPKB import PKB

def main():
    pkb = PKB(CARD_DATABASE)
    domDocument = pkb.load()

    from Reviewer import ReviewList
    reviewList = ReviewList(domDocument)

    gui = GUI(reviewList)
    gui.main()

if __name__ == '__main__':
    main()
