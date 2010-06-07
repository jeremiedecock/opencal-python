# -*- coding: utf-8 -*-

# Copyright (c) 2010 Jérémie DECOCK (http://www.jdhp.org)

import time

class Controler:

    cardlist = []
    data = None

    author = "Jérémie Decock"

    def __init__(self, data):
        self.data = data

    def add(self, question, answer, tags, source):
        question = question[:-1].strip()
        answer = answer[:-1].strip()
        tags = tags[:-1].strip()
        author = self.author
        source = source[:-1].strip()
        creation_date = str(time.time())

        success = False

        # Don't do anything if question is empty
        if question != "":
            self.cardlist.append({'question': question,
                                  'answer': answer,
                                  'tags': tags,
                                  'author': author,
                                  'source': source,
                                  'creation_date': creation_date})
            self.save()
            success = True

        return success

    def save(self):
        self.data.export(self.cardlist)
