# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:10:59 2020

@author: Lenovo
"""

import unittest
import cfg
import os
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from DesktopPet import DesktopPet

class DesktopPetTestCase(unittest.TestCase):
    """Test for DesktopPet class"""
    def test_LoadPetImages(self):
        """Test whether the corresponding pet path imported is correct, take pet 39 as an example"""
        iconpath = os.path.join(cfg.ROOT_DIR, 'pet_39', 'shime1.png')
        file = open(r'D:/python_test/a.txt','r') 
        content = file.read()
        self.assertEquals(iconpath, content)
        
unittest.main()