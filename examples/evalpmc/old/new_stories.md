## New Story2

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
* ProductAvailable{"article":"petite robe black"}
    - slot{"article":"petite robe black"}
    - action_Search_product
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Previous
    - utter_ProductAvailable_ProvideInfo_Searchorder
* ProductOrigin
    - AskDetails_StoreLocation_DeliveryTime_ProvideInfo
* ProductOrigin
    - action_Default_fallback

## New Story4

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
    - action_Save

## story5
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

## New Story9

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## New Story8

* DeliveryNews{"order":"commande 608380"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story7

* Discount{"discount":"code promo"}
    - utter_Discount_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story5

* DeliveryNews{"date":"31/05"}
    - utter_AskOrder
* Rien{"order":"546333"}
    - slot{"order":"546333"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story6

* CancelOrder
    - utter_AskOrder
* rien{"order":"15345"}
    - slot{"order":"15345"}
    - action_Perform_action
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
    - utter_Goodbye
    - action_Save


## New Story10

* DeliveryTime{"date":"noel"}
    - utter_DeliveryTime_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story11

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


## New Story12

* DeliveryNews{"date":"31 mai"}
    - utter_AskOrder
* Rien{"order":"5785"}
    - slot{"order":"5785"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* AskDetails{"date":"31 mai"}
    - utter_DeliveryNews_AskDetails_CustomerComplaint_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save


## New Story13

* ProductQuality{"origin":"origine"}
    - utter_ProductQuality_ProvideInfo
* DeliveryCost{"fdp":"coût de livraison"}
    - utter_DeliveryCost_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## Story from conversation with 2833e306c0484e7190f0442a9f796ba3 on June 30th 2020

* AccountIssue
    - utter_Reinit
* Login{"pwd":"mot de passe"}
    - utter_Login_Repeatprevious
* Login{"pwd":"mot de passe"}
    - action_Default_fallback
    - action_Save


## New Story15

* DeliveryNews
    - utter_AskOrder
* Rien{"order":"699072"}
    - slot{"order":"699072"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save


## New Story16

* AccountIssue{,"pwd":"mot de passe"}
    - utter_AskPwd
* Login
    - utter_Reinit
* Thanks
    - utter_Goodbye
    - action_Save


## New Story17
* DeliveryNews{"channel":"e-mail","channel":"téléphone"}
    - utter_AskDetails
* DeliveryTime{"delivery":"acheminement","delivery":"livraison"}
    - utter_DeliveryTime_ProvideInfo
* ProductOrigin{"place":"France"}
    - utter_AskDetails_StoreLocation_DeliveryTime_ProvideInfo
* CustomerService{"channel":"mail","channel":"téléphoner"}
    - utter_CustomerService_Contact
* Previous{"channel":"e-mails"}
    - action_Default_fallback


## New Story18

* ConfirmationOrder{,"billing":"facture"}
    - utter_DeliveryTime_ProvideInfo
    - utter_Goodbye
    - action_Save

## New Story19

* ProductAvailable{"article":"Ted Lapidus"}
    - utter_AskTarget
* Rien{"target":"femme"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
* Thanks
    - utter_Goodbye
    - action_Save


## New Story20

* DeliveryNews{"delivery":"livraison","date":"15 mai","order":"716640"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## New Story22

* DeliveryNews{"order":"649843"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## New Story21

* DeliveryNews{"order":"716640","delivery":"livraison","date":"15 mai"}
    - slot{"date":"15 mai"}
    - slot{"delivery":"livraison"}
    - slot{"order":"716640"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## Story from conversation with bf9a980148ea4e6fa0ebe1b0e45384e9 on July 15th 2020

* DeliveryNews{"order":"15","delivery":"livraison","date":"mai"}
    - slot{"date":"mai"}
    - slot{"delivery":"livraison"}
    - slot{"order":"15"}
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save

## New Storype

* DeliveryNews{"order":"649843"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - slot{"order":"649843"}

## New Story sample

* ProductAvailable{"article":"Bvlgari","sample":"échantillons"}
    - slot{"article":"Bvlgari","sample":"échantillons"}
    - action_Search_product
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story23

* ProductAvailable{"article":"coffret cadeau homme idéal","size":"100ml"}
    - slot{"article":"coffret cadeau homme idéal"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder

## New Story24

* ProductTarget{"article":"eau de toilette","target":"pré-ado"}
    - slot{"article":"eau de toilette","target":"pré-ado"}
    - utter_ProductTargetNoIdea

## New Story26

* DeliveryPlace{"pr":"point relais","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"pr":"point relais"}
    - utter_DeliveryNews_CustomerComplaint_ProvideInfo_Apologize

## Story from conversation with ab41c713572743dfba7340220b4e7d5a on July 15th 2020

* DeliveryCountry
    - utter_DeliveryCountry
* Thanks
    - utter_Goodbye

## New Story27

* DeliveryNews{"order":"726648","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"order":"726648"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story28

* DeliveryCost
    - action_Default_fallback

## New Story29

* ProductAvailable{"article":"Repetto"}
    - slot{"article":"Repetto"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
* AskDetails
    - utter_ProductRedirection
* Non
    - action_Default_fallback

## New Story30

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

## New Story31

* Discount{"discount":"code promo"}
    - slot{"discount":"code promo"}
    - utter_Discount_ProvideInfo

## New Story32

* AccountIssue
    - utter_AskConfirmation_ProvideInfo
* Oui
    - utter_Reinit
