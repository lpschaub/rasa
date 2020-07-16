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
    - utter_goodbye
    - action_save
    - action_restart

## New Story4

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
    - utter_goodbye
    - action_save
    - action_restart

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
    - utter_goodbye
    - action_save
    - action_restart

## New Story9

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* goodbye{"order":"commande"}
    - utter_goodbye
    - action_save
    - action_restart

## New Story8

* DeliveryNews{"order":"commande 608380"}
    - utter_deliveryNews_ProvideInfopart
    - utter_goodbye
    - action_save
    - action_restart

## New Story7

* Discount{"discount":"code promo"}
    - utter_Discount
    - utter_goodbye
    - action_save
    - action_restart

## New Story5

* DeliveryNews{"date":"31/05"}
    - utter_deliveryNews_ProvideInfopart
    - utter_goodbye
    - action_save
    - action_restart

## New Story6

* Change+CancelOrder{"order":"commande"}
    - utter_CancelOrder_Searchorder_Askforwaiting_ProvideInfo
    - utter_goodbye
    - action_save
    - action_restart

## New Story10

* DeliveryNews{"date":"noel"}
    - utter_deliveryNews_ProvideInfogen
    - utter_goodbye
    - action_save
    - action_restart

## New Story11

* DeliveryNews{"date":"20 mars"}
    - utter_deliveryNews_ProvideInfopart
* thanks
    - utter_Askforanotherquestion
* deny
    - utter_goodbye
    - utter_goodbye
    - action_save
    - action_restart

## New Story12

* DeliveryNews{"date":"31 mai"}
    - utter_deliveryNews_ProvideInfopart
* AskDetails{"date":"31 mai"}
    - utter_deliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* thanks
    - utter_goodbye
    - action_save
    - action_restart

## New Story13

* ProductQuality{"origin":"origine"}
    - utter_ProductQuality_ProvideInfo
* DeliveryCost{"fdp":"coût de livraison"}
    - utter_DeliveryCost
* goodbye{"order":"commande"}
    - utter_goodbye
    - action_save
    - action_restart

## New Story14

* AccountIssue{"order":"1"}
    - utter_goodbye
    - action_save
    - action_restart

## Story from conversation with 2833e306c0484e7190f0442a9f796ba3 on June 30th 2020

* AccountIssue
    - utter_AccountIssue_Performaction_ProvideInfo_Suggeststo
* Login{"pwd":"passe"}
    - utter_Login
* Login{"order":"commande","article":"de","pwd":"mot"}
    - action_default_fallback
    - utter_goodbye
    - action_save
    - action_restart

## New Story15

* DeliveryNews{"order":"commande"}
    - utter_AskForMissingSlots_delivery
* rien{"order":"699072"}
    - utter_deliveryNews_ProvideInfopart
* thanks
    - utter_goodbye
    - action_save
    - action_restart

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
    - utter_goodbye
    - action_save
    - action_restart

## New Story17
* DeliveryNews{"channel":"e-mail","channel":"téléphone"}
    - utter_AskForMissingSlots_delivery
* DeliveryNews{"delivery":"acheminement","delivery":"livraison"}
    - utter_deliveryNews_ProvideInfogen
* ProductOrigin{"place":"France"}
    - utter_ProductOrigin
* Customer_service{"channel":"mail","channel":"téléphoner"}
    - utter_CustomerService
* Previous{"channel":"e-mails"}
    - action_default_fallback
* DeliveryPlace{"pr":"point relais"}
    - utter_DeliveryPlace
    - utter_goodbye
    - action_save
    - action_restart

## New Story18

* ConfirmationOrder{"order":"commande","billing":"facture"}
    - utter_deliveryNews_ProvideInfogen
    - utter_goodbye
    - action_save
    - action_restart

## New Story19

* ProductAvailable{"article":"Ted Lapidus"}
    - utter_AskForMissingSlots_perfume
* rien{"target":"femme"}
    - utter_ProductTarget_ProvideInfo
* thanks
    - utter_goodbye
    - utter_goodbye
    - action_save
    - action_restart

## New Story20

* DeliveryNews{"delivery":"livraison","date":"15 mai","order":"716640"}
    - utter_deliveryNews_ProvideInfopart
* goodbye
    - utter_goodbye
    - utter_goodbye
    - action_save
    - action_restart

## New Story22

* DeliveryNews{"order":"649843"}
    - utter_deliveryNews_ProvideInfo
* goodbye
    - utter_goodbye
    - utter_goodbye
    - action_save
    - action_restart

## New Story21

* DeliveryNews{"order":"716640","delivery":"livraison","date":"15 mai"}
    - slot{"date":"15 mai"}
    - slot{"delivery":"livraison"}
    - slot{"order":"716640"}
    - utter_deliveryNews_ProvideInfopart
* goodbye
    - utter_goodbye
    - action_save

## Story from conversation with bf9a980148ea4e6fa0ebe1b0e45384e9 on July 15th 2020

* DeliveryNews{"order":"15","delivery":"livraison","date":"mai"}
    - slot{"date":"mai"}
    - slot{"delivery":"livraison"}
    - slot{"order":"15"}
    - utter_deliveryNews_ProvideInfopart
* goodbye
    - utter_goodbye
    - action_save

## New Storype

* DeliveryNews{"order":"649843"}
    - slot{"order":"649843"}
    - slot{"order":"649843"}
    - utter_deliveryNews_ProvideInfopart
    - slot{"order":"649843"}

## New Story sample

* ProductAvailable{"article":"Bvlgari","sample":"échantillons"}
    - slot{"article":"Bvlgari","sample":"échantillons"}
    - utter_ProductAvailableSample
* goodbye
    - utter_goodbye
    - action_save

## New Story23

* ProductAvailable{"article":"coffret cadeau homme idéal","size":"100ml"}
    - slot{"article":"coffret cadeau homme idéal"}
    - utter_ProductAvailableQuality

## New Story24

* ProductTarget{"article":"eau de toilette","target":"pré-ado"}
    - slot{"article":"eau de toilette","target":"pré-ado"}
    - utter_ProductTarget_ProvideInfo

## New Story26

* deliveryPlace{"pr":"point relais","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"pr":"point relais"}
    - utter_deliveryPlace_CustomerComplaint_ProvideInfo_Apologize

## Story from conversation with ab41c713572743dfba7340220b4e7d5a on July 15th 2020

* DeliveryCountry
    - utter_DeliveryCountry
* thanks
    - utter_goodbye

## New Story27

* DeliveryNews{"order":"726648","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"order":"726648"}
    - utter_deliveryNews_ProvideInfopart
* thanks
    - utter_goodbye
    - action_save

## New Story28

* DeliveryCost
    - action_default_fallback

## New Story29

* ProductAvailable{"article":"Repetto"}
	- slot{"article":"Repetto"}
    - utter_ProductAvailable_ProvideInfo_Searchorder
* AskDetails
    - utter_ProductAvailableRedirection
* deny

## New Story30

* DeliveryNews
    - utter_AskForMissingSlots_delivery
* rien{"order":"465897"}
    - slot{"order":"465897"}
    - utter_deliveryNews_ProvideInfopart
* ProductOrigin
    - utter_ProductOrigin
* goodbye
    - utter_goodbye
    - action_save

## New Story31

* Discount{"discount":"code promo"}
    - slot{"discount":"code promo"}
    - utter_Discount_ProvideInfo

## New Story32

* AccountIssue{"order":"commande"}
    - slot{"order":"commande"}
    - utter_AccountCreation_ProvideInfo_Lookforcustomerfile
* oui{"oui":"oui"}
    - utter_AccountIssue_Performaction_ProvideInfo_Suggeststo
