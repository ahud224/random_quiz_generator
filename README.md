The initial idea was taken from Automate the Boring Stuff with Python.

However i made some notable changes to make the program a bit more modular

- using a json file to store quiz data input vs. hardcoding in a dictionary within the code
- prompting user for quiz info (quiz name and questions) vs. hardcodign that
- minor improvements to the output



How to use:
Enter in your quiz data into quizdata.json in a format of answer:question.

The program will then generate n number of quizes that mix/match the questions/answers and provide you with a quiz specific answer sheet.