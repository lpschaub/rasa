intents report : 

Statistiques sur l'évaluation des données

pour chaque intent :
	 combien de phrases d'exemple. (support)
	 combien de phrases ont été correctement prédites (precision-recall)
	 avec quelles intentions les exemples ont été confondus. 

puis Moyenne des précisions (micro/macro avg)


Exemple : 

{
  "Refund": { -> nom de l'intention 
    "precision": 0.5, -> pour chaque exemple étiqueté "Refund", combien sont vraiment des "Refund"
    "recall": 1.0, -> pour chaque exemple vraiment "Refund", combien le système a-t-il trouvé ? 
    "f1-score": 0.6666666666666666, -> moyenne de précision et recall 
    "support": 1, -> nombre d'exemples dans le corpus
    "confused_with": {} -> avec quoi l'exemple a été confondu ? 
  },


  Intents error : 

  Montre ici pour chaque phrase mal prédite, l'intent attendu, l'intent prédit, et le taux de confiance du chatbot 

  Exemple : 
  {
    "text": "bonjour je souhaiterai savoir le prix de la livraison.", -> phrase elle-même
    "intent": "DeliveryCost", -> intent ATTENDU
    "intent_prediction": { 
      "name": "DeliveryTime", -> intent PREDIT
      "confidence": 0.7129412293434143 -> taux de confiance
    }
  },


 Hist.png 

 Montre à partir de quel taux de confiance (Confidence) le système est fiable (hits)

 On voit sur le graphique qu'il faut un score de 0.95 de confiance pour être "sûr" qu'il soit bon. 

 