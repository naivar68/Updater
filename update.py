#!/usr/bin/python3
import subprocess as sp
import datetime as dt


# Function to perform the BTRFS or RSYNC snapshot
def snapshot():
    date = dt.datetime.now()
    print(f"The current date and time is: {date}")
    print("Do you have a specific name you would like to give this update?")
    name = input().strip()  # Added strip method to remove whitespace from input
    if name == '':
        print("The update has been named: ", name)
        print("Press Enter to continue.")
        input()
    else:
        title = name.strip()  # Modified line for correct variable assignment
        print(f"The update has been named: {title}")
        print("Press Enter to continue.")
        input()

    try:
        print("Creating a BTRFS snapshot of the system...")
        if name == "":
            sp.run(['sudo', 'timeshift', '--create', '--comments', name])
        else:
            print(f"The snapshot will be named: {title}")
            sp.run(['sudo', 'timeshift', '--create', '--comments', title])
    except sp.CalledProcessError as e:
        print(f"An error occurred while trying to create the snapshot.")
        print(f"Error: {e}")
        print("Press Enter to continue.")
        input()
        print("Now attempting Timeshift with 'rsync'...")
        try:
            sp.run(['sudo', 'timeshift', '--create', '--comments', title])
        except sp.CalledProcessError as e:
            print(f"An {e} error occured...")
            raise SystemExit


def update():
    sp.run(['clear'])
    print("About to start a full system upgrade...")
    print("Are you running Debian[Ubuntu], Arch Linux, or Fedora?[type 'debian', 'arch', or 'fedora']")
    system = input().strip()  # Added strip method to remove whitespace from input
    if system.lower() == "debian":
        print(f"updating {system}...")
        sp.run(['sudo', 'apt', 'update'])
        sp.run(['sudo', 'apt', 'upgrade', '-y'])
        sp.run(['sudo', 'apt-get', 'update'])
        sp.run(['sudo', 'apt-get', 'upgrade', '-y'])
    elif system.lower() == "fedora":
        sp.run(['sudo', 'dnf', 'upgrade'])
    elif system.lower() == "arch":
        sp.run(['sudo', 'pacman', '-Syu'])
        sp.run(['yay', '-Syu'])
        sp.run(['pamac', 'upgrade'])
        
    else:
        print("Please enter a valid response: 'Arch' 'Debian' 'Fedora'")
        update()

    print("Now updating 'snap' and 'flatpak'")
    # snap
    sp.run(['sudo', 'snap', 'refresh'])
    # flatpak
    sp.run(['sudo', 'flatpak', 'upgrade'])

    # Conclusion of script
    
    print("If core modules have been updated you will want to reboot.")
    print("Do you wish to reboot the system? [y/n]")
    answer = input().strip()  # Added strip method to remove whitespace from input
    if answer.lower() == 'y':
        sp.run(['sudo', 'systemctl', 'reboot'])
    else:
        print("Goodbye!")
        raise SystemExit


def main():
    sp.run(['clear'])
    print("Starting update process...")
    print("Continue?[y/n] ")
    input()  # Removed print statement to remove unnecessary line
    snapshot()

    print("Do you wish to update the system now? [y/n]")
    query = input().strip()  # Added strip method to remove whitespace from input
    if query.lower() == 'y':
        update()
    else:
        print("Goodbye!")
        raise SystemExit


if __name__ == "__main__":
    main()
    
