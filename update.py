#! /usr/bin/python3

# The multi-upgrade utility for Linux systems


import subprocess as sp


# Upadte Function

def update():
    sp.run(['clear'])
    print("Preparing to update the system, \n")
    print("Please select from the following options:")
    print("""
    1. Create a snapshot of the current system
    2. Update the system
    3. System reboot
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Enter a name for the snapshot, or leave empty for none: ")
        name = input()

        try:
            print("Creating snapshot with Timeshift...")
            sp.run(['sudo', 'timeshift', '--create', '--comment', name])
            print(f"Snapshot {name} created successfully!")
            print("Here is a list of your snapshots for confirmation:\n")
            sp.run(['sudo', 'timeshift', '--list'])
            print("\n")
            print("Press any key to continue...")
            input()
            main()
        except Exception as e:
            print(f"An error occured: {e}")
            print("Press any key to continue...")
            input()
            main()

    elif choice == '2':
        sp.run(['clear'])
        print("Which package manager would you like to use?\n")
        print("""
        1. apt and apt-get
        2 .nala package wrapper for Apt
        3 yum
        4 dnf
        5. pacman and yay
        6 flatpak
        7. pamac
        8: snap
        9. Exit
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Updating the system with apt and apt-get...")
            try:
                sp.run(['sudo', 'apt', 'update', '-y'])
                sp.run(['sudo', 'apt', 'upgrade', '-y'])
                print("System updated successfully!")
                print("do you need to upgrade the distribution? (y/n)")
                dist = input()
                distro = dist.lower()

                if distro == 'y':
                    print("Upgrading the distribution...")

                    try:
                        sp.run(['sudo', 'apt', 'dist-upgrade', '-y'])
                        print("Distribution upgraded successfully!")
                        print("Press any key to continue...")
                        input()
                        main()

                    except Exception as e:
                        print(f"An error occured: {e}")
                        print("Press any key to continue...")
                        input()
                        main()
                else:
                    print("Distribution upgrade skipped.")
                    print("Press any key to continue...")
                    input()
                    main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()

        elif choice == '2':
            print("Updating the system with nala package wrapper for Apt...")
            try:
                sp.run(['sudo', 'nala', 'update', '-y'])
                sp.run(['sudo', 'nala', 'upgrade', '-y'])
                print("System updated successfully!")
                print("do you need to upgrade the distribution? (y/n)")
                dist = input()
                distro = dist.lower()

                if distro == 'y':
                    print("Upgrading the distribution...")

                    try:
                        sp.run(['sudo', 'nala', 'dist-upgrade', '-y'])
                        print("Distribution upgraded successfully!")
                        print("Press any key to continue...")
                        input()
                        main()

                    except Exception as e:
                        print(f"An error occured: {e}")
                        print("Press any key to continue...")
                        input()
                        main()
                else:
                    print("Distribution upgrade skipped.")
                    print("Press any key to continue...")
                    input()
                    main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()

        elif choice == '3':
            print("Updating the system with yum...")
            try:
                sp.run(['sudo', 'yum', 'update', '-y'])
                print("System updated successfully!")
                print("Press any key to continue...")
                input()
                main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()

        elif choice == '4':
            print("Updating the system with dnf...")
            try:
                sp.run(['sudo', 'dnf', 'update', '-y'])
                print("System updated successfully!")
                print("Press any key to continue...")
                input()
                main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()

        elif choice == '5':
            print("Updating the system with pacman and yay...")
            try:
                sp.run(['sudo', 'pacman', '-Syu', '--noconfirm'])
                print("System updated successfully!")
                print("Press any key to continue...")
                input()
                print("Now updating AUR packages with yay...")
                sp.run(['yay', '-Syu', '--noconfirm'])
                print("AUR packages updated successfully!")
                print("Press any key to continue...")
                input()
                main()


            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()

        elif choice == "6":
            print("Updating the system with flatpak...")
            try:
                sp.run(['sudo','flatpak', 'update', '-y'])
                print("System updated successfully!")
                print("Press any key to continue...")
                input()
                main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()

        elif choice == "7":
            print("Updating the system with pamac...")
            try:
                sp.run(['pamac', 'upgrade', '-y'])
                print("System updated successfully!")
                print("Press any key to continue...")
                input()
                main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()


        elif choice == "8":
            print("Updating the system with snap...")
            try:
                sp.run(['sudo', 'snap', 'refresh'])
                print("System updated successfully!")
                print("Press any key to continue...")
                input()
                main()

            except Exception as e:
                print(f"An error occured: {e}")
                print("Press any key to continue...")
                input()
                main()




        elif choice == '9':
            print("Exiting the utility...")
            raise SystemExit
        else:
            print("Invalid choice, please try again.")
            print("Press any key to continue...")
            input()
            main()

    elif choice == '3':
        print("Rebooting the system...")
        try:
            sp.run(['sudo', 'reboot'])
        except Exception as e:
            print(f"An error occured: {e}")
            print("Press any key to continue...")
            input()
            main()

    else:
        print("Invalid choice, please try again.")
        print("Press any key to continue...")
        input()
        main()





# Main Function

def main():
    sp.run(['clear'])
    print("Welcome to the Nala Update Utility!")
    print("Please select from the following options:")
    print("""
    1. Update the system
    2. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        update()
    elif choice == '2':
        print("Exiting the utility...")
        exit()
    else:
        print("Invalid choice, please try again.")
        print("Press any key to continue...")
        input()
        main()

# Main Function Call

if __name__ == '__main__':
    main()



