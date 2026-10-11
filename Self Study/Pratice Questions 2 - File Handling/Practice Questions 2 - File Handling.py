import csv
import json
import random

# file data for filestats
# File	   Lines  Words	Characters
# story.txt	20	   160	 917
# notes.txt	22	   85	 517



# Q1 : Count lines, words, and characters in a text file (like the Unix wc command).
# file_stats("story.txt")   # {'lines': 12, 'words': 240, 'chars': 1380}

def filestats(file) :
    with open(file) as f : # with open assure that even if a line of code causes an error the file still closes.
        count = 0
        words = 0
        charas = 0
        for line in f :
            count= count+1 # counts # of lines 
            words = words + len(line.split()) # counts the number of words 
            charas = charas + len(line)
        print(f"There are {count} lines, {words} words and {charas} characters")

#Q2)
def filterlogs(logfile): #filter out all ERRORS from a logfile and add them to a new file error.log
    with open(logfile) as readfile, open("error.log","w") as errorfile: 
        for line in readfile: 
            checkline= line.split()
            if len(checkline) >= 3 and checkline[2] == "ERROR" :
                errorfile.write(line)
    
    with open("error.log","r") as errorfile:
        print(errorfile.read())
            
#Q3)
def most_common_word(article) : # find the most common word in the file 
    dict = {}
    with open(article) as f :
        for line in f: 
            for word in line.split() :
                dict[word] = dict.get(word,0) +1 
        print(max(dict, key=dict.get) ) #<- lowkey smurfed! this grabs the key (in this case the word) associated to the highest value in the dictionary 

#Q4)
def avg_grade(csvfile) : #compute avg grade from csb info 
    with open(csvfile) as f : 
        divisor = 0 
        total = 0 
        reader = csv.DictReader(f) #DictReader uses the first line as column names (name, grade) and skips it automatically, so you access fields by name instead of position. That’s usually more readable. 
        for row in reader: 
           divisor = divisor +1  
           total = total+ int(row["grade"])
        
    print(total/divisor)
        
#Q5) edit JSON file within python and update it
def editJSON(jsonfile) : #just want to open and edit a file, also going to print calls to show certain json functions.
    with open(jsonfile, "r") as f : 
        info = json.load(f)
    print(info["store"]) #print to show access
    print(info["employees"][1]["id"])

    info["employees"][1]["id"] = random.randrange(100,150)
        
    with open(jsonfile, "w") as f :
        json.dump(info,f, indent = 2) # here indent just specifies how many white spaces are used as the indent for nested levels

    print(info["employees"][1]["id"])




# TESTS
#filestats("story.txt")
#filestats("notes.txt")

#filterlogs("firewall.log")
#filterlogs("server.log")

#most_common_word("article.txt")

#avg_grade("grades.csv")

#editJSON("practicedata.json")