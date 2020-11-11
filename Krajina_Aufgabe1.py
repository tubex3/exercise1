# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:51:03 2019

@author: Krajina
"""

#Berechnung größter gemeinsamer Teiler (greatest common divisor)
def gcd(a,b):
    while a != b:
           if a<b:
               a,b=b,a
           a=a-b
    return a

#Addition Brüche
def add_frac(z1,n1,z2,n2):
   #Fehlermeldung falls für ungeeignete Eingabe
   if type(z1)!= int or type(z2)!= int or type(n1)!= int or type(n2) != int:
       print("Bitte nur ganze Zahlen angeben!")
   if n1 is 0 or n2 is 0:
       print("Nenner darf nicht 0 sein!")
   
   else:
       #Brüche auf gleichen Nenner bringen
       new_n1=n1*n2
       new_z1=z1*n2
       new_n2=n2*n1
       new_z2=z2*n1
       #Addition der Brüche
       new_z=new_z1+new_z2
       new_n=new_n1
       #bestimmen größter gemeinsamer Nenner
       a=gcd(new_z,new_n)
       #Küzen Bruch
       new_z=int(new_z/a)
       new_n=int(new_n/a)
       print("Das Ergebnis lautet: ", new_z, "/", new_n)

