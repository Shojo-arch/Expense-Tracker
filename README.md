# Expense Tracker

A simple command-line expense tracker built with Python. It helps you record daily expenses, see where your money goes, and stay within monthly budgets. It also has two extra features: **Quick Add** and **Forecast**.

## Features

- Add expenses with an amount, category, note and date
- View all expenses with the total
- Monthly summary by category
- Set a monthly budget for any category
- Data is saved in a local JSON file, so nothing is lost when you close the program

### Unique features

**1. Quick Add**
Type an expense as a normal sentence instead of filling in separate fields.

```
Type your expense: coffee 120 yesterday
Category guessed: food
Added!
```

The program finds the amount, understands words like "yesterday" as the date, and guesses the category from keywords (for example, coffee → food, uber → transport). If it doesn't recognise the words, the category is set to `other`.

**2. Forecast**
Predicts how much you will have spent by the end of the month, using your average spending per day so far. For every budget you set, it tells you whether you are on track or will go over, and how much you can spend per day to stay within the budget.

```
food - budget: 3000.0 spent: 570.0 predicted: 5890
  You will go over! Spend less than 84 per day
```

Formula used: `predicted = spent so far / days passed x days in the month`

Note: the forecast is more accurate later in the month, because early on it only has a few days of data.

## Requirements

- Python 3.6 or higher
- No external libraries needed (only the Python standard library)

## Setup and Run

1. Clone the repository:
   ```
   git clone https://github.com/YOUR-USERNAME/expense-tracker.git
   ```
2. Go into the project folder:
   ```
   cd expense-tracker
   ```
3. Run the program:
   ```
   python expense_tracker.py
   ```
   (On some systems, use `python3 expense_tracker.py`.)

## How to Use

When you run the program, this menu appears:

```
1. Add  2. Quick add  3. View  4. Summary  5. Budget  6. Forecast  7. Exit
```

| Option | What it does |
|--------|--------------|
| 1 | Add an expense by entering the amount, category and note |
| 2 | Quick add an expense by typing a sentence like `uber 230` |
| 3 | View all expenses and the total |
| 4 | Show this month's spending for each category |
| 5 | Set a monthly budget for a category |
| 6 | Show the forecast and budget advice |
| 7 | Exit the program |

## Project Structure

```
expense-tracker/
├── expense_tracker.py   # main program (all the code)
├── README.md            # project description and setup steps
└── .gitignore           # files Git should ignore
```

The program creates an `expenses.json` file the first time you add an expense. This file stores your data and is not included in the repository.

## Demo Video

[Watch the demo here](ADD-YOUR-VIDEO-LINK-HERE)

## Author

Your Name - [GitHub profile](https://github.com/YOUR-USERNAME)
