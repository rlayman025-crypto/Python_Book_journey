import shelve,random,copy,os
from pathlib import Path

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]
capitals = [
    "Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento",
    "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta",
    "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines",
    "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis",
    "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City",
    "Helena", "Lincoln", "Carson City", "Concord", "Trenton",
    "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus",
    "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia",
    "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier",
    "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"
]


for j in range(35):
    for i in range(50):
        quiz= f'\n{i+1} what is the capital for this US state'
        quiz+=' '+states[i]+':'
        options=[]
        wrong_choices=capitals.copy()
        wrong_choices.remove(capitals[i])
        options.append(capitals[i])
        while len(options)<4:
            wrong_choice=random.choice(wrong_choices)
            if wrong_choice not in options:
                options.append(wrong_choice)
            else:
                continue
            
        random.shuffle(options)
        for whatever in range(4):
            quiz+= f'\n{whatever+1} - {options[whatever]}'
    
        quiz_answers=''
        quiz_answers+=f'\n{i+1} what is the capita for this US state'
        quiz_answers+=' '+states[i]+':'
        quiz_answers+='\nanswer -->\n'+ capitals[i]
        exams_path=r'C:\Users\Ayman\Desktop\my_stuff\exams'
        exams_answers_path=r'C:\Users\Ayman\Desktop\my_stuff\exams_answers'
        file=f'exam{j+1}.txt'
        with open(exams_path +'\\'+ file ,'a',encoding="UTF-8") as exam:
            exam.write(quiz)
        file=f'exam_answers{j+1}.txt'
        with open(exams_answers_path +'\\'+ file,'a',encoding='UTF-8') as exam_answer:
            exam_answer.write(quiz_answers)

        # This next commented code was slowing the program , because it was constantly changing the program's cwd 3500 during the program execution
        # the code above DOESN'T do this , 

        # os.chdir(r'C:\Users\Ayman\Desktop\my_stuff\exams')
        # file=f'exam{j+1}.txt'
        # with open(file , 'a',encoding='UTF-8') as exam:
        #     exam.write(quiz)
        # os.chdir(r'C:\Users\Ayman\Desktop\my_stuff\exams_answers')
        # file=f'exam_answers{j+1}.txt'
        # with open(file,'a',encoding='UTF8') as exam_answer:
        #     exam_answer.write(quiz_answers)
        # print(file)

