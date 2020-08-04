## story_1
* deliveryCost{"fdp": "frais de port","free": "0 €","email": "_Email1_","order":"00"}
 - slot{"order":"00"}
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

## New Story30

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
    - action_search_order
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

## New Story32

* deliveryNews{"email":"_Email_","article":"parfum","order":"00"}
    - slot{"order":"00"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email_"}
    - utter_deliveryNews_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story38

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

## New Story35

* deliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_deliveryNews_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story33

* deliveryNews{"order":"00","pr":"point relais"}
    - slot{"order":"00"}
    - slot{"pr":"point relais"}
    - utter_deliveryNews_ProvideInfo
* deliveryNews+AskDetails
    - slot{"order":"00"}
    - slot{"pr":"point relais"}
    - utter_deliveryNews_AskDetails_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story34

* Discount{"discount":"code promo"}
    - slot{"discount":"code promo"}
    - utter_AskEmail
* rien{"email":"email@emaiil.fr"}
    - slot{"discount":"code promo"}
    - slot{"email":"email@emaiil.fr"}
    - utter_Discount_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story36

* Discount{"article":"parfum","discount":"réduction"}
    - slot{"article":"parfum"}
    - slot{"discount":"réduction"}
    - utter_AskEmail
* rien{"email":"mon@adress.fr"}
    - slot{"discount":"réduction"}
    - slot{"email":"mon@adress.fr"}
    - utter_Discount_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story37

* damagedPackage{"article":"parfum","email":"_Email1_","mood":"déçue"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - utter_damagedPackage_AskForMissingSlots_Apologize
* autre
    - utter_RefundResend
* autre{"action":"renvoie"}
    - slot{"action":"renvoi"}
    - utter_autre_ProvideInfo_Performaction
    - action_Perform_action
* thanks
    - utter_goodbye
    - action_save

## New Story40

* missingItem
    - utter_missingItem_Searchorder_Askforwaiting_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story41

* deliveryNews
    - utter_deliveryNews_ProvideInfo

## New Story39

* deliveryNews{"order":"00"}
    - slot{"order":"00"}
    - utter_deliveryNews_ProvideInfo
* ReceptionAlert{"fdp":"portable"}
    - slot{"order":"00"}
    - slot{"fdp":"portable"}
    - utter_ReceptionAlert_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story42

* deliveryNews{"email":"_Email1_","order":"00"}
    - slot{"email":"_Email1_"}
    - slot{"order":"00"}
    - utter_deliveryNews_ProvideInfo
* autre
    - utter_goodbye
    - action_save

## New Story43

* CancelOrder
    - action_search_order
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* thanks
    - utter_goodbye
    - action_save

## New Story44

* deliveryCost+Discount
    - utter_deliveryCost_ProvideInfo_Apologize
* thanks
    - utter_goodbye
    - action_save

## New Story45

* deliveryNews
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* deliveryTime{"present":"cadeau"}
    - slot{"present":"cadeau"}
    - utter_deliveryTime_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story47

* CommuncationInterruption{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - utter_AskForMissingSlots_SayHello
* rien{"date":"15/09/18","order":"00"}
    - slot{"date":"15/09/18"}
    - slot{"order":"00"}
    - action_search_order
    - utter_rien_ProvideInfo_Offeralternative
* CustomerComplaint{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - utter_CustomerComplaint_ProvideInfo_Apologize
* CustomerComplaint{"present":"cadeau","transporter":"Chronopost"}
    - slot{"present":"cadeau"}
    - slot{"transporter":"Chronopost"}
    - utter_deliveryNews_ProvideInfo_Offeralternative
* goodbye
    - utter_goodbye
    - action_save

## New Story48

* deliveryTime
    - utter_deliveryTime_ProvideInfo
* thanks
    - utter_goodbye

## New Story54

* deliveryCost{"fdp":"frais"}
    - slot{"fdp":"frais"}
    - utter_deliveryCost_ProvideInfo_Proceedtocheckpoint
* thanks
    - utter_goodbye
    - action_save

## New Story55

* autre

## New Story56

* ProductPrice{"article":"parfum"}
    - slot{"article":"parfum"}
    - action_search_order
    - utter_ProductPrice_ProvideInfo
* ProductPrice{"article":"Guerlain"}
    - slot{"article":"Guerlain"}
    - utter_ProductPrice_ProvideInfo_Advisetolookelsewhere

## New Story53

* deliveryNews{"date":"22/09","event":"anniversaire","order":"00"}
    - slot{"order":"00"}
    - slot{"date":"22/09"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* autre
    - utter_goodbye
    - action_save

## New Story52

* delivery{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskOrder
* rien{"order":"4523"}
    - slot{"order":"4523"}
    - slot{"email":"_Email1_"}
    - action_default_fallback

## New Story51

* Discount{"discount":"remise","code":"MDM0"}
    - slot{"discount":"remise"}
    - slot{"code":"MDM0"}
    - utter_Discount_ProvideInfo
* ProductAvailable
    - action_search_order
    - utter_ProductAvailable_ProvideInfo_Searchorder
* goodbye+thanks
    - utter_goodbye
    - action_save

## New Story57

* deliveryTime{"date":"Noël"}
    - slot{"date":"Noël"}
    - utter_deliveryTime_ProvideInfo
* AskDetails
    - slot{"date":"Noël"}
    - utter_deliveryTime_ProductAvailable_ProvideInfo_Apologize
* thanks
    - utter_goodbye
    - action_save

## New Story58

* deliveryNews{"order":"00","action":"envoi"}
    - slot{"action":"envoi"}
    - slot{"order":"00"}
    - action_search_order
    - utter_deliveryNews_CustomerComplaint_ProvideInfo_Apologize
* deliveryNews+CustomerComplaint{"action":"envoi"}
    - slot{"action":"envoi"}
    - utter_deliveryNews_AskDetails_ProvideInfo
* deliveryNews+CustomerComplaint
    - utter_deliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* CustomerComplaint+goodbye
    - utter_goodbye

## New Story59

* deliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story60

* deliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* deliveryNews+AskDetails
    - utter_deliveryNews_AskDetails_ProvideInfo
* autre
    - utter_CustomerComplaint_goodbye_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story_troll1

* PaymentRefused{"tool":"carte bancaire"}
    - slot{"tool":"carte bancaire"}
    - utter_troll
* AskDetails
    - slot{"tool":"carte bancaire"}
    - utter_PaymentTool_AskForMissingSlots_SayHello
* oui
    - utter_PaymentTool_ProvideInfo_Apologize_Offeralternative

## New Story61

* deliveryNews{"email":"_Email1_","date":"09/04/19","fdp":"frais","order":"00"}
    - slot{"date":"09/04/19"}
    - slot{"order":"00"}
    - slot{"email":"_Email1_"}
    - slot{"fdp":"frais"}
    - utter_deliveryNews_ProvideInfo
* CustomerComplaint+goodbye
    - utter_goodbye
    - action_save

## New Story62

* saluer
    - utter_AskForMissingSlots_SayHello
* deliveryNews+AskDetails{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* AskDetails
    - action_default_fallback

## New Story63

* ConfirmationOrder{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_search_order
    - utter_ConfirmationOrder_Searchorder_Askforwaiting_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story64

* deliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_search_order
    - utter_deliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* ReceptionAlert
    - action_default_fallback

## New Story65

* deliveryNews{"transporter":"chrono"}
    - slot{"transporter":"chrono"}
    - slot{"transporter":"chrono"}
    - utter_deliveryNews_AskDetails_ProvideInfo
    - slot{"transporter":"chrono"}
* StoreLocation+deliveryTime{"transporter":"chrono","date":"31/12"}
    - slot{"date":"31/12"}
    - slot{"transporter":"chrono"}
    - utter_AskDetails_StoreLocation_deliveryTime_ProvideInfo
* AskDetails
    - utter_deliveryTime_ProvideInfo
* deliveryNews+AskDetails{"date":"samedi"}
    - slot{"date":"samedi"}
    - utter_deliveryNews_ProvideInfo
* thanks
    - utter_goodbye

## New Story66

* damagedPackage{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_damagedPackage_AskForMissingSlots_Apologize
* CustomerComplaint
    - utter_damagedPackage_ProvideInfo_Searchorder

## New Story67

* deliveryNews
    - utter_AskEmail
* rien{"email":"e@mel.fr"}
    - slot{"email":"e@mel.fr"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Story68

* deliveryNews
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* goodbye
    - utter_goodbye
    - action_save

## New Storytroll2

* deliveryNews
    - utter_AskOrder
* non{"date":"7/06"}
    - slot{"date":"7/06"}
    - utter_troll

## New Story69

* ConfirmationOrder{"tool":"carte bancaire","payment":"paiement","confirmation":"confirmation"}
    - slot{"confirmation":"confirmation"}
    - utter_ConfirmationOrder_AskForMissingSlots_SayHello
* oui
    - utter_oui_Askforwaiting_SayGoodbye
* thanks
    - utter_goodbye
    - action_save

## New Story80

* rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskForMissingSlots_SayHello
* ReceptionAlert
    - utter_ReceptionAlert_ProvideInfo
* thanks
    - utter_oui_Askforanotherquestion
    - slot{"email":"_Email1_"}
* ChangeData{"pwd":"mot de passe"}
    - slot{"pwd":"mot de passe"}
    - utter_ChangeData_Performaction_ProvideInfo_Suggeststo
* thanks
    - utter_goodbye
    - action_save

## New Story79

* saluer
    - utter_AskForMissingSlots_SayHello
* deliveryNews+AskDetails{"email":"_Email1_","date":"samedi","follow-up":"suivi"}
    - slot{"date":"samedi"}
    - slot{"follow-up":"suivi"}
    - slot{"email":"_Email1_"}
    - action_search_order
* deliveryNews+deliveryPlace{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - slot{"follow-up":"suivi"}
    - utter_deliveryNews_AskDetails_ProvideInfo

## New Story72

* ProductAvailable{"article":"Courrèges in blue"}
    - slot{"article":"Courrèges in blue"}
    - action_search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder

## New StoryInterestingMemory

* missingItem
    - action_search_order
    - utter_missingItem_ProvideInfo
* AskDetails
    - utter_deliveryNews_ProvideInfo_Apologize_Offeralternative
* non
    - utter_ConfirmRefund
* oui+CustomerComplaint
    - utter_Refund_SayGoodbye
    - action_save

## New Story78

* missingItem{"order":"00"}
    - slot{"order":"00"}
    - action_search_order
    - utter_deliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* goodbye+thanks
    - utter_goodbye
    - action_save

## New Story77

* saluer
    - utter_AskForMissingSlots_SayHello
* damagedPackage{"email":"_Email1_","article":"Angel"}
    - slot{"email":"_Email1_"}
    - slot{"article":"Angel"}
    - action_search_order
    - utter_damagedPackage_ProvideInfo_Searchorder
* thanks
    - utter_goodbye
    - action_save

## New Story76

* ReceptionAlert{"channel":"sms","pr":"point relais"}
    - slot{"channel":"sms"}
    - slot{"pr":"point relais"}
    - utter_ReceptionAlert_ProvideInfo
* goodbye+thanks
    - utter_goodbye
    - action_save

## New Story75

* deliveryNews+AskDetails{"follow-up":"suivi","mood":"inquiète"}
    - slot{"follow-up":"suivi"}
    - slot{"mood":"inquiète"}
    - utter_AskOrder
* rien{"order":"54678"}
    - slot{"order":"54678"}
    - utter_deliveryNews_AskDetails_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story73

* deliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_search_order
    - utter_deliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* ReceptionAlert{"channel":"mail"}
    - slot{"channel":"mail"}
    - slot{"order":"00"}
    - utter_ReceptionAlert_ProvideInfo
* goodbye
    - utter_goodbye

## New Storypassepas

* Discount{"code":"NOEL02"}
    - slot{"code":"NOEL02"}
    - utter_Discount_AskForMissingSlots_SayHello
* rien{"email":"mon@mel.fr"}
    - slot{"code":"NOEL02"}
    - slot{"email":"mon@mel.fr"}
    - utter_Discount_ProvideInfo
* Discount
    - action_default_fallback

## New Story81

* deliveryNews{"order":"00"}
    - action_search_order
    - slot{"order":"00"}
    - utter_deliveryNews_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New StoryrenvoirDur

* deliveryNews{"email":"_Email1_2","order":"03"}
    - slot{"email":"_Email1_2"}
    - slot{"order":"03"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* deliveryNews+deliveryPlace{"home":"domicile"}
    - slot{"home":"domicile"}
    - slot{"order":"03"}
    - utter_deliveryNews_ProvideInfo_Apologize_Offeralternative
* deliveryPlace{"action":"recommander"}
    - slot{"home":"domicile"}
    - slot{"action":"recommander"}
    - slot{"order":"03"}
    - utter_deliveryNews_deliveryPlace_ProvideInfo_Offeralternative
    - slot{"email":"_Email1_2"}
* ConfirmationOrder{"pr":"point relais","confirmation":"confirmer"}
    - slot{"confirmation":"confirmer"}
    - slot{"pr":"point relais"}
    - utter_Resend
* thanks
    - utter_goodbye
    - action_save

## New Story

* deliveryNews{"date":"mars"}
    - slot{"date":"mars"}
    - slot{"date":"mars"}
    - action_search_order
    - utter_deliveryNews_AskDetails_CustomerComplaint_ProvideInfo
    - slot{"date":"mars"}
* deliveryNews+AskDetails{"fdp":"transporteur"}
    - slot{"fdp":"transporteur"}
    - utter_deliveryNews_AskDetails_ProvideInfo
* goodbye+thanks{"date":"vendredi"}
    - slot{"date":"vendredi"}
    - utter_goodbye
    - action_save

## New Story

* deliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_search_order
    - utter_deliveryNews_Lost
    - utter_RefundResend
    - slot{"email":"_Email1_"}

## New Story

* deliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo
* goodbye+thanks
    - utter_goodbye
    - action_save

## New Story

* deliveryTime
    - utter_deliveryTime_ProvideInfo
* thanks
    - utter_goodbye
    - action_save

## New Story

* deliveryCost+Discount{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_deliveryCost_ProvideInfo_Apologize
* Discount
    - utter_Discount_ProvideInfo
* goodbye+thanks
    - utter_goodbye

## New Story

* PaymentRefused
    - utter_PaymentRefused_AskForMissingSlots
    - utter_PaymentRefused_AskForMissingSlots_SayHello
* non
    - utter_DeliveryMode
* non
    - utter_non_ProvideInfo
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo
* WebsiteBug
    - action_default_fallback

## New Story

* deliveryCost+Discount{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_deliveryCost_ProvideInfo_Apologize

## New Story

* PaymentRefused{"email":"_Email1_2","payment":"paiement","tool":"carte"}
    - slot{"email":"_Email1_2"}
    - slot{"payment":"paiement"}
    - slot{"tool":"carte"}
    - slot{"email":"_Email1_2"}
    - slot{"payment":"paiement"}
    - slot{"tool":"carte"}
    - utter_PaymentTool_PaymentRefused_ProvideInfo
    - slot{"email":"_Email1_2"}
    - slot{"payment":"paiement"}
    - slot{"tool":"carte"}
* non
    - action_default_fallback

## New Story

* Login{"connection":"connecter","bug":"authentification"}
    - slot{"bug":"authentification"}
    - slot{"connection":"connecter"}
    - utter_Login_AskForMissingSlot
* rien{"email":"_Email2_","pwd":"passe"}
    - slot{"email":"_Email2_"}
    - slot{"pwd":"passe"}
    - utter_Reinit
* thanks
    - utter_goodbye
    - action_save

## New Story

* deliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_search_order
    - utter_deliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* CustomerComplaint+goodbye
    - utter_goodbye

## New Story

* deliveryPlace{"country":"France","present":"cadeau"}
    - slot{"country":"France"}
    - slot{"present":"cadeau"}
    - action_default_fallback

## New Story

* deliveryNews
    - utter_AskOrder
* rien{"order":"4968"}
    - slot{"order":"4968"}
    - action_search_order
    - utter_deliveryNews_ProvideInfo_Offeralternative
* CustomerComplaint+goodbye{"action":"remboursement","country":"Française","transporter":"Chronopost","fdp":"Française","article":"fond"}
    - slot{"action":"remboursement"}
    - slot{"article":"fond"}
    - slot{"country":"Française"}
    - slot{"fdp":"Française"}
    - slot{"transporter":"Chronopost"}
    - action_default_fallback
