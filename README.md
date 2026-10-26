# Personal Journal Manager

A simple, menu-driven Python application that lets users maintain a
personal journal using a text file. It demonstrates basic
Object-Oriented Programming (OOP), file handling, searching, and
exception handling.

## Features

-   **Add a New Entry:** Save a journal entry with the current date and
    time.
-   **View All Entries:** Display all saved journal entries.
-   **Search for an Entry:** Find entries using a keyword or date.
-   **Delete All Entries:** Delete the journal file after confirmation.
-   **Input Validation:** Show a helpful message for invalid menu
    choices.
-   **Error Handling:** Handle cases such as a missing journal file or
    permission errors.

## Requirements

-   Python 3.x
-   No external libraries are required.

## Project Structure

``` text
PersonalJournalManager/
├── journal_manager.py
└── journal.txt              # Created automatically when the first entry is added
```

## How to Run

1.  Install Python 3 if it is not already installed.

2.  Save the program in a file named `journal_manager.py`.

3.  Open a terminal or command prompt in the project folder.

4.  Run:

    ``` bash
    python journal_manager.py
    ```

5.  Select an option from the menu.

## Menu Options

  Option   Action
  -------- -----------------------------------
  1        Add a new journal entry
  2        View all journal entries
  3        Search entries by keyword or date
  4        Delete all journal entries
  5        Exit the program

## Example

``` text
Welcome to Personal Journal Manager!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
Enter your choice: 1

Enter your journal entry: Today I learned Python file handling.
Entry added successfully!
```

## Concepts Used

-   Classes and objects
-   Instance methods
-   File handling (`open`, read, append)
-   File modes (`r` and `a`)
-   Exception handling (`FileNotFoundError`, `PermissionError`,
    `ValueError`)
-   Conditional statements and loops
-   String searching
-   Date and time using `datetime`
-   File deletion using `os`

## Data Storage

Journal entries are stored in `journal.txt`. Each entry includes a
timestamp and the text entered by the user. Keep a backup of this file
if you want to preserve your journal.

**Note:** The "Delete All Entries" option removes `journal.txt` after
confirmation. This action deletes the saved journal entries, so use it
carefully.

## Future Improvements

-   Edit an existing journal entry.
-   Add a password or other privacy protection.
-   Export journal entries to another format.
-   Add a graphical user interface.

## License

This project is for learning and educational purposes. Add a license if
you plan to distribute it publicly.
