from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import List, Text, Optional, Dict, Any, Generator
print(Action)

class PerfumeAPI:
    def search(self, info):
        return "Parfum moins cher"


class ActionPerformAction(Action):
    def name(self):
        return "action_Perform_action"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="performing action")
        perfume_api = PerfumeAPI()
        perfumes = perfume_api.search(tracker.get_slot("refund"))
        return [SlotSet("matches", perfumes)]


class ActionSearchOrder(Action):
    def name(self):
        return "action_Search_order"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Voici ce que j'ai trouvé:")
        dispatcher.utter_message(text=tracker.get_slot("order_nbr"))
        dispatcher.utter_message(
            text="is it ok for you? hint: I'm not going to find anything else :)"
        )
        return []

class ActionLookForCustomerFilel(Action):

    def name(self):
        return "action_Look_for_customer_file"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Je regarde votre dossier:")
        dispatcher.utter_message(text=tracker.get_slot("_Email_"))
        dispatcher.utter_message(
            text="is it ok for you? hint: I'm not going to find anything else :)"
        )
        return []

from pprint import pprint
import os

class ActionSave(Action):
    """Resets the tracker to its initial state.
    Utters the restart response if available."""

    def name(self):
        return "action_save"

    # def __init__(self) -> None:
    #     super().__init__("utter_restart", silent_fail=True)
    def build_content(self,user,agent,content="",turn = 1):
        if not user and not agent : 
            return content
        else : 
            print(content)
            content += f"turn : {turn}, user :{user[0]}, bot :{agent[0]}###"
            return self.build_content(user[1:], agent[1:], content, turn +1)


    def send(self,content):
        request = ('curl -X POST "https://unified.akio.cloud/aip/api/v1/thread" -H  "accept: application/json" -H  "Auth-Token: 3294a4ec-4953-42d7-b52e-fcaa75b65344" -H  "Authorization: Bearer 3294a4ec-4953-42d7-b52e-fcaa75b65344" -H  "Content-Type: application/json" -d "{\\"queueUuid\\": \\"e8690e25-5453-442e-b1a8-faf81baa7ec0\\",\\"subject\\": \\"Conversation Chatbot\\",\\"headers\\": {\\"From\\":\\"srumeur@akio.com\\"},\\"htmlBody\\": \\"'+content+'\\",\\"triggerRoutingEngine\\": true} "')
        print(request)
        os.system(request)

    def parse_events(self,events) : 
        out = {"user":[],"bot":[]}
        for elem in events : 
            if 'event' in elem : 
                if elem['event'] == 'user' and elem['text'] not in out['user'] :
                    out['user'].append(elem['text'])
                elif elem['event'] == 'bot' and elem['text'] not in out['bot'] :
                    out['bot'].append(elem['text'])
        out['bot'].insert(1, "Avez-vous d'autres questions ? ")

        return out

    def run (self, dispatcher, tracker, domain):
        events = tracker.events_after_latest_restart()

        out = self.parse_events(events)
        pprint(out)
        content = self.build_content(out['user'], out['bot'])
        print('\\')
        print(content)
        self.send(content)
