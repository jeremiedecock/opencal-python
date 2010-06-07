# -*- coding: utf-8 -*-

# OpenCAL version 3.0
# Copyright (c) 2010 Jérémie Decock (http://www.jdhp.org)

import xml.dom.minidom

class PKB:

    uri = None

    def __init__(self, uri):
        self.uri = uri

    def load(self):
        cardDatabaseFile = open(self.uri, 'rU')
        domDocument = xml.dom.minidom.parse(cardDatabaseFile)
        cardDatabaseFile.close() 

        return domDocument

    def save(self):
        pass
