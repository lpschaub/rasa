## story_1
* DeliveryNews
    - utter_AskOrder
* Rien{"order":"167351"}
    - slot{"order":"167351"}
    - action_search_order
    - utter_DeliveryNews_ProvideInfo

## story10317
* DeliveryNews
    - utter_AskOrder
* Rien{"order":"716283","order":"716664"} 
    - slot{"order":"716664"}
    - slot{"order":"716283"}
    - action_search_order
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
* Rien{"email":_Email1_"}
    - slot{"email":_Email1_"}
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
    - utter_DiscountRegistrer
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
    - slot{"mood_neg":"déçue}
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

























