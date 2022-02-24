import re, sys, yaml

def _logs(filename, service):
    words = []
    with open ('searchTerms.yaml', 'r') as yf:
        contents = yaml.safe_load_all(yf)
    
        for line in contents:
            for key, value in line[service].items():
                words.append(value)
                
    # Open a file
    with open(filename) as f:

        # Read the file
        file = f.readlines()
    print(file)
    # Lists to store the results
    results = []

    # Loop through the list
    for line in file:
    
        for eachKeyword in words:

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