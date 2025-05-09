#!/usr/bin/python

import subprocess as sp
import datetime as dt
import time
from os import WCONTINUED


# Function to perform the BTRFS or RSYNC snapshot
def snapshot():
    date = dt.datetime.now()
    print("The current date and time is: ", date)
    print("Do you have a specific name you would like to give this update?")
    name = input()
    if name == '':
        print("The update has been named: ", name)
        print("Press Enter to continue.")
        input()
    else:
        title = name
        print("The update has been named: ", title)
        print("Press Enter to continue.")
        input()

    try:
        print("Creating a BTRFS snapshot of the system...")
        if name == "":
            print(f"The snapshot will be named: {name}")
            print("Press Enter to continue.")
            input()
            sp.run(['sudo', 'timeshift', '--create', '--comments', name])
        else:
            print("The snapshot will be named: ", title)
            print("Press Enter to continue.")
            input()
            sp.run(['sudo', 'timeshift', '--create', '--comments', title])

    except sp.CalledProcessError as e:
        print("An error occurred while trying to create the snapshot.")
        print("Error: ", e)
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
    print("Are you running Debian[Ubuntu], Arch Linux, or Fedora?")
    system = input()
    if system.lower() == "Debian":
        print(f"updating {system}...")
        sp.run(['sudo', 'apt' 'update'])
        sp.run(['sudo', 'apt' 'upgrade', '-y'])
        sp.run(['sudo', 'apt-get' 'update'])
        sp.run(['sudo', 'apt-get', 'upgrade', '-y'])
    elif system.lower() == "Fedora":
        sp.run(['sudo', 'yum', 'upgrade'])
    else:
        pass

    print("Press Enter to continue.")
    input()

    # The update script

    sp.run(['sudo', 'pacman', '-Syu'])

    # yay
    sp.run(['yay', '-Syu'])
    # pamac
    sp.run(['pamac', 'upgrade'])
    # snap
    sp.run(['sudo', 'snap', 'refresh'])
    # flatpak
    sp.run(['sudo', 'flatpak', 'upgrade'])

    # Conclusion of script

    print("If core modules have been updated you will want to reboot.")
    print("Do you wish to reboot the system? [y/n]")
    answer = input()

    if answer.lower() == 'y':
        sp.run(['sudo', 'systemctl', 'reboot'])
    else:
        print("Goodbye!")
        raise SystemExit


def main():
    sp.run(['clear'])
    print("Starting update process...")
    print("Continue?[y/n] ")
    input()
    snapshot()


    print("Do you wish to update the system now? [y/n]")
    query = input()
    if query.lower() == 'y':
        update()
    else:
        print("Goodbye!")
        raise SystemExit


if __name__ == "__main__":
    main()

    

    
