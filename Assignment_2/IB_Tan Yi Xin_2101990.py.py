"""
1. This code is about a multiple choice question.
2. Student is required to answer the 20 questions provided.
3. The correct answer have been stored in a list in the main code.
4. The answer from student will be stored in a list(stu_ans) in the main code in order to make convenience to write in into text file.
5. The text file's name will be named based on student's name so that can find it easier.
6. After student answered the question, the list (stu_ans) will be write in the text file.
7. One more list(stu_record) is created to retrieved the student's answer from the text file that wrote previously.
8. The student's result(pass/fail?? @@ score ) will be display only the record is found in the text file.
"""
# allow to store several student's record in different text file.


letter = ['A', 'B', 'C', 'D']

answer = ['A', 'C', 'A', 'A',
          'D', 'B', 'C', 'A',
          'C', 'B', 'A', 'D',
          'C', 'A', 'D', 'C',
          'B', 'B', 'D', 'A']
stu_ans = []
score = 0
question = ['What is the full name for UTAR?',
            'When the UTAR is established?',
            'How many campus does UTAR have?',
            'How many intakes in a year in UTAR?',
            'How long does the sem break in UTAR normally?',
            'What is the general entry requirement for SPM students?',
            'What is the use of WBLE?',
            'What is the study mode for June 2022 intake?',
            'What is the COVID-19 vaccination status restriced to the student to access into campus?',
            'How to apply leave of absence?',
            'What should you do if you wish to change the programmes/ intake/ campus during the application process',
            'When should you submit the health declaration form?',
            'How should you make the payment on student bill?',
            'What is the minimum English level requirement to entry UTAR?',
            'What is the platform to scan and check your class attendance?',
            'What is the minimum attendance percentage to allow you sitting for FINAL Exam?',
            'Where can you download past year FINAL Exam paper?',
            'Where is the UTAR main campus located?',
            'Where you should go if you wish to give your feedback to UTAR?',
            'If you wish to have pre-study for the next semester subject, where should you go to archived notes?']

choice = [['Universiti Tunku Abdul Rahman', 'Universiti Tak Ade Rehat', 'Universiti Tun Abudul Razak',
           'Universiti Teknologi Asia Rahman'],  # 1
          [1998, 2000, 2002, 2004],  # 2
          [2, 4, 6, 8],  # 3
          [3, 2, 1, 5],  # 4
          ['No sem break', '1 week', '2 months', '2-3 weeks'],  # 5
          ['10As and above', '5C and above', 'Pass all the subject', 'No requirement'],  # 6
          ['Useless web', 'Entertainment web', 'Access the latest course material', 'Investment web'],  # 7
          ["Lecture:Online,Tutorial:Physical", 'All online', 'Hybrid mode', 'No need to attend class'],  # 8
          ['No need vaccine', '1 dose vaccination', '2 dose vaccination + 1 vaccine enhancement', '2 dose vaccination'],
          # 9
          ['Get approve from friends', 'Complete and submit the application form to FGO', 'No need to apply', 'Apply with Academic Advisor'],  # 10
          ['Contact Division of Admissions and Credit Evaluation (DACE)', 'Just attend other class without any process',
           'Contact my friends', 'Contact my parents'],  # 11
          ['No need to submit', 'After graduation', "Do not need to have a body check-up",
           "When I'm pyhiscally return to the campus"],  # 12
          ["I don't want to pay", '', 'Jom Pay or Public Bank Internet Banking', 'Ambank Internet Banking'],  # 13
          ['Grade C', 'Grade B', 'Grade A', 'Do not have any requirement'],  # 14
          ['WBLE', 'UTAR Portal', 'My Sejahtera', 'HiHive'],  # 15
          [40, 60, 80, 100],  # 16
          ['UTAR official website', 'UTAR Portal', 'WBLE', 'WBLE2'],  # 17
          ['Sungai Long', 'Kampar', 'Singapore', 'George Town'],  # 18
          ['Portal-->Academic Calender', 'WBLE', 'MS Teams', 'Portal-->Student Feedback'],  # 19
          ['WBLE 2', 'UTAR Portal', 'WBLE', 'Microsoft Teams'],  # 20
          ]
print('Welcome to the quiz!')
print('*' * 50)
print('This quiz is about the general knowledge about UTAR.')
input('Press ENTER to start your quiz!')
name = input('Enter your name: ')
print()

for i in range(20):
    print('Question %d.' % (i + 1), question[i])
    for j in range(4):
        print(letter[j], choice[i][j])
    option = input('Your Answer: ')
    stu_ans.append(option.upper())
    print()
print('Congratulation! You done all the questions in this quiz.')
input('Press ENTER to check your result')
print('#' * 50)

filename = name+'.txt'
with open(filename, 'w') as f:
    f.write('Name: ' + name + '\n' + '-' * 50 + '\n')
    f.write('\n')
    for item in stu_ans:
        f.write('%s\n' % item)
file = open(filename, 'r')
file = file.readlines()

stu_record = []
for line in file:
    stu_record.append(line.strip())
stu_record = stu_record[3:23]
for i in range(len(stu_record)):
    if stu_record[i] == answer[i]:
        score += 1
    else:
        print('Answer {0} is wrong'.format(i + 1), ';#Correct Answer: ', answer[i])

if score >= 15:
    result = 'PASSED'
else:
    result = 'FAILED'

print('-' * 50)
print('Total Number correct: ', score)
print('Total Number incorrect: ', (20-score))
print('-' * 50)
print('%s, you are %s with a score: %d' % (name, result, score))
print('#' * 50)