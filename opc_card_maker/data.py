# -*- coding: utf-8 -*-

# Copyright (c) 2010 Jérémie DECOCK (http://www.jdhp.org)

class Data:
    
    path = '/home/decock/opc.cs'

    def __init__(self):
        pass

    def export(self, cardlist):
        file = open(self.path, 'w')

        file.write('<cardset>\n')

        for card in cardlist:
            question = card['question']
            answer = card['answer']
            tags = card['tags']
            author = card['author']
            source = card['source']
            creation_date = card['creation_date']

            file.write('<card>\n')
            file.write('<question>' + question + '</question>\n')
            if answer != "":
                file.write('<answer>' + answer + '</answer>\n')
            if tags != "":
                for tag in tags.splitlines():
                    file.write('<tag>' + tag + '</tag>\n')
            if author != "":
                file.write('<author>' + author + '</author>\n')
            if source != "":
                file.write('<source>' + source + '</source>\n')
            if creation_date != "":
                file.write('<creation_date>' + creation_date + '</creation_date>\n')
            file.write('</card>\n')

        file.write('</cardset>\n')

        file.close()

