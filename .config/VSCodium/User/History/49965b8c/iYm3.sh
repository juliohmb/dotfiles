#!/bin/bash

# Check if yay is installed
if ! command -v yay >/dev/null 2>&1; then
  echo "Error: yay is not installed. Please install it and try again."
  exit 1
fi

# Read the list of packages from the file
while IFS= read -r pkg; do
  # Install the package with yay, without needing confirmation
  yay -Sy "$pkg"
done < packages.txt
