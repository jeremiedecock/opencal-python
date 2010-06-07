#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2010 Jérémie DECOCK (http://www.jdhp.org)

from data import Data
from controler import Controler
from tk_gui import Gui

def main():
    data = Data()
    controler = Controler(data)
    gui = Gui(controler)
    gui.run()

if __name__ == '__main__':
    main()
