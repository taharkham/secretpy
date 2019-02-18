#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash 
from secretpy import Caesar

from secretpy import CryptMachine 
from secretpy.cmdecorators import *

def encdec(machine, plaintext):
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)
	print("-----------------------------------")

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

cm = CryptMachine(cipher, key)
encdec(cm, plaintext)

cm.setAlphabet(alphabet)
encdec(cm, plaintext)

cm = SaveSpaces(cm)
cm.setKey(9)
plaintext  = u"the quick brown fox jumps over the lazy dog"
encdec(cm, plaintext)

cm = NoSpaces(UpperCase(cm))
cm.setCipher(Atbash())
plaintext  = u"Achtung Minen"
encdec(cm, plaintext)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
-----------------------------------
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqirämxpsvryhuwkhodüögrj
thequickbrownfoxjumpsoverthelazydog
-----------------------------------
the quick brown fox jumps over the lazy dog
üqn zßrlt käxbw oxc sßvyö xanä üqn ujed mxp
the quick brown fox jumps over the lazy dog
-----------------------------------
Achtung Minen
ßÖWKJQXRVQZQ
ACHTUNGMINEN
-----------------------------------
'''
