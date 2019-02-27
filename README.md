SecretPy
===========

[![Go to PyPi](https://badge.fury.io/py/secretpy.svg)](https://pypi.org/project/secretpy)
[![Go to PyPi](https://img.shields.io/pypi/pyversions/secretpy.svg)](https://pypi.org/project/secretpy)
[![Read the Docs](https://img.shields.io/readthedocs/secretpy.svg)](https://secretpy.readthedocs.io/en/latest)
[![](https://img.shields.io/github/license/tigertv/secretpy.svg)]()

***Download:***

https://pypi.org/project/secretpy

***Documentation:***

https://secretpy.readthedocs.io

***Source code & Development:***

https://github.com/tigertv/secretpy

Description
-----------

SecretPy is a cryptographic Python package. It uses the following classical cipher algorithms:

- ADFGX, ADFGVX
- Affine
- Atbash
- Autokey
- Beaufort 
- Bifid
- Caesar
- Keyword
- Simple Substitution
- Polybius
- Rot13, Rot5, Rot18, Rot47
- Trifid
- Vigenere
- Zigzag

Installation
------------

To install this library, you can use pip:

```bash
pip install secretpy
```

Alternatively, you can install the package using the repo's cloning and the make:

```bash
git clone https://github.com/tigertv/secretpy
cd secretpy
make install
```

Usage
-----

### Simple way

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar
from secretpy import alphabet

alphabet = alphabet.GERMAN
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

print('=====================================')

print(plaintext)
# use default english alphabet
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqirämxpsvryhuwkhodüögrj
thequickbrownfoxjumpsoverthelazydog
=====================================
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
'''
```

### CryptMachine

In the previous example, plaintext contains only letters existing in the alphabet and in the lower case without spaces.
To change the behaviour you can use CryptMachine and decorators(UpperCase, NoSpace, SaveCase and etc.):

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash 
from secretpy import Caesar

from secretpy import CryptMachine 
from secretpy.cmdecorators import *
from secretpy import alphabet

def encdec(machine, plaintext):
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)
	print("-----------------------------------")

plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

cm = CryptMachine(cipher, key)
encdec(cm, plaintext)

cm.set_alphabet(alphabet.GERMAN)
encdec(cm, plaintext)

cm = SaveSpaces(cm)
cm.set_key(9)
plaintext  = u"the quick brown fox jumps over the lazy dog"
encdec(cm, plaintext)

cm = NoSpaces(UpperCase(cm))
cm.set_cipher(Atbash())
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
```

### CompositeMachine

Combining several ciphers to get more complex cipher, you can use CompositeMachine:

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13
from secretpy import Caesar
from secretpy import CryptMachine
from secretpy import CompositeMachine
from secretpy.cmdecorators import *

def encdec(machine, plaintext):
	print("=======================================")
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)

key = 5
plaintext = u"Dog jumps four times and cat six times"
print(plaintext)

cm1 = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
enc = cm1.encrypt(plaintext)
print(enc)

cm2 = SaveSpaces(SaveCase(CryptMachine(Rot13())))
enc = cm2.encrypt(enc)
print(enc)

print("=======================================")

cm = CompositeMachine(cm1)
cm.add_machines(cm2)
enc = cm.encrypt(plaintext)
print(enc)

encdec(cm, plaintext)

cm.add_machines(cm1, cm2)
encdec(cm, plaintext)

'''
Output:

Dog jumps four times and cat six times
Itl ozrux ktzw ynrjx fsi hfy xnc ynrjx
Vgy bmehk xgmj laewk sfv usl kap laewk
=======================================
Vgy bmehk xgmj laewk sfv usl kap laewk
=======================================
Dog jumps four times and cat six times
Vgy bmehk xgmj laewk sfv usl kap laewk
Dog jumps four times and cat six times
=======================================
Dog jumps four times and cat six times
Nyq tewzc pyeb dswoc kxn mkd csh dswoc
Dog jumps four times and cat six times
'''
```

Maintainers
-----------

- [@tigertv](https://github.com/tigertv) (Max Vetrov)

