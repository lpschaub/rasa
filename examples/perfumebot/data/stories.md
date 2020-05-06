## story_1
* deliveryCost{"fdp": "frais de port", "free": "0 €", "email": "_Email1_"}
 - utter_ProvideInfo
* goodbye
 - utter_SayGoodbye

## story_2
* PaymentRefused{"payment": "régler"}
 - utter_ProvideInfo
* PaymentTool{"tool": "PayPal"}
 - utter_ProvideInfo
* thanks
 - utter_Proceedtocheckpoint
* non
 - utter_AskForMissingSlots
* PaymentRefused{"delivery": "livraison"}
 - utter_Proceedtocheckpoint
* oui
 - utter_ProvideInfo
* non
 - utter_Repeatprevious
* oui
 - utter_SayGoodbye

## story_3
* ProductAvailable{"present": "offrir", "article": "womanity EAU de parfum spray", "reload": "rechargeable"}
 - utter_ProvideInfo_Searchorder
 - action_Search_order
* goodbye+thanks
 - utter_SayGoodbye

## story_4
* damagedPackage{"damaged": "casse", "transporter": "Chronopost"}
 - utter_AskForMissingSlots
* damagedPackage{"resend": "renvoi", "home": "chez nous"}
 - utter_Proceedtocheckpoint
* autre{"phone": "tel mob"}
 - utter_ProvideInfo_Performaction
 - action_Perform_action
* thanks+goodbye
 - utter_ProvideInfo_SayGoodbye

## story_5
* deliveryCost{"billing": "facturation", "fdp": "frais de transport", "delivery": "livrer", "home": "domicile"}
 - utter_AskForMissingSlots
* goodbye
 - utter_ProvideInfo

## story_6
* deliveryCost{"email": "_Email1_", "delivery": "livraison", "free": "offerte"}
 - utter_ProvideInfo
* Discount{"discount": "code promo"}
 - utter_ProvideInfo_SayGoodbye

## story_7
* autre
 - utter_ProvideInfo_AskForMissingSlots
* deliveryCost{"fdp": "frais de livraison", "free": "offerts", "discount": "code"}
 - utter_ProvideInfo_Apologize
* thanks+oui
 - utter_Askforanotherquestion
* non+thanks
 - utter_SayGoodbye

## story_8
* WebsiteBug{"basket": "panier", "article": "insolence Guerlain", "discount": "code promo", "email": "_Email1_", "billing": "total TTC"}
 - utter_AskForMissingSlots
* CommuncationInterruption
 - utter_ProvideInfo_Offeralternative
* WebsiteBug+goodbye{"channel": "chat"}
 - utter_SayGoodbye

## story_9
* rien+goodbye
 - utter_SayGoodbye
* goodbye
 - utter_SayGoodbye

## story_10
* Login{"pwd": "numéro de passe"}
 - utter_AskForMissingSlots
* autre
 - utter_AskForMissingSlots_Repeatprevious
* autre{"email": "_Email1_"}
 - utter_ProvideInfo
* thanks+Login
 - utter_Askforanotherquestion
* goodbye
 - utter_SayGoodbye

## story_11
* deliveryNews{"order": "61"}
 - utter_Searchorder_Askforwaiting_ProvideInfo
 - action_Search_order
* deliveryNews+AskDetails{"store": "chez vous"}
 - utter_ProvideInfo
* AskDetails
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_12
* PaymentRefused{"device": "portable", "delivery": "livraison", "pr": "point relais", "payment": "régler"}
 - utter_AskForMissingSlots
* PaymentRefused{"phone": "numéro de portable"}
 - utter_ProvideInfo_Offeralternative
* autre+CancelOrder{"cancel": "j'annule"}
 - utter_SayGoodbye
* autre
 - utter_SayGoodbye

## story_13
* Login{"facebook": "FB", "pwd": "mot de passe"}
 - utter_AskForMissingSlots
* AskConfirmation
 - utter_ProvideInfo
* WebsiteBug+goodbye{"bug": "dysfonctionnait", "website": "site"}
 - utter_SayGoodbye

## story_14
* missingItem{"missing": "manque"}
 - utter_Askforwaiting
* rien{"order": "00"}
 - utter_ProvideInfo

## story_15
* deliveryNews{"order": "00"}
 - utter_ProvideInfo_Askforwaiting
* ReceptionAlert{"channel": "sms"}
 - utter_ProvideInfo

## story_16
* ProductPrice{"article": "Lolita Lempicka", "discount": "remise"}
 - utter_AskForMissingSlots
* ProductPrice{"size": "100ml"}
 - utter_ProvideInfo
* CustomerComplaint{"add": "publicité"}
 - utter_ProvideInfo
* autre
 - utter_AskForMissingSlots
* purchase
 - utter_AskForMissingSlots

## story_17
* deliveryNews{"present": "offrir", "article": "parfum", "date": "dimanche 26", "email": "_Email1_"}
 - utter_Searchorder_Askforwaiting
 - action_Search_order
* oui
 - utter_ProvideInfo
* deliveryNews{"status": "en cours de traitement"}
 - utter_ProvideInfo
* goodbye+thanks
 - utter_SayGoodbye

## story_18
* deliveryTime+ProductAvailable{"article": "eau de toilette", "size": "200ml", "target": "homme", "present": "cadeau", "delivery": "livraison", "fdp": "frais de port"}
 - utter_ProvideInfo_Apologize
* product+AskDetails
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_19
* customer_service{"channel": "mail"}
 - utter_ProvideInfo
* goodbye
 - utter_SayGoodbye

## story_20
* deliveryCost{"article": "parfums", "delivery": "livraison"}
 - utter_ProvideInfo
* deliveryCost
 - utter_ProvideInfo
* deliveryCost{"discount": "code promo", "pr": "relais"}
 - utter_ProvideInfo_Performaction
 - action_Perform_action
* CustomerComplaint+goodbye{"billing": "prélèvement"}
 - utter_ProvideInfo

## story_21
* AccountIssue
 - utter_AskForMissingSlots
* AccountIssue{"pwd": "mot de passe", "channel": "mail"}
 - utter_AskForMissingSlots
* rien{"email": "_Email1_"}
 - utter_Performaction_ProvideInfo_Suggeststo
 - action_Perform_action
* oui+thanks
 - utter_Askforanotherquestion

## story_22
* ProductTarget{"article": "fond de teint make up for ever fluide tenseur", "color": "sable"}
 - utter_AskForMissingSlots
* ProductTarget
 - utter_Askforwaiting
* thanks
 - utter_ProvideInfo_AskForMissingSlots
* ProductTarget
 - utter_ProvideInfo
* goodbye+thanks
 - utter_SayGoodbye

## story_23
* Login{"email": "_Email1_"}
 - utter_AskForMissingSlots
* Login{"pwd": "mot de passe"}
 - action_listen
* Login{"connection": "authentification"}
 - utter_Repeatprevious
* rien
 - utter_Proceedtocheckpoint
* rien
 - utter_ProvideInfo

## story_24
* autre{"email": "_Email1_"}
 - utter_AskForMissingSlots
* Discount{"discount": "code"}
 - utter_ProvideInfo
* Discount+CustomerComplaint{"website": "site"}
 - utter_ProvideInfo
* Discount{"code": "amour"}
 - utter_AskForMissingSlots
* autre
 - utter_AskForMissingSlots
* autre
 - utter_ProvideInfo
* purchase{"article": "10412339"}
 - utter_ProvideInfo_Searchorder
 - action_Search_order
* WebsiteBug{"bug": "bug"}
 - utter_ProvideInfo_Offeralternative
* WebsiteBug{"connection": "déconnecter", "operation": "manip"}
 - utter_Repeatprevious
* WebsiteBug{"pwd": "mot de passe"}
 - utter_ProvideInfo_AskForMissingSlots
* WebsiteBug{"account": "compte"}
 - utter_AskForMissingSlots
* autre
 - utter_AskForMissingSlots
* autre
 - utter_Apologize_SayGoodbye

## story_25
* CancelOrder{"order": "00", "cancel": "annuler"}
 - utter_Searchorder_ProvideInfo_Performaction_Askforwaiting
 - action_Search_order
 - action_Perform_action
* thanks+goodbye
 - utter_SayGoodbye

## story_26
* ProductQuality{"article": "parfums"}
 - utter_ProvideInfo
* payment{"payment": "paiement"}
 - utter_ProvideInfo
* goodbye+thanks
 - utter_SayGoodbye

## story_27
* deliveryNews{"transporter": "Chronopost", "order": "00"}
 - utter_Askforwaiting_Searchorder
 - action_Search_order
* thanks
 - utter_ProvideInfo
* deliveryNews{"status": "évolue"}
 - utter_ProvideInfo
* thanks+goodbye+oui
 - utter_SayGoodbye

## story_28
* PaymentRefused{"payment": "payer"}
 - utter_AskForMissingSlots
* PaymentRefused+Login{"connection": "authentification"}
 - utter_AskForMissingSlots
* rien{"email": "_Email1_"}
 - utter_Suggeststo_ProvideInfo
* deliveryTime{"delivery": "livrée", "date": "semaine prochaine", "place": "Martinique", "home": "chez mon fils", "city": "_City1_"}
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_29
* deliveryNews
 - utter_Searchorder_ProvideInfo_Askforwaiting
 - action_Search_order
* autre
 - utter_ProvideInfo
* deliveryTime
 - utter_ProvideInfo
* oui
 - utter_Askforanotherquestion
* non+thanks{"date": "le 19"}
 - utter_SayGoodbye

## story_30
* PaymentRefused{"tool": "carde américaine MasterCard", "payment": "paiement", "email": "_Email1_"}
 - utter_Offeralternative
* PaymentTool
 - utter_ProvideInfo
* CancelOrder{"cancel": "abandonner"}
 - utter_SayGoodbye

## story_31
* deliveryNews{"article": "parfum", "date": "la semaine dernière", "order": "00", "transporter": "Chronopost", "store": "chez vous"}
 - utter_ProvideInfo_Askforwaiting
* goodbye
 - utter_SayGoodbye

## story_32
* autre
 - utter_AskForMissingSlots_Apologize
* CustomerComplaint{"billing": "factures", "order": "00", "website": "sites", "account": "compte"}
 - utter_SayGoodbye

## story_33
* deliveryNews{"order": "00", "email": "_Email1_", "article": "parfum"}
 - utter_ProvideInfo_Askforwaiting
* goodbye
 - utter_SayGoodbye

## story_34
* missingItem{"date": "18juillet"}
 - utter_ProvideInfo_Searchorder
 - action_Search_order
* ConfirmationOrder{"channel": "message", "follow-up": "numéro de suivi"}
 - utter_ProvideInfo
* CustomerComplaint{"pr": "relais", "delivery": "livraison", "fdp": "frais de port", "concurrence": "nocive"}
 - utter_Askforwaiting_Searchorder_ProvideInfo
 - action_Search_order
* ConfirmationOrder
 - utter_ProvideInfo_Offeralternative
* oui+ConfirmationOrder{"website": "site"}
 - utter_ProvideInfo
* oui+goodbye
 - utter_SayGoodbye

## story_35
* deliveryNews{"order": "00", "email": "_Email1_", "date": "10/06/19"}
 - utter_Askforwaiting
* goodbye
 - utter_SayGoodbye

## story_36
* deliveryNews{"order": "00", "delivery": "livraison", "date": "samedi", "pr": "point relais", "mood": "inquiète"}
 - utter_Searchorder_Askforwaiting
 - action_Search_order
* thanks
 - utter_ProvideInfo
* AskDetails{"status": "en dépôt"}
 - utter_ProvideInfo
* oui+thanks
 - utter_SayGoodbye

## story_37
* Discount{"discount": "code promo"}
 - utter_AskForMissingSlots
* rien{"email": "_Email1_"}
 - utter_Askforwaiting
* thanks
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_38
* Discount{"article": "parfum", "date": "aujourd'hui", "discount": "réduction"}
 - utter_ProvideInfo
* goodbye{"email": "_Email1_"}
 - utter_SayGoodbye

## story_39
* damagedPackage{"article": "Insolence de _Name2_", "store": "chez vous", "mood": "déception", "damaged": "viré", "email": "_Email1_"}
 - utter_AskForMissingSlots
* rien{"order": "00"}
 - utter_SayGoodbye

## story_40
* missingItem{"order": "00"}
 - utter_AskForMissingSlots
* missingItem{"article": "angel", "target": "homme"}
 - utter_Searchorder_Askforwaiting
 - action_Search_order
* thanks
 - utter_ProvideInfo_Askforanotherquestion
* thanks+goodbye+autre
 - utter_SayGoodbye

## story_41
* deliveryNews{"order": "00", "status": "en cours", "delivery": "livraison"}
 - utter_ProvideInfo_Searchorder
 - action_Search_order

## story_42
* deliveryNews{"order": "00"}
 - utter_ProvideInfo_Searchorder_Askforwaiting
 - action_Search_order
* ReceptionAlert{"device": "portable", "pr": "point relais", "phone": " N"}
 - utter_ProvideInfo
* goodbye+thanks
 - utter_SayGoodbye

## story_43
* deliveryNews{"article": "parfum", "email": "_Email1_", "order": "00"}
 - utter_Askforwaiting
* rien
 - utter_ProvideInfo

## story_44
* CancelOrder{"cancel": "annuler", "order": "00"}
 - utter_Searchorder_Askforwaiting
 - action_Search_order
* rien{"email": "_Email1_", "channel": "mail"}
 - utter_ProvideInfo
* CancelOrder{"refund": "un avoir"}
 - utter_Repeatprevious
* Refund{"resend": "renvoi"}
 - utter_SayGoodbye

## story_45
* deliveryCost+Discount{"fdp": "tarif de livraison", "discount": " geste commercial"}
 - utter_ProvideInfo
* goodbye
 - utter_Offeralternative_SayGoodbye

## story_46
* deliveryNews{"order": "00"}
 - utter_Askforwaiting_ProvideInfo_Searchorder
 - action_Search_order
* deliveryTime{"date": "week-end", "present": "cadeau"}
 - utter_ProvideInfo
* oui
 - utter_SayGoodbye

## story_47
* CommuncationInterruption+deliveryNews{"transporter": "Chronopost", "date": "1er octobre"}
 - utter_Searchorder
 - action_Search_order
* rien{"order": "00"}
 - utter_ProvideInfo_Offeralternative
* CustomerComplaint{"channel": "système conversation", "bug": "fonctionnait", "customer": "service client", "mood": "furieuse"}
 - utter_Apologize_ProvideInfo
* deliveryNews{"refund": "remboursement", "present": "cadeau"}
 - utter_Offeralternative_ProvideInfo
* goodbye
 - utter_Apologize

## story_48
* deliveryTime{"article": "parfum", "delivery": "livrer", "date": "fin du mois"}
 - utter_ProvideInfo
* AskDetails+deliveryTime
 - utter_ProvideInfo
* oui+deliveryPlace{"home": "domicile"}
 - utter_SayGoodbye

## story_49
* deliveryCost{"article": "parfums", "place": "USA", "fdp": "frais de douane"}
 - utter_ProvideInfo_Proceedtocheckpoint
* goodbye
 - utter_SayGoodbye

## story_50
* deliveryPlace{"order": "0201 7041 4639 69773", "delivery": "delivered"}
 - utter_AskForMissingSlots
* rien{"transporter": "UPS"}
 - utter_SayGoodbye

## story_51
* ProductPrice{"article": "Guerlain"}
 - utter_ProvideInfo_Apologize
* ProductPrice
 - utter_ProvideInfo_Advisetolookelsewhere

## story_52
* deliveryNews{"order": "00", "date": "22/09", "delivery": "livraison"}
 - utter_Askforwaiting
* rien
 - utter_ProvideInfo

## story_53
* delivery{"email": "_Email1_", "resend": "retourné"}
 - utter_AskForMissingSlots
* delivery
 - utter_SayGoodbye

## story_54
* Discount{"code": "MDM10", "discount": "remise"}
 - utter_ProvideInfo
* Discount+AskDetails
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye
* ProductAvailable{"article": "Doorella"}
 - utter_ProvideInfo_Searchorder
 - action_Search_order
* goodbye+thanks
 - utter_SayGoodbye

## story_55
* deliveryTime{"date": "Noël", "delivery": "livrer"}
 - utter_ProvideInfo
* AskDetails
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_56
* deliveryNews{"order": "00"}
 - utter_Searchorder_ProvideInfo
 - action_Search_order
* deliveryNews+CustomerComplaint{"date": "26 mars"}
 - utter_ProvideInfo_Apologize
* deliveryNews+AskDetails+CustomerComplaint
 - utter_ProvideInfo
* goodbye{"refund": "remboursement"}
 - utter_SayGoodbye

## story_57
* deliveryNews{"email": "_Email1_"}
 - utter_AskForMissingSlots_Searchorder_Askforwaiting
 - action_Search_order
* thanks
 - utter_ProvideInfo
* oui+thanks
 - utter_SayGoodbye

## story_58
* deliveryNews{"order": "00"}
 - utter_ProvideInfo_Searchorder_Askforwaiting
 - action_Search_order
* deliveryNews{"status": "en préparation", "date": "24 mai"}
 - utter_ProvideInfo
* deliveryPlace{"place": "France"}
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_59
* PaymentRefused{"tool": "carte bancaire"}
 - utter_AskForMissingSlots
* rien
 - utter_Apologize_Offeralternative

## story_60
* deliveryNews{"email": "_Email1_", "delivery": "livraison", "date": "09/04/19", "fdp": "frais de livraison"}
 - utter_ProvideInfo
* CustomerComplaint+goodbye
 - utter_ProvideInfo

## story_61
* saluer
 - utter_AskForMissingSlots
* deliveryNews{"delay": "tarde", "transporter": "Chronopost"}
 - utter_Searchorder_ProvideInfo
 - action_Search_order
* ReceptionAlert{"follow-up": "lien"}
 - utter_ProvideInfo
* delivery
 - utter_SayGoodbye

## story_62
* ConfirmationOrder{"payment": "débité", "email": "_Email1_"}
 - utter_ProvideInfo_Askforwaiting
* goodbye+thanks
 - utter_SayGoodbye

## story_63
* deliveryNews{"order": "00", "date": "10 jour", "place": "france"}
 - utter_ProvideInfo_Askforwaiting
* ReceptionAlert
 - utter_SayGoodbye

## story_64
* CommuncationInterruption+deliveryNews{"transporter": "chrono post", "status": "prêt chez l'expéditeur"}
 - utter_ProvideInfo
* deliveryNews+AskDetails{"article": "Chloé", "date": "le 31"}
 - utter_ProvideInfo
* AskDetails+StoreLocation+deliveryTime{"follow-up": "lien", "place": "France"}
 - utter_ProvideInfo
* deliveryTime
 - utter_ProvideInfo
* deliveryTime+AskDetails
 - utter_ProvideInfo
* thanks+oui
 - utter_Askforanotherquestion
* non
 - utter_SayGoodbye

## story_65
* damagedPackage{"email": "_Email1_", "order": "00", "article": "crèmes onctueuses lolitalempica", "damaged": "abîmées"}
 - utter_Apologize_AskForMissingSlots
* CustomerComplaint{"channel": "mails", "date": "15 jours"}
 - utter_ProvideInfo

## story_66
* deliveryNews{"order": "10", "date": "5 jours"}
 - utter_AskForMissingSlots
* rien{"email": "_Email1_"}
 - utter_Searchorder_Askforwaiting_ProvideInfo
 - action_Search_order
* thanks+goodbye
 - utter_SayGoodbye

## story_67
* deliveryNews{"date": "26 août", "order": "00"}
 - utter_ProvideInfo
* goodbye{"delivery": "livraison"}
 - utter_SayGoodbye

## story_68
* saluer+deliveryNews
 - utter_Askforwaiting_Searchorder
 - action_Search_order
* thanks
 - utter_ProvideInfo_AskForMissingSlots
* non{"date": "27/06"}
 - utter_AskForMissingSlots

## story_69
* ConfirmationOrder{"tool": "carte bancaire", "payment": "paiement", "account": "compte"}
 - utter_AskForMissingSlots
* oui
 - utter_Askforwaiting
* oui
 - utter_Askforwaiting_SayGoodbye
* rien
 - action_listen
* rien{"mood": "rassurée"}
 - action_listen

## story_70
* rien{"email": "_Email1_"}
 - utter_AskForMissingSlots
* ReceptionAlert{"delivery": "livraison"}
 - utter_ProvideInfo
* oui
 - utter_Askforanotherquestion
* ChangeData{"pwd": "mot de passe"}
 - utter_ProvideInfo_Suggeststo
* thanks+goodbye
 - utter_SayGoodbye

## story_71
* saluer
 - utter_AskForMissingSlots
* deliveryNews{"email": "_Email1_", "date": "samedi", "follow-up": "suivi"}
 - utter_AskForMissingSlots
* deliveryTime+deliveryPlace{"transporter": "Chronopost", "home": "boîte aux lettre", "order": "00", "mood": "rassurez"}
 - utter_ProvideInfo_Askforwaiting

## story_72
* ProductAvailable{"article": "Courrèges in blue"}
 - utter_Askforwaiting_ProvideInfo_Apologize

## story_73
* missingItem{"missing": "totalité"}
 - utter_ProvideInfo
* deliveryNews
 - utter_ProvideInfo_Apologize_Offeralternative
* non{"date": "12 14 jours"}
 - utter_Proceedtocheckpoint
* oui+CustomerComplaint
 - utter_ProvideInfo_Performaction
 - action_Perform_action
* goodbye
 - utter_SayGoodbye

## story_74
* missingItem{"order": "00", "missing": "reste"}
 - utter_Searchorder_Askforwaiting
 - action_Search_order
* thanks
 - utter_Askforanotherquestion
* non
 - utter_SayGoodbye

## story_75
* saluer
 - utter_AskForMissingSlots
* damagedPackage{"article": "Angel", "color": "bleu gris", "email": "_Email1_"}
 - utter_ProvideInfo_Searchorder
 - action_Search_order
* autre+goodbye
 - utter_SayGoodbye_Apologize

## story_76
* ReceptionAlert{"delivery": "livraison", "pr": "point relais"}
 - utter_ProvideInfo
* goodbye
 - utter_SayGoodbye

## story_77
* Discount{"code": "NOEL5"}
 - utter_AskForMissingSlots
* rien{"article": "prada"}
 - utter_ProvideInfo
* Discount+non{"discount": "réduction"}
 - utter_SayGoodbye

## story_78
* deliveryTime{"date": "Noel"}
 - utter_ProvideInfo
* goodbye
 - utter_SayGoodbye

## story_79
* deliveryNews{"follow-up": "numéro de suivi", "mood": "inquiète"}
 - utter_ProvideInfo
* deliveryNews{"store": "chez vous", "status": "en préparation"}
 - utter_ProvideInfo_Askforanotherquestion

## story_80
* deliveryNews{"delivery": "livraison", "date": "14 octobre", "order": "00"}
 - utter_Askforwaiting_ProvideInfo_Searchorder
 - action_Search_order
* ReceptionAlert{"channel": "mail"}
 - utter_ProvideInfo
* goodbye+thanks
 - utter_SayGoodbye

## story_81
* deliveryNews{"order": "00"}
 - utter_ProvideInfo
* rien
 - utter_Askforanotherquestion
* goodbye
 - utter_SayGoodbye

## story_82
* deliveryNews{"delivery": "livraison", "order": "03"}
 - utter_ProvideInfo
* deliveryNews{"home": "domicile"}
 - utter_ProvideInfo
* deliveryNews
 - utter_ProvideInfo_Offeralternative
* deliveryNews+deliveryPlace{"address": "202 rue du château des rentiers"}
 - utter_ProvideInfo_Offeralternative
* deliveryPlace{"pr": "point relais"}
 - utter_Askforwaiting_Performaction
 - action_Perform_action
* thanks
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_83
* deliveryNews{"order": "02", "date": "27 mars"}
 - utter_ProvideInfo
* deliveryNews{"transporter": "transporteur"}
 - utter_ProvideInfo
* thanks+goodbye
 - utter_SayGoodbye

## story_84
* deliveryNews{"order": "00", "date": "1 juin 2019", "email": "_Email1_"}
 - utter_Searchorder_ProvideInfo_AskForMissingSlots
 - action_Search_order
* deliveryNews{"resend": "renvoyez"}
 - utter_Performaction_Suggeststo
 - action_Perform_action
* thanks+oui
 - utter_Askforanotherquestion
* non+goodbye
 - utter_SayGoodbye

## story_85
* deliveryNews{"order": "00"}
 - utter_Askforwaiting_ProvideInfo_Askforanotherquestion
* goodbye
 - utter_SayGoodbye

## story_86
* deliveryTime{"delivery": "livraison"}
 - utter_ProvideInfo
* goodbye
 - utter_SayGoodbye

## story_87
* deliveryCost{"fdp": "frais de port", "article": "parfum"}
 - utter_ProvideInfo
* Discount{"discount": "geste commercial"}
 - utter_ProvideInfo
* Discount+goodbye
 - utter_SayGoodbye

## story_88
* PaymentRefused{"payment": "payment"}
 - utter_AskForMissingSlots
* non
 - utter_AskForMissingSlots
* non
 - utter_ProvideInfo
* WebsiteBug
 - utter_ProvideInfo_AskForMissingSlots
* WebsiteBug{"website": "caches"}
 - utter_ProvideInfo
* WebsiteBug{"billing": "total"}
 - utter_SayGoodbye

## story_89
* deliveryCost+Discount{"fdp": "frais de port", "discount": "code d'ebienvenue"}
 - utter_ProvideInfo

## story_90
* PaymentRefused{"payment": "paiement", "website": "site", "tool": "carte mastercard"}
 - utter_Offeralternative
* PaymentTool{"place": "France"}
 - utter_AskForMissingSlots
* rien
 - utter_Offeralternative_ProvideInfo_Apologize
* thanks+goodbye+oui
 - utter_SayGoodbye

## story_91
* PaymentRefused{"payment": "payer"}
 - utter_AskForMissingSlots
* non
 - utter_AskForMissingSlots
* PaymentTool+PaymentRefused{"tool": "carte"}
 - utter_ProvideInfo
* non
 - utter_ProvideInfo_Repeatprevious

## story_92
* Login{"customer": "conseiller", "connection": "connecter"}
 - utter_Lookforcustomerfile_Askforwaiting_AskForMissingSlots
 - action_Look_for_customer_file
* rien{"address": "75 avenue du docteur _Name4_ résidence _City3_ _ZipCode1_ _City2_", "pwd": "mot de passe"}
 - utter_ProvideInfo
* CustomerComplaint{"phone": "Num tel"}
 - utter_ProvideInfo_Suggeststo
* CustomerComplaint
 - utter_AskForMissingSlots
* rien
 - utter_Proceedtocheckpoint
* non
 - utter_ProvideInfo
* CustomerComplaint+AccountCreation{"account": "compte", "website": "site"}
 - utter_Suggeststo
* AccountIssue+CustomerComplaint
 - utter_Searchorder_Negaterequest
 - action_Search_order
* AccountCreation
 - utter_ProvideInfo
* thanks+CustomerComplaint
 - utter_ProvideInfo_Performaction
 - action_Perform_action
* thanks+oui
 - utter_ProvideInfo
* thanks
 - utter_SayGoodbye

## story_93
* deliveryNews{"delivery": "livraison", "order": "00"}
 - utter_Askforwaiting_Searchorder
 - action_Search_order
* goodbye+ReceptionAlert{"channel": "message"}
 - utter_SayGoodbye

## story_94
* deliveryCountry{"article": "parfum", "place": "France"}
 - utter_ProvideInfo

## story_95
* deliveryNews
 - utter_AskForMissingSlots
* rien{"order": "00"}
 - utter_Askforwaiting_Searchorder_ProvideInfo_Performaction
 - action_Search_order
 - action_Perform_action
* CustomerComplaint+deliveryNews{"article": "parfums", "refund": "remboursement", "transporter": "Chronopost", "customer": "avocat", "store": "boutique"}
 - utter_ProvideInfo
* customer_service+goodbye{"date": "vendredi"}
 - utter_SayGoodbye

## story_96
* deliveryNews{"date": "16/11/2018"}
 - utter_Searchorder_Askforwaiting_ProvideInfo_AskForMissingSlots
 - action_Search_order
* deliveryNews{"resend": "renvoyez"}
 - utter_ProvideInfo_Performaction
 - action_Perform_action
* Refund{"discount": "déduire"}
 - utter_ProvideInfo_Suggeststo_Apologize
* thanks
 - utter_SayGoodbye

## story_97
* AccountCreation{"connection": "inscrire", "channel": "mail"}
 - utter_AskForMissingSlots
* AccountCreation{"email": "_Email1_"}
 - utter_ProvideInfo_Lookforcustomerfile
 - action_Look_for_customer_file
* Login{"pwd": "mot de passe"}
 - utter_AskForMissingSlots
* thanks
 - utter_ProvideInfo
* ChangeData{"place": "_City1_"}
 - utter_ProvideInfo
* thanks
 - utter_Askforanotherquestion

