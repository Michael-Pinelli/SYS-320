import re, sys

def _syslog(filename,listOfKeywords):

    # Open a file
    with open('../../logs/smallSyslog.log') as f:

        # Read the file
        contents = f.readlines()
    # Lists to store the results
    results = []

    # Loop through the list
    for line in contents:
    
         for eachKeyword in listOfKeywords:

            x = re.findall(r''+eachKeyword+'', line)

            for found in x:

                results.append(x)
    
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    results = sorted(results)

    results = set(results)

    print(results)
    return results
            #print(x)