LISEZ-MOI : 

fichiers : 

* nlu.md 
  - contient l'ensemble des intentions (annotées par ## intention:xxx) du corpus jusqu'à maintenant. 
  - sur chaque exemple d'intention, on trouve les entités de la forme [valeur](type)
* train/test/eval.md
  - chacun des trois fichiers contient des stories (scénarios de conversation)
  - le nom de chaque story est l'id de conversation dans la base parfum moins cher
* train/test/eval.csv
  - chacun des trois fichiers contient la conversation réelle à l'origine des stories. 
  - la première ligne de chaque conversation est son id. 

* domain.yml
   - contient l'ensemble des élements qu'on trouve dans notre config : 
   		+ liste des intents
   		+ liste des entités
   		+ liste des slots
   		+ liste des réponses-type
   - contient l'ensemble des réponses-type. 

   