## story_1
* DeliveryCost{"fdp": "frais de port","free": "0 €","email": "_Email1_","order":"00"}
    - slot{"order":"00"}
    - slot{"email": "_Email1_"}
    - slot{"fdp":"frais de port"}
    - utter_DeliveryCost_ProvideInfo
* Goodbye{"mood_neg":"dommage"}
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1028

* PaymentRefused{"payment":"régler"}
    - utter_PaymentRefused_ProvideInfo
* PaymentTool{"tool":"PayPal"}
    - slot{"paypal":"PayPal"}
    - utter_PaymentRefused_ProvideInfo_Offeralternative
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1044

* ProductAvailable{"email":"_Email1_","article":"womanity EAU de parfum spray","target":"amie","reload":"rechargeable"}
    - slot{"email":"_Email1_"}
    - slot{"article":"womanity EAU de parfum spray"}
    - slot{"target":"amie","reload":"rechargeable"}
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Goodbye
    - slot{"email":"_Email1_"}
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1060

* DamagedPackage{"damaged":"casse","transporter":"Chronopost"}
    - slot{"damaged":"casse"}
    - utter_RefundResend
* DamagedPackage{"resend":"renvoi","home":"chez nous"}
    - slot{"resend":"renvoi"}
    - slot{"home":"chez nous"}
    - utter_DamagedPackageAskForMissingSlots
* Rien
    - utter_Autre_ProvideInfo_Performaction
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Storyx2

* DeliveryCost{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DeliveryCost_ProvideInfo
* Discount
    - utter_Discount_ProvideInfo
    - action_restart

## New Storyx1

* DeliveryNews{"order":"48512"}
    - slot{"order":"48512"}
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1175

* DeliveryCost{"fdp":"frais de transport"}
    - slot{"fdp":"frais de transport"}
    - utter_DeliveryCost_ProvideInfo
    - action_restart

## New Story1177

* DeliveryCost{"email":"_Email1_","free":"offerte"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DeliveryCost_ProvideInfo
    - slot{"free":"offerte"}
* Discount
    - utter_Discount_ProvideInfo
    - slot{"email":"_Email1_"}
    - action_Save
    - action_restart

## New Story1208

* Autre
    - utter_Autre_ProvideInfo_AskForMissingSlots
* DeliveryCost{"fdp":"frais de livraison"}
    - slot{"fdp":"frais de livraison"}
    - utter_DeliveryCost_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

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
    - action_restart

## New Story1225

* Goodbye{"mood_pos":"🙂"}
    - utter_Goodbye
    - action_restart

## New Story1309

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
    - action_restart

## New Story1315

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
    - action_restart

## New Story1354

* PaymentRefused{"device":"portable"}
    - slot{"device":"portable"}
    - utter_PaymentRefused_Phone
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1376

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
    - action_restart

## New Story1391

* MissingItem
    - utter_MissingItem_ProvideInfo
    - action_restart

## New Story1403

* DeliveryNews{"order":"40535"}
    - slot{"order":"40535"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* ReceptionAlert{"channel":"sms"}
    - slot{"channel":"sms"}
    - utter_ReceptionAlert_ProvideInfo
    - action_restart

## New Story1420

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
    - action_restart

## New Story1426

* DeliveryNews{"article":"parfum","email":"_Email1_"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* AskDetails
    - utter_DeliveryNews_AskDetails
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1439

* ProductAvailable{"article":"cadeau","fdp":"port"}
    - slot{"article":"cadeau"}
    - slot{"fdp":"port"}
    - utter_DeliveryTime_ProductAvailable_ProvideInfo_Apologize
* AskDetails
    - utter_Product_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1459

* CustomerService{"channel":"mail"}
    - slot{"channel":"mail"}
    - utter_CustomerService_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1467

* DeliveryCost
    - utter_DeliveryCost_ProvideInfo
* AskDetails
    - utter_default_fallback
    - action_restart

## New Story1495

* AccountIssue
    - utter_ErrorMessage
* Login{"pwd":"passe","resend":"renvoie"}
    - slot{"resend":"renvoie"}
    - slot{"pwd":"passe"}
    - utter_Login_AskForMissingSlots_SayHello
* Rien{"email":"email@email.com"}
    - slot{"email":"email@email.com"}
    - utter_Reinit
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1540

* Login{"email":"_Email_"}
    - slot{"email":"_Email_"}
    - slot{"email":"_Email_"}
    - utter_ErrorMessage
* Login{"pwd":"passe"}
    - slot{"pwd":"passe"}
    - utter_Reinit
* Login{"bug":"authentification"}
    - slot{"bug":"authentification"} 
    - utter_default_fallback
    - action_restart

## New Story158

* CancelOrder
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1599

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* PaymentSafe
    - utter_Payment_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1641

* DeliveryNews
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+AskDetails
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1644

* PaymentRefused
    - utter_ErrorMessage
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
    - action_restart

## New Story1646

* DeliveryNews
    - utter_AskOrder
* Rien{"order":"56"}
    - slot{"order":"56"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo

* AskDetails
    - utter_DeliveryTime_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1647

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
    - action_restart

## New Story1661

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
    - action_restart

## New Story1708

* WebsiteBug{"action":"téléchargé"}
    - slot{"action":"téléchargé"}
    - action_default_ask_rephrase
* AccountIssue{"biling":"factures"}
    - utter_default_fallback
    - action_restart

## New Story1741

* DeliveryNews{"email":"_Email_","article":"parfum","order":"00"}
    - slot{"order":"00"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1761

* MissingItem
    - utter_MissingItem_ProvideInfo_Searchorder
* ConfirmationOrder
    - utter_ConfirmationOrder_ProvideInfo
* CustomerComplaint{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_CustomerComplaint_Searchorder_Askforwaiting_ProvideInfo
* AskDetails
    - utter_ConfirmationOrder_ProvideInfo_Offeralternative
* ConfirmationOrder{"mood_neg":"dommage"}
    - slot{"mood_neg":"dommage"}
    - utter_Oui_ConfirmationOrder_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1763

* DeliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1777

* DeliveryNews{"order":"00","pr":"point relais"}
    - slot{"order":"00"}
    - slot{"pr":"point relais"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+AskDetails
    - slot{"order":"00"}
    - slot{"pr":"point relais"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1799

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
    - action_restart

## New Story1840

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
    - action_restart

## New Story1851

* DamagedPackage{"article":"parfum","email":"_Email1_","mood_neg":"déçue"}
    - slot{"article":"parfum"}
    - slot{"email":"_Email1_"}
    - slot{"mood_neg":"déçue"}
    - utter_DamagedPackage_AskForMissingSlots_Apologize
* Autre
    - utter_RefundResend
* Resend{"resend":"renvoie"}
    - slot{"resend":"renvoi"}
    - utter_Resend
    - action_Perform_action
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1862

* MissingItem
    - utter_MissingItem_Searchorder_Askforwaiting_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1870

* DeliveryNews
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - action_restart

## New Story1880

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* ReceptionAlert{"fdp":"portable"}
    - slot{"order":"00"}
    - slot{"fdp":"portable"}
    - utter_ReceptionAlert_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1882

* DeliveryNews{"email":"_Email1_","order":"00"}
    - slot{"email":"_Email1_"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1915

* CancelOrder
    - action_Search_order
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1929

* DeliveryCost
    - utter_DeliveryCost_ProvideInfo_Apologize
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1930

* DeliveryNews
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryTime{"present":"cadeau"}
    - slot{"present":"cadeau"}
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1971

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
    - action_restart

## New Story1973

* DeliveryTime
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_restart

## interactive_story_1
* Saluer
    - utter_AskForMissingSlots_SayHello

## interactive_story_1
* DeliveryNews
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## purchase issue 

* PurchaseIssue 
    - utter_ErrorMessage
* Non 
    - utter_Non_ProvideInfo

## purchase issue Oui 

* PurchaseIssue 
    - utter_ErrorMessage
* Oui 
    - utter_WebsiteBug_ProvideInfo