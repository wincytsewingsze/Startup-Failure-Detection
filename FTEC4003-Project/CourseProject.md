# FFTEC4003 Data Mining for FinTech Course Project Assignment

### Due Date
- Submission of the report: <font color=red size=3>23:59:59 on December 18 (Sun.), 2022</font>.

### Reminder
- This is a group project including two tasks. The number of team members in each team is up to 3.
- You are **NOT** allowed to **COPY** code/report from the Internet or others (unless specified for some exceptional cases). Any plagiarism case will be seriously punished.
- The assessment will be based on your results, submitted files, and report.
- You are not allowed to use any information from the test data (e.g.,  the output in our evaluation).
- Please send your group information to ftec4003@se.cuhk.edu.hk before 23:59:59 on November 13 (Sun.), 2022.
- For late submission, a penalty per day will be applied after the deadline (30%, 30%, and 40% for the following days, respectively). You won’t get any marks for more than a **3-day delay**. Please submit your assignment before the deadline.
- Language: **Python 3**. You can use any package you like.
- Operating System Platform: Windows / Linux / macOS.
- You are strongly encouraged to read the tutorial materials on the <font color=red size=3>blackboard website</font>.

### Marking Scheme (Total: 19 marks)
- TASK 1: 8 marks
- TASK 2: 11 marks

## TASK 1: Debt Default Prediction.
The first task is to conduct a classification task with Python 3 and compare the performance of several standard methods learned from class. The detailed requirements are described as follows.
1. Run the classification task using all methods among DecisionTree, k-Nearest Neighbor, Naive Bayes, SVM, and Ensemble Methods. As for the Emsemble Method, choose one from the three learned methods, i.e., bagging, AdaBoost, and random forest. Compare the performance of the two best methods in your report. Please show how you have tuned the basic parameters (those covered in the lecture) and justify your final choice of the parameters according to your experimental analysis.
2. Description of datasets: Please refer to the file <font color=red size=3>README.md</font> under the directory <font color=red size=3>Task-1-Debt-Default-Prediction</font> for details.
3. Output: For each item in <font color=red size=3>assignment-test.csv</font>, you need to predict its class (1/0). Please store your result in a file named <font color=red size=3>submission_1_method.csv</font> (replace "method" with the best two method name. e.g., submission_1_svm.csv). The format should be the same as <font color=red size=3>samplesubmission.csv</font>. It would help if you were careful about <font color=red size=3>the number of lines</font> and the predicted result, which should be <font color=red size=3>1 or 0</font>. 
4. In your report, record the performance of the classification task. Please use the command line tool named  <font color=red size=3>evaluate_1</font> (tool names may get a little different depending on the platforms) under the directory  <font color=red size=3>Task-1-Debt-Default-Prediction</font> to get the performance of your result. We will use the F1-score of the "1" class to measure your submission.

## TASK 2: Startup Failure Prediction.
1. This is a competitive classification task. Please achieve an as high score as you can. Methods are unlimited in this task (i.e., you can use techniques not covered in this class).
2. The champion and runner-up for <font color=red size=3>this task</font> will get an award certificate.
3. Descriptions of the datasets can be found in a README file under the directory <font color=red size=3>Task-2-Startup-Failure-Prediction</font>.
4. Output & report: The output is similar to task 1 except that you should store your result in file <font color=red size=3>submission_2.csv</font> and evaluate the result via <font color=red size=3>evaluate_2</font> (tool names may get slightly different depending on the platforms). The format should be the same as <font color=red size=3>samplesubmission.csv</font>. It would help if you were careful about <font color=red size=3>the number of lines</font> and the predicted result, which should be <font color=red size=3>1 or 0</font>. We will use the F1-score of the "1" class to measure your submission.

## Submission Guidelines
### What to Submit
1. A README file. Please name it <font color=red size=3>README.txt</font> or <font color=red size=3>README.md</font> (the latter is recommended). This file should include the following sections:
	- Student numbers and names of all team members.
	- A brief description of all files.
2. Output files (i.e., <font color=red size=3>submission_1.csv</font> and <font color=red size=3>submission_2.csv</font>).
3. A file named<font color=red size=3> FTEC4003_report_XX.pdf</font>, where **XX** denotes your group ID. The file should include a brief description of the platform, the method, experimental evaluations, results, and conclusions of the two tasks. Please show your names and student numbers on the cover page of your report.

### Submission Instructions
1. Please package all your code files (including the <font color=red size=3>README.txt</font> (or <font color=red size=3>README.md</font>), the output files, and your report <font color=red size=3>FTEC4003_report_XX.pdf</font> into a **ZIP** file named FTEC4003_project_XX.zip</font>, where **XX** is your group ID.
2. Submit the package file with the Subject **FTEC4003 SUBMISSION XX** to the course mail, **ftec4003@se.cuhk.edu.hk**, where **XX** is your group ID. (Please do use upper case in the Subject to ease the submission process)

