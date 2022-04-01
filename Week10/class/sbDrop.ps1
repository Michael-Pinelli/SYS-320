<#
    Storyline: Dropper for our spambot that will save to a directory 
    and then execute it.
#>

$writeSbBot = @'

# Send an email using Powershell

$toSend = @('michael.pinelli@mymail.champlain.edu')

# Message body
$msg = "Hello"

while ($true) {

    foreach ($email in $toSend) {
        # Send the email
        write-host "Send-MailMessage -from 'michael.pinelli@mymail.champlain.edu' -To 'michael.pinelli@mymail.champlain.edu' -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"

        # Pause for 1 second
        start-sleep 1

    }
}
'@

# Directory to write the bot
$sbDir = 'C:\Users\mikep\Documents\SYS-320\Week10\class\'

# Create a random number to add to the file

$sbRand = Get-random -Minimum 1000 -Maximum 1999

# Create the file and location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file
$writeSbBot | out-file -Filepath $file

# Executes the PowerShell script
#Invoke-Expression $file