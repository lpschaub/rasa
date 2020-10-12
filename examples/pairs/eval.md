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

## New Story4543

* ProductQuality{"origin":"originaux"}
    - utter_ProductQuality_ProvideInfo
    - action_Save

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

## New Story9016

* ProductQuality
    - utter_ProductQuality_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## New Story26972

* DeliveryNews{"order":"608380"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story14440

* Discount{"discount":"code promo"}
    - utter_Discount_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story26335

* DeliveryNews{"date":"31/05"}
    - utter_AskOrder
* Rien{"order":"546333"}
    - slot{"order":"546333"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save


## New Story5839

* CancelOrder
    - utter_AskOrder
* Rien{"order":"15345"}
    - slot{"order":"15345"}
    - action_Perform_action
    - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
    - utter_Goodbye
    - action_Save


## New Story8606

* DeliveryTime{"date":"noel"}
    - utter_DeliveryTime_ProvideInfo
    - utter_Goodbye
    - action_Save


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


## New Story18222

* ProductQuality{"origin":"origine"}
    - utter_ProductQuality_ProvideInfo
* DeliveryCost{"fdp":"coût de livraison"}
    - utter_DeliveryCost_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## Story 9959

* AccountIssue
    - utter_Reinit
* Login{"pwd":"mot de passe"}
    - utter_Login_Repeatprevious
* Login{"pwd":"mot de passe"}
    - action_default_fallback
    - action_Save


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


## New Story2540

* AccountIssue{"pwd":"mot de passe"}
    - utter_AskPwd
* Login
    - utter_Reinit
* Thanks
    - utter_Goodbye
    - action_Save


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


## New Story9750

* ConfirmationOrder{"billing":"facture","order":"658965"}
    - slot{"order":"658965"}
    - utter_DeliveryNews_ProvideInfo
    - utter_Goodbye
    - action_Save

## New Story16601

* ProductAvailable{"article":"Ted Lapidus"}
    - utter_AskTarget
* Rien{"target":"femme"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
* Thanks
    - utter_Goodbye
    - action_Save


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


## New Story22637

* DeliveryNews{"order":"649843"}
    - slot{"order":"649843"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Goodbye
    - utter_Goodbye
    - action_Save


## New Story sample3603

* ProductAvailable{"article":"Bvlgari","sample":"échantillons"}
    - slot{"article":"Bvlgari","sample":"échantillons"}
    - action_Search_product
    - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize
* Goodbye
    - utter_Goodbye
    - action_Save

## New Story3632

* ProductAvailable{"article":"coffret cadeau homme idéal","size":"100ml"}
    - slot{"article":"coffret cadeau homme idéal"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder

## New Storyx1

* ProductTarget{"article":"eau de toilette","target":"pré-ado"}
    - slot{"article":"eau de toilette","target":"pré-ado"}
    - utter_ProductTargetNoIdea

## New Story20943

* DeliveryPlace{"pr":"point relais","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"pr":"point relais"}
    - utter_DeliveryNews_CustomerComplaint_ProvideInfo_Apologize

## Story6473

* DeliveryCountry{"country":"Guadeloupe"}
    - slot{"country":"Guadeloupe"}
    - utter_DeliveryCountry
* Thanks
    - utter_Goodbye

## New Story3120

* DeliveryNews{"order":"726648","delivery":"livraison"}
    - slot{"delivery":"livraison"}
    - slot{"order":"726648"}
    - action_Search_order
    - utter_DeliveryNews_ProvideInfo
* Thanks
    - utter_Goodbye
    - action_Save

## New Story18130

* DeliveryCost
    - action_default_fallback

## New Story23605

* ProductAvailable{"article":"Repetto"}
    - slot{"article":"Repetto"}
    - action_Search_product
    - utter_ProductAvailable_ProvideInfo_Searchorder
* AskDetails
    - utter_ProductRedirection
* Non
    - action_default_fallback

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

## New Story3846

* Discount{"discount":"code promo"}
    - slot{"discount":"code promo"}
    - utter_Discount_ProvideInfo

## New Story13098

* AccountIssue
    - utter_AskConfirmation_ProvideInfo
* Oui
    - utter_Reinit
