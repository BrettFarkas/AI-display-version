#  AI Class
 
#TO DO: bypass "create good neuron" for tic tac toe program

#########################################################################################
def testmethod(): #testing out importing the file
	return "Hello World"

#########################################################################################


from datetime import datetime
now = 0
#now = datetime.now()
#mm = str(now.month)
#dd = str(now.day)
#yyyy = str(now.year)
#hour = str(now.hour)
#mi = str(now.minute)
#ss = str(now.second)
#microsecond = now.microsecond
#print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss

#hour = now.hour
#second = now.second

##########################################################################################

currentlyActiveNeurons = [] #for faster iterating through active neurons, add when active, delete when not
topOfTheChainList = []
newlyActivatedList = []

##########################################################################################
class Neuron: 
	def __init__(self, value):
		global now
		self.value = value #this keeps track of the object # (is this necessary in a list??)
		self.neuronActive = 0	
		self.neuronActivationThreshold = 1
		self.neuronNewlyActivated = 0	
		self.inhibited = 0
		self.neuronActivatedTime = now
		self.goodNeuronActivatingOthersStartTime = 0
		self.goodPartialNeuronActivatedOthers = 0
		self.neuronCurrentActivationLevel = 0
		self.outgoingNeuronsConnectedTo = {} #dictionary contains value'OutgoingNeuronStrength' (default is .5)
		self.incomingNeuronsConnectedTo = {} 
		self.incomingNeuronsActivated = []#to figure out how many in the chain have been activated, need to use this when a neuron is first activated, send it out to this array
		self.outgoingNeuronsActivated = []

		self.alreadyPriorConnectedTo = [] #list in 2nd neuron that is is already connected to 1st so you don't make a duplicate 3rd

		self.secondIncomingConnectedTo = -1 #3rd neuron stores 2's location to steal top of chain from it
		self.unlocked = 0
		self.good = 0
		self.simultaneousNeuronsConnectedTo = []#when it is lit simultaneously with others that are not at the top of a chain
		self.topOfTheChain = 0
		self.strengthenedAlready = 0#a switch so it only strengthens once

	def get(self):
		return self.value #this returns the object # in the neuronList[]

	def makeCurrentlyActiveNeuronsList(self):
		if self.neuronActive == 1:
			if self.get() not in currentlyActiveNeurons:
				currentlyActiveNeurons.append(self.get())	

	def makeNewlyActivatedList(self):
		if self.neuronNewlyActivated == 1:	
			if self.get() not in newlyActivatedList:
				newlyActivatedList.append(self.get())

	def makeTopOfTheChainAndAddToList(self):
		self.topOfTheChain = 1
		if self.get() not in topOfTheChainList:	
			topOfTheChainList.append(self.get())
		

	def stealTopOfTheChainFromBelow(self):
		for incoming in self.incomingNeuronsActivated:		
			if neuronList[incoming].topOfTheChain == 1:
				neuronList[incoming].topOfTheChain == 0
				if incoming in topOfTheChainList:
					topOfTheChainList.remove(incoming)

	def removeTopOfTheChainAndFromList(self):
		if self.topOfTheChain == 1:
			self.topOfTheChain = 0 #deactivate top of chain
			if self.value in topOfTheChainList:
				topOfTheChainList.remove(self.value) #remove from top of chain list


	def activateOutgoingNeurons(self): #if it's newly activated it does this
		for key,level in self.outgoingNeuronsConnectedTo.items():
			neuronList[key].neuronCurrentActivationLevel += level #add activation to outgoing neurons

			neuronList[key].incomingNeuronsActivated.append(self.get())

	def checkWeightsAndUnlock(self): #this adds incoming activation amounts & activates the neuron 
		if self.neuronCurrentActivationLevel >= self.neuronActivationThreshold: 
			if self.neuronActive == 0 and self.neuronNewlyActivated == 0: #if it's not already active
				if self.secondIncomingConnectedTo not in currentlyActiveNeurons:	
					self.unlocked = 1
					

	def finallyActivateIfUnlocked(self):	
		if self.unlocked == 1:
			
			if self.secondIncomingConnectedTo in currentlyActiveNeurons:
				activateANewNeuronMethod(self.get())
				self.strengthenConnections()

	def strengthenConnections(self):
		if self.strengthenedAlready == 0:
			self.strengthenedAlready = 1
			#increase incoming activated strengths and also self threshhold
			for key in self.incomingNeuronsConnectedTo.keys(): #look at all incoming neurons
				if key in currentlyActiveNeurons:	#if it is active
					neuronList[key].outgoingNeuronsConnectedTo[self.get()] += 1 
					print "Hello"

			self.neuronActivationThreshold += 1
			if self.neuronCurrentActivationLevel > self.neuronActivationThreshold:
				self.neuronActivationThreshold = self.neuronCurrentActivationLevel #change this to activation level if it is bigger?????????????????????????????????????????????
			

	def removeActivationFromUpperNeurons(self):
		for key,level in self.outgoingNeuronsConnectedTo.items(): #lower activation of upper neurons
			neuronList[key].neuronCurrentActivationLevel -= level 
			if neuronList[key].neuronCurrentActivationLevel < 0:
				neuronList[key].neuronCurrentActivationLevel = 0
			neuronList[key].incomingNeuronsActivated.remove(self.get())#remove from upper neurons activated list

	def deactivateMethod(self): #turn off, remove from lists, lower activation of upper neurons
		global now
		if now - self.neuronActivatedTime >= 3: # if it has been active 3 seconds
			
			self.neuronActive = 0	 #deactivate neuron
			currentlyActiveNeurons.remove(self.value) #remove neuron from neuron active list

			self.removeTopOfTheChainAndFromList()
			
			self.removeActivationFromUpperNeurons()

			self.unlocked = 0 # relock it
			self.inhibited = 0 #turn off the inhibitor
			self.strengthenedAlready = 0 #turn off strengthening switchoff
###################################################################################################################
	#CHECKING THE GOOD NEURONS
	def checkGoodNeurons(self):	#If GOOD is even partially activated, activate all of the incoming neurons
				#in the future can selectively activate only motor neurons
		if self.good == 1:	
			if self.neuronCurrentActivationLevel > 0 and self.neuronCurrentActivationLevel < self.neuronActivationThreshold:
				self.activateGoodIncoming()
	

	def activateGoodIncoming(self): #activate all incoming neurons
		global now
		if self.goodPartialNeuronActivatedOthers == 0:
			#"if good and is half-activated (or even partially?) then activate all the incoming neurons (and ones below those all the way down?)"
			#"if going all the way down to the base, can put it in a while loop"
			for key in self.incomingNeuronsConnectedTo.keys():
				if key not in newlyActivatedList and key not in currentlyActiveNeurons:
					neuronList[key].inhibited = 1
					activateANewNeuronMethod(key)					
					self.goodPartialNeuronActivatedOthers = 1
					self.goodNeuronActivatingOthersStartTime = now
					

	def allowActivationOfGoodNeuronAgain(self):
		global now
		if now - self.goodNeuronActivatingOthersStartTime >= 4: #a longer time than lower neurons are activated
			self.goodPartialNeuronActivatedOthers = 0			
	
		

	def weakenConnections(self):
		pass #increase threshhold


#####################################################################################################
# ACTIVATE  ACTIVATE ACTIVATE ACTIVATE ACTIVATE ACTIVATE ACTIVATE ACTIVATE ACTIVATE ACTIVATE
def activateANewNeuronMethod(neuronnumber):#activate a neuron (from another import program)
		global now
		if neuronList[neuronnumber].neuronActive == 0 and neuronList[neuronnumber].neuronNewlyActivated == 0:#if it's not already active
			neuronList[neuronnumber].neuronNewlyActivated = 1
			neuronList[neuronnumber].neuronActivatedTime = now
			neuronList[neuronnumber].makeTopOfTheChainAndAddToList()

def checkNewlyActivatedToMakeNewThirdNeuron():
	for second in newlyActivatedList:
		
		if neuronList[second].topOfTheChain ==1: #if it is a top of the chain
		#look in the back connected to in new neuron and compare with active neuron list 
		#if there is a new connection to be made:
			if neuronList[second].inhibited == 0: #if it isn't inhibited from good neuron activation
				for first in currentlyActiveNeurons:
					if neuronList[first].topOfTheChain == 1 : #if they are both top of the chain			
						if first not in neuronList[second].alreadyPriorConnectedTo: #check to see if a third connection exists already
							if first not in neuronList[second].incomingNeuronsConnectedTo.keys():
								createNewThirdNeuron(first,second)
					

def calculateThresholdValue():

	threshold = len(currentlyActiveNeurons) + 1	
	return threshold

def createNewThirdNeuron(first,second):
	global now
	global neuronList

	newvalue = len(neuronList)
	neuronList += [Neuron(newvalue)]

	
	neuronList[newvalue].neuronActivationThreshold = calculateThresholdValue()
	
	
	for oldNeurons in currentlyActiveNeurons:
		neuronList[newvalue].incomingNeuronsConnectedTo[oldNeurons]= 1  #add incoming neurons with their weights to dictionary

		neuronList[newvalue].secondIncomingConnectedTo = second #add to second incoming

		neuronList[second].alreadyPriorConnectedTo.append(oldNeurons) #add 1st to 2nd so don't make duplicate 3rd

		neuronList[oldNeurons].outgoingNeuronsConnectedTo[newvalue] = 1 #add 3rd neuron to 1st outgoing list

		neuronList[newvalue].neuronCurrentActivationLevel += 1  #add first's activation to new neuron
		neuronList[newvalue].incomingNeuronsActivated.append(oldNeurons)#add first to new incoming list

		neuronList[oldNeurons].removeTopOfTheChainAndFromList()
		neuronList[second].removeTopOfTheChainAndFromList()
		neuronList[newvalue].makeTopOfTheChainAndAddToList()

	neuronList[newvalue].incomingNeuronsConnectedTo[second]= 1 #add the newly activated neuron to the incoming list
	neuronList[second].outgoingNeuronsConnectedTo[newvalue] = 1 #add 3rd neuron to 2nd outgoing list??????????
	neuronList[newvalue].neuronActivatedTime = now

	activateANewNeuronMethod(newvalue) #ACTIVATE THE NEW 3RD NEURON
	
def makeNeuronActive(neuronnumber):
		neuronList[neuronnumber].neuronNewlyActivated = 0 #deactivate newly active
		newlyActivatedList.remove(neuronnumber) #remove from newly activated list
		neuronList[neuronnumber].neuronActive = 1 #activate neuron
		
#######################################################################################
# GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD
def createGoodNeuron(neuronnumber): #determine what kind of neuron gets called 'Good'
	if neuronnumber.topOfTheChain == 1:
		if 4 in neuronnumber.incomingNeuronsConnectedTo.keys(): #right now, 4 active is 'good' but it could be anything
			if neuronnumber.good == 0:
				neuronnumber.good = 1
	
	
#####################################################################################################
#######################################################################################
#Create the original neurons

neuronList = []
for value in range(0,5):
	neuronList += [Neuron(value)]

for index in range(0,len(neuronList)):
	print neuronList[index].get()


######################################################################################
######################################################################################
# MAIN BRAIN MAIN BRAIN MAIN BRAIN MAIN BRAIN MAIN BRAIN MAIN BRAIN MAIN BRAIN MAIN BRAIN
then = 0
now = 0

def mainBrainMethod(): #main control (include the clock and iterates through neurons) (activated continuously in ais program)
	global then
	global now
	global timenow
	fulltime = datetime.now()
	timenow = fulltime.second
	if timenow != then:
		then = timenow
		now += 1 #now is the number of seconds that have passed


	iterateThroughNeuronsMakeActiveList() #make 'Active' list

############################################################################################
# ITERATE THROUGH NEURONS
def iterateThroughNeuronsMakeActiveList(): #This one is outside the class
	
			#iterate through the neurons, connect neurons that are together 
			#could iterate in 'levels' so that connections are only made one level at 
			# a time, though that may be a mistake.  could try it later on.
			# Also, deactivate expired neurons here
	
	
	for i in neuronList: 
		i.checkWeightsAndUnlock() #if weight is above threshhold
		i.makeNewlyActivatedList()
		i.finallyActivateIfUnlocked()
		i.makeCurrentlyActiveNeuronsList()		
		
		if i.get() in newlyActivatedList:
			checkNewlyActivatedToMakeNewThirdNeuron() #check newly active list to make a 3rd neuron

			makeNeuronActive(i.get()) #make it officially active
			
			i.makeTopOfTheChainAndAddToList()
			i.stealTopOfTheChainFromBelow()

			i.activateOutgoingNeurons() #activate outgoing neurons (do last to avoid accidental pairing)

		createGoodNeuron(i)
		i.checkGoodNeurons()#check for good activation
		i.allowActivationOfGoodNeuronAgain()#so good neuron isn't constantly being activated			
				
		if i.get() in currentlyActiveNeurons: #if it is active
			i.deactivateMethod()	#check time for deactivation


#to add:
# short term memory for top of chain list, memorize every 30 seconds or so.  Use it for good reinforcing. With dictionary values that can be adjusted.			
#need to remember the order of large number of neurons for back activating??
#may need to go through all neurons at regular intervals so that some are simultaneous, and only before/after if enough time has passed between them
# modules of 100 neurons that top off and then connect to one another
		


