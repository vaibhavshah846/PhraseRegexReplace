# PhraseRegexReplace
Replace multiple occurences of a regular expression with different values provided in a list 

Usage:
Initialize:
regexRep = RegexReplace(regular expression to replace,phrase or sentence in which it needs to be replaced)

Replace:
regexRep.findAndReplaceOccurences(['laundry','Pune'])

Returns:
The resulting sentence with occurences of the Regular Expression replaced with the values in the list.

Eg:
from regexReplace import RegexReplace
sent = 'Our {main_service} is best in {location}'
regexRep = RegexReplace('{[^}]*}',sent)
regexRep.findAndReplaceOccurences(['laundry','Pune'])

Output:
'Our laundry is best in Pune'

Note:
This is just an basic version of one a problem I faced while working on a product.
It allows us to replace multiple occurences of a given regular expression in a sentence,phrase,text or a given string with multiple different values specified in a list.
Further development will continue as I explore more possibilities with it.
Suggestions are welcome.
