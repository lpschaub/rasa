## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- Merci beaucoup, bonne journée.
- ha oui je vais prodécer à une [commande](order), merci et bonne journée
- je vous remercie pour vos explications. je vais concrétiser la commande bonne journée
- Merci je n'avais pas de suivi. bonne journée. cordialement

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- non merci

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:ProductAvailable
- bonjour je cherche [parure de Gerlain](article) pouvez vous me le trouver c'est un ancien parfum
- vous allez, es chercher à travers le monde etc suite à quoi, liquidations ou autres. avez vous la [petite robe black](article)
- quels sont vos parfums [Ted Lapidus](article) ?

## intent:ChangeData
- pouvez vous changer l'adresse de facturation pour ma commande n° [625652](order). mettre la même adresse que celle de la livraison, car la facture doit être jointe à l'envoi. Merci de me confirmer

## intent:oui
- [oui](oui). Merci

## intent:ProductQuality
- bonjour, les produits sont bien des  [originaux](order)?
- bonjour, les produits sont bien des [originaux](origin) ?
- bonjour bonjour les pargums sont ils des [originaux](origin) svp
- bonjour _Name1_, vos parfums sont ils les[vrais](origin)? ou copies ? sans vouloir vous vexer mais les prix sont juste époustouflants !
- bonjour, je suis très intéressé par les prix que vous affichez mais qui me prouve l'[origine](origin) des produits ?
- bonjour _Name1_, vos parfums sont ils les [vrais ](origin)? ou copies ? sans vouloir vous vexer mais les prix sont juste époustouflants !

## intent:Previous
- la réponse à ma question précédente ? ! !
- répondez vous vraiment aux [e-mails](channel) ?

## intent:ProductOrigin
- non, cette question : vous allez chercher vos produits à travers le monde etc unité à des liquidations faillites et autres ?
- oui, mis à qui les achetez vous ?
- donc votre site n'est pas en [France](place) ?

## intent:Discount
- bonjour, étant bon client, je souhaiterais avoir un [code promo](discount) avant de passer commande c'est possible ? Merci.
- je souhaite bénéficier un [code promo](discount)

## intent:ProductTarget
- que me conseillez vous en parfum [femme](target) pour ma [mère](target) ( 75 ans ) merci.

## intent:thanks
- OK Merci.
- merci beaucoup
- ok merci
- d'accord merci car je pensais qu'il avait pu être volé dans ma boite aux lettres
- ok je vais essayer c'est BON j'avais écrit le [mot de passe](pwd) EN minuscule Merci beaucoup
- OK je vous remercie
- Merci

## intent:Send
- Merci de bien vouloir m'envoyer les[ codes de réductions](discount) par [mail](channel).

## intent:DeliveryTime
- bonjour j'attends ma commande du [16 juin](date)[6 jui](article)n toujours en attente chez l'expéditeur. le délai est très long. [commande 608380](order)
- bonjour Madame ma [commande 605565](date) sur chronoposte est toujours en préparation depuis le [24/05](date) etc et je parts à l'étranger le [31/05](order) Mercie de me renseigner
- bonjour, la livraison sera pour avant Noel ? cordialement.
- bonjour email _Email1_ je n'ai toujours pas reçu ma [commande](order) du [20](order) mars est ce normal ?
- bonjour, numéro de [commande 604337](order) j'aimerais savoir ou est le colis aucun détail depuis le [31 mai](date)
- bonjour j'aimerais savoir où en est l'expédition de ma [commande](order).
- bonjour il y a t il un recours en cas de non [livraison](delivery), un [e-mail](channel) ou un [téléphone](channel) où vous appelé si nous avons un problème
- je me suis fait avoir en commandant ailleurs, pouvez vous me confirmer le délai d'[acheminement](order) pour une commande que je serai susceptible de vous faire et quel recours j'ai en xcas de non [livraison](delivery)
- [716640](order) bonjour cette [commande](order) est en cours de [livraison](delivery) depuis le [15 mai](date) dernier. pourrais je avoir de plus amples informations
- bonsoir, pouvez me dire si ma commande a été expédiée [649843](order)

## intent:Change+CancelOrder
- _Name3_ je modifier ma [commande](order) puisque non partie ?

## intent:AskDetails
- ok, mais vous ne mettez rien a jour ? si le colis a été expédié le [31](date) ou est il ?

## intent:DeliveryCost
- , est il possible de réduire le [coût de livraison](fdp) ?

## intent:AccountIssue
- _Email1_ suis en train désespérément de vous passer une [commande](order). quant le panier est OK et que je passe à l'étape suivante etc etc on me dit vos adresses Fact et exp sont ci-dessous etc etc et rien n'apparaît ? et si je veux ajouter une adresse etc etc ça me répond " " 1 _Name1_ " ". je ne peux donc passer à l'étape paiement et suis [bloquée](bug)
- bonjour je n'arrive pas à [valider](action) ma commande malgré le nouveau [mot de passe](pwd) mon adresse [mail](channel) est [_Email1_](email)

## intent:Login
- EN fait, je reprends toujours le [mot de passe](pwd) que vous me donnez etc etc comment modifier ce [mot de passe](fdp) ?
- et je suis sur mon compte etc etc etc l'adresse qui est indiquée dans les commands précédentes est celle de _City1_ dans le Nord etc etc mais nous sommes dans le Var maintenant. je le vois parce que je suis sur LA rubrique : MES commandes, mais si je vais sur la rubrique " " MES adresses " " je n'ai rien du tout et ne peux rien changer on me le refuse et donc, si je vais sur " " mes informations " " je retrouve le nom, le prénom, l'adresse mail, la date de naissance et oui effectivement on me demande un nouveau [mot de passe](pwd) mais lequel ? je vais devenir chèvre avec cette commande ?
- celui donne par vos collègues _Name2_
- pour les prochaines commandes dois je toujours me servir du même [mot de passe](pwd) ?

## intent:rien
- [699072](order)
- [femme](target)

## intent:Customer_service
- peux tu vous écrire par [mail](channel) ou vous [téléphoner](channel) ? ce serait plus simple en cas de problème Ok mais ce que je désire c'est de pouvoir avoir un interlocuteur en cas de problème sous quelque forme que ce soit

## intent:DeliveryPlace
- en [point relais](pr) peut on choisir en comment faire

## intent:ConfirmationOrder
- [commande](order) N° [653320](order) bonjour etc es ce normal suite à une [commande](order) passée hier soir que je n'ai pas reçu un [mail ](channel)de confirmation de commande alors que j'ai pu avoir la facture accessible sur le compte créé ?
