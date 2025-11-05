A university has hired our Software Development company to modernize their student assessment system. As we know,
universities evaluate students based on various components throughout the academic year. There are several aspects
to determining a student's overall performance, such as their attendance, coursework submissions, exam results, and
participation. The university administration wishes to implement a categorical marking system to provide more detailed
and standardized feedback to students. You have been tasked to create a program that automates this calculation and
categorization process.
For the Software Development 1 module, student performance is assessed through the following components:
2. Coursework 1: Flowchart concepts (10%)
3. Coursework 2: Basic Programming concepts (20%)
3. Coursework 3: Complex program implementation (30%)
4. Test: Theoretical and practical assessment (40%)
You have been tasked to create a program that calculates a student's overall score for this module and assigns a category
based on the university's categorical marking framework. The program should take into account the weighted scores
from each component, calculate the overall score, and then map it to the appropriate category:
- 100 (Aurum Standard)
- 92, 85, 82 (Upper First)
- 78, 75, 72 (First)
- 68, 65, 62 (2:1 Upper Second)
- 58, 55, 52 (2:2 Lower Second)
- 48, 45, 42 (Third)
- 38, 35, 32 (Condonable Fail)
- 25, 15, 5 (Fail)
- 0 (Defecit Opus) - nothing of merit, non-submission, or academic misconduct
Here's a basic outline of how the main calculation could work:
1. Calculate overall weighted score:
Overall_score = (coursework1 * 0.10)+ (coursework2 * 0.20) + (coursework3 * 0.30) + (final_exam * 0.40)

Example: If a student scores 58 in coursework 1, 65 in coursework 2, 55 in coursework 3, and 72 in the final exam,
their overall score would be calculated as:
(58 * 0.10) + (65 * 0.20) + (55 * 0.30) + (72 * 0.40) = 5.8 + 13 + 16.5 + 28.8 = 64.1
This would be rounded to the nearest category, which is 65, placing the student in the "Upper Second" category
- If the overall score is equal to 100, the output should be "Aurum Standard".
- If the overall score is between 82 and 92, the output should be "Upper First".
- If the overall score is between 72 and 78, the output should be "First ".
- If the overall score is between 62 and 68, the output should be "2:1".
- If the overall score is between 52 and 58, the output should be "2:2".
- If the overall score is between 42 and 48, the output should be " Third”.
- If the overall score is between 32 and 38, the output should be " Condonable Fail".
- If the overall score is between 5 and 25, the output should be "Fail".
- If the overall score is 0, the output should be "Defecit Opus".


There are two tasks you need to complete for this coursework:
Task 1. Following the flowchart you designed for Coursework 1, craft a program in Python which has the features listed
below:
a. You program should use the input() function that includes message text to instruct the user to enter each
b. c. d. student’s data.
Use an appropriate data structure to create and store this dataset, which contains the student’s ID, and
overall score.
Your program calculates the overall rate for each player, using the four main criteria described above
(coursework 1, coursework 2, coursework 3 and final test)
Your program should estimate the suitable category for each student by using the category dataset provided.
For instance, if the overall score of the player is between 72 and 78, the output should be:
72- First
e. The computed score should be printed out as an integer (no decimals).