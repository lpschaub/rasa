## story_1
* DeliveryCost{"fdp": "frais de port","free": "0 €","email": "_Email1_","order":"00"}
    - slot{"order":"00"}
    - slot{"fdp":"frais de port"}
    - utter_DeliveryCost_ProvideInfo
* Goodbye{"mood":"dommage"}
    - utter_Goodbye
    - action_Save

## New Story2

* PaymentRefused{"payment":"régler"}
    - utter_PaymentRefused_ProvideInfo
* PaymentTool{"tool":"PayPal"}
	- slot{"paypal":"PayPal"}
    - utter_PaymentRefused_ProvideInfo_Offeralternative
* Thanks
    - utter_Goodbye
    - action_Save

## New Story3

* ProductAvailable{"email":"_Email1_","article":"womanity EAU de parfum spray","target":"amie","reload":"rechargeable"}
    - slot{"email":"_Email1_"}
    - slot{"article":"womanity EAU de parfum spray"}
    - slot{"target":"amie","reload":"rechargeable"}
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Goodbye
    - slot{"email":"_Email1_"}
    - utter_Goodbye
    - action_Save

## New Story4

* DamagedPackage{"damaged":"casse","transporter":"Chronopost"}
    - slot{"damaged":"casse"}
    - utter_RefundResend
* DamagedPackage{"action":"renvoi","home":"chez nous"}
    - slot{"action":"renvoi"}
    - slot{"home":"chez nous"}
    - utter_DamagedPackageAskForMissingSlots
* Rien
    - utter_Autre_ProvideInfo_Performaction
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story6

* DeliveryCost{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DeliveryCost_ProvideInfo
* Discount
    - utter_Discount_ProvideInfo

## New Story5

* DeliveryNews{"order":"48512"}
    - slot{"order":"48512"}
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story6

* DeliveryCost{"fdp":"frais de transport"}
    - slot{"fdp":"frais de transport"}
    - utter_DeliveryCost_ProvideInfo

## New Story15

* DeliveryCost{"email":"_Email1_","free":"offerte"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DeliveryCost_ProvideInfo
    - slot{"free":"offerte"}
* Discount
    - utter_Discount_ProvideInfo
    - slot{"email":"_Email1_"}
    - action_Save

## New Story7

* Autre
    - utter_Autre_ProvideInfo_AskForMissingSlots
* DeliveryCost{"fdp":"frais de livraison"}
    - slot{"fdp":"frais de livraison"}
    - utter_DeliveryCost_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

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
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story9

* Goodbye{"mood":"🙂"}
    - utter_Goodbye

## New Story10

* Login{"pwd":"numéro de passe"}
    -slot{"pwd":"numéro de passe"}
    - utter_Login_AskForMissingSlots_SayHello
* Autre
    - utter_Login_Repeatprevious
* Rien{"email":"_Email_1"}
    - slot{"email":"_Email_1"}
    - utter_Login_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story11

* DeliveryNews{"order":"361"}
    - slot{"order":"361"}
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+AskDetails
    - utter_DeliveryNews_AskDetails_ProvideInfo
* AskDetails{"fdp":"portant"}
    - slot{"fdp":"portant"}
    - utter_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story13

* PaymentRefused{"device":"portable"}
    - slot{"device":"portable"}
    - utter_PaymentRefused_Phone
* Thanks
    - utter_Goodbye
    - action_Save

## New Story14

* Login{"facebook": "FB","pwd": "mot de passe"}
    - slot{"facebook": "FB"}
    - slot{"pwd": "mot de passe"}
    - utter_Login_AskForMissingSlot
* AskDetails{"email":"_Email_"}
    - slot{"email":"_Email_"}
    - utter_AskConfirmation_ProvideInfo
* WebsiteBug
    - utter_Goodbye
    - action_Save

## New Story17

* MissingItem
    - utter_MissingItem_ProvideInfo

## New Story12

* DeliveryNews{"order":"40535"}
    - slot{"order":"40535"}
    - utter_DeliveryNews_ProvideInfo
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
* Thanks
    - utter_Goodbye
    - action_Save

## New Story17

* DeliveryNews{"article":"parfum","email":"_Email1_"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - utter_DeliveryNews_ProvideInfo
* AskDetails
    - utter_DeliveryNews_AskDetails
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story18

* ProductAvailable{"article":"cadeau","fdp":"port"}
    - slot{"article":"cadeau"}
    - slot{"fdp":"port"}
    - utter_DeliveryTime_ProductAvailable_ProvideInfo_Apologize
* AskDetails
    - utter_Product_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story19

* CustomerService{"channel":"mail"}
    - slot{"channel":"mail"}
    - utter_Customer_service_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story20

* DeliveryCost
    - utter_DeliveryCost_ProvideInfo
* AskDetails
    - action_Default_fallback

## New Story21

* AccountIssue
    - utter_AccountIssueError
* Login{"pwd":"passe","action":"renvoie"}
    - slot{"action":"renvoie"}
    - slot{"pwd":"passe"}
    - slot{"action":"renvoie"}
    - slot{"pwd":"passe"}
    - utter_Login_AskForMissingSlots_SayHello
* Rien{"email":"email@email.com"}
    - slot{"email":"email@email.com"}
    - utter_Reinit
* Thanks
    - utter_Goodbye
    - action_Save

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
    - action_Default_fallback

## New Story30

* CancelOrder
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* Thanks
    - utter_Goodbye
    - action_Save

## New Story25

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* PaymentSecure
    - utter_Payment_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story24

* DeliveryNews
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+AskDetails
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story23

* PaymentRefused
    - utter_PaymentRefused_AskForMissingSlots_SayHello
* Login{"bug":"authentification"}
    - slot{"bug":"authentification"}
    - utter_Login_AskForMissingSlot
* Rien{"email":"_Email@ntin.fr"}
    - slot{"email":"_Email@ntin.fr"}
    - utter_Reinit
* DeliveryTime
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye

## New Story29

* DeliveryNews
    - utter_DeliveryNews_ProvideInfo
* AskDetails
    - utter_DeliveryTime_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save

## New Story26

* PaymentRefused{"email":"_Email_","tool":"MasterCard","payment":"payer"}
    - slot{"email":"_Email_"}
    - slot{"payment":"payer"}
    - slot{"tool":"MasterCard"}
    - utter_PaymentRefused_ProvideInfo_Offeralternative
* PaymentTool{"tool":"Paypal"}
    - slot{"tool":"Paypal"}
    - utter_PaymentTool_PaymentRefused_ProvideInfo
* Goodbye
    - utter_Goodbye

## New Story28

* DeliveryNews+AskDetails{"article":"parfum","transporter":"Chronopost"}
    - slot{"article":"parfum"}
    - slot{"transporter":"Chronopost"}
    - slot{"article":"parfum"}
    - slot{"transporter":"Chronopost"}
    - action_Search_order
    - utter_DeliveryNews_AskDetails_ProvideInfo
    - slot{"article":"parfum"}
    - slot{"transporter":"Chronopost"}
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story27

* WebsiteBug{"action":"téléchargé"}
    - slot{"action":"téléchargé"}
    - action_Default_ask_rephrase
* AccountIssue{"biling":"factures"}
    - action_Default_fallback

## New Story32

* DeliveryNews{"email":"_Email_","article":"parfum","order":"00"}
    - slot{"order":"00"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email_"}
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story38

* MissingItem
    - utter_MissingItem_ProvideInfo_Searchorder
* ConfirmationOrder
    - utter_ConfirmationOrder_ProvideInfo
* CustomerComplaint{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_CustomerComplaint_Searchorder_Askforwaiting_ProvideInfo
* AskDetails
    - utter_ConfirmationOrder_ProvideInfo_Offeralternative
* ConfirmationOrder{"mood":"dommage"}
    - slot{"mood":"dommage"}
    - utter_Oui_ConfirmationOrder_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story35

* DeliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story33

* DeliveryNews{"order":"00","pr":"point relais"}
    - slot{"order":"00"}
    - slot{"pr":"point relais"}
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+AskDetails
    - slot{"order":"00"}
    - slot{"pr":"point relais"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story34

* Discount{"discount":"code promo"}
    - slot{"discount":"code promo"}
    - utter_AskEmail
* Rien{"email":"email@emaiil.fr"}
    - slot{"discount":"code promo"}
    - slot{"email":"email@emaiil.fr"}
    - utter_Discount_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story36

* Discount{"article":"parfum","discount":"réduction"}
    - slot{"article":"parfum"}
    - slot{"discount":"réduction"}
    - utter_AskEmail
* Rien{"email":"mon@adress.fr"}
    - slot{"discount":"réduction"}
    - slot{"email":"mon@adress.fr"}
    - utter_Discount_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story37

* DamagedPackage{"article":"parfum","email":"_Email1_","mood":"déçue"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - utter_DamagedPackage_AskForMissingSlots_Apologize
* Autre
    - utter_RefundResend
* Autre{"action":"renvoie"}
    - slot{"action":"renvoi"}
    - utter_Autre_ProvideInfo_Performaction
    - action_Perform_action
* Thanks
    - utter_Goodbye
    - action_Save

## New Story40

* MissingItem
    - utter_MissingItem_Searchorder_Askforwaiting_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story41

* DeliveryNews
    - utter_DeliveryNews_ProvideInfo

## New Story39

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - utter_DeliveryNews_ProvideInfo
* ReceptionAlert{"fdp":"portable"}
    - slot{"order":"00"}
    - slot{"fdp":"portable"}
    - utter_ReceptionAlert_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story42

* DeliveryNews{"email":"_Email1_","order":"00"}
    - slot{"email":"_Email1_"}
    - slot{"order":"00"}
    - utter_DeliveryNews_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save

## New Story43

* CancelOrder
    - action_Search_order
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* Thanks
    - utter_Goodbye
    - action_Save

## New Story44

* DeliveryCost+Discount
    - utter_DeliveryCost_ProvideInfo_Apologize
* Thanks
    - utter_Goodbye
    - action_Save

## New Story45

* DeliveryNews
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryTime{"present":"cadeau"}
    - slot{"present":"cadeau"}
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story47

* CommuncationInterruption{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - utter_AskForMissingSlots_SayHello
* Rien{"date":"15/09/18","order":"00"}
    - slot{"date":"15/09/18"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_Rien_ProvideInfo_Offeralternative
* CustomerComplaint{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - utter_CustomerComplaint_ProvideInfo_Apologize
* CustomerComplaint{"present":"cadeau","transporter":"Chronopost"}
    - slot{"present":"cadeau"}
    - slot{"transporter":"Chronopost"}
    - utter_DeliveryNews_ProvideInfo_Offeralternative
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story48

* DeliveryTime
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye

## New Story54

* DeliveryCost{"fdp":"frais"}
    - slot{"fdp":"frais"}
    - utter_DeliveryCost_ProvideInfo_Proceedtocheckpoint
* Thanks
    - utter_Goodbye
    - action_Save

## New Story55

* Autre

## New Story56

* ProductPrice{"article":"parfum"}
    - slot{"article":"parfum"}
    - action_Search_order
    - utter_ProductPrice_ProvideInfo
* ProductPrice{"article":"Guerlain"}
    - slot{"article":"Guerlain"}
    - utter_ProductPrice_ProvideInfo_Advisetolookelsewhere

## New Story53

* DeliveryNews{"date":"22/09","event":"anniversaire","order":"00"}
    - slot{"order":"00"}
    - slot{"date":"22/09"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save

## New Story52

* Returned{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskOrder
* Rien{"order":"4523"}
    - slot{"order":"4523"}
    - slot{"email":"_Email1_"}
    - action_Default_fallback

## New Story51

* Discount{"discount":"remise","code":"MDM0"}
    - slot{"discount":"remise"}
    - slot{"code":"MDM0"}
    - utter_Discount_ProvideInfo
* ProductAvailable
    - action_Search_order
    - utter_ProductAvailable_ProvideInfo_Searchorder
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story57

* DeliveryTime{"date":"Noël"}
    - slot{"date":"Noël"}
    - utter_DeliveryTime_ProvideInfo
* AskDetails
    - slot{"date":"Noël"}
    - utter_DeliveryTime_ProductAvailable_ProvideInfo_Apologize
* Thanks
    - utter_Goodbye
    - action_Save

## New Story58

* DeliveryNews{"order":"00","action":"envoi"}
    - slot{"action":"envoi"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_CustomerComplaint_ProvideInfo_Apologize
* DeliveryNews+CustomerComplaint{"action":"envoi"}
    - slot{"action":"envoi"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
* DeliveryNews+CustomerComplaint
    - utter_DeliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* CustomerComplaint+goodbye
    - utter_Goodbye

## New Story59

* DeliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story60

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+AskDetails
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Autre
    - utter_CustomerComplaint_goodbye_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story_troll1

* PaymentRefused{"tool":"carte bancaire"}
    - slot{"tool":"carte bancaire"}
    - utter_Troll
* AskDetails
    - slot{"tool":"carte bancaire"}
    - utter_PaymentTool_AskForMissingSlots_SayHello
* Oui
    - utter_PaymentTool_ProvideInfo_Apologize_Offeralternative

## New Story61

* DeliveryNews{"email":"_Email1_","date":"09/04/19","fdp":"frais","order":"00"}
    - slot{"date":"09/04/19"}
    - slot{"order":"00"}
    - slot{"email":"_Email1_"}
    - slot{"fdp":"frais"}
    - utter_DeliveryNews_ProvideInfo
* CustomerComplaint+goodbye
    - utter_Goodbye
    - action_Save

## New Story62

* Saluer
    - utter_AskForMissingSlots_SayHello
* DeliveryNews+AskDetails{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* AskDetails
    - action_Default_fallback

## New Story63

* ConfirmationOrder{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_ConfirmationOrder_Searchorder_Askforwaiting_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story64

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* ReceptionAlert
    - action_Default_fallback

## New Story65

* DeliveryNews{"transporter":"chrono"}
    - slot{"transporter":"chrono"}
    - slot{"transporter":"chrono"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
    - slot{"transporter":"chrono"}
* StoreLocation+deliveryTime{"transporter":"chrono","date":"31/12"}
    - slot{"date":"31/12"}
    - slot{"transporter":"chrono"}
    - utter_AskDetails_StoreLocation_deliveryTime_ProvideInfo
* AskDetails
    - utter_DeliveryTime_ProvideInfo
* DeliveryNews+AskDetails{"date":"samedi"}
    - slot{"date":"samedi"}
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye

## New Story66

* DamagedPackage{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DamagedPackage_AskForMissingSlots_Apologize
* CustomerComplaint
    - utter_DamagedPackage_ProvideInfo_Searchorder

## New Story67

* DeliveryNews
    - utter_AskEmail
* Rien{"email":"e@mel.fr"}
    - slot{"email":"e@mel.fr"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story68

* DeliveryNews
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Storytroll2

* DeliveryNews
    - utter_AskOrder
* Non{"date":"7/06"}
    - slot{"date":"7/06"}
    - utter_Troll

## New Story69

* ConfirmationOrder{"tool":"carte bancaire","payment":"paiement","confirmation":"confirmation"}
    - slot{"confirmation":"confirmation"}
    - utter_ConfirmationOrder_AskForMissingSlots_SayHello
* Oui
    - utter_Oui_Askforwaiting_SayGoodbye
* Thanks
    - utter_Goodbye
    - action_Save

## New Story80

* Rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskForMissingSlots_SayHello
* ReceptionAlert
    - utter_ReceptionAlert_ProvideInfo
* Thanks
    - utter_Oui_Askforanotherquestion
    - slot{"email":"_Email1_"}
* ChangeData{"pwd":"mot de passe"}
    - slot{"pwd":"mot de passe"}
    - utter_ChangeData_Performaction_ProvideInfo_Suggeststo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story79

* Saluer
    - utter_AskForMissingSlots_SayHello
* DeliveryNews+AskDetails{"email":"_Email1_","date":"samedi","follow-up":"suivi"}
    - slot{"date":"samedi"}
    - slot{"follow-up":"suivi"}
    - slot{"email":"_Email1_"}
    - action_Search_order
* DeliveryNews+deliveryPlace{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - slot{"follow-up":"suivi"}
    - utter_DeliveryNews_AskDetails_ProvideInfo

## New Story72

* ProductAvailable{"article":"Courrèges in blue"}
    - slot{"article":"Courrèges in blue"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder

## New StoryInterestingMemory

* MissingItem
    - action_Search_order
    - utter_MissingItem_ProvideInfo
* AskDetails
    - utter_DeliveryNews_ProvideInfo_Apologize_Offeralternative
* Non
    - utter_ConfirmRefund
* Oui+CustomerComplaint
    - utter_Refund_SayGoodbye
    - action_Save

## New Story78

* MissingItem{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story77

* Saluer
    - utter_AskForMissingSlots_SayHello
* DamagedPackage{"email":"_Email1_","article":"Angel"}
    - slot{"email":"_Email1_"}
    - slot{"article":"Angel"}
    - action_Search_order
    - utter_DamagedPackage_ProvideInfo_Searchorder
* Thanks
    - utter_Goodbye
    - action_Save

## New Story76

* ReceptionAlert{"channel":"sms","pr":"point relais"}
    - slot{"channel":"sms"}
    - slot{"pr":"point relais"}
    - utter_ReceptionAlert_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story75

* DeliveryNews+AskDetails{"follow-up":"suivi","mood":"inquiète"}
    - slot{"follow-up":"suivi"}
    - slot{"mood":"inquiète"}
    - utter_AskOrder
* Rien{"order":"54678"}
    - slot{"order":"54678"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story73

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* ReceptionAlert{"channel":"mail"}
    - slot{"channel":"mail"}
    - slot{"order":"00"}
    - utter_ReceptionAlert_ProvideInfo
* Goodbye
    - utter_Goodbye

## New Storypassepas

* Discount{"code":"NOEL02"}
    - slot{"code":"NOEL02"}
    - utter_Discount_AskForMissingSlots_SayHello
* Rien{"email":"mon@mel.fr"}
    - slot{"code":"NOEL02"}
    - slot{"email":"mon@mel.fr"}
    - utter_Discount_ProvideInfo
* Discount
    - action_Default_fallback

## New Story81

* DeliveryNews{"order":"00"}
    - action_Search_order
    - slot{"order":"00"}
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New StoryrenvoirDur

* DeliveryNews{"email":"_Email1_2","order":"03"}
    - slot{"email":"_Email1_2"}
    - slot{"order":"03"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+deliveryPlace{"home":"domicile"}
    - slot{"home":"domicile"}
    - slot{"order":"03"}
    - utter_DeliveryNews_ProvideInfo_Apologize_Offeralternative
* DeliveryPlace{"action":"recommander"}
    - slot{"home":"domicile"}
    - slot{"action":"recommander"}
    - slot{"order":"03"}
    - utter_DeliveryNews_deliveryPlace_ProvideInfo_Offeralternative
    - slot{"email":"_Email1_2"}
* ConfirmationOrder{"pr":"point relais","confirmation":"confirmer"}
    - slot{"confirmation":"confirmer"}
    - slot{"pr":"point relais"}
    - utter_Resend
* Thanks
    - utter_Goodbye
    - action_Save

## New Story

* DeliveryNews{"date":"mars"}
    - slot{"date":"mars"}
    - slot{"date":"mars"}
    - action_Search_order
    - utter_DeliveryNews_AskDetails_CustomerComplaint_ProvideInfo
    - slot{"date":"mars"}
* DeliveryNews+AskDetails{"fdp":"transporteur"}
    - slot{"fdp":"transporteur"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Goodbye{"date":"vendredi"}
    - slot{"date":"vendredi"}
    - utter_Goodbye
    - action_Save

## New Story

* DeliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_Lost
    - utter_RefundResend
    - slot{"email":"_Email1_"}

## New Story

* DeliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story

* DeliveryTime
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story

* DeliveryCost+Discount{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_DeliveryCost_ProvideInfo_Apologize
* Discount
    - utter_Discount_ProvideInfo
* Goodbye
    - utter_Goodbye

## New Story

* PaymentRefused
    - utter_PaymentRefused_AskForMissingSlots
    - utter_PaymentRefused_AskForMissingSlots_SayHello
* Non
    - utter_DeliveryMode
* Non
    - utter_Non_ProvideInfo
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo
* WebsiteBug
    - action_Default_fallback

## New Story

* DeliveryCost+Discount{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_DeliveryCost_ProvideInfo_Apologize

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
* Non
    - action_Default_fallback

## New Story

* Login{"connection":"connecter","bug":"authentification"}
    - slot{"bug":"authentification"}
    - slot{"connection":"connecter"}
    - utter_Login_AskForMissingSlot
* Rien{"email":"_Email2_","pwd":"passe"}
    - slot{"email":"_Email2_"}
    - slot{"pwd":"passe"}
    - utter_Reinit
* Thanks
    - utter_Goodbye
    - action_Save

## New Story

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* CustomerComplaint+goodbye
    - utter_Goodbye

## New Story

* DeliveryPlace{"country":"France","present":"cadeau"}
    - slot{"country":"France"}
    - slot{"present":"cadeau"}
    - action_Default_fallback

## New Story

* DeliveryNews
    - utter_AskOrder
* Rien{"order":"4968"}
    - slot{"order":"4968"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo_Offeralternative
* CustomerComplaint+goodbye{"action":"remboursement","country":"Française","transporter":"Chronopost","fdp":"Française","article":"fond"}
    - slot{"action":"remboursement"}
    - slot{"article":"fond"}
    - slot{"country":"Française"}
    - slot{"fdp":"Française"}
    - slot{"transporter":"Chronopost"}
    - action_Default_fallback
