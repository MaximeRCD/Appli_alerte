# Appli_alerte

## 0. Contexte

Ce programme python constitue notre projet rendu pour le module de langage script.
Il s'articule autour d'une aplication de scrapping de site web. L'objectif est de
fournir une application d'alerte de bonne affaire. 

Nous scrappons le site de backmarket pour les produits Iphones 11 et 12
afin de récupérer les champs nécessaires à notre étude.

Ainsi nous récupérons dans les données :
    
    Model : Nom de l'iphone présenté sur le site.
    Stockage : Capacité de stockage de l'iphone concerné.
    Couleur : Couleur de l'iphone concerné.
    Etat : Niveau de réaration de l'iphone concerné.
    Prix : Prix de vente de l'iphone concerné.
    Url : Lien vers le site vendeur.

Ces données sont enregistrées de façon partionnée de sorte à avoir 
un historique sur les prix de vente des models présentés sur le site.
ces données feront l'objet d'étude de tendance d'évolution du prix.

## 1. Scrapping

Dans le module scrap, dans le fichier scrapping, on retrouve l'ensemble des 
fonctions qui nous ont permis de récupérer les données sur le site de 
Backmarket.

## 2. Storing data

Depuis le module de scrapping, il nous faut enregistrer les 
données en local afin de pouvoir les requêter par la suite.
Les données récupérées dans un tableau python sont transformées et 
stockées au format csv dans des dossiers partitionnés.

## 3. 


