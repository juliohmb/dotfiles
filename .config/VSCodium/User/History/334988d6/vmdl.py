#!/usr/bin/env python

import os

# Read the package names from the requirements.txt file
with open('requirements.txt') as f:
    pkgs = f.read().strip().split('\n')

# Read the package names from the linux_only_requirements.txt file
with open('linux_only_requirements.txt') as f:
    linux_pkgs = f.read().strip().split('\n')

# Read the package names from the windows_only_requirements.txt file
with open('windows_only_requirements.txt') as f:
    win_pkgs = f.read().strip().split('\n')

# Generate the playbook tasks for both
tasks = ""
for pkg in pkgs:
    tasks += f"""
  - name: Install {pkg} using Yay
    package:
      name: {pkg}
      state: present
      manager: yay
    when: ansible_os_family == 'Archlinux'

  - name: Install {pkg} using Winget
    win_winget:
      name: {pkg}
      state: present
    when: ansible_os_family == 'Windows'

  - name: Install {pkg} using default
    package:
      name: {pkg}
      state: present
    else: true
"""

# Generate the playbook tasks for linux
for pkg in linux_pkgs:
    tasks += f"""
  - name: Install {pkg} using Winget
    win_winget:
      name: {pkg}
      state: present
    when: ansible_os_family == 'Windows'
"""

# Generate the playbook tasks for windows
for pkg in linux_pkgs:
    tasks += f"""
  - name: Install {pkg} using Yay
    package:
      name: {pkg}
      state: present
      manager: yay
    when: ansible_os_family == 'Archlinux'

  - name: Install {pkg} using default
    package:
      name: {pkg}
      state: present
    else: true
"""

# Generate the playbook content
playbook = f"""
---
- name: Install packages
  hosts: all
  tasks:
{tasks}
"""

# Save the playbook to a file with the .yml extension
with open('packages-playbook.yml', 'w') as f:
    f.write(playbook)
