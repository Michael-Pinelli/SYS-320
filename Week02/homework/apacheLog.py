import logCheck, yaml
import importlib
importlib.reload(logCheck)

def apache_events(filename, service, term):

    is_found = logCheck._logs(filename, service, term)

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + sp_results[7])

    getValues = set(found)

    for eachHost in getValues:
        
        print(eachHost)
        
        
def apache_export(filename, service, term, output):
    
    is_found = logCheck._logs(filename, service, term)

    found = []

    for eachFound in is_found:

        sp_results = eachFound.split(" ")

        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + sp_results[7])
    
    with open(output, 'w') as file:
        yaml.dump(found, file)