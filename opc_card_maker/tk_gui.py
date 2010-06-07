# -*- coding: utf-8 -*-

# Copyright (c) 2010 Jérémie DECOCK (http://www.jdhp.org)

import Tkinter as tk

class Gui:
    
    controler = None

    root = None
    question_text = None
    answer_text = None
    tags_text = None
    source_text = None

    def __init__(self, controler):
        self.controler = controler
        self.root = tk.Tk()

        # Menu
        root_menu = tk.Menu(self.root)

        file_menu = tk.Menu(root_menu, tearoff=0)
        root_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.root.quit)
        file_menu.add_command(label="Open...", command=self.root.quit)
        file_menu.add_command(label="Save As...", command=self.root.quit)
        file_menu.add_command(label="Save", command=self.root.quit)
        file_menu.add_command(label="Quit", command=self.root.quit)

        self.root.config(menu=root_menu)

        # Frame buttons
        frame = tk.Frame(self.root)
        add_frame_button = tk.Button(frame, text="Add", command=self.root.quit)
        add_frame_button.pack(side="left")
        edit_frame_button = tk.Button(frame, text="Edit", command=self.root.quit)
        edit_frame_button.pack(side="right")
        frame.pack()

        # Text widgets
        self.question_text = tk.Text(self.root, width=80, height=15)
        self.question_text.pack()

        self.answer_text = tk.Text(self.root, width=80, height=15)
        self.answer_text.pack()

        self.tags_text = tk.Text(self.root, width=80, height=3)
        self.tags_text.pack()

        self.source_text = tk.Text(self.root, width=80, height=2)
        self.source_text.pack()

        # TODO : le code suivant est très intéressant : on peut insérer
        #        n'importe quel widget dans le widget text (y compris
        #        des images !)
        #txt = tk.Text(self.root, width=40, height=15)
        #txt.pack()
        #txt.insert(tk.END, "Test du widget text")
        #button = tk.Button(txt, text="Quit", command=self.root.quit)
        #txt.window_create(tk.INSERT, window=button)
        #txt.insert(tk.END, "Blablablablablablabal Test du widget text")

        # Add button
        add_button = tk.Button(self.root,
                               text="Add",
                               command=self.add_callback)
        add_button.pack()

    def add_callback(self):
        question = self.question_text.get(1.0, tk.END)
        answer = self.answer_text.get(1.0, tk.END)
        tags = self.tags_text.get(1.0, tk.END)
        source = self.source_text.get(1.0, tk.END)

        success = self.controler.add(question, answer, tags, source)

        # Don't do anything if question is empty
        if success:
            self.question_text.delete(1.0, tk.END)
            self.answer_text.delete(1.0, tk.END)
            self.tags_text.delete(1.0, tk.END)
            self.source_text.delete(1.0, tk.END)

    def run(self):
        self.root.mainloop()

