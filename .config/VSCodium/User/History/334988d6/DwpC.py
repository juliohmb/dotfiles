#!/usr/bin/env python

import os

# Read the package names from the requirements.txt file
with open('requirements.txt') as f:
    pkgs = f.read().strip().split('\n')

# Generate the playbook tasks
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

  - name: Print an error message for {pkg}
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
with open('playbook.yml', 'w') as
