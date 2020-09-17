from rasa_sdk import Action
from rasa_sdk.events import SlotSet


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
class ActionSearchProduct(Action):
    def name(self):
        return "action_search_product"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Voici ce que j'ai trouvé:")
        dispatcher.utter_message(text=tracker.get_slot("article"))
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