# 📚 Library Management System

A simple, menu-driven Library Management System built using Python. This project allows users to manage books, track their availability, and perform basic library operations with data stored persistently in a JSON file.

## ✨ Features

- **Add Books:** Add new books with a unique book ID, title, and author.
- **View All Books:** Display all books stored in the library.
- **Search Books:** Find a book using its ID.
- **Borrow Books:** Borrow a book if it is available.
- **Return Books:** Return borrowed books and update their availability.
- **Delete Books:** Delete available books after confirmation.
- **Data Persistence:** Store book records in a JSON file so that data remains available after restarting the program.
- **Input Validation:** Handle invalid menu choices and unavailable or nonexistent books.

## 🛠️ Technologies Used

- Python 3
- JSON
- File Handling
- Object-Oriented Programming (OOP)

## 📂 Project Structure

```text
Library-Management-System/
│
├── main.py
├── library.json
└── README.md
```

- `main.py` — Contains the main program and library management logic.
- `library.json` — Stores book records. It is created when data is saved.
- `README.md` — Project documentation.

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

3. Navigate to the project directory:

   ```bash
   cd Library-Management-System
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## 📋 Available Operations

| Option | Operation |
|---|---|
| 1 | Add a book |
| 2 | View all books |
| 3 | Search for a book |
| 4 | Borrow a book |
| 5 | Return a book |
| 6 | Delete a book |
| 7 | Change the selected book ID |
| 8 | Exit the program |

## 💾 Data Storage

Book information is stored in `library.json` in JSON format. Each book record contains:

- `id` — Unique book identifier
- `title` — Title of the book
- `author` — Author's name
- `availability` — Current status (`available` or `borrowed`)

## 🎯 Learning Outcomes

Through this project, I practiced:

- Designing classes and methods using OOP
- Working with lists and dictionaries
- Reading and writing JSON files
- Implementing CRUD operations
- Managing book availability and handling edge cases
- Debugging conditional statements and loops

## 🔮 Future Improvements

- Add library member registration.
- Track which member borrows each book.
- Add due dates and borrowing history.
- Improve the user interface.
- Add stronger input validation and error handling.

## 👨‍💻 Author

**Junaid Arifin**

Built as a Python practice project to strengthen programming fundamentals and problem-solving skills.
