#PLANS TO DO:
#ALPHABET LETTERS AS 26 NEURONS - HAVE PROGRAM READ IN SEQUENCE
#TIC TAC TOE
# SIMPLE AVOIDANCE GAME                                        
#ARDUINO AVOIDANCE
#SIMPLE POSITIVE REINFORCEMENT
#ARDUINO POSITIVE REINFORCEMENT


from Tkinter import *



master = Tk()

master.title("AI Test Program")



import ai


####################################################################
#testing out importing a method
x = ai.testmethod()
print str(x)
####################################################################


def display():
	global color0
	global color1
	global color2
	global color3
	global color4
	text.delete(1.0,END)

	text.insert(INSERT, '#')
	text.insert(INSERT, '\t')
	text.insert(INSERT, 'State')
	text.insert(INSERT, '\t')
	text.insert(INSERT, 'Level')
	text.insert(INSERT, '\t')
	text.insert(INSERT, 'Threshold')
	text.insert(INSERT, '\t')
	text.insert(INSERT, 'Incoming / Weight Value')
	text.insert(INSERT, '\t')
	#text.insert(INSERT, 'Level Now')
	#text.insert(INSERT, '\t')

	for x in ai.neuronList:
		text.insert(INSERT, '\n')
		text.insert(INSERT, x.get())

		text.insert(INSERT, '\t')
		data = x.neuronActive 
		text.insert(INSERT, str(data))#neuron state

		text.insert(INSERT, '\t')		
		level = x.neuronCurrentActivationLevel
		text.insert(INSERT, str(level))#activatio level

		text.insert(INSERT, '\t')		
		level = x.neuronActivationThreshold
		text.insert(INSERT, str(level))#activatio level

		text.insert(INSERT, '\t')
		text.insert(INSERT, '\t')
		incoming = x.incomingNeuronsConnectedTo
		text.insert(INSERT, str(incoming))#incoming
	
		#text.insert(INSERT, '\t')
		#text.insert(INSERT, '     ')
		#levelnow = x.neuronCurrentActivationLevel
		#text.insert(INSERT, str(levelnow))#current activation level

	text2.delete(1.0,END)
	
	text2.insert(INSERT, str(ai.now))#Seconds elapsed
	text2.insert(INSERT, '\n')
	text2.insert(INSERT, 'Active Neurons: ')
	text2.insert(INSERT, str(ai.currentlyActiveNeurons))
	text2.insert(INSERT, '\n')
	text2.insert(INSERT, 'Top Of The Chain List: ')
	text2.insert(INSERT, str(ai.topOfTheChainList))
	text2.insert(INSERT, '\n')

	#text2.insert(INSERT, ai.neuronList[4].get())



	brainActive() #turn the brain on
	
	master.after(1,display)

master.after(1, display)


def brainActive(): #activates the mainBrainMethod in ai.py
	ai.mainBrainMethod()

####################################################################

####################################################################

def method0(): #a button activates this method
	ai.activateANewNeuronMethod(0)

	


def method1(): #a button activates this method
	ai.activateANewNeuronMethod(1)

	


def method2(): #a button activates this method
	ai.activateANewNeuronMethod(2)

def method3(): #a button activates this method
	ai.activateANewNeuronMethod(3)

	
def method4(): #a button activates this method
	ai.activateANewNeuronMethod(4)
	






def answermethod(typedin): #what you typed into the entry gets sent here

	data= text3.get()

	text3.delete(0,END)



	text.insert(INSERT, "You just typed something and pressed enter!")

	text.insert(INSERT, "\n")

	text.insert(INSERT, "You said: " + str(data) )





##################################################################################

#LABEL

global v

v=StringVar()

r = StringVar()

#text.insert(INSERT, "Num is 0")

entryLabel = Label(master,textvariable=v)

#entryLabel["text"] = "Hello"

entryLabel.grid(row=5,column=2)



v.set("Hello, here is a label") #this is a random label that doesn't actually do anything



entryLabel2 = Label(master,textvariable=r)

entryLabel2.grid(row=8,column=1,columnspan = 3)

r.set("Type something and press enter:") #this is a random label that doesn't actually do anything

################################################################################





	





#################################################################################

def delete(): #to delete the textboxes, you could make a button call this method, right now nothing is activating it

	text2.delete (1.0,END)

	text.delete (1.0,END)

	

################################################################################









#this creates the GUI for the computer program



text = Text(master,width=105, height=40, bg="white", wrap="word") #creates a text box

text2 = Text(master, width=30, height=10, bg="white", wrap="word") #creates another text box



#global x #the variable that the radio buttons toggle

x=IntVar()

rad=Radiobutton(master, text="A Button", variable=x, value=1,command=method3) #this is called a radio button

#rad.grid(row=3,column=1,rowspan=1, sticky=N+E+S+W)





rad2=Radiobutton(master, text="delete all", variable=x, value=2,command=delete) #this is called a radio button

#rad2.grid(row=3,column=2,rowspan=1, sticky=N+E+S+W)

color0 = "lightgreen"
color1 = "lightgreen"
color2 = "lightgreen"
color3 = "lightgreen"
color4 = "lightblue"

#BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON BUTTON 
def plotButtonsMethod():
	global color0
	global color1
	global color2
	global color3
	global color4
	####################################################################
	new = Button(master, text= "Neuron 0", bd=10,bg=color0, command=method0) #calls method0
	new.grid(row=1, column=1, rowspan=1, columnspan=3, sticky=N+E+S+W)
	####################################################################

	####################################################################
	new = Button(master, text= "Neuron 1", bd=10,bg=color1, command=method1) #calls method 1
	new.grid(row=2, column=1, rowspan=1, columnspan=3, sticky=N+E+S+W)
	####################################################################

	####################################################################
	new = Button(master, text= "Neuron 2", bd=10,bg=color2, command=method2) #calls method 2
	new.grid(row=3, column=1, rowspan=1, columnspan=3, sticky=N+E+S+W)
	####################################################################

	####################################################################
	new = Button(master, text= "Neuron 3", bd=10,bg=color3, command=method3) #calls method 3
	new.grid(row=4, column=1, rowspan=1, columnspan=3, sticky=N+E+S+W)
	####################################################################

	####################################################################
	new = Button(master, text= "GOOD", bd=10,bg=color4, command=method4) #calls method 4
	new.grid(row=5, column=1, rowspan=1, columnspan=3, sticky=N+E+S+W)
	####################################################################
plotButtonsMethod()

text.grid(row=0, column=4, sticky=N+E+S+W, padx=3, pady=3, rowspan=20, columnspan=9) #places the text box on the grid

text2.grid(row=6, column=1, columnspan=3) #places the second text box on the grid



######################################################################

#make the entry box

data = 1

text3 = Entry(master, width=20, bg="white", font=35, textvariable=data) #create the entry box



text3.bind('<Return>', answermethod) #makes it so you can press enter to send information

text3.bind('<KP_Enter>',answermethod)

text3.grid(row=9, column=1, columnspan =3) #puts the entry box on the grid









mainloop() 









