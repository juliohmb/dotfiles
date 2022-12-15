# Check if it is running as ADMIN
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
  Write-Output "This script must be run with administrator privileges"
  exit
}

# Check Winget
winget --version

# Install WSL
wsl --install

# Update WSL
wsl --set-default-version 2

# Run Debloater
Set-ExecutionPolicy Unrestricted -Force
iwr -useb https://git.io/JJ8R4 | iex

# Install Arch
Invoke-WebRequest -Uri "https://github.com/yuk7/ArchWSL/releases/latest" -OutFile "C:\arch\arch.zip"
Write-Host "https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#setup-after-install"
