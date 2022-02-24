#Imports necessary libraries
#Added import for re
import csv, re, yaml
#Defines the function and adds variable that are able to be put in from another file
#Was ur1HausOpen changed 1 to l
def search(filename, attack):
    words = []
    with open ('searchTerms.yaml', 'r') as yf:
        contents = yaml.safe_load_all(yf)
    
        for word in contents:
            for key, value in word[attack].items():
                words.append(value)
    #Opens the file as read-only
    #Changed formatting also changed while to with, csv.review to csv.reader, made read-only
    with open(filename, 'r', encoding="UTF-8") as f:
        #Takes the contents of the file and adds them to the contents variable
        contents = csv.reader(f, delimiter = ',')
        #For loop to run through each piece of the contents variable
        for _ in range(6):
            next(contents)
        #For loop to run through each line of the file
        #Changed first parameter to eachLine and second one to contents
        for eachLine in contents:
            #For loop to run through each word we want to search for
            #Changed first parameter to keyword and second one to searchTerm
            for keyword in words:
                #Regex to scan the file for what we want
                #Fixed formatting, changed regex to ('\\'+keyword, eachLine[2])
                    x = re.findall(keyword, eachLine[1])
                    #Runs through what we found
                    for _ in x:
                        
                    # Don't edit this line. It is here to show how it is possible
                    # to remove the "tt" so programs don't convert the malicious
                    # domains to links that an be accidentally clicked on.
                        #Changed 6 to 7 for the non test data csv
                        arguments = eachLine[1]
                        hostname = eachLine[2]
                        name = eachLine[3]
                        path = eachLine[4]
                        pid = eachLine[5]
                        username = eachLine[6]
                        #Prints the info we want
                        print("""
                        Arguments:{}
                        Hostname:{}
                        Name:{}
                        Path:{}
                        PID:{}
                        Username:{}
                        Attack Used:{}
                        Attack Description:{}
                        ************************************************
                        """.format(arguments, hostname, name, path, pid, username, attack_used, attack_description))
                        #We use.format to setup the output to our liking
                        #Removed the "*"+60 and the {} on the format line, added {} after url and info