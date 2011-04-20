'''
Creates a table of the frequencies of the letters in a ciphertext
including the most probable corresponding letter in the plaintext
using the frequency table from http://en.wikipedia.org/wiki/Letter_frequency.

@author: Willi Schoenborn
'''

import string
from string import join

class LetterFrequency(object):
    
    frequencies = {
        'A': 6.51,
        'B': 1.89,
        'C': 3.06,
        'D': 5.08,
        'E': 17.40,
        'F': 1.66,
        'G': 3.01,
        'H': 4.76,
        'I': 7.55,
        'J': 0.27,
        'K': 1.21,
        'L': 3.44,
        'M': 2.53,
        'N': 9.78,
        'O': 2.51,
        'P': 0.79,
        'Q': 0.02,
        'R': 7.00,
        'S': 7.27,
        'T': 6.15,
        'U': 4.35,
        'V': 0.67,
        'W': 1.89,
        'X': 0.03,
        'Y': 0.04,
        'Z': 1.13
    }

    def __init__(self, text, key):
        self.key = key
        self.letters = {}
        
        text = self.shift(text)
        for letter in string.ascii_uppercase:
            self.letters[letter] = float(text.count(letter)) / len(text) * 100
            
    def of(self, letter):
        return self.letters[letter];
        
    def shift(self, text):
        return join(map(lambda l: chr(((ord(l) - 65 + self.key) % 26) + 65), text), '')
        
    def deviation(self, letter):
        return abs(self.of(letter) - self.frequencies[letter])
        
    def average_deviation(self):
        return reduce(lambda d, l: d + self.deviation(l), string.ascii_uppercase, 0.0) / len(self.frequencies)
    
    def __str__(self):
        return join(["%s => %s" % (l, f) for l, f in self.letters.items()], '\n')
    