'''
an automated bruteforce attack on a shift cipher

@author: Willi Schoenborn
'''
from LetterFrequency import LetterFrequency
from string import upper

def main():
    
    text_file = open('../resources/hinter-den-wortbergen.txt', 'r')
    #text_file = open('../resources/theaterstueck-mit-g.txt', 'r')
    #text_file = open('../resources/geschichten-von-a-z.txt', 'r')
    #text_file = open('../resources/quark.txt', 'r')
    
    cipher_text = text_file.read()
    text_file.close()
    
    dictionary_file = open('../resources/ngerman', 'r')
    dictionary = set(upper(dictionary_file.read()).split("\n"))
    dictionary_file.close()
    
    frequencies = map(lambda key:LetterFrequency(cipher_text, key) , range(26))
    frequencies = sorted(frequencies, key=LetterFrequency.average_deviation)

    max_wordlength = 25
    length = len(cipher_text)
    limit = length * 1/3

    def find():
        for frequency in frequencies:
            text = frequency.shift(cipher_text)
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
        print best.shift(cipher_text)
        
if __name__ == '__main__':
    main()
