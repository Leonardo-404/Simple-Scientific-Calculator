import tkinter as tk
from math import *

class Calculator:
	def __init__(self, master):
		# expression that will be displayed on screen
		self.expression = ""
		# be used to store data in memory
		self.recall = ""
		# used to switch between units of rad,deg and grad
		self.inv_convert_constant = ""
		self.convert_constant = ""
		# self.answer
		self.sum_up = ""
		# create string for text input
		text_Input = tk.StringVar()
		# assign instance to master
		self.master = master
		# set frame showing inputs and title
		top_frame = tk.Frame(master, width=650,height = 20, bd=4, relief='flat',bg = '#666666')
		top_frame.pack(side=tk.TOP)
		# set frame showing all buttons
		bottom_frame = tk.Frame(master, width=650, height = 470, bd=4, relief='flat',bg = '#666666')
		bottom_frame.pack(side=tk.BOTTOM)
		# name of calculator
		my_item = tk.Label(top_frame,text="Simple Scientific Calculator", font=('arial',14),fg='white',width=26,bg = '#666666')
		my_item.pack()
		# entry interface for inputs
		txtDisplay = tk.Entry(top_frame,font=('arial',36),relief='flat',bg = '#666666',fg='white',textvariable = text_Input,width=60,bd=4,justify = 'right')
		txtDisplay.pack()

		# row 0 
		# left bracket button
		btn_left_brack = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="(",relief='flat', command=lambda: btnClick('(')).grid(row=0, column=0)
		# right bracket button
		btn_right_brack = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),
		width=2, height=2,relief='flat',text=")", command=lambda: btnClick(')')).grid(row=0, column=1)
		# takes e to some exponent that you insert into the function
		btn_exp = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="exp", command=lambda: btnClick('exp(')).grid(row=0, column=2)
		# constant pi
		btn_pi = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),
		width=2, height=2,relief='flat', text="π", command=lambda: btnClick('pi')).grid(row=0, column=3)
		# clears self.expression
		btn_clear = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="C",relief='flat', command=lambda: btnClearAll()).grid(row=0, column=4)
		# deletes last string input
		btn_del = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="del",relief='flat', command=lambda: btnClear1()).grid(row=0, column=5)
		# inputs a negative sign to the next entry
		btn_change_sign = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),
		width=2, height=2,relief='flat',text="+/-", command=lambda: change_signs()).grid(row=0, column=6)
		# division
		btn_div = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="÷",relief='flat', command=lambda: btnClick('/')).grid(row=0, column=7)
		# square root
		btn_sqrt = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="sqrt", command=lambda: btnClick('sqrt(')).grid(row=0, column=8)

		# row 1
		# changes trig function outputs to degrees
		btn_Deg = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="Deg",relief='flat', command=lambda: convert_deg()).grid(row=1, column=0)
		# changes trig function outputs to default back to radians
		btn_Rad = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,text="Rad",relief='flat', command=lambda: convert_rad()).grid(row=1, column=1)
		# changes trig function outputs to gradians
		btn_root_of = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="x√ ",relief='flat', command=lambda:btnClick('**(1/')).grid(row=1, column=2)
		# takes the absolute value of an expression
		btn_abs = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat', text="abs", command=lambda: btnClick('abs' + '(')).grid(row=1, column=3)
		# seven
		btn_7 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="7", relief='flat',command=lambda: btnClick(7)).grid(row=1, column=4)
		# eight
		btn_8 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="8",relief='flat', command=lambda: btnClick(8)).grid(row=1, column=5)
		# nine
		btn_9 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="9",relief='flat', command=lambda: btnClick(9)).grid(row=1, column=6)
		# multiplication
		btn_mult = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="x", command=lambda: btnClick('*')).grid(row=1, column=7)
		# 'memory clear' button. Wipes self.recall to an empty string
		btn_MC = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="MC",relief='flat',command=lambda:memory_clear()).grid(row=1,column=8)

		# row 2
		# sin function that returns value from -1 to 1 by default
		btn_sin = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="sin",relief='flat',command=lambda:btnClick('sin(' + self.convert_constant)).grid(row=2,column=0)
		# cos function that returns value from -1 to 1 by default
		btn_cos = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="cos",relief='flat', command=lambda: btnClick('cos(' + self.convert_constant)).grid(row=2, column=1)
		# tan function
		btn_tan = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2,
		height=2,relief='flat',text="tan", command=lambda: btnClick('tan(' + self.convert_constant)).grid(row=2, column=2)
		#
		btn_log = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="log",relief='flat',command=lambda:btnClick('log(')).grid(row=2,column=3)
		# four
		btn4 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="4",relief='flat', command=lambda: btnClick(4)).grid(row=2, column=4)
		# five
		btn5 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="5",relief='flat', command=lambda: btnClick(5)).grid(row=2, column=5)
		# six
		btn6 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="6",relief='flat', command=lambda: btnClick(6)).grid(row=2, column=6)
		# seven
		btnSub = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="-",relief='flat',command=lambda:btnClick('-')).grid(row=2,column=7)
		# outputs what is in self.recall
		btn_MR = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="MR",relief='flat', command=lambda: memory_recall()).grid(row=2, column=8)
		
		# row 3
		# sin inverse function
		btn_sin_inverse = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="sin^-1",relief='flat',command=lambda:btnClick(self.inv_convert_constant + 'asin(')).grid(row=3,column=0)
		# cos inverse function
		btn_cos_inverse = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="cos^-1",relief='flat',command=lambda:btnClick(self.inv_convert_constant + 'acos(')).grid(row=3,column=1)
		# tan inverse function
		btn_tan_inverse = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="tan^-1",relief='flat',command=lambda:btnClick(self.inv_convert_constant + 'atan(')).grid(row=3,column=2)
		# takes the natural log
		btn_ln = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="ln",relief='flat',command=lambda:btnClick('log1p(')).grid(row=3,column=3) 
		# one
		btn1 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="1",relief='flat', command=lambda: btnClick(1)).grid(row=3, column=4)
		# two
		btn2 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="2",relief='flat', command=lambda: btnClick(2)).grid(row=3, column=5)
		# three
		btn3 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#4d4d4d', font=('arial', 18), width=2, height=2,
		text="3",relief='flat', command=lambda: btnClick(3)).grid(row=3, column=6)
		# addition
		btn_add = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="+",relief='flat', command=lambda: btnClick('+')).grid(row=3, column=7)
		# adds current self.expression to self.recall string
		btn_M_plus = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="M+",relief='flat', command=lambda: memory_add()).grid(row=3, column=8)
		
		# row 4
		# factorial function
		btn_fact = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text="n!",relief='flat',command=lambda:btnClick('factorial(')).grid(row=4,column=0)
		# square function
		btn_sqr = tk.Button(bottom_frame,padx=16,pady=1,bd=4,fg='white',bg = '#666666',font =('arial',18),width=2,height=2,
		text=u"x\u00B2",relief='flat',command=lambda:btnClick('**2')).grid(row=4,column=1) 
		# to the power of function
		btn_power = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text="x^y",relief='flat', command=lambda: btnClick('**')).grid(row=4, column=2)
		# stores previous expression as an answer value
		btn_ans = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18), width=2, height=2,
		text="ans",relief='flat',command=lambda:answer()).grid(row=4, column=3)
		# zero
		btn_0 = tk.Button(bottom_frame, padx=16, pady=1, bd=5, fg='white',bg = '#4d4d4d', font=('arial', 18),width=7, height=2,
		text="0",relief='flat', command=lambda: btnClick(0))
		btn_0.grid(row=4, column=4,columnspan=2)
		# equals button
		btn_eq = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#ff9980', font=('arial', 18), width=2, height=2,
		text="=",relief='flat',command=lambda:btnEqual()).grid(row=4, column=6)
		# decimal to convert to float
		btn_dec = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text=".",relief='flat', command=lambda: btnClick('.')).grid(row=4, column=7)
		# comma to allow for more than one parameter!
		btn_comma = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white',bg = '#666666', font=('arial', 18),width=2, height=2,
		text=",",relief='flat', command=lambda: btnClick(',')).grid(row=4, column=8)

		# functions
		# allows button you click to be put into self.expression
		def btnClick(expression_val):
			self.expression = self.expression + str(expression_val)
			text_Input.set(self.expression)
		# clears last item in string
		def btnClear1():
			self.expression = self.expression[:-1]
			text_Input.set(self.expression)
		# adds in a negative sign
		def change_signs():
			self.expression = self.expression + '-'
			text_Input.set(self.expression)
		# clears memory_recall
		def memory_clear():
			self.recall = ""
		# adds whatever is on the screen to self.recall
		def memory_add():
			self.recall = self.recall + '+' + self.expression
		# uses whatever is stored in memory_recall
		def answer():
			self.answer = self.sum_up
			text_Input.set(self.expression + self.answer)
		# uses whatever is stored in memory_recall
		def memory_recall():
			if self.expression == "":
				text_Input.set('0' + self.expression + self.recall)
			else:
				text_Input.set(self.expression + self.recall)
		# changes self.convert_constant to a string that allows degree conversion when button is clicked
		def convert_deg():
			self.inv_convert_constant = "degrees("
			self.convert_constant = '(radians('
		# allows self.convert_constant to be empty so that it defaults back to radians
		def convert_rad():
			self.convert_constant = ""
		# changes self.convert_constant to a string that allows gradian conversion when button is clicked
		# clears self.expression
		def btnClearAll():
			self.expression = ""
			text_Input.set("")
		# converts self.expression into a mathematical expression and evaluates it
		def btnEqual():
			self.sum_up = str(eval(self.expression))
			text_Input.set(self.sum_up)
			self.expression = ""

# tkinter layout
root = tk.Tk()
b = Calculator(root)
root.title("Simple Scientific Calculator")
root.geometry("650x490+50+50")
root.resizable(False,False)
root.mainloop()