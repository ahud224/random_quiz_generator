import random, json, os

# import quiz data
with open('quizdata.json') as f:
    qdata = json.load(f)

quizCount = int(input('How many quizes do you want to generate: '))
quizName = input('What would you like the name of the quiz to be?')

# create folder for quiz files
folderName = 'quizzes/' + quizName
os.makedirs(folderName, exist_ok=True)

# generate quiz files
for quizNum in range(quizCount):
    # create quiz and answer key files
    quizFile = open(folderName + '/quiz%s.txt' % (quizNum+1),'w')
    answerFile = open(folderName + '/answer%s.txt' % (quizNum+1),'w')

    #write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 20) + 'Quiz: (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    # shuffle
    questions = list(qdata.keys())
    random.shuffle(questions)

# loop through input and create quiz
    for questionNum in range(len(questions)):
        # get correct and incorrect answers
        correctAnswer=qdata[questions[questionNum]]
        wrongAnswers=list(qdata.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the question and answer options to the quiz file
        quizFile.write('%s. %s\n' % (questionNum+1, questions[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer key to the answer file
        answerFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerFile.close()