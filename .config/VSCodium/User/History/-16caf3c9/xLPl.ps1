# Check if it is running as ADMIN
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
  Write-Output "This script must be run with administrator privileges"
  exit
}

# install Power Shell 7
winget install --id Microsoft.Powershell --source winget

# Install Python
winget install -e --id Python.Python.3.9

# Install Ansible

# Install WSL

# Update WSL

# Install Arch

# generate playbook

# Run ansible playbook

# Run Debloater
Set-ExecutionPolicy Unrestricted -Force
iwr -useb https://git.io/JJ8R4 | iex