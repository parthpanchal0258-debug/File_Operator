import os
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("Enter your journal entry: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n{entry}\n\n")
            print("Entry added successfully!")
        except PermissionError:
            print("Error: Permission denied.")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

                if content.strip():
                    print("\nYour Journal Entries:")
                    print("--------------------------------")
                    print(content)
                else:
                    print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied.")

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ").lower()

        try:
            with open(self.filename, "r") as file:
                content = file.read().strip()

            if not content:
                print("No journal entries found.")
                return

            entries = content.split("\n\n")
            found = False

            print("\nMatching Entries:")
            print("--------------------------------")

            for entry in entries:
                if keyword in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied.")

    def delete_all_entries(self):
        try:
            with open(self.filename, "r"):
                pass

            confirm = input("Are you sure you want to delete all entries? (yes/no): ").lower()

            if confirm == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            else:
                print("Deletion cancelled.")

        except FileNotFoundError:
            print("No journal entries to delete.")
        except PermissionError:
            print("Error: Permission denied.")

    def run(self):
        print("Welcome to Personal Journal Manager!")

        while True:
            print("\nPlease select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.add_entry()
                elif choice == 2:
                    self.view_entries()
                elif choice == 3:
                    self.search_entry()
                elif choice == 4:
                    self.delete_all_entries()
                elif choice == 5:
                    print("Thank you for using Personal Journal Manager. Goodbye!")
                    break
                else:
                    print("Invalid option. Please select a valid option from the menu.")

            except ValueError:
                print("Invalid input. Please enter a number.")

journal = JournalManager()
journal.run()
