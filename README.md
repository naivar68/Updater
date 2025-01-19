
# Multi Distro Update Utility

## Overview

The Nala Update Utility is a Python script designed to help users manage system updates and create system snapshots. It provides a user-friendly interface to perform various update-related tasks using different package managers.

## Features

- **Create System Snapshots**: Allows users to create a snapshot of the current system state using Timeshift.
- **Update System**: Provides options to update the system using various package managers such as `apt`, `nala`, `yum`, `dnf`, and `pacman`.
- **System Reboot**: Offers an option to reboot the system after performing updates.

## Usage

### Running the Script

To run the script, execute the following command in your terminal:

```bash
chmod +x update.py
./update.py
```
or, if you prefer to use Python directly:`
```

```bash
python3 update.py
```

(Example output below)

Welcome to the Nala Update Utility!
Please select from the following options:

1. Update the system
2. Exit

Preparing to update the system,

Please select from the following options:

1. Create a snapshot of the current system
2. Update the system
3. System reboot


Which package manager would you like to use?

1. apt and apt-get
2. nala package wrapper for Apt
3. yum
4. dnf
5. pacman and yayRequirements
6. exit


Python 3.x
Timeshift (for creating snapshots)
Appropriate package managers installed (apt, nala, yum, dnf, pacman, yay)







## License
*This project is licensed under the MIT License.*


