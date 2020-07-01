## story_1
* deliveryCost{"fdp": "frais de port","free": "0 €","email": "_Email1_"}
 - utter_deliveryCost_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_2
* PaymentRefused{"payment": "régler"}
 - utter_PaymentRefused_ProvideInfo
* PaymentTool{"tool": "PayPal"}
 - utter_PaymentTool_ProvideInfo
* thanks
 - utter_thanks_Proceedtocheckpoint
* non
 - utter_non_AskForMissingSlots_SayHello
* PaymentRefused{"delivery": "livraison"}
 - utter_PaymentRefused_Proceedtocheckpoint
* oui
 - utter_oui_ProvideInfo
* non
 - utter_non_Repeatprevious
* oui
 - utter_oui_SayGoodbye

## story_3
* ProductAvailable{"present": "offrir","article": "womanity EAU de parfum spray","reload": "rechargeable"}
 - utter_ProductAvailable_ProvideInfo_Searchorder
* goodbye+thanks
 - utter_goodbye_thanks_SayGoodbye

## story_4
* damagedPackage{"damaged": "casse","transporter": "Chronopost"}
 - utter_damagedPackage_AskForMissingSlots_SayHello
* damagedPackage{"resend": "renvoi","home": "chez nous"}
 - utter_damagedPackage_Proceedtocheckpoint
* damagedPackage{"phone": "tel mob"}
 - utter_autre_ProvideInfo_Performaction
* thanks+goodbye
 - utter_thanks_goodbye_ProvideInfo_SayGoodbye

## story_5
* deliveryCost{"billing": "facturation","fdp": "frais de transport","delivery": "livrer","home": "domicile"}
 - utter_deliveryCost_AskForMissingSlots_SayHello
* goodbye
 - utter_goodbye_ProvideInfo

## story_6
* deliveryCost{"email": "_Email1_","delivery": "livraison","free": "offerte"}
 - utter_deliveryCost_ProvideInfo
* Discount{"discount": "code promo"}
 - utter_Discount_ProvideInfo_SayGoodbye

## story_7
* autre
 - utter_autre_ProvideInfo_AskForMissingSlots
* deliveryCost{"fdp": "frais de livraison","free": "offerts","discount": "code"}
 - utter_deliveryCost_ProvideInfo_Apologize
* thanks+oui
 - utter_thanks_oui_Askforanotherquestion
* non+thanks
 - utter_non_thanks_SayGoodbye

## story_11
* deliveryNews{"order": "61"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* deliveryNews+AskDetails{"store": "chez vous"}
 - utter_deliveryNews_AskDetails_ProvideInfo
* AskDetails
 - utter_AskDetails_ProvideInfo
* thanks
 - utter_thanks_SayGoodbye

## story_14
* missingItem{"missing": "manque"}
 - utter_missingItem_Searchorder_Askforwaiting_ProvideInfo
* missingItem{"order": "00"}
 - utter_missingItem_ProvideInfo_Searchorder

## story_15
* deliveryNews{"order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* ReceptionAlert{"channel": "sms"}
 - utter_ReceptionAlert_ProvideInfo

## story_16
* ProductPrice{"article": "Lolita Lempicka","discount": "remise"}
 - utter_ProductPrice_AskForMissingSlots_SayHello
* ProductPrice{"size": "100ml"}
 - utter_ProductPrice_ProvideInfo
* CustomerComplaint{"add": "publicité"}
 - utter_CustomerComplaint_ProvideInfo
* purchase
 - utter_purchase_AskForMissingSlots_SayHello

## story_17
* deliveryNews{"present": "offrir","article": "parfum","date": "dimanche 26","email": "_Email1_"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* oui
 - utter_oui_ProvideInfo
* deliveryNews{"status": "en cours de traitement"}
 - utter_deliveryNews_ProvideInfo
* goodbye+thanks
 - utter_goodbye_thanks_SayGoodbye

## story_20
* deliveryCost{"article": "parfums","delivery": "livraison"}
 - utter_deliveryCost_ProvideInfo
* deliveryCost
 - utter_deliveryCost_ProvideInfo
* deliveryCost{"discount": "code promo","pr": "relais"}
 - utter_deliveryCost_ProvideInfo_Performaction
* CustomerComplaint+goodbye{"billing": "prélèvement"}
 - utter_CustomerComplaint_goodbye_ProvideInfo

## story_21
* AccountIssue
 - utter_AccountIssue_AskForMissingSlots_SayHello
* AccountIssue{"pwd": "mot de passe","channel": "mail"}
 - utter_AccountIssue_AskForMissingSlots_SayHello
* AccountIssue{"email": "_Email1_"}
 - utter_AccountIssue_Performaction_ProvideInfo_Suggeststo
* oui+thanks
 - utter_oui_thanks_Askforanotherquestion

## story_22
* ProductTarget{"article": "fond de teint make up for ever fluide tenseur","color": "sable"}
 - utter_ProductTarget_AskForMissingSlots_SayHello
* ProductTarget
 - utter_ProductTarget_Searchorder_Askforwaiting_ProvideInfo
* thanks
 - utter_thanks_ProvideInfo_AskForMissingSlots
* ProductTarget
 - utter_ProductTarget_ProvideInfo
* goodbye+thanks
 - utter_goodbye_thanks_SayGoodbye

## story_23
* Login{"email": "_Email1_"}
 - utter_Login_AskForMissingSlots_SayHello
* Login{"pwd": "mot de passe"}
action_listen
* Login{"connection": "authentification"}
 - utter_Login_Repeatprevious
* Login
 - utter_rien_Proceedtocheckpoint

## story_25
* CancelOrder{"order": "00","cancel": "annuler"}
 - utter_CancelOrder_Searchorder_ProvideInfo_Performaction_Askforwaiting
* thanks+goodbye
 - utter_thanks_goodbye_SayGoodbye

## story_27
* deliveryNews{"transporter": "Chronopost","order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* thanks
 - utter_thanks_ProvideInfo
* deliveryNews{"status": "évolue"}
 - utter_deliveryNews_ProvideInfo
* thanks+goodbye+oui
 - utter_thanks_goodbye_oui_SayGoodbye

## story_29
* deliveryNews
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* autre
 - utter_autre_ProvideInfo
* deliveryTime
 - utter_deliveryTime_ProvideInfo
* oui
 - utter_oui_Askforanotherquestion
* non+thanks{"date": "le 19"}
 - utter_non_thanks_SayGoodbye

## story_30
* PaymentRefused{"tool": "carde américaine MasterCard","payment": "paiement","email": "_Email1_"}
 - utter_PaymentRefused_ProvideInfo_Offeralternative
* PaymentTool
 - utter_PaymentTool_ProvideInfo
* CancelOrder{"cancel": "abandonner"}
 - utter_CancelOrder_SayGoodbye

## story_31
* deliveryNews{"article": "parfum","date": "la semaine dernière","order": "00","transporter": "Chronopost","store": "chez vous"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_32
* autre
 - utter_autre_AskForMissingSlots_Apologize
* CustomerComplaint{"billing": "factures","order": "00","website": "sites","account": "compte"}
 - utter_CustomerComplaint_SayGoodbye

## story_33
* deliveryNews{"order": "00","email": "_Email1_","article": "parfum"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_35
* deliveryNews{"order": "00","email": "_Email1_","date": "10/06/19"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_36
* deliveryNews{"order": "00","delivery": "livraison","date": "samedi","pr": "point relais","mood": "inquiète"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* thanks
 - utter_thanks_ProvideInfo
* AskDetails{"status": "en dépôt"}
 - utter_AskDetails_ProvideInfo
* oui+thanks
 - utter_oui_thanks_SayGoodbye

## story_37
* Discount{"discount": "code promo"}
 - utter_Discount_AskForMissingSlots_SayHello
* Discount{"email": "_Email1_"}
 - utter_rien_Searchorder_Askforwaiting_ProvideInfo
* thanks
 - utter_thanks_ProvideInfo
* thanks
 - utter_thanks_SayGoodbye

## story_38
* Discount{"article": "parfum","date": "aujourd'hui","discount": "réduction"}
 - utter_Discount_ProvideInfo
* goodbye{"email": "_Email1_"}
 - utter_goodbye_SayGoodbye

## story_39
* damagedPackage{"article": "Insolence de _Name2_","store": "chez vous","mood": "déception","damaged": "viré","email": "_Email1_"}
 - utter_damagedPackage_AskForMissingSlots_SayHello
* damagedPackage{"order": "00"}
 - utter_rien_SayGoodbye

## story_41
* deliveryNews{"order": "00","status": "en cours","delivery": "livraison"}
 - utter_deliveryNews_ProvideInfo_Searchorder

## story_42
* deliveryNews{"order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* ReceptionAlert{"device": "portable","pr": "point relais","phone": " N"}
 - utter_ReceptionAlert_ProvideInfo
* goodbye+thanks
 - utter_goodbye_thanks_SayGoodbye

## story_43
* deliveryNews{"article": "parfum","email": "_Email1_","order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo

## story_44
* CancelOrder{"cancel": "annuler","order": "00"}
 - utter_CancelOrder_Searchorder_Askforwaiting_ProvideInfo
* CancelOrder{"email": "_Email1_","channel": "mail"}
 - utter_CancelOrder_Repeatprevious
* CancelOrder{"refund": "un avoir"}
 - utter_CancelOrder_Repeatprevious
* Refund{"resend": "renvoi"}
 - utter_Refund_SayGoodbye

## story_45
* deliveryCost+Discount{"fdp": "tarif de livraison","discount": " geste commercial"}
 - utter_deliveryCost_Discount_ProvideInfo
* goodbye
 - utter_goodbye_Offeralternative_SayGoodbye

## story_46
* deliveryNews{"order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* deliveryTime{"date": "week-end","present": "cadeau"}
 - utter_deliveryTime_ProvideInfo
* oui
 - utter_oui_SayGoodbye

## story_47
* CommuncationInterruption+deliveryNews{"transporter": "Chronopost","date": "1er octobre"}
 - utter_CommuncationInterruption_deliveryNews_ProvideInfo_Searchorder
* deliveryNews{"order": "00"}
 - utter_rien_ProvideInfo_Offeralternative
* CustomerComplaint{"channel": "système conversation","bug": "fonctionnait","customer": "service client","mood": "furieuse"}
 - utter_CustomerComplaint_ProvideInfo_Apologize
* deliveryNews{"refund": "remboursement","present": "cadeau"}
 - utter_deliveryNews_ProvideInfo_Offeralternative
* goodbye
 - utter_goodbye_ProvideInfo_Apologize

## story_49
* deliveryCost{"article": "parfums","place": "USA","fdp": "frais de douane"}
 - utter_deliveryCost_ProvideInfo_Proceedtocheckpoint
* goodbye
 - utter_goodbye_SayGoodbye

## story_50
* deliveryPlace{"order": "0201 7041 4639 69773","delivery": "delivered"}
 - utter_deliveryPlace_AskForMissingSlots_SayHello
* deliveryPlace{"transporter": "UPS"}
 - utter_rien_SayGoodbye

## story_51
* ProductPrice{"article": "Guerlain"}
 - utter_ProductPrice_ProvideInfo_Apologize
* ProductPrice
 - utter_ProductPrice_ProvideInfo_Advisetolookelsewhere

## story_52
* deliveryNews{"order": "00","date": "22/09","delivery": "livraison"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo

## story_53
* delivery{"email": "_Email1_","resend": "retourné"}
 - utter_delivery_AskForMissingSlots_SayHello
* delivery
 - utter_delivery_SayGoodbye

## story_55
* deliveryTime{"date": "Noël","delivery": "livrer"}
 - utter_deliveryTime_ProvideInfo
* AskDetails
 - utter_AskDetails_ProvideInfo
* thanks
 - utter_thanks_SayGoodbye

## story_57
* deliveryNews{"email": "_Email1_"}
 - utter_deliveryNews_AskForMissingSlots_Searchorder_Askforwaiting
* thanks
 - utter_thanks_ProvideInfo
* oui+thanks
 - utter_oui_thanks_SayGoodbye

## story_58
* deliveryNews{"order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* deliveryNews{"status": "en préparation","date": "24 mai"}
 - utter_deliveryNews_ProvideInfo
* deliveryPlace{"place": "France"}
 - utter_deliveryPlace_ProvideInfo
* thanks
 - utter_thanks_SayGoodbye

## story_59
* PaymentRefused{"tool": "carte bancaire"}
 - utter_PaymentRefused_AskForMissingSlots_SayHello
* PaymentRefused
 - utter_rien_Apologize_Offeralternative

## story_60
* deliveryNews{"email": "_Email1_","delivery": "livraison","date": "09/04/19","fdp": "frais de livraison"}
 - utter_deliveryNews_ProvideInfo
* CustomerComplaint+goodbye
 - utter_CustomerComplaint_goodbye_ProvideInfo

## story_61
* saluer
 - utter_saluer_AskForMissingSlots_SayHello
* deliveryNews{"delay": "tarde","transporter": "Chronopost"}
 - utter_deliveryNews_ProvideInfo_Searchorder
* ReceptionAlert{"follow-up": "lien"}
 - utter_ReceptionAlert_ProvideInfo
* delivery
 - utter_delivery_SayGoodbye

## story_62
* ConfirmationOrder{"payment": "débité","email": "_Email1_"}
 - utter_ConfirmationOrder_Searchorder_Askforwaiting_ProvideInfo
* goodbye+thanks
 - utter_goodbye_thanks_SayGoodbye

## story_63
* deliveryNews{"order": "00","date": "10 jour","place": "france"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* ReceptionAlert
 - utter_ReceptionAlert_SayGoodbye

## story_65
* damagedPackage{"email": "_Email1_","order": "00","article": "crèmes onctueuses lolitalempica","damaged": "abîmées"}
 - utter_damagedPackage_AskForMissingSlots_Apologize
* CustomerComplaint{"channel": "mails","date": "15 jours"}
 - utter_CustomerComplaint_ProvideInfo

## story_66
* deliveryNews{"order": "10","date": "5 jours"}
 - utter_deliveryNews_AskForMissingSlots_SayHello
* deliveryNews{"email": "_Email1_"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* thanks+goodbye
 - utter_thanks_goodbye_SayGoodbye

## story_67
* deliveryNews{"date": "26 août","order": "00"}
 - utter_deliveryNews_ProvideInfo
* goodbye{"delivery": "livraison"}
 - utter_goodbye_SayGoodbye

## story_69
* ConfirmationOrder{"tool": "carte bancaire","payment": "paiement","account": "compte"}
 - utter_ConfirmationOrder_AskForMissingSlots_SayHello
* oui
 - utter_oui_Searchorder_Askforwaiting_ProvideInfo
* oui
 - utter_oui_Askforwaiting_SayGoodbye
* oui
action_listen
* oui{"mood": "rassurée"}
action_listen

## story_70
* autre{"email": "_Email1_"}
 - utter_rien_AskForMissingSlots_SayHello
* ReceptionAlert{"delivery": "livraison"}
 - utter_ReceptionAlert_ProvideInfo
* oui
 - utter_oui_Askforanotherquestion
* ChangeData{"pwd": "mot de passe"}
 - utter_ChangeData_Performaction_ProvideInfo_Suggeststo
* thanks+goodbye
 - utter_thanks_goodbye_SayGoodbye

## story_72
* ProductAvailable{"article": "Courrèges in blue"}
 - utter_ProductAvailable_Askforwaiting_ProvideInfo_Apologize

## story_74
* missingItem{"order": "00","missing": "reste"}
 - utter_missingItem_Searchorder_Askforwaiting_ProvideInfo
* thanks
 - utter_thanks_Askforanotherquestion
* non
 - utter_non_SayGoodbye

## story_76
* ReceptionAlert{"delivery": "livraison","pr": "point relais"}
 - utter_ReceptionAlert_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_78
* deliveryTime{"date": "Noel"}
 - utter_deliveryTime_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_79
* deliveryNews{"follow-up": "numéro de suivi","mood": "inquiète"}
 - utter_deliveryNews_ProvideInfo
* deliveryNews{"store": "chez vous","status": "en préparation"}
 - utter_deliveryNews_ProvideInfo_Askforanotherquestion

## story_80
* deliveryNews{"delivery": "livraison","date": "14 octobre","order": "00"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo
* ReceptionAlert{"channel": "mail"}
 - utter_ReceptionAlert_ProvideInfo
* goodbye+thanks
 - utter_goodbye_thanks_SayGoodbye

## story_81
* deliveryNews{"order": "00"}
 - utter_deliveryNews_ProvideInfo
* deliveryNews
 - utter_rien_Askforanotherquestion
* goodbye
 - utter_goodbye_SayGoodbye

## story_83
* deliveryNews{"order": "02","date": "27 mars"}
 - utter_deliveryNews_ProvideInfo
* deliveryNews{"transporter": "transporteur"}
 - utter_deliveryNews_ProvideInfo
* thanks+goodbye
 - utter_thanks_goodbye_SayGoodbye

## story_85
* deliveryNews{"order": "00"}
 - utter_deliveryNews_Askforwaiting_ProvideInfo_Askforanotherquestion
* goodbye
 - utter_goodbye_SayGoodbye

## story_86
* deliveryTime{"delivery": "livraison"}
 - utter_deliveryTime_ProvideInfo
* goodbye
 - utter_goodbye_SayGoodbye

## story_88
* PaymentRefused{"payment": "payment"}
 - utter_PaymentRefused_AskForMissingSlots_SayHello
* non
 - utter_non_AskForMissingSlots_SayHello
* non
 - utter_non_ProvideInfo
* WebsiteBug
 - utter_WebsiteBug_ProvideInfo_AskForMissingSlots
* WebsiteBug{"website": "caches"}
 - utter_WebsiteBug_ProvideInfo
* WebsiteBug{"billing": "total"}
 - utter_WebsiteBug_SayGoodbye

## story_89
* deliveryCost+Discount{"fdp": "frais de port","discount": "code d'ebienvenue"}
 - utter_deliveryCost_Discount_ProvideInfo

## story_90
* PaymentRefused{"payment": "paiement","website": "site","tool": "carte mastercard"}
 - utter_PaymentRefused_ProvideInfo_Offeralternative
* PaymentTool{"place": "France"}
 - utter_PaymentTool_AskForMissingSlots_SayHello
* PaymentTool
 - utter_PaymentTool_ProvideInfo_Apologize_Offeralternative
* thanks+goodbye+oui
 - utter_thanks_goodbye_oui_SayGoodbye

## story_96
* deliveryNews{"date": "16/11/2018"}
 - utter_deliveryNews_Searchorder_Askforwaiting_ProvideInfo_AskForMissingSlots
* deliveryNews{"resend": "renvoyez"}
 - utter_deliveryNews_ProvideInfo_Performaction
* Refund{"discount": "déduire"}
 - utter_Refund_ProvideInfo_Suggeststo_Apologize
* thanks
 - utter_thanks_SayGoodbye

## story_97
* AccountCreation{"connection": "inscrire","channel": "mail"}
 - utter_AccountCreation_AskForMissingSlots_SayHello
* AccountCreation{"email": "_Email1_"}
 - utter_AccountCreation_ProvideInfo_Lookforcustomerfile
* Login{"pwd": "mot de passe"}
 - utter_Login_AskForMissingSlots_SayHello
* thanks
 - utter_thanks_ProvideInfo
* ChangeData{"place": "_City1_"}
 - utter_ChangeData_ProvideInfo
* thanks
 - utter_thanks_Askforanotherquestion

