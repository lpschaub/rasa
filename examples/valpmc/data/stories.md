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
    - action_default_fallback
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
    - action_default_fallback
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
    - action_default_fallback
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

## New Story1988

* DeliveryCost{"fdp":"frais"}
    - slot{"fdp":"frais"}
    - utter_DeliveryCost_ProvideInfo_Proceedtocheckpoint
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story1993

* Autre
    - action_default_fallback
    - action_restart

## New Story2013

* ProductPrice{"article":"parfum"}
    - slot{"article":"parfum"}
    - action_Search_order
    - utter_ProductPrice_ProvideInfo
* ProductPrice{"article":"Guerlain"}
    - slot{"article":"Guerlain"}
    - utter_ProductPrice_ProvideInfo_Advisetolookelsewhere
    - action_restart

## New Story2044

* DeliveryNews{"date":"22/09","event":"anniversaire","order":"00"}
    - slot{"order":"00"}
    - slot{"date":"22/09"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story2067

* Returned{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskOrder
* Rien{"order":"4523"}
    - slot{"order":"4523"}
    - slot{"email":"_Email1_"}
    - action_default_fallback
    - action_restart

## New Story2070

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
    - action_restart

## New Story2073

* DeliveryTime{"date":"Noël"}
    - slot{"date":"Noël"}
    - utter_DeliveryTime_ProvideInfo
* AskDetails
    - slot{"date":"Noël"}
    - utter_DeliveryTime_ProductAvailable_ProvideInfo_Apologize
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story2192

* DeliveryNews{"order":"00","resend":"envoi"}
    - slot{"resend":"envoi"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_CustomerComplaint_ProvideInfo_Apologize
* DeliveryNews+CustomerComplaint{"resend":"envoi"}
    - slot{"resend":"envoi"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
* DeliveryNews+CustomerComplaint
    - utter_DeliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* CustomerComplaint+goodbye
    - utter_Goodbye
    - action_restart

## New Story2196

* DeliveryNews{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story2280

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
    - action_restart

## New Story_troll2340

* PaymentRefused{"tool":"carte bancaire"}
    - slot{"tool":"carte bancaire"}
    - utter_Troll
* AskDetails
    - slot{"tool":"carte bancaire"}
    - utter_PaymentTool_AskForMissingSlots_SayHello
* Oui
    - utter_PaymentTool_ProvideInfo_Apologize_Offeralternative
    - action_restart

## New Story2345

* DeliveryNews{"email":"_Email1_","date":"09/04/19","fdp":"frais","order":"00"}
    - slot{"date":"09/04/19"}
    - slot{"order":"00"}
    - slot{"email":"_Email1_"}
    - slot{"fdp":"frais"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* CustomerComplaint+goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story240

* Saluer
    - utter_AskForMissingSlots_SayHello
* DeliveryNews+AskDetails{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* AskDetails
    - action_default_fallback
    - action_restart

## New Story252

* ConfirmationOrder{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_ConfirmationOrder_Searchorder_Askforwaiting_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story260

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* ReceptionAlert
    - action_default_fallback
    - action_restart

## New Story277

* DeliveryNews{"transporter":"chrono"}
    - slot{"transporter":"chrono"}
    - slot{"transporter":"chrono"}
    - action_Search_order
    - utter_DeliveryNews_AskDetails_ProvideInfo
    - slot{"transporter":"chrono"}
* StoreLocation+DeliveryTime{"transporter":"chrono","date":"31/12"}
    - slot{"date":"31/12"}
    - slot{"transporter":"chrono"}
    - utter_AskDetails_StoreLocation_DeliveryTime_ProvideInfo
* AskDetails
    - utter_DeliveryTime_ProvideInfo
* DeliveryNews+AskDetails{"date":"samedi"}
    - slot{"date":"samedi"}
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_restart

## New Story281

* DamagedPackage{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_DamagedPackage_AskForMissingSlots_Apologize
* CustomerComplaint
    - utter_DamagedPackage_ProvideInfo_Searchorder
    - action_restart

## New Story287

* DeliveryNews
    - utter_AskEmail
* Rien{"email":"e@mel.fr"}
    - slot{"email":"e@mel.fr"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story293

* DeliveryNews
    - utter_AskEmail
* Rien{"email":"e@mel.fr"}
    - slot{"email":"e@mel.fr"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Storytroll300

* DeliveryNews
    - utter_AskOrder
* Non{"date":"7/06"}
    - slot{"date":"7/06"}
    - utter_Troll
    - action_restart

## New Story307

* ConfirmationOrder{"tool":"carte bancaire","payment":"paiement","confirmation":"confirmation"}
    - slot{"confirmation":"confirmation"}
    - utter_ConfirmationOrder_AskForMissingSlots_SayHello
* Oui
    - utter_Oui_Askforwaiting_SayGoodbye
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story313

* Rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskForMissingSlots_SayHello
* ReceptionAlert
    - utter_ReceptionAlert_ProvideInfo
* Thanks
    - utter_Askforanotherquestion
    - slot{"email":"_Email1_"}
* ChangeData{"pwd":"mot de passe"}
    - slot{"pwd":"mot de passe"}
    - utter_ChangeData_Performaction_ProvideInfo_Suggeststo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story325

* Saluer
    - utter_AskForMissingSlots_SayHello
* DeliveryNews+AskDetails{"email":"_Email1_","date":"samedi","follow-up":"suivi"}
    - slot{"date":"samedi"}
    - slot{"follow-up":"suivi"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+DeliveryPlace{"transporter":"Chronopost"}
    - slot{"transporter":"Chronopost"}
    - slot{"follow-up":"suivi"}
    - utter_DeliveryNews_AskDetails_ProvideInfo
    - action_restart

## New Story330

* ProductAvailable{"article":"Courrèges in blue"}
    - slot{"article":"Courrèges in blue"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
    - action_restart

## New StoryInterestingMemory341

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
    - action_restart

## New Story371

* MissingItem{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story412

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
    - action_restart

## New Story420

* ReceptionAlert{"channel":"sms","pr":"point relais"}
    - slot{"channel":"sms"}
    - slot{"pr":"point relais"}
    - utter_ReceptionAlert_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story444

* DeliveryNews+AskDetails{"follow-up":"suivi","mood_neg":"inquiète"}
    - slot{"follow-up":"suivi"}
    - slot{"mood_neg":"inquiète"}
    - utter_AskOrder
* Rien{"order":"54678"}
    - slot{"order":"54678"}
    - action_Search_order
    - utter_DeliveryNews_AskDetails_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story457

* DeliveryNews{"order":"00","date":"14 octobre"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* ReceptionAlert{"channel":"mail"}
    - slot{"channel":"mail"}
    - slot{"order":"00"}
    - utter_ReceptionAlert_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_restart

## New Storypassepas438

* Discount{"code":"NOEL02"}
    - slot{"code":"NOEL02"}
    - utter_Discount_AskForMissingSlots_SayHello
* Rien{"email":"mon@mel.fr"}
    - slot{"code":"NOEL02"}
    - slot{"email":"mon@mel.fr"}
    - utter_Discount_ProvideInfo
* Discount
    - action_default_fallback
    - action_restart

## New Story468

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Storyrenvoir477

* DeliveryNews{"email":"_Email1_2","order":"03"}
    - slot{"email":"_Email1_2"}
    - slot{"order":"03"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* DeliveryNews+DeliveryPlace{"home":"domicile"}
    - slot{"home":"domicile"}
    - slot{"order":"03"}
    - utter_DeliveryNews_ProvideInfo_Apologize_Offeralternative
* DeliveryPlace{"resend":"recommander"}
    - slot{"home":"domicile"}
    - slot{"resend":"recommander"}
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
    - action_restart

## New Story510

* DeliveryNews{"date":"27 mars"}
    - slot{"date":"27 mars"}
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
    - action_restart

## New Story566

* DeliveryNews{"email":"_Email1_","order":"00","date":"1 juin 2019"}
    - slot{"email":"_Email1_"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Lost
    - utter_RefundResend
    - slot{"date":"1 juin 2019"}
* Resend{"operation":"renvoyez"}
    - action_Perform_action
    - utter_Resend
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story579

* DeliveryNews{"email":"_Email1_","order":"00"}
    - slot{"order":"00"}
    - slot{"email":"_Email1_"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story612

* DeliveryTime
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story655

* DeliveryCost{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_DeliveryCost_ProvideInfo_Apologize
* Discount
    - utter_Discount_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_restart

## New Story661

* PaymentRefused
    - utter_ErrorMessage
* Non
    - utter_DeliveryMode
* Non
    - utter_Non_ProvideInfo
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo
* WebsiteBug
    - action_default_fallback
    - action_restart

## New Story714

* DeliveryCost{"fdp":"port"}
    - slot{"fdp":"port"}
    - utter_DeliveryCost_ProvideInfo_Apologize
    - action_restart

## New Story731

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
    - action_default_fallback
    - action_restart

## New Story750

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
    - action_restart

## New Story802

* DeliveryNews{"order":"00"}
    - slot{"order":"00"}
    - action_Search_order
    - utter_DeliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* CustomerComplaint+goodbye
    - utter_Goodbye
    - action_restart

## New Story820

* DeliveryPlace{"country":"France","present":"cadeau"}
    - slot{"country":"France"}
    - slot{"present":"cadeau"}
    - action_default_fallback
    - action_restart

## New Story843

* DeliveryNews
    - utter_AskOrder
* Rien{"order":"4968"}
    - slot{"order":"4968"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo_Offeralternative
* CustomerComplaint+goodbye{"refund":"remboursement","country":"Française","transporter":"Chronopost","fdp":"Française","article":"fond"}
    - slot{"refund":"remboursement"}
    - slot{"article":"fond"}
    - slot{"country":"Française"}
    - slot{"fdp":"Française"}
    - slot{"transporter":"Chronopost"}
    - action_default_fallback
    - action_restart

## New story858

* DeliveryNews{"date":"16/11/2018"}
    - slot{"date":"16/11/2018"}
    - utter_AskOrder
* Rien{"order":"785898"}
    - utter_DeliveryNews_Lost
    - utter_RefundResend
* Resend{"resend":"renvoyez"}
    - slot{"resend":"renvoyez"}
    - utter_Resend
* Thanks 
    - utter_Goodbye
    - action_Save
    - action_restart

## new story868

* AccountCreation
    - utter_AskEmail
* Rien{"email":"mon@mail.com"}
    - slot{"email":"mon@mail.com"}
    - utter_AccountCreation_ProvideInfo_Lookforcustomerfile
* ChangeData{"place":"_City1_"}
    - slot{"place":"_City1_"}
    - utter_ChangeData_ProvideInfo
* Thanks
    - utter_Goodbye
## New Story3539

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
* ProductAvailable{"article":"petite robe black"}
    - slot{"article":"petite robe black"}
    - action_Search_product
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Previous
    - utter_ProductAvailable_ProvideInfo_Searchorder
* ProductOrigin
    - utter_AskDetails_StoreLocation_DeliveryTime_ProvideInfo
* ProductOrigin
    - action_default_fallback
    - action_restart

## New Story4543

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
    - action_Save
    - action_restart

## story13474
* Discount{"discount":"code promo"}
    - utter_Discount_ProvideInfo
* ProductTarget{"target":"femme","target":"mere"}
    - utter_ProductTargetNoIdea
* Thanks
    - utter_Askforanotherquestion
* Discount{"discount":"codes de réduction","channel":"email"}
    - utter_Discount_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story9016

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story26972

* DeliveryNews{"order":"608380"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story14440

* Discount{"discount":"code promo"}
    - utter_Discount_ProvideInfo
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story26335

* DeliveryNews{"date":"31/05"}
    - utter_AskOrder
* Rien{"order":"546333"}
    - slot{"order":"546333"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story5839

* CancelOrder
    - utter_AskOrder
* Rien{"order":"15345"}
    - slot{"order":"15345"}
    - action_Perform_action
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story8606

* DeliveryTime{"date":"noel"}
    - utter_DeliveryTime_ProvideInfo
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story8507

* DeliveryNews{"date":"20 mars"}
    - utter_AskOrder
* Rien {"order":"4868"}
    - slot{"order":"4868"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo

* Thanks
    - utter_Askforanotherquestion
* Non
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story9912

* DeliveryNews{"date":"31 mai","order":"5785"}
    - slot{"order":"5785"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* AskDetails{"date":"31 mai"}
    - utter_DeliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story18222

* ProductQuality{"origin":"origine"}
    - utter_ProductQuality_ProvideInfo
* DeliveryCost{"fdp":"coût de livraison"}
    - utter_DeliveryCost_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## Story 9959

* AccountIssue
    - utter_Reinit
* Login{"pwd":"mot de passe"}
    - utter_Login_Repeatprevious
* Login{"pwd":"mot de passe"}
    - action_default_fallback
    - action_Save
    - action_restart

## New Story8298

* DeliveryNews
    - utter_AskOrder
* Rien{"order":"699072"}
    - slot{"order":"699072"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story2540

* AccountIssue{"pwd":"mot de passe"}
    - utter_AskPwd
* Login
    - utter_Reinit
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story14983
* DeliveryNews{"channel":"e-mail","channel":"téléphone"}
    - utter_AskDetails
* DeliveryTime{"delivery":"acheminement","delivery":"livraison"}
    - utter_DeliveryTime_ProvideInfo
* ProductOrigin{"place":"France"}
    - utter_AskDetails_StoreLocation_DeliveryTime_ProvideInfo
* CustomerService{"channel":"mail","channel":"téléphoner"}
    - utter_CustomerService_Contact
* Previous{"channel":"e-mails"}
    - action_default_fallback
    - action_restart

## New Story9750

* ConfirmationOrder{"billing":"facture","order":"658965"}
    - slot{"order":"658965"}
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story16601

* ProductAvailable{"article":"Ted Lapidus"}
    - utter_AskTarget
* Rien{"target":"femme"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story12747

* DeliveryNews{"order":"716640","delivery":"livraison","date":"15 mai"}
    - slot{"date":"15 mai"}
    - slot{"delivery":"livraison"}
    - slot{"order":"716640"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story22637

* DeliveryNews{"order":"649843"}
    - slot{"order":"649843"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story sample3603

* ProductAvailable{"article":"Bvlgari","sample":"échantillons"}
    - slot{"article":"Bvlgari","sample":"échantillons"}
    - action_Search_product
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story3632

* ProductAvailable{"article":"coffret cadeau homme idéal","size":"100ml"}
    - slot{"article":"coffret cadeau homme idéal"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
    - action_restart

## New Storyx1

* ProductTarget{"article":"eau de toilette","target":"pré-ado"}
    - slot{"article":"eau de toilette","target":"pré-ado"}
    - utter_ProductTargetNoIdea
    - action_restart

## New Story20943

* DeliveryPlace{"pr":"point relais","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"pr":"point relais"}
    - utter_DeliveryNews_CustomerComplaint_ProvideInfo_Apologize
    - action_restart

## Story6473

* DeliveryCountry{"country":"Guadeloupe"}
    - slot{"country":"Guadeloupe"}
    - utter_DeliveryCountry
* Thanks
    - utter_Goodbye
    - action_restart

## New Story3120

* DeliveryNews{"order":"726648","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"order":"726648"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story18130

* DeliveryCost
    - action_default_fallback
    - action_restart

## New Story23605

* ProductAvailable{"article":"Repetto"}
    - slot{"article":"Repetto"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
* AskDetails
    - utter_ProductRedirection
* Non
    - action_default_fallback
    - action_restart

## New Story536

* DeliveryNews
    - utter_AskOrder
* Rien{"order":"465897"}
    - slot{"order":"465897"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* ProductOrigin
    - utter_AskDetails_StoreLocation_DeliveryTime_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save
    - action_restart

## New Story3846

* Discount{"discount":"code promo"}
    - slot{"discount":"code promo"}
    - utter_Discount_ProvideInfo
    - action_restart

## New Story13098

* AccountIssue
    - utter_AskConfirmation_ProvideInfo
* Oui
    - utter_Reinit
    - action_restart

## reset 

* Reset
    - action_restart

## New Story hello 

* Saluer
    - utter_AskForMissingSlots_SayHello
* Reset 
    - action_restart

## New Story bonjour 

* Saluer 
    - utter_AskForMissingSlots_SayHello

## story_1-test
* DeliveryNews
    - utter_AskOrder
* Rien{"order":"167351"}
    - slot{"order":"167351"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo

## story10317
* DeliveryNews
    - utter_AskOrder
* Rien{"order":"716283","order":"716664"} 
    - slot{"order":"716664"}
    - slot{"order":"716283"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## story22909
* PurchaseIssue{"transporter":"transporteur"}
    - slot{"transporter":"transporteur"}
    - utter_DeliveryMode
* Previous{"pr":"point relais"}
    - slot{"pr":"point relais"}
    - utter_Non_ProvideInfo
* Oui 
    - utter_Goodbye
    - action_Save

## story21449
* Login{"channel":"adresse mail","wrong":"incorrecte"}
    - slot{"wrong":"incorrecte"}
    - slot{"channel":"adresse mail"}
    - utter_AskEmail
* Rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_Login_ProvideInfo
* Thanks 
    - utter_Goodbye
* WebsiteBug{"authentification":"authentification"}
    - slot{"authentification":"authentification"}
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
    - action_Save

## story3802
* Rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskForMissingSlots_SayHello
* MissingItem{"article":"Gucci by Gucci","payment":"débité"}
    - slot{"article":"Gucci by Gucci"}
    - slot{"payment":"débité"}
    - utter_AskOrder
* Rien{"order":"XU073810295FR","order":"xu073787671r"}
    - slot{"order":"XU073810295FR"}
    - slot{"order":"xu073787671r"}
    - utter_DeliveryNews_ProvideInfo
* AskDetails{"channel":"mail","missing":"manquant"}
    - slot{"channel":"mail"}
    - slot{"missing":"manquant"}
    - utter_ReceptionAlert_ProvideInfo
    - utter_Goodbye
    - action_Save

## story15844
* Discount{"email":"_Email1_","discount":"code promo"}
    - slot{"email":"_Email1_"}
    - slot{"discount":"code promo"}
    - utter_Discount_ProvideInfo

## story15244
* DeliveryNews{"channel":"mail"}
    - slot{"channel":"mail"}
    - utter_DeliveryNews_ProvideInfo
* ReceptionAlert{"channel":"mail"}
    - slot{"channel":"mail"}
    - utter_ReceptionAlert_ProvideInfo
* Thanks 
    - utter_Goodbye
    - action_Save

## story14589
* DamagedPackage{"mood_neg":"mécontentement","photo":"photo" ,"anormale":"damaged"}
    - slot{"mood_neg":"mécontentement"}
    - slot{"photo":"photo"} 
    - slot{"anormale":"damaged"}
    - utter_DamagedPackage_DeliveryNews
* Goodbye
    - utter_Goodbye
    - action_Save

## story6069
* PurchaseIssue
    - utter_ErrorMessage
* AccountIssue{"channel":"email"}
    - slot{"channel":"email"}
    - utter_AskEmail
* Rien{"email":"mail@e.co"}
    - slot{"email":"mail@e.co"}
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* AskDetails{"website":"navigateur"}
     - slot{"website":"navigateur"}
     - action_default_fallback
     - action_Save

## story15610
* Discount{"discount":"code promotionnel"}
    - slot{"discount":"code promotionnel"}
    - utter_AskCode
* Rien{"code":"Soldes10"}
    - slot{"code":"Soldes10"}
    - utter_Discount_ProvideInfo

## story9549
* CustomerComplaint
    - action_default_fallback

## story 10438
* DeliveryPlace{"pr":"point relais","address":"adresse"}
    - slot{"pr":"point relais"}
    - slot{"address":"adresse"}
    - utter_AskAdress
* Oui
    - utter_UpdateAccount
* Discount{"discount":"bon"}
    - slot{"discount":"bon"}
    - utter_Discount_ProvideInfo
* Discount+CustomerComplaint
    - utter_DiscountRegistred
* WebsiteBug
    - utter_WebsiteBug_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## story6243
* WebsiteBug{"email":"em@pofd.fr"}
    - slot{"email":"em@pofd.fr"}
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* WebsiteBug{"basket":"panier"}
    - slot{"basket":"panier"}
    - utter_WebsiteBug_ProvideInfo
* Autre
    - utter_Goodbye
    - action_Save

## story19709

* AccountCreation{"channel":"adresse mail"}
    - slot{"channel":"adresse mail"}
    - utter_ErrorMessage
* AccountIssue
    - slot{"channel":"adresse mail"}
    - utter_AskEmail
* Rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskData
* Rien{"email":"_Email1_", "order":"679295","date":"01/11/1967","address":"31 rue _City2 _ZipCode1_ _City1_"}
    - slot{"email":"_Email1_"}
    - slot{"order":"679295"}
    - slot{"date":"01/11/1967"}
    - slot{"address":"31 rue _City2 _ZipCode1_ _City1_"}
    - utter_AskPhone
* Rien{"phone":"_Phone1_"}
    - slot{"email":"_Email1_"}
    - slot{"order":"679295"}
    - slot{"date":"01/11/1967"}
    - slot{"address":"31 rue _City2 _ZipCode1_ _City1_"}
    - slot{"phone":"_Phone1_"}
    - utter_AccountCreation_Done
* Thanks 
    - utter_Goodbye
    - action_Save

## story19709bis

* AccountCreation{"channel":"adresse mail"}
    - slot{"channel":"adresse mail"}
    - utter_ErrorMessage
* AccountIssue
    - slot{"channel":"adresse mail"}
    - utter_AskEmail
* Rien{"email":"_Email1_"}
    - slot{"email":"_Email1_"}
    - utter_AskData
* Rien{"email":"_Email1_", "order":"679295","phone":"_Phone1_","date":"01/11/1967","address":"31 rue _City2 _ZipCode1_ _City1_"}
    - slot{"email":"_Email1_"}
    - slot{"order":"679295"}
    - slot{"date":"01/11/1967"}
    - slot{"address":"31 rue _City2 _ZipCode1_ _City1_"}
    - slot{"phone":"_Phone1_"}
    - utter_AccountCreation_Done
* Thanks 
    - utter_Goodbye
    - action_Save

## story24555
* Autre{"article":"bain de champagne"}
    - action_default_fallback

## story24247
* CustomerComplaint{"pr":"point relais"}
    - action_default_fallback

## story4183
* AccountCreation
    - utter_ErrorMessage

## story5223
* MissingItem{"date":"29/06","refund":"remboursé","status":"en cours"}
    - slot{"date":"29/06"}
    - slot{"refund":"remboursé"}
    - slot{"status":"en cours"}
    - utter_DeliveryNews_Lost
* Refund{"payment":"payé","paypal":"paypal","refund":"remboursez"}
    - slot{"payment":"payé"}
    - slot{"paypal":"paypal"}
    - slot{"refund":"remboursez"}
    - utter_Refund_SayGoodbye
* CustomerComplaint+Attrition{"mood_neg":"déçue","attrition":"perdre"}
    - slot{"mood_neg":"déçue"}
    - slot{"attrition":"perdre"}
    - utter_DeliveryNews_CustomerComplaint_ProvideInfo_Apologize
    - action_Save

## story14574
* DeliveryCost{"fdp":"frais de port","free":"gratuits"}
    - slot{"fdp":"frais de port"}
    - slot{"free":"gratuits"}
    - utter_DeliveryCost_ProvideInfo
* Discount{"discount":"code","code":"Name2"}
    - slot{"code":"Name2"}
    - utter_Oui
* Thanks 
    - utter_Goodbye
    - action_Save

## story25271

* DeliveryNews{"order":"719512"}
    - slot{"order":"719512"}
    - utter_DeliveryNews_ProvideInfo
* ReceptionAlert{"channel":"sms"}
    - slot{"channel":"sms"}
    - utter_ReceptionAlert_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save 

## story16622
* PaymentTool{"payment":"payer","tool":"CB"}
    - slot{"payment":"payer"}
    - slot{"tool":"CB"}
    - utter_Payment_Apologize
    - action_Save

## story7935
* DeliveryNews
    - utter_DeliveryNews_ProvideInfo

## story25404
* AccountIssue{"channel":"l'adresse mail","pwd":"mot de passe"}
    - slot{"channel":"l'adresse mail"}
    - slot{"pwd":"mot de passe"}
    - utter_AskEmail
* Rien{"email":"_Email56_"}
    - slot{"pwd":"mot de passe"}
    - slot{"email":"_Email56_"}
    - utter_Login_ProvideInfo

## story21811
* PurchaseIssue{"home":"domicile"}
    - utter_DeliveryMode
    - slot{"home":"domicile"}
* WebsiteBug{"bug":"bloque"}
    - slot{"bug":"bloque"}
    - utter_AskDetails
* WebsiteBug{"transporter":"transporteur"}
    - slot{"transporter":"transporteur"}
    - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* Thanks
    - utter_Goodbye
    - action_Save

## story11478
* Login{"pwd":"mot de passe"}
    - slot{"pwd":"mot de passe"}
    - utter_AskEmail
* Rien{"email":"_Email1_"}
    - slot{"pwd":"mot de passe"}
    - slot{"email":"_Email1_"}
    - utter_Login_ProvideInfo
* Goodbye{"mood_pos":"efficace"}
    - utter_Goodbye
    - action_Save

## story6923
* DeliveryTime
    - utter_DeliveryTime_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## story6510
* PaymentRefused{"article":"cerruti"}
    - slot{"article":"cerruti"}
    - utter_ErrorMessage

























