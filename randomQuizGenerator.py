import random, json

# import quiz data
with open('quizdata.json') as f:
    qdata = json.load(f)

quizCount = int(input('How many quizes do you want to generate: '))
quizName = input('What would you like the name of the quiz to be?')

# generate quiz files
 
#####  Look to generate these in a separate directory from the code #####

for quizNum in range(quizCount):
    # create quiz and answer key files
    quizFile = open('quiz%s.txt' % (quizNum+1),'w')
    answerFile = open('answer%s.txt' % (quizNum+1),'w')

    #write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 20) + 'Quiz: (Form %s)' % (quizNum+1) + quizName)
    quizFile.write('\n\n')

    # shuffle
    questions = list(qdata.keys())
    random.shuffle(questions)

# loop through input and create questions
