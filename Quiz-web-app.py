from tkinter import *
root=Tk()
root.geometry("500x300")
text=Text(root)

q=[
   "Who is the richest sportsperson in the world?",
   "Which country has more number of animals than humans?",
   "In which is cycling a common mode of transport?",
   "In which country is baseball played?",
]
options = [
    ["Floyd Mayweather","Christiano Ronaldo","Lionel Messi","Virat Kohli"],
    ["Australia","New Zealand","Zimbabwe","South Africa"],
    ["England","Ireland","Netherlands","France"],
    ["Germany","Sri Lanka","India","United States of America"],
          ]

a=[1,2,3,4]
Score=[1/4,2/4,3/4,4/4]
class Quiz:
      def __init__(self,master):
          self.option_selected = IntVar()
          self.question=0
          self.correct=0
          self.ques = self.create_q(master,self.question)
          self.opts = self.create_options(master,4)
          self.display_q(self.question)
          self.button = Button(root,text="Next",command=self.next_btn)
          self.button.pack(side=BOTTOM)

      def create_q(self,master,question):
         w=Label(master,text=q[question])
         w.pack(side=TOP)
         return w

      def create_options(self,master,n):
          b_val = 0
          b = []
          while b_val < n:
             btn = Radiobutton(master, text="foo", variable=self.option_selected ,value=b_val+1)
             b.append(btn)
             btn.pack(side=TOP, anchor="w")
             b_val= b_val+1
          return b

      def display_q(self,question):
           b_val = 0
           self.option_selected.set(0)
           self.ques['text'] = q[question]
           for op in options[question]:
               self.opts[b_val]['text'] = op
               b_val=b_val+1 

      def check_q(self,question):
          if(question >= len(a)):
              exit()
          if self.option_selected.get() == a[question]:
              return True
          return False
          

      def print_results(self,root):
          global q,number_of_questions
          number_of_questions= len(q)
          Label(root,text="Thanks for answering the questions." + str(self.correct) + " of " + str(number_of_questions) + " questions answered right").pack()
              


      def next_btn(self):
          if self.check_q(self.question): 
              
              self.correct+=1
              
                
          else:
             self.question=self.question+1
          if self.question >= len(q):
             self.print_results(root)
             self.button['state'] = 'disabled'
          else:
            self.display_q(self.question)


app=Quiz(root)
root.mainloop()          
                               
