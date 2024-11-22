

# Student Performance Tracker - README

## What Is This Program?

This program helps you track and manage students' scores in different subjects like Math, Science, and English. You can enter the students' names and their scores for each subject, and the program will calculate their average score, tell you if they are passing, and display the overall class performance.

## Main Features

- **Enter student information**: You can add a student's name and their scores for Math, Science, and English.
- **Average score**: The program will automatically calculate the average score for each student.
- **Passing or failing**: It will check if each student is passing or failing based on their scores.
- **Class summary**: It will also show the average score of all students in the class.
- **Error handling**: If you make a mistake while entering scores (like typing letters instead of numbers), the program will ask you to try again.

## How It Works

### Classes in the Program

The program has two main parts called **classes**, which help organize everything:

### 1. `Student` Class

This part stores each student’s name and scores. It also has methods (functions inside the class) to:

- **Calculate the average score**: It adds up the student's scores and divides by the number of subjects.
- **Check if the student is passing**: If any score is below the passing mark (default is 40), the student is considered failing.

### 2. `PerformanceTracker` Class

This part keeps track of all the students and their scores. It has methods to:

- **Add a student**: Store a student's name and their scores.
- **Calculate the class average**: Find the average score of all the students in the class.
- **Show each student’s performance**: Display the student's name, their average score, and whether they are passing or failing.

### Helper Functions

- **`get_student_input()`**: This is where you enter student names and scores. You will be asked to enter each student's name and their scores for Math, Science, and English. When you’re done, type `finish` to stop adding students.
- **`main()`**: This is the starting point of the program. It uses the classes and functions to collect student information, calculate averages, and display the results.

## Example Walkthrough

1. **Starting the Program**: When you run the program, it will welcome you and ask you to enter student information.
2. **Entering Data**: You will enter the student's name and their scores in three subjects (Math, Science, English).
3. **Finish Data Entry**: Once you're done entering students, type `finish` when asked for a student's name.
4. **Results**: The program will show:
   - Each student's average score.
   - Whether the student is passing or failing.
   - The class average score for all students.

## Example Output

Here's what the program looks like when you run it:

```
==================================================
            Welcome to the Student Performance Tracker
==================================================
Please enter student information (type 'finish' to finish):

Enter student's name ('finish' to finish the program): John
Enter Numan's score for math: 80
Enter Numan's score for science: 75
Enter Numan's score for English: 90

Enter student's name ('finish' to finish the program): Sarah
Enter Saad's score for math: 60
Enter Saad's score for science: 65
Enter Saad's score for English: 70

Enter student's name ('finish' to finish the program): finish

--- Student Performance Summary ---
Student: Numan
Average Score: 81.67
Status: Passing
--------------------
Student: Saad
Average Score: 65.0
Status: Passing
--------------------

--- Overall Class Performance ---
Class Average Score: 73.83

=====================================
   Thank you for using the Tracker!
=====================================
```

In this example:
- Numan has an average of 81.67, and he is passing.
- Saad has an average of 65.0, and she is passing too.
- The class average is 73.83.

