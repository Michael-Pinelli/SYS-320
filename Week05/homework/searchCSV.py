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
                        if attack == 'cred_collection':
                            attack_used = 'Registry Attack'
                            attack_description = """The Windows Registry stores configuration information that can be used by the system or other programs.
                        Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services.
                        Sometimes these credentials are used for automatic logons.Adversaries could also inject malicious DLLs into registry keys that are loaded after reboot.
                        When a user authenticates the DLLs have a routine that captures their credentials after login."""
                        elif attack == 'java_or_vbscript':
                            attack_used = 'Javascript or VBScript'
                            attack_description = """Adversaries may use scripts to aid in operations and perform multiple actions that would otherwise be manual.
                        Scripting is useful for speeding up operational tasks and reducing the time required to gain access to critical resources.
                        Some scripting languages may be used to bypass process monitoring mechanisms by directly interacting with the operating system at an API level instead of calling other programs.
                        Common scripting languages for Windows include VBScript and PowerShell but could also be in the form of command-line batch scripts."""
                        else:
                            attack_used = 'Powershell Execution'
                            attack_description = """PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.
                        Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code.
                        Examples include the Start-Process cmdlet which can be used to run an executable and the Invoke-Command cmdlet which runs a command locally or on a remote computer."""
                        
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