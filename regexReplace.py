import re

class RegexReplace(object):
    def __init__(self,regex,phrase):
        self.regex = regex
        self.phrase = phrase
        
    def findAndReplaceOccurences(self,lst):
        for val in lst:
            self.phrase = re.sub(self.regex,val,self.phrase,1)
        return self.phrase   