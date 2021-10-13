# Game statistics

## Story

You are a software architect at game development company named Eastwood Studios.
Judy, a colleague from sales, asks you to help her in a competitor
evaluation project. She has lots of data files with statistical
information about famous games of all time. Judy has some unanswered
questions about the games and expects you to write a program that
can answer these questions.

There is an additional request: Judy likes to explore the data
manually, and for that she needs a simple terminal interface
where she can pick her questions, type the required inputs, and
get the answer printed on the screen. On the other hand,
there are many files that need to be processed, so you also need
a way to answer the questions programmatically
and save them into a target file.

Since you are an architect, you cannot help but use a modular structure,
where no code is duplicated, and the responsibilities are strictly separated.
So you decide to create three modules: reports.py, printing.py,
and export.py to cover all the requested features.

## What are you going to learn?

- Use modules.
- Conform to test requirements.
- Filter data.
- Work with files.
- Handle errors.
- Follow clean code practices.


## Tasks

1. "How many games are in the file?" asks Judy. Implement `count_games(file_name)` to answer this question. The expected output of the function is a number.
    - The function returns the number of games (as an integer), based on the data file.

2. "Is there a game from a given year?" asks Judy. Implement `decide(file_name, year)` to answer this question. The expected output of the function is a boolean value.
    - The function returns `True` or `False` to answer the question, based on the data file.

3. "Which is the latest game?" asks Judy. Implement `get_latest(file_name)` to answer this question. The expected output of the function is the title of the latest game. If there is more than one, return the first title from the file.
    - The function returns the title that answers the question, based on the data file.

4. "How many games are in the file by genre?" asks Judy. Implement `count_by_genre(file_name, genre)` to answer this question. The expected output of the function is a number.
    - The function returns the number of games in the given genre (as an integer), based on the data file.

5. "What is the line number of a given title?" asks Judy. Implement `get_line_number_by_title(file_name, title)` to answer this question, based on the data file. The expected output of the function is an integer. If the title is not found, raise a `ValueError` exception.
    - The function returns the number of games of the given (as an integer) title, based on the data file.
    - The function raises a `ValueError` exception if the title is not found in the data file.

6. "Can you give me the alphabetically ordered list of the titles?" asks Judy. Implement `sort_abc(file_name)` to answer this question based on the given data file. The expected output of the function is a list of titles. _Do not use the `sort` method or the built-in `sorted`, `min`, and `max` functions. Implement an easy sorting algorithm on your own._
    - The function returns the sorted list of the titles based on the given data file.
    - The code uses a custom sort algorithm implementation without the forbidden functions.

7. "Which genres occur in the data file?" asks Judy. Implement `get_genres(file_name)` to answer this question based on the given data file. The expected output of the function is a list of the genres without duplicates, in alphabetical order. _Do not use the `sort` method or the built-in `sorted`, `min`, and `max` functions. Implement an easy sorting algorithm on your own._
    - The function returns the sorted list of the unique genres based on the given data file.
    - The code uses a custom sort algorithm implementation without the forbidden functions.

8. "What is the release year of the top selling first-person shooter game?" asks Judy. Implement `when_was_top_sold_fps(file_name)` to answer this question based on the given data file. The expected output of the function is the year of the release (as an integer). If there is no first-person shooter game in the data file, a `ValueError` exception is raised.
    - The function returns the release year of the top selling first-person shooter game based on the given data file.
    - The function raises a `ValueError` exception if the FPS genre is not found in the given data file.

9. The three modules share responsibilities as described in the introduction: `reports` contains the functions providing the answers, `printing` asks for user input and prints output to the terminal, `export` gets the required input parameters as command line arguments, then saves the results. The latter two modules call the core functions of `reports`.
    - The `reports` module does not ask for user input and does not print anything.
    - The `printing` module asks for user input, first for the name of a data file, then it goes through all the questions, asks for the extra arguments, and prints the results to the screen.
    - The `printing` module does not exit on the exceptions of `reports`. It handles them and communicates them to the user.
    - The `printing` module does not implement the answers themselves but imports `report` (and does not import `export`).
    - The `export` module needs command line arguments in this form `python3 export.py source_file_name target_file_name input_year input_genre input_title` where the last 3 are arguments for questions #2, #4, and #5, respectively. The results are saved into a file `target_file_name`, the individual answers written into new lines.
    - The `export` module does not exit on the exceptions of `reports`. It handles them and sends informative text snippets to the output instead.
    - The `export` module does not implement the answers themselves but imports `report` (and does not import `printing`).

## General requirements

- Variable names in the program are meaningful, non-abbreviated nouns.
- Function names in the program are meaningful, non-abbreviated verbs.
- There are no unnecessary (dead) code parts or comments in the program.
- There are no duplicate code parts or code parts doing the same thing differently in the program.
- There are no functions doing more than one thing in the program.
- There are no external imports in the program.

## Hints

- Check your code by running `test.py` after implementing each function.
- Keep in mind: [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)!
  When a piece of code appears in multiple locations, try to extract it into a function.
- Add some _abstraction_ if it helps you to reduce the code (such as using parameters
  to unify similar snippets in one function).
- Your functions need to process any input files with the same structure
  as `game_stat.txt`. Every line contains the **title**, the **copies sold**
  (in millions), the **release year**, the **genre**, and the **publisher** of a
  popular computer game. The columns are separated by tab characters, such as
  `Minecraft⟶23⟶2009⟶Survival game⟶Microsoft↲`.
  Create files with the same structure but different data and test your solution on them.
- Avoid magic numbers.
- Command line arguments separated by space by default. To provide a single
  command line argument that contains space, put it between quotation marks,
  such as "Electronic Arts".


## Background materials

- <i class="far fa-exclamation"></i> [File handling](project/curriculum/materials/competencies/python-basics/python-file-handling.md.html)
- <i class="far fa-exclamation"></i> [Error handling in Python](https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html) (until the section "Debugging programs")
- <i class="far fa-exclamation"></i> [About Python modules](https://realpython.com/python-modules-packages/) (until the section "Python Packages")
- <i class="far fa-exclamation"></i> [Magic numbers](project/curriculum/materials/competencies/clean-code/magic-numbers.md.html)
- <i class="far fa-exclamation"></i> [Clean code](project/curriculum/materials/competencies/clean-code.md.html)

