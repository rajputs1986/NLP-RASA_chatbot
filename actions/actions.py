# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("You are in action_hello_world.")
        dispatcher.utter_message(text="This is Hello World action!")

        return []

class ActionSearchRestrorant(Action):

    def name(self) -> Text:
        return "action_search_restrorant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]
        print(entities)

        for e in entities:
            if(e["entity"]=="cusuine"):
                name = e["value"]
            
            if(name=="indian"):
                message = "indian1, indian2, indian3"
            if(name=="chinese"):
                message = "chinese1, chinese2, chinese3"
            if(name=="italian"):
                message = "italian1, italian2, italian3"

        dispatcher.utter_message(text=message)

        return []

class ActionSearchCapital(Action):

    def name(self) -> Text:
        return "action_search_capital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot("country")
        print(country)

        capital = ""
        if(country=="india"):
            capital = "capital is delhi"
        if(country=="china"):
            capital = "capital is beijing"
        if(country=="US"):
            capital = "capital is NY"

        dispatcher.utter_message(text=capital)

        return [SlotSet("capital", capital)]