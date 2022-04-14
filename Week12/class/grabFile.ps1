# Create commandline parameters to copy a file and place into evidence directory
param(

[Parameter(Mandatory = $true)]
[int]$reportNo,

[Parameter(Mandatory = $true)]
[String]$filePath

)

# Create a directory with the report number
$reportDir = "rpt$reportno"

# Creating a new directory
mkdir $reportDir

# Copy the file into the new directory
copy-item $filePath $reportDir