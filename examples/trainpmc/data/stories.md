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

## New Story6

* deliveryCost{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_deliveryCost_ProvideInfo
* Discount
    - utter_Discount_ProvideInfo

## New Story5

* deliveryNews{"order":"48512"}
    - slot{"order":"48512"}
    - utter_deliveryNews_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story6

* deliveryCost{"fdp":"frais de transport"}
    - slot{"fdp":"frais de transport"}
    - utter_deliveryCost_ProvideInfo

## New Story15

* deliveryCost{"email":"_Email1_","free":"offerte"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_deliveryCost_ProvideInfo
    - slot{"free":"offerte"}
* Discount
    - utter_Discount_ProvideInfo
    - slot{"email":"_Email1_"}
    - action_save

## New Story7

* autre
    - utter_autre_ProvideInfo_AskForMissingSlots
* deliveryCost{"fdp":"frais de livraison"}
    - slot{"fdp":"frais de livraison"}
    - utter_deliveryCost_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story8

* WebsiteBug{"email":"_Email1_","article":"Guerlain","fdp":"frais de port"}
    - slot{"article":"Guerlain"}
    - slot{"email":"_Email1_"}
    - slot{"fdp":"frais de port"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - utter_WebsiteBug_AskForMissingSlots_SayHello
* CommuncationInterruption
    - slot{"article":"Guerlain"}
    - slot{"email":"_Email1_"}
    - slot{"fdp":"frais de port"}
    - utter_CommuncationInterruption_ProvideInfo_Offeralternative
* goodbye
    - utter_goodbye
    - action_save

## New Story9

* goodbye{"mood":"🙂"}
    - utter_goodbye

## New Story10

* Login{"pwd":"numéro de passe"}
    -slot{"pwd":"numéro de passe"}
    - utter_Login_AskForMissingSlots_SayHello
* autre
    - utter_Login_Repeatprevious
* rien{"email":"_Email_1"}
    - slot{"email":"_Email_1"}
    - utter_Login_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story11

* deliveryNews{"order":"361"}
    - slot{"order":"361"}
    - utter_deliveryNews_ProvideInfo
* deliveryNews+AskDetails
    - utter_deliveryNews_AskDetails_ProvideInfo
* AskDetails{"fdp":"portant"}
    - slot{"fdp":"portant"}
    - utter_AskDetails_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story13

* PaymentRefused{"device":"portable"}
    - slot{"device":"portable"}
    - utter_PaymentRefused_Phone
* thanks
    - utter_goodbye
    - action_save

## New Story14

* Login{"facebook": "FB","pwd": "mot de passe"}
    - slot{"facebook": "FB"}
    - slot{"pwd": "mot de passe"}
    - utter_Login_AskForMissingSlot
* AskDetails{"email":"_Email_"}
    - slot{"email":"_Email_"}
    - utter_AskConfirmation_ProvideInfo
* WebsiteBug
    - utter_goodbye
    - action_save

## New Story17

* missingItem
    - utter_missingItem_ProvideInfo

## New Story12

* deliveryNews{"order":"40535"}
    - slot{"order":"40535"}
    - utter_deliveryNews_ProvideInfo
* ReceptionAlert{"channel":"sms"}
    - slot{"channel":"sms"}
    - utter_ReceptionAlert_ProvideInfo

## New Story16

* ProductPrice{"article":"Lolita lempicka","discount":"remise"}
    - slot{"article":" Lolita lempicka"}
    - utter_ProductPrice_AskForMissingSlots
* ProductPrice{"size":"100ml"}
    - slot{"size":"100ml"}
    - slot{"article":"Lolita lempicka"}
    - utter_ProductPrice_ProvideInfo
* CustomerComplaint
    - slot{"size":"100ml"}
    - slot{"article":"Lolita lempicka"}
    - utter_CustomerComplaint_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story17

* deliveryNews{"article":"parfum","email":"_Email1_"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - utter_deliveryNews_ProvideInfo
* AskDetails
    - utter_DeliveryNews_AskDetails
* goodbye
    - utter_goodbye
    - action_save

## New Story18

* ProductAvailable{"article":"cadeau","fdp":"port"}
    - slot{"article":"cadeau"}
    - slot{"fdp":"port"}
    - utter_deliveryTime_ProductAvailable_ProvideInfo_Apologize
* AskDetails
    - utter_product_AskDetails_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story19

* customerService{"channel":"mail"}
    - slot{"channel":"mail"}
    - utter_customer_service_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story20

* deliveryCost
    - utter_deliveryCost_ProvideInfo
* AskDetails
    - action_default_fallback

## New Story21

* AccountIssue
    - utter_AccountIssueError
* Login{"pwd":"passe","action":"renvoie"}
    - slot{"action":"renvoie"}
    - slot{"pwd":"passe"}
    - slot{"action":"renvoie"}
    - slot{"pwd":"passe"}
    - utter_Login_AskForMissingSlots_SayHello
* rien{"email":"email@email.com"}
    - slot{"email":"email@email.com"}
    - utter_Reinit
* thanks
    - utter_goodbye
    - action_save

## New Story22

* Login{"email":"_Email_"}
    - slot{"email":"_Email_"}
    - slot{"email":"_Email_"}
    - utter_AccountIssueError
* Login{"pwd":"passe"}
    - slot{"pwd":"passe"}
    - utter_Reinit
* Login{"bug":"authentification"}
    - slot{"bug":"authentification"} 
    - action_default_fallback

## New Story

* CancelOrder
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* thanks
    - utter_goodbye
    - action_save

## New Story25

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* Payment
    - utter_payment_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story24

* deliveryNews
    - utter_deliveryNews_ProvideInfo
* deliveryNews+AskDetails
    - utter_deliveryNews_AskDetails_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story23

* PaymentRefused
    - utter_PaymentRefused_AskForMissingSlots_SayHello
* Login{"bug":"authentification"}
    - slot{"bug":"authentification"}
    - utter_Login_AskForMissingSlot
* rien{"email":"_Email@ntin.fr"}
    - slot{"email":"_Email@ntin.fr"}
    - utter_Reinit
* deliveryTime
    - utter_deliveryTime_ProvideInfo
* thanks
    - utter_goodbye

## New Story29

* deliveryNews
    - utter_deliveryNews_ProvideInfo
* AskDetails
    - utter_deliveryTime_ProvideInfo
* autre
    - utter_goodbye
    - action_save

## New Story26

* PaymentRefused{"email":"_Email_","tool":"MasterCard","payment":"payer"}
    - slot{"email":"_Email_"}
    - slot{"payment":"payer"}
    - slot{"tool":"MasterCard"}
    - utter_PaymentRefused_ProvideInfo_Offeralternative
* PaymentTool{"tool":"Paypal"}
    - slot{"tool":"Paypal"}
    - utter_PaymentTool_PaymentRefused_ProvideInfo
* goodbye
    - utter_goodbye

## New Story28

* deliveryNews+AskDetails{"article":"parfum","transporter":"Chronopost"}
    - slot{"article":"parfum"}
    - slot{"transporter":"Chronopost"}
    - slot{"article":"parfum"}
    - slot{"transporter":"Chronopost"}
    - utter_deliveryNews_AskDetails_ProvideInfo
    - slot{"article":"parfum"}
    - slot{"transporter":"Chronopost"}
* goodbye
    - utter_goodbye
    - action_save

## New Story27

* WebsiteBug{"action":"téléchargé"}
    - slot{"action":"téléchargé"}
    - action_default_ask_rephrase
* AccountIssue{"biling":"factures"}
    - action_default_fallback

## New Story

* deliveryNews{"email":"_Email_","article":"parfum"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email_"}
    - utter_deliveryNews_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story

* missingItem
    - utter_missingItem_ProvideInfo_Searchorder
* ConfirmationOrder
    - utter_ConfirmationOrder_ProvideInfo
* CustomerComplaint{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_CustomerComplaint_Searchorder_Askforwaiting_ProvideInfo
* AskDetails
    - utter_ConfirmationOrder_ProvideInfo_Offeralternative
* ConfirmationOrder{"mood":"dommage"}
    - slot{"mood":"dommage"}
    - utter_oui_ConfirmationOrder_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save
