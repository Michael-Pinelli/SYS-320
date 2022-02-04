#Added import for re
import csv, re
#Was ur1HausOpen changed 1 to l
def urlHausOpen(filename, searchTerm):
    #Changed formatting also changed while to with, csv.review to csv.reader, made read-only
    with open(filename, 'r') as f:
        contents = csv.reader(f)
        
        for _ in range(9):
            next(contents)
        #Changed first parameter to eachLine and second one to contents
        for eachLine in contents:
            #Changed first parameter to keyword and second one to searchTerm
            for keyword in searchTerm:
                    #Fixed formatting, changed keyword to searchTerm
                    x = re.findall(r''+keyword+'', eachLine[2])

                    for _ in x:
        # Don't edit this line. It is here to show how it is possible
        # to remove the "tt" so programs don't convert the malicious
        # domains to links that an be accidentally clicked on.
                        the_url = eachLine[2].replace("http","hxxp")
                        #Changed 6 to 7 for the non test data csv
                        the_src = eachLine[7]
                        print("""
                        URL:{}
                        Info:{}
                        ************************************************
                        """.format(the_url, the_src))
                        #Removed the "*"+60 and the {} on the format line, added {} after url and info