Write-Output "Running mypy.....";
mypy .;

Write-Output "Running flake8.....";
flake8 .;

Write-Output "Done."