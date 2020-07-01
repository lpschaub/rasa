## New Story2

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
* ProductAvailable{"article":"petite robe black"}
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Previous
    - utter_ProductAvailableRedirection
* ProductOrigin
    - utter_ProductOrigin
* ProductOrigin

## New Story4

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo

## story5
* Discount{"discount":"code promo"}
    - utter_Discount_ProvideInfo
* ProductTarget{"target":"femme","target":"mere"}
    - utter_ProductTarget_ProvideInfo
* thanks
    - utter_Askforanotherquestion
* Send{"discount":"codes de réduction","channel":"email"}
    - utter_Send_Performaction
* goodbye
    - utter_goodbye

## New Story9

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* goodbye{"order":"commande"}

## New Story8

* DeliveryTime{"order":"commande 608380"}
    - utter_deliveryTime_ProvideInfopart

## New Story7

* Discount{"discount":"code promo"}
    - utter_Discount

## New Story5

* DeliveryTime{"date":"31/05"}
    - utter_deliveryTime_ProvideInfopart

## New Story6

* Change+CancelOrder{"order":"commande"}
    - utter_CancelOrder_Searchorder_Askforwaiting_ProvideInfo

## New Story10

* DeliveryTime{"date":"noel"}
    - utter_deliveryTime_ProvideInfogen

## New Story11

* DeliveryTime{"date":"20 mars"}
    - utter_deliveryTime_ProvideInfopart
* thanks
    - utter_Askforanotherquestion
* deny
    - utter_goodbye

## New Story12

* DeliveryTime{"date":"31 mai"}
    - utter_deliveryTime_ProvideInfopart
* AskDetails{"date":"31 mai"}
    - utter_deliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* thanks

## New Story13

* ProductQuality{"origin":"origine"}
    - utter_ProductQuality_ProvideInfo
* DeliveryCost{"fdp":"coût de livraison"}
    - utter_DeliveryCost
* goodbye{"order":"commande"}

## New Story14

* AccountIssue{"order":"1"}

## Story from conversation with 2833e306c0484e7190f0442a9f796ba3 on June 30th 2020

* AccountIssue
    - utter_AccountIssue_Performaction_ProvideInfo_Suggeststo
* Login{"pwd":"passe"}
    - utter_Login
* Login{"order":"commande","article":"de","pwd":"mot"}
    - action_default_fallback

## New Story15

* DeliveryTime{"order":"commande"}
    - utter_AskForMissingSlots_delivery
* rien{"order":"699072"}
    - utter_deliveryTime_ProvideInfopart
* thanks

## New Story16

* AccountIssue{"order":"commande","pwd":"mot de passe"}
    - utter_AskForMissingSlots_login
* Login
    - utter_Login_Repeatprevious
* thanks{"pwd":"mot de passe"}
    - utter_Askforanotherquestion
* Login{"pwd":"mot de passe"}
    - utter_ProvideInfo
* thanks
    - utter_goodbye

## New Story17
* DeliveryTime{"channel":"e-mail","channel":"téléphone"}
    - utter_AskForMissingSlots_delivery
* DeliveryTime{"delivery":"acheminement","delivery":"livraison"}
    - utter_deliveryTime_ProvideInfogen
* ProductOrigin{"place":"France"}
    - utter_ProductOrigin
* Customer_service{"channel":"mail","channel":"téléphoner"}
    - utter_CustomerService
* Previous{"channel":"e-mails"}
    - action_default_fallback
* DeliveryPlace{"pr":"point relais"}
    - utter_DeliveryPlace

## New Story18

* ConfirmationOrder{"order":"commande","billing":"facture"}
    - utter_deliveryTime_ProvideInfogen

## New Story19

* ProductAvailable{"article":"Ted Lapidus"}
    - utter_AskForMissingSlots_perfume
* rien{"target":"femme"}
    - utter_ProductTarget_ProvideInfo
* thanks
    - utter_goodbye

## New Story20

* DeliveryTime{"delivery":"livraison","date":"15 mai","order":"716640"}
    - utter_deliveryTime_ProvideInfopart
* goodbye
    - utter_goodbye

## New Story

* DeliveryTime{"order":"649843"}
    - utter_deliveryTime_ProvideInfo
* goodbye
    - utter_goodbye
