$var = Read-host -Prompt "Please enter Windows or IPTables"

switch ( $var )
{
    0 { $result = 1 }
    1 { $result = 2 }
}

if ( $result = 2 ) {
    # Array of websites containing threat intell
    $drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

    # Loop through the URLs for the rules list
    foreach ($u in $drop_urls) {

        # Extract the filename
        $temp = $u.split("/")
        $file_name = $temp[-1]

        if (Test-Path $file_name) {

            continue
        } else {
            # Download the rules list
        Invoke-WebRequest -Uri $u -OutFile $file_name
        }
    }
    # Array containing the filename
    $input_paths = @('.\compromised-ips.txt','.\emerging-botcc.rules')

    # Extract the IP addresses
    $regex_drop = '\b\d{1,3\.\d{1,3\.\d{1,3\.\d{1,3\b'

    # Append the IP addresses to the temporary IP list
    select-string -Path $input_paths -Pattern $regex_drop | `
    ForEach-Object { $_.Matches } | `
    ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
    Out-File -FilePath "ips-bad.tmp"

    # Get the IP addresses discovered, loop through and replace the beginnign of the line with the IPTables syntax
    # After the IP address, add the remailing IPTables syntax and save the results to a file
    (Get-Content -Path ".\ips-bad.tmp") | % `
    { $_ -replace "^","iptables -A INPUT -s " -replace "$", " -j DROP" } | `
    Out-File -FilePath "iptables.bash"
} else {
    # Array of websites containing threat intell
    $drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

    # Loop through the URLs for the rules list
    foreach ($u in $drop_urls) {

        # Extract the filename
        $temp = $u.split("/")
        $file_name = $temp[-1]

        if (Test-Path $file_name) {

            continue
        } else {
            # Download the rules list
        Invoke-WebRequest -Uri $u -OutFile $file_name
        }
    }
    # Array containing the filename
    $input_paths = @('.\compromised-ips.txt','.\emerging-botcc.rules')

    # Extract the IP addresses
    $regex_drop = '\b\d{1,3\.\d{1,3\.\d{1,3\.\d{1,3\b'

    # Append the IP addresses to the temporary IP list
    select-string -Path $input_paths -Pattern $regex_drop | `
    ForEach-Object { $_.Matches } | `
    ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
    Out-File -FilePath "ips-bad.tmp"

    # Get the IP addresses discovered, loop through and replace the beginnign of the line with the IPTables syntax
    # After the IP address, add the remailing IPTables syntax and save the results to a file
    (Get-Content -Path ".\ips-bad.tmp") | % `
    { $_ -replace "^","New-NetFirewallRule -DisplayName 'BLOCK IP ADDRESS - '" -replace "$", " -Direction inbound -Profile Any -Action Block -RemoteAddress " -replace "$" } #| `
    Out-File -FilePath "iptables.ps1"
}