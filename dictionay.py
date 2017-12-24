import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
#help(difflib.SequenceMatcher)
import json

#SequenceMatcher(None,"rainnnnn","rain").ratio()

#get_close_matches("rainn",["pyramid", "sapanrain","rain"])


data = json.load(open("data.json"))

#data.keys()
#type(data.keys())

#get_close_matches("sapan",data.keys(),n = 5) #n indicates no of simmilar value
#get_close_matches("sapan",data.keys())[0] #first item has index zero
#get_close_matches("sapan",data.keys(), cutoff = 0.8) 
#type(data)
#print(data)

def dict(word):
    word = word.lower()
    
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "delhi" this will check for "Delhi" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn= input("Did you mean %s instead? Enter Y if yes or N for no:"  % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "please double check"
        else :
            return "world doesnt exist"
    else :
        return "bye"
  
word = str(input("search your word: "))

word = word.lower()


output = dict(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
 
#print (word) ,data[word] ######## without defining function
