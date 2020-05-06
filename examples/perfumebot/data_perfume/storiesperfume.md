## story_1
* deliveryCost{"Store name": "Parfum moins cher", "delivery": " free"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_2
* PaymentRefused{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* PaymentTool{"paypal": " no paypal"}
 - utter_Provide Info
* thanks
 - utter_Proceed to checkpoint
* non
 - utter_Ask For Missing Slots
* PaymentRefused{"payment_tool": "cb", "step": "delivery"}
 - utter_Proceed to checkpoint
* oui
 - utter_Provide Info
* non
 - utter_Repeat previous
* oui
 - utter_Say Goodbye

## story_3
* ProductAvailable{"Store name": "Parfum moins cher", "article": "womanity EAU de parfum spray", "reload": "yes"}
 - utter_Provide Info_Search order
 - action_Search order
* goodbye+thanks
 - utter_Say Goodbye

## story_4
* damagedPackage{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* damagedPackage{"operation": "resend", "address": "17 avenue _Name3_ _ZipCode1_ _City1_"}
 - utter_Proceed to checkpoint
* autre
 - utter_Provide Info_Perform action
 - action_Perform action
* thanks+goodbye
 - utter_Provide Info_Say Goodbye

## story_5
* deliveryCost{"Store name": "Parfum moins cher", "place": "home"}
 - utter_Ask For Missing Slots
* goodbye
 - utter_Provide Info

## story_6
* deliveryCost{"Store name": "Parfum moins cher", "delivery": " free"}
 - utter_Provide Info
* Discount
 - utter_Provide Info_Say Goodbye

## story_7
* autre{"Store name": "Parfum moins cher"}
 - utter_Provide Info_Ask For Missing Slots
* deliveryCost
 - utter_Provide Info_Apologize
* thanks+oui
 - utter_Ask for another question
* non+thanks
 - utter_Say Goodbye

## story_8
* WebsiteBug{"Store name": "Parfum moins cher", "operation": "payment"}
 - utter_Ask For Missing Slots
* CommuncationInterruption
 - utter_Provide Info_Offer alternative
* WebsiteBug+goodbye
 - utter_Say Goodbye

## story_9
* rien+goodbye{"Store name": "Parfum moins cher"}
 - utter_Say Goodbye
* goodbye
 - utter_Say Goodbye

## story_10
* Login{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* autre
 - utter_Ask For Missing Slots_Repeat previous
* autre{"email": "_Email1_"}
 - utter_Provide Info
* thanks+Login
 - utter_Ask for another question
* goodbye
 - utter_Say Goodbye

## story_11
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "61"}
 - utter_Search order_Ask for waiting_Provide Info
 - action_Search order
* deliveryNews+AskDetails{"status": "in deposit"}
 - utter_Provide Info
* AskDetails
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_12
* PaymentRefused{"Store name": "Parfum moins cher", "device": "computer"}
 - utter_Ask For Missing Slots
* PaymentRefused{"error": "yes", "payment_tool": "cb"}
 - utter_Provide Info_Offer alternative
* autre+CancelOrder
 - utter_Say Goodbye
* autre
 - utter_Say Goodbye

## story_13
* Login{"Store name": "Parfum moins cher", "error": "yes"}
 - utter_Ask For Missing Slots
* AskConfirmation{"email": "_Email1_"}
 - utter_Provide Info
* WebsiteBug+goodbye{"account_connection": "issue", "operation": "registration"}
 - utter_Say Goodbye

## story_14
* missingItem{"Store name": "Parfum moins cher"}
 - utter_Ask for waiting
* rien{"order_nbr": "00"}
 - utter_Provide Info

## story_15
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00", "place": "point-relais"}
 - utter_Provide Info_Ask for waiting
* ReceptionAlert
 - utter_Provide Info

## story_16
* ProductPrice{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* ProductPrice{"complaint": "bad add", "article": "Lolita Lempicka", "price": "36.99", "size": "100ml", "add": "yes"}
 - utter_Provide Info
* CustomerComplaint
 - utter_Provide Info
* autre
 - utter_Ask For Missing Slots
* purchase
 - utter_Ask For Missing Slots

## story_17
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "_Email1_"}
 - utter_Search order_Ask for waiting
 - action_Search order
* oui
 - utter_Provide Info
* deliveryNews{"status": "in process"}
 - utter_Provide Info
* goodbye+thanks
 - utter_Say Goodbye

## story_18
* deliveryTime+ProductAvailable{"Store name": "Parfum moins cher", "article": "present"}
 - utter_Provide Info_Apologize
* product+AskDetails
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_19
* customer_service{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_20
* deliveryCost{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* deliveryCost
 - utter_Provide Info
* deliveryCost{"delivery": " details"}
 - utter_Provide Info_Perform action
 - action_Perform action
* CustomerComplaint+goodbye
 - utter_Provide Info

## story_21
* AccountIssue{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* AccountIssue{"pwd": "forgotten", "relog": "yes"}
 - utter_Ask For Missing Slots
* {"email": "_Email1_"}
 - utter_Perform action_Provide Info_Suggests to
 - action_Perform action
* oui+thanks
 - utter_Ask for another question

## story_22
* ProductTarget{"Store name": "Parfum moins cher", "article": "fond de teint make up for ever fluide tenseur"}
 - utter_Ask For Missing Slots
* ProductTarget
 - utter_Ask for waiting
* thanks
 - utter_Provide Info_Ask For Missing Slots
* ProductTarget{"profile": "mate"}
 - utter_Provide Info
* goodbye+thanks
 - utter_Say Goodbye

## story_23
* Login{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* Login{"email": "_Email1_", "reinit": "pwd"}
action_listen
* Login
 - utter_Repeat previous
* rien
 - utter_Proceed to checkpoint
* rien
 - utter_Provide Info

## story_24
* autre{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* Discount{"code": "name1", "email": "_Email1_"}
 - utter_Provide Info
* Discount+CustomerComplaint
 - utter_Provide Info
* Discount
 - utter_Ask For Missing Slots
* autre{"uppercase": "yes"}
 - utter_Ask For Missing Slots
* autre{"account_connection": "yes", "operation": "discount"}
 - utter_Provide Info
* purchase
 - utter_Provide Info_Search order
 - action_Search order
* WebsiteBug
 - utter_Provide Info_Offer alternative
* WebsiteBug
 - utter_Repeat previous
* WebsiteBug
 - utter_Provide Info_Ask For Missing Slots
* WebsiteBug{"cache": "yes"}
 - utter_Ask For Missing Slots
* autre
 - utter_Ask For Missing Slots
* autre
 - utter_Apologize_Say Goodbye

## story_25
* CancelOrder{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Search order_Provide Info_Perform action_Ask for waiting
 - action_Search order
 - action_Perform action
* thanks+goodbye
 - utter_Say Goodbye

## story_26
* ProductQuality{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* payment
 - utter_Provide Info
* goodbye+thanks
 - utter_Say Goodbye

## story_27
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask for waiting_Search order
 - action_Search order
* thanks
 - utter_Provide Info
* deliveryNews{"status": "unchanged"}
 - utter_Provide Info
* thanks+goodbye+oui
 - utter_Say Goodbye

## story_28
* PaymentRefused{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* PaymentRefused+Login{"error": "yes", "step": "authentification"}
 - utter_Ask For Missing Slots
* rien{"email": "_Email1_", "reinit": "yes"}
 - utter_Suggests to_Provide Info
* deliveryTime
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_29
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Search order_Provide Info_Ask for waiting
 - action_Search order
* autre
 - utter_Provide Info
* deliveryTime{"date": "09/07"}
 - utter_Provide Info
* oui
 - utter_Ask for another question
* non+thanks
 - utter_Say Goodbye

## story_30
* PaymentRefused{"Store name": "Parfum moins cher", "payment_tool": "cb", "error": "yes"}
 - utter_Offer alternative
* PaymentTool{"paypal": " no paypal"}
 - utter_Provide Info
* CancelOrder
 - utter_Say Goodbye

## story_31
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Provide Info_Ask for waiting
* goodbye
 - utter_Say Goodbye

## story_32
* autre{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots_Apologize
* CustomerComplaint
 - utter_Say Goodbye

## story_33
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Provide Info_Ask for waiting
* goodbye
 - utter_Say Goodbye

## story_34
* missingItem{"Store name": "Parfum moins cher"}
 - utter_Provide Info_Search order
 - action_Search order
* ConfirmationOrder{"email": "not recieved"}
 - utter_Provide Info
* CustomerComplaint{"complaint": "splitted delivery"}
 - utter_Ask for waiting_Search order_Provide Info
 - action_Search order
* ConfirmationOrder
 - utter_Provide Info_Offer alternative
* oui+ConfirmationOrder
 - utter_Provide Info
* oui+goodbye
 - utter_Say Goodbye

## story_35
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask for waiting
* goodbye
 - utter_Say Goodbye

## story_36
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00", "status": "in deposit"}
 - utter_Search order_Ask for waiting
 - action_Search order
* thanks
 - utter_Provide Info
* AskDetails
 - utter_Provide Info
* oui+thanks
 - utter_Say Goodbye

## story_37
* Discount{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* rien{"email": "_Email2_"}
 - utter_Ask for waiting
* thanks{"code": "PANTALEO5"}
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_38
* Discount{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_39
* damagedPackage{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* rien{"order_nbr": "00"}
 - utter_Say Goodbye

## story_40
* missingItem{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask For Missing Slots
* missingItem{"article": "Kenzo"}
 - utter_Search order_Ask for waiting
 - action_Search order
* thanks
 - utter_Provide Info_Ask for another question
* thanks+goodbye+autre
 - utter_Say Goodbye

## story_41
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Provide Info_Search order
 - action_Search order

## story_42
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Provide Info_Search order_Ask for waiting
 - action_Search order
* ReceptionAlert
 - utter_Provide Info
* goodbye+thanks
 - utter_Say Goodbye

## story_43
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask for waiting
* rien
 - utter_Provide Info

## story_44
* CancelOrder{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Search order_Ask for waiting
 - action_Search order
* rien
 - utter_Provide Info
* CancelOrder
 - utter_Repeat previous
* Refund
 - utter_Say Goodbye

## story_45
* deliveryCost+Discount{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* goodbye
 - utter_Offer alternative_Say Goodbye

## story_46
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Ask for waiting_Provide Info_Search order
 - action_Search order
* deliveryTime
 - utter_Provide Info
* oui
 - utter_Say Goodbye

## story_47
* CommuncationInterruption+deliveryNews{"Store name": "Parfum moins cher", "topic": "news", "info": "order 00"}
 - utter_Search order
 - action_Search order
* rien
 - utter_Provide Info_Offer alternative
* CustomerComplaint{"complaint": "no answer"}
 - utter_Apologize_Provide Info
* deliveryNews{"operation": "resend"}
 - utter_Offer alternative_Provide Info
* goodbye
 - utter_Apologize

## story_48
* deliveryTime{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* AskDetails+deliveryTime
 - utter_Provide Info
* oui+deliveryPlace{"place": "home"}
 - utter_Say Goodbye

## story_49
* deliveryCost{"Store name": "Parfum moins cher", "delivery": " douane"}
 - utter_Provide Info_Proceed to checkpoint
* goodbye
 - utter_Say Goodbye

## story_50
* deliveryPlace{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* rien
 - utter_Say Goodbye

## story_51
* ProductPrice{"Store name": "Parfum moins cher", "article": "Guerlain+Chanel"}
 - utter_Provide Info_Apologize
* ProductPrice
 - utter_Provide Info_Advise to look elsewhere

## story_52
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask for waiting
* rien
 - utter_Provide Info

## story_53
* delivery{"Store name": "Parfum moins cher", "separated": "returned"}
 - utter_Ask For Missing Slots
* delivery{"order_nbr": "?"}
 - utter_Say Goodbye

## story_54
* Discount{"Store name": "Parfum moins cher", "code": "MDM10"}
 - utter_Provide Info
* Discount+AskDetails
 - utter_Provide Info
* thanks
 - utter_Say Goodbye
* ProductAvailable{"article": "Doorella Diorissimo"}
 - utter_Provide Info_Search order
 - action_Search order
* goodbye+thanks
 - utter_Say Goodbye

## story_55
* deliveryTime{"Store name": "Parfum moins cher", "date": "24/12"}
 - utter_Provide Info
* AskDetails
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_56
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Search order_Provide Info
 - action_Search order
* deliveryNews+CustomerComplaint
 - utter_Provide Info_Apologize
* deliveryNews+AskDetails+CustomerComplaint
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_57
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots_Search order_Ask for waiting
 - action_Search order
* thanks
 - utter_Provide Info
* oui+thanks
 - utter_Say Goodbye

## story_58
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Provide Info_Search order_Ask for waiting
 - action_Search order
* deliveryNews
 - utter_Provide Info
* deliveryPlace{"place": "France"}
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_59
* PaymentRefused{"Store name": "Parfum moins cher", "payment_tool": "cb"}
 - utter_Ask For Missing Slots
* rien
 - utter_Apologize_Offer alternative

## story_60
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Provide Info
* CustomerComplaint+goodbye
 - utter_Provide Info

## story_61
* saluer{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* deliveryNews
 - utter_Search order_Provide Info
 - action_Search order
* ReceptionAlert
 - utter_Provide Info
* delivery
 - utter_Say Goodbye

## story_62
* ConfirmationOrder{"Store name": "Parfum moins cher", "email": "_Email1_"}
 - utter_Provide Info_Ask for waiting
* goodbye+thanks
 - utter_Say Goodbye

## story_63
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Provide Info_Ask for waiting
* ReceptionAlert
 - utter_Say Goodbye

## story_64
* CommuncationInterruption+deliveryNews{"Store name": "Parfum moins cher", "operation": "resend", "status": "ready"}
 - utter_Provide Info
* deliveryNews+AskDetails
 - utter_Provide Info
* AskDetails+StoreLocation+deliveryTime{"store": "location"}
 - utter_Provide Info
* deliveryTime
 - utter_Provide Info
* deliveryTime+AskDetails
 - utter_Provide Info
* thanks+oui
 - utter_Ask for another question
* non
 - utter_Say Goodbye

## story_65
* damagedPackage{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Apologize_Ask For Missing Slots
* CustomerComplaint
 - utter_Provide Info

## story_66
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask For Missing Slots
* {"email": "_Email1_"}
 - utter_Search order_Ask for waiting_Provide Info
 - action_Search order
* thanks+goodbye
 - utter_Say Goodbye

## story_67
* deliveryNews{"Store name": "Parfum moins cher", "country": "USA", "order_nbr": "00"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_68
* saluer+deliveryNews{"Store name": "Parfum moins cher", "email": "_Email1_"}
 - utter_Ask for waiting_Search order
 - action_Search order
* thanks
 - utter_Provide Info_Ask For Missing Slots
* non
 - utter_Ask For Missing Slots

## story_69
* ConfirmationOrder{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* oui
 - utter_Ask for waiting
* oui
 - utter_Ask for waiting_Say Goodbye
* 
action_listen
* 
action_listen

## story_70
* rien{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* ReceptionAlert
 - utter_Provide Info
* oui
 - utter_Ask for another question
* ChangeData{"data": "pwd"}
 - utter_Provide Info_Suggests to
* thanks+goodbye
 - utter_Say Goodbye

## story_71
* saluer{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* deliveryNews
 - utter_Ask For Missing Slots
* deliveryTime+deliveryPlace{"place": "home", "date": "6/?", "order_nbr": "00"}
 - utter_Provide Info_Ask for waiting

## story_72
* ProductAvailable{"Store name": "Parfum moins cher", "article": "Courr\u00e8ges in blue"}
 - utter_Ask for waiting_Provide Info_Apologize

## story_73
* missingItem{"Store name": "Parfum moins cher", "article": "Valentino Donna"}
 - utter_Provide Info
* deliveryNews
 - utter_Provide Info_Apologize_Offer alternative
* non
 - utter_Proceed to checkpoint
* oui+CustomerComplaint{"operation": "refund"}
 - utter_Provide Info_Perform action
 - action_Perform action
* goodbye
 - utter_Say Goodbye

## story_74
* missingItem{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Search order_Ask for waiting
 - action_Search order
* thanks
 - utter_Ask for another question
* non
 - utter_Say Goodbye

## story_75
* saluer{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* damagedPackage
 - utter_Provide Info_Search order
 - action_Search order
* autre+goodbye
 - utter_Say Goodbye_Apologize

## story_76
* ReceptionAlert{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_77
* Discount{"Store name": "Parfum moins cher", "code": "NOEL5", "uppercase": "yes"}
 - utter_Ask For Missing Slots
* rien
 - utter_Provide Info
* Discount+non
 - utter_Say Goodbye

## story_78
* deliveryTime{"Store name": "Parfum moins cher", "date": "24/12"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_79
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* deliveryNews
 - utter_Provide Info_Ask for another question

## story_80
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Ask for waiting_Provide Info_Search order
 - action_Search order
* ReceptionAlert{"order_nbr": "00"}
 - utter_Provide Info
* goodbye+thanks
 - utter_Say Goodbye

## story_81
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Provide Info
* rien
 - utter_Ask for another question
* goodbye
 - utter_Say Goodbye

## story_82
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "03"}
 - utter_Provide Info
* deliveryNews{"operation": "returned", "place": "home"}
 - utter_Provide Info
* deliveryNews
 - utter_Provide Info_Offer alternative
* deliveryNews+deliveryPlace
 - utter_Provide Info_Offer alternative
* deliveryPlace
 - utter_Ask for waiting_Perform action
 - action_Perform action
* thanks
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_83
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "02+00"}
 - utter_Provide Info
* deliveryNews{"status": "in process"}
 - utter_Provide Info
* thanks+goodbye
 - utter_Say Goodbye

## story_84
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00", "email": "_Email1_", "status": "lost"}
 - utter_Search order_Provide Info_Ask For Missing Slots
 - action_Search order
* deliveryNews{"operation": "resend"}
 - utter_Perform action_Suggests to
 - action_Perform action
* thanks+oui
 - utter_Ask for another question
* non+goodbye
 - utter_Say Goodbye

## story_85
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask for waiting_Provide Info_Ask for another question
* goodbye
 - utter_Say Goodbye

## story_86
* deliveryTime{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* goodbye
 - utter_Say Goodbye

## story_87
* deliveryCost{"Store name": "Parfum moins cher"}
 - utter_Provide Info
* Discount
 - utter_Provide Info
* Discount+goodbye
 - utter_Say Goodbye

## story_88
* PaymentRefused{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* non{"error": "no"}
 - utter_Ask For Missing Slots
* non{"step": "delivery"}
 - utter_Provide Info
* WebsiteBug{"operation": "payment"}
 - utter_Provide Info_Ask For Missing Slots
* WebsiteBug{"cache": "unable"}
 - utter_Provide Info
* WebsiteBug
 - utter_Say Goodbye

## story_89
* deliveryCost+Discount{"Store name": "Parfum moins cher"}
 - utter_Provide Info

## story_90
* PaymentRefused{"Store name": "Parfum moins cher", "error": "yes", "step": "payment", "payment_tool": "cb"}
 - utter_Offer alternative
* PaymentTool{"paypal": " no paypal"}
 - utter_Ask For Missing Slots
* 
 - utter_Offer alternative_Provide Info_Apologize
* thanks+goodbye+oui
 - utter_Say Goodbye

## story_91
* PaymentRefused{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* non{"error": "no"}
 - utter_Ask For Missing Slots
* PaymentTool+PaymentRefused{"payment_tool": "cb", "step": "payment"}
 - utter_Provide Info
* non
 - utter_Provide Info_Repeat previous

## story_92
* Login{"Store name": "Parfum moins cher"}
 - utter_Look for customer file_Ask for waiting_Ask For Missing Slots
 - action_Look for customer file
* rien{"email": "_Email2_", "address": "75 avenue du docteur _Name4_ r\u00e9sidence _City3_ _ZipCode1_ _City2_"}
 - utter_Provide Info
* CustomerComplaint{"complaint": "long phone"}
 - utter_Provide Info_Suggests to
* CustomerComplaint
 - utter_Ask For Missing Slots
* rien
 - utter_Proceed to checkpoint
* non
 - utter_Provide Info
* CustomerComplaint+AccountCreation
 - utter_Suggests to
* AccountIssue+CustomerComplaint
 - utter_Search order_Negate request
 - action_Search order
* AccountCreation
 - utter_Provide Info
* thanks+CustomerComplaint{"pwd": "azerty"}
 - utter_Provide Info_Perform action
 - action_Perform action
* thanks+oui
 - utter_Provide Info
* thanks
 - utter_Say Goodbye

## story_93
* deliveryNews{"Store name": "Parfum moins cher", "order_nbr": "00"}
 - utter_Ask for waiting_Search order
 - action_Search order
* goodbye+ReceptionAlert
 - utter_Say Goodbye

## story_94
* deliveryCountry{"Store name": "Parfum moins cher", "country": "USA"}
 - utter_Provide Info

## story_95
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* rien{"order_nbr": "00"}
 - utter_Ask for waiting_Search order_Provide Info_Perform action
 - action_Search order
 - action_Perform action
* CustomerComplaint+deliveryNews{"complaint": "no package"}
 - utter_Provide Info
* customer_service+goodbye
 - utter_Say Goodbye

## story_96
* deliveryNews{"Store name": "Parfum moins cher"}
 - utter_Search order_Ask for waiting_Provide Info_Ask For Missing Slots
 - action_Search order
* deliveryNews{"status": "lost", "operation": "resend"}
 - utter_Provide Info_Perform action
 - action_Perform action
* Refund
 - utter_Provide Info_Suggests to_Apologize
* thanks
 - utter_Say Goodbye

## story_97
* AccountCreation{"Store name": "Parfum moins cher"}
 - utter_Ask For Missing Slots
* AccountCreation{"email": "_Email1_"}
 - utter_Provide Info_Look for customer file
 - action_Look for customer file
* Login
 - utter_Ask For Missing Slots
* thanks
 - utter_Provide Info
* ChangeData{"data": "address"}
 - utter_Provide Info
* thanks
 - utter_Ask for another question

