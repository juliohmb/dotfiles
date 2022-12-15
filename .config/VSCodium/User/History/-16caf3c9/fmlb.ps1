# Check if it is running as ADMIN
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
  Write-Output "This script must be run with administrator privileges"
  exit
}

# Check if Winget is installed
if (!(Get-Command winget -ErrorAction SilentlyContinue)) {
  Write-Host "Winget is not installed. Installing winget..."
}

# Read the list of programs from the windows_only_requirements.txt file
$programs = Get-Content windows_only_requirements.txt

# Download each program in the list with winget
foreach ($program in $programs) {
  winget install -e $program
}

# Install WSL
wsl --install

# Update WSL
wsl --set-default-version 2

# Run Debloater
Set-ExecutionPolicy Unrestricted -Force
iwr -useb https://git.io/JJ8R4 | iex

# Install Arch
Invoke-WebRequest -Uri "https://github.com/yuk7/ArchWSL/releases/latest" -OutFile "C:\arch\arch.zip"
Expand-Archive -LiteralPath "C:\arch\arch.zip" -DestinationPath "C:\arch"
Write-Host "https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/#setup-after-install"
Write-Host "https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/#set-the-systemd-flag-set-in-your-wsl-distro-settings"
8