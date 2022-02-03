#Added import for re
import csv, re
#Was ur1HausOpen changed 1 to l
def urlHausOpen(filename,searchTerm):
    #Changed formatting also changed while to with, csv.review to csv.reader
    with open(filename) as f:
        contents = csv.reader(f)
        for _ in range(9):
            next(contents)
        #Was searchTerms removed the s
        for keyword in searchTerm:
    
            for eachLine in contents:
                    #Fixed formatting
                    x = re.findall(r''+keyword+'', eachLine[2])

                    for _ in x:
        # Don't edit this line. It is here to show how it is possible
        # to remove the "tt" so programs don't convert the malicious
        # domains to links that an be accidentally clicked on.
                        the_url = eachLine[2].replace("http","hxxp")
                        the_src = eachLine[4]
                        print("""
                        URL:
                        Info: 
                        {}""".format(the_url, the_src, 60))
                         #Removed the * and made it just 60