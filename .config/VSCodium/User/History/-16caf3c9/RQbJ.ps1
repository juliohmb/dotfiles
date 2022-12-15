# Check if it is running as ADMIN
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
  Write-Output "This script must be run with administrator privileges"
  exit
}

# install Power Shell 7
winget install --id Microsoft.Powershell --source winget

# Run Debloater
Set-ExecutionPolicy Unrestricted -Force
iwr -useb https://git.io/JJ8R4 | iex
