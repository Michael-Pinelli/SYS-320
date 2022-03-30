# Get list of running processes
#Get-process

# Get list of members
#Get-process | get-member

# Get a list of processes: name, id, path
#Get-process | Select-object ProcessName, id, Path

#$outputName = "C:\Users\mikep\Documents\SYS-320\Week09\class\Processes.csv"

# Save the Output to a CSV
#Get-process | Select-object ProcessName, id, Path | Export-csv -Path `
#C:\Users\mikep\Documents\SYS-320\Week09\class\Processes.csv

#$outputName = "C:\Users\mikep\Documents\SYS-320\Week09\class\Services.csv"

# System Services and properties
#Get-service | get-member
#Get-service | select-object Status, Name, DisplayName, BinaryPathName | export-csv -Path `
#$outputName

$outputName = "C:\Users\mikep\Documents\SYS-320\Week09\class\Running-Services.csv"

# Get a list of running services
Get-service | Where-object { $_.Status -eq "Running" }

# Check to see if file exists
if (Test-path $outputName ) {

    write-host -backgroundcolor "Green" -foregroundcolor "White" "Services file was created"

} else {

    write-host -backgroundcolor "Red" -foregroundcolor "White" "Services file was not created"
}