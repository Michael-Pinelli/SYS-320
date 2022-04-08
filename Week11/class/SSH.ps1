# Login to a remote SSH server
#New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential michael.pinelli)
<#
while ($True) {
    # Add a prompt to run commands
    $the_cmd = read-host -Prompt "Please enter a command"

    # Run command on remote SSH server
    (Invoke-SSHCommand -index 0 $the_cmd).Output
}
#>

Set-SCPitem -Computername '192.168.6.71' -Credential (Get-Credential michael.pinelli)
-Destination '/home/sys320' -Path '.\test.txt'