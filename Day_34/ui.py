THEME_COLOR = "#375362"
from tkinter import *  
from quiz_brain import QuizBrain
class Quiz_interface:
    
    def __init__(self,quizs_brain: QuizBrain):
        self.quiz = quizs_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.score = Label(text=f"Score : {self.quiz.score}",background=THEME_COLOR,foreground="white")
        self.score.grid(row=0,column=1,pady=20)

        self.canvans = Canvas(width=300,height=250,background="white")
        self.question = self.canvans.create_text( 150,
                                                 125, 
                                                 width=280,
                                                 text="Some question",
                                                 fill= THEME_COLOR,
                                                 font=("Arial",20,"italic"))
        self.canvans.grid(row=1,column=0,columnspan=2)

        self.next_question()


        self.image_corret = PhotoImage(file="./imagess/true.png")
        self.button_corret = Button(image=self.image_corret,highlightthickness=0,command=self.corret)
        self.button_corret.config(padx=20,pady=20)
        self.button_corret.grid(row=2,column=0,pady=50)

        self.image_incorret = PhotoImage(file="./imagess/false.png")
        self.button_incorret = Button(image=self.image_incorret,highlightthickness=0,command=self.incorret)
        self.button_incorret.grid(row=2,column=1)


        self.window.mainloop()

    def next_question(self):
        self.canvans.config(background='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvans.itemconfig(self.question,text=q_text)
        else:
            self.canvans.itemconfig(self.question,text="THE END OF THE QUESTION")
            self.button_corret.config(state="disabled")
            self.button_incorret.config(state="disabled")
    def corret(self):
        self.str = "True"
        self.check =  self.quiz.check_answer(self.str)
        self.feed_back(self.check)

    def incorret(self):
        self.str = "False"
        self.check = self.quiz.check_answer(self.str)
        self.feed_back(self.check)

    def feed_back(self,boolean):
        if boolean:
            self.canvans.config(background="green")

        else:
            self.canvans.config(background="red")            
        
        self.window.after(1000,self.next_question)