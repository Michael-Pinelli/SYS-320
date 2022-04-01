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