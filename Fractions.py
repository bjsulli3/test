# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:36:41 2020

@author: bjsul
"""

def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
            
        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    
    def __init__(self, top, bottom):
        
        self.num = top
        self.den = bottom
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
        
    def __add__(self, otherfraction):
        
        newnum = self.num*otherfraction.den + otherfraction.num*self.den
        newden = self.den*otherfraction.den
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)

    def __sub__(self, otherfractionSub):
        
        newnumS = self.num*otherfractionSub.den - otherfractionSub.num*self.den
        newdenS = self.den*otherfractionSub.den
        commonS = gcd(newnumS, newdenS)
        
        return Fraction(newnumS//commonS, newdenS//commonS)
    
    def __mul__(self, otherfractionMult):
        
        newnumM = self.num*otherfractionMult.num
        newdenM = self.den*otherfractionMult.den
        commonM = gcd(newnumM, newdenM)

        return(newnumM//commonM, newdenM//commonM)

    def __div__(self, otherfractionDiv):
        
        newnumD = self.num*otherfractionDiv.den
        newdenD = self.den*otherfractionDiv.num
        commonD = gcd(newnumD, newdenD)
        
        return(newnumD//commonD, newdenD//commonD)

    def __eq__(self, other):
       
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        
        return firstnum == secondnum
    
    def __lt__(self, otherLt):
        
        firstfrac = self.num/self.den
        secondfrac = otherLt.num/otherLt.den
        
        return firstfrac < secondfrac
    
    def __gt__(self, otherGt):
        
        firstfracGt = self.num/self.den
        secondfracGt = otherGt.num/otherGt.den

        return firstfracGt > secondfracGt
    
    def __le__(self, otherLe):
        
        firstfracLe = self.num/self.den
        secondfracLe = otherLe.num/otherLe.den
        
        return firstfracLe <= secondfracLe
    
    def __ge__(self, otherGe):
        
        firstfracGe = self.num/self.den
        secondfracGe = otherGe.num/otherGe.den
        
        return firstfracGe >= secondfracGe
    
    def numer(self):
        return self.num
    
    def denom(self):
        return self.den
    
    def cd(self):
        
        commonCd = gcd(self.num, self.den)
        
        return Fraction(self.num//commonCd, self.den//commonCd)

myFrac = Fraction(3, 5)  
mySecondFrac = Fraction(2, 4)
myThirdFrac = Fraction(4, 8)




