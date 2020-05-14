from rasa_sdk import Action
from rasa_sdk.events import SlotSet



class ActionPlacementstat(Action):
	def name(self):
    		return 'action_placementstat'    
	
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('branch')
		if  streams == 'cse':
			response1=""" We have a very good record of placing students from the Cse field,Every year atleast 99% of students get placed with median CTC 12 lakhs"""
			dispatcher.utter_message(response1)
			return [SlotSet('branch',"cse")]
		if	streams == 'ece':
			response2=""" We have a very good record of placing students from the Ece field,Every year atleast 70% of students get placed with median CTC 7 lakhs"""
			dispatcher.utter_message(response2)
			return [SlotSet('branch',"ece")]
class Actionfaculty(Action):
	def name(self):
		return 'action_faculty'    
	
	def run(self,dispatcher,tracker,domain):
		streams=tracker.get_slot('faculty')
		if	streams == 'sruthi':
			response1="""Ms. Sruthi N Paul is a faculty at cse department.Currently shes taking nlp to cs students.She is sitting in CSE staff room in main building.intercom no:6819 and email id is sruthinp@nitc.ac.in"""
			dispatcher.utter_message(response1)
			return [SlotSet('faculty',"sruthi")]