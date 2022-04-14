# List the files in a directory 
# List all files and print the full path
#Get-Childitem -recurse -Include *.docx,*.pdf,*.txt -Path .\Documents |Select FullName
Get-Childitem -recurse -Include *.docx,*.pdf,*.txt -Path .\Documents |export-csv `
-Path files.csv

# Import CSV file
$fileList = import-csv -Path .\files.csv -header FullName

# Loop through the results
foreach ($f in $fileList) {

    Get-Childitem -Path $f.FullName
    
}