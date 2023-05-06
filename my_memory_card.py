#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.resize(600, 400)
text = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Негры')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат теста')
correct = QLabel('Правильно или неправильно')
r_answer = QLabel('чулымцы')
vline3 = QVBoxLayout()
vline3.addWidget(correct)
vline3.addWidget(r_answer)
AnsGroupBox.setLayout(vline3)
AnsGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

vline2 = QVBoxLayout()


vline2.addWidget(text)
vline2.addWidget(RadioGroupBox)
vline2.addWidget(AnsGroupBox)
vline2.addWidget(button)

main_win.setLayout(vline2)

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3


main_win.cur_question = -1



def next_question():
    cur_question = randint(0,len(question_list)-1)     
    q = question_list[cur_question]   
    main_win.total += 1
    ask(q)
    print('Статистика:') 
    print('Всего вопросов:',main_win.total)
    print('Правильных ответов:',main_win.score)

def Show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def Show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle (answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    Show_question()

def check_answer():
    if answers[0].isChecked():  
        show_correct('Правильно')     
        main_win.score += 1  
    else:
        if answers[0].isChecked() or answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
    print('Статистика:') 
    print('Всего вопросов:',main_win.total)
    print('Правильных ответов:',main_win.score)
    print('Рейтинг:', main_win.score/main_win.total*100)

def show_correct(result):
    correct.setText(result)
    Show_result()  

question_list = []
q = Question('Государственный язык бразилии', 'португальский', 'неформальский','астралопитекский','БравлСтарский')
question_list.append(q)
question_list.append(Question('в каком году изобрели попит','2021','1965','1245','4 век до Н.Э'))
question_list.append(Question('вчера играл с дедом в шахматы...','а он коня двинул','и он победил меня', 'у меня нет деда','сидит лось на рельсах'))
question_list.append(Question('сидит лось на рельсах. К нему подходит другой лось, и говорит...','подвинься','ухади','-смачно рыгнул-','будешь мухомор?'))
question_list.append(Question('какой ответ правильный?','правильный','никакой','бебебе','бамбалейла'))
question_list.append(Question('опути нипутю','ну кому я говорю','фу фигня','-смачно отрыгнул-','милана пон'))
question_list.append(Question('продам гараж в челябинске','в лс','в личные сообщения','в директ','мне не нужен гараж'))
question_list.append(Question('erhyr8f0t2gier3hjvf','hyawfetdft','iwyuetf8o','iuywefyywf','wsihuyyedfruycw8y76t'))
question_list.append(Question('Почему буратино поехал на кавказ?','потому что на кавказе могут вырезать семью', 'потому что толстая свинья', 'а мне пофег', 'я хз'))





main_win.score = 0
main_win.total = 0
next_question()

button.clicked.connect(click_OK)
main_win.show()
app.exec()
