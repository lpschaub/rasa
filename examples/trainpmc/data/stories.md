## story_1
* deliveryCost{"fdp": "frais de port","free": "0 €","email": "_Email1_"}
 - slot{"fdp":"frais de port"}
 - utter_deliveryCost_ProvideInfo
* goodbye{"mood":"dommage"}
 - utter_goodbye
 - action_save

## New Story2

* PaymentRefused{"payment":"régler"}
    - utter_PaymentRefused_ProvideInfo
* PaymentTool{"tool":"PayPal"}
	- slot{"paypal":"PayPal"}
    - utter_PaymentRefused_ProvideInfo_Offeralternative
* thanks
    - utter_goodbye
    - action_save

## New Story3

* ProductAvailable{"email":"_Email1_","article":"womanity EAU de parfum spray","target":"amie","reload":"rechargeable"}
    - slot{"email":"_Email1_"}
    - slot{"article":"womanity EAU de parfum spray"}
    - slot{"target":"amie","reload":"rechargeable"}
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* goodbye
    - slot{"email":"_Email1_"}
    - utter_goodbye
    - action_save

## New Story4

* damagedPackage{"damaged":"casse","transporter":"Chronopost"}
    - slot{"damaged":"casse"}
    - utter_RefundResend
* damagedPackage{"action":"renvoi","home":"chez nous"}
    - slot{"action":"renvoi"}
    - slot{"home":"chez nous"}
    - utter_damagedPackageAskForMissingSlots
* rien
    - utter_autre_ProvideInfo_Performaction
* goodbye
    - utter_goodbye
    - action_save

## New Story

* deliveryCost{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_deliveryCost_ProvideInfo
* Discount
    - utter_Discount_ProvideInfo
