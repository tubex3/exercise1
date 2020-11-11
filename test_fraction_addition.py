# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20::43 2020

@author: Toni Krajina
"""

from Krajina_Aufgabe1 import gcd
from Krajina_Aufgabe1 import add_frac

def test_gcd():
    assert gcd(10,5) == 5

 
def test_add_frac():
    assert add_frac(4,2,8,2) == print("Das Ergebnis lautet: ", 6, "/", 1)
    
    
