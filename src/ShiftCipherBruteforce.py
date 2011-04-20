'''
an automated bruteforce attack on a shift cipher

@author: Willi Schoenborn
'''
from LetterFrequency import LetterFrequency
from string import upper
import sys

def main():
    
    if len(sys.argv) is 1:
        filename = '../resources/hinter-den-wortbergen.txt'
    else:
        filename = sys.argv[1]
    
    textfile = open(filename, 'r')

    ciphertext = textfile.read()
    textfile.close()
    
    dictionaryfile = open('../resources/ngerman', 'r')
    dictionary = set(upper(dictionaryfile.read()).split("\n"))
    dictionaryfile.close()
    
    frequencies = map(lambda key:LetterFrequency(ciphertext, key) , range(26))
    frequencies = sorted(frequencies, key=LetterFrequency.average_deviation)

    max_wordlength = 25
    length = len(ciphertext)
    limit = length * 1/3

    def find():
        for frequency in frequencies:
            text = frequency.shift(ciphertext)
            limit = length * 1/3
            
            words = []
            letters = 0
            start = 0
            end = 1
            while start < length:
                word = text[start:end]
                if word in dictionary:
                    words.append(word)
                    letters += len(word)
                    
                    if letters > limit:
                        return frequency
                    
                    start = end
                    
                end += 1 
                    
                if end > length or end - start > max_wordlength:
                    start += 1
                    end = start + 1
        
        return None
    
    best = find()

    if best is None:
        print "Nothing found"
    else:
        print "Encryption key is %s" % best.key
        print best.shift(ciphertext)
        
if __name__ == '__main__':
    main()
