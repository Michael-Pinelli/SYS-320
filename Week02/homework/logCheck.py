import re, sys, yaml

try:

    with open ('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)

def _logs(filename, service, term):

    terms = keywords[service][term]

    listOfKeywords = terms.split(",")

    # Open a file
    with open(filename) as f:

        # Read the file
        contents = f.readlines()
    # Lists to store the results
    results = []

    # Loop through the list
    for line in contents:
    
         for eachKeyword in listOfKeywords:

            x = re.findall(r''+eachKeyword+'', line)

            for found in x:

                results.append(found)
    
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    results = sorted(results)

    results = set(results)

    return results
    #print(x)