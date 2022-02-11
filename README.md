# Appli_alerte
Ce projet constitue le rendu pour le module de programmation script Python pour le Groupe RICHAUDEAU / FALL
## Avant Propos : 
En partant d'une page blanche, vous devez créer un programme python manipulant des données de diverses manières :

lecture / écriture / modification d'un fichier de configuration (type config.ini par exemple) avec des paires clef-valeur
fichiers de sortie liés à un traitement interne (création de fichiers PDF, gestion d'un fichier top-scores par exemple)
réaliser un traitement de données : à partir de données/fichiers en entrées, créer des données/fichiers en sortie
pas d'obligation d'interface graphique
pas d'obligation de bases de données
Si interface graphique : fenêtre en 1366*768, ou réglages via le fichier de configuration !
Exemples de précédentes réalisations :

Jeu de société avec IA poussée (if then else) : Monopoly, Scotland Yard, Yams ou autre jeu de dés, Mastermind, Touché coulé. 6 qui prend, Loup Garou, Démineur
Jeu casino avec sauvegarde et consultation de top score
Script pour manipuler ses comptes Facebook et Twitter
Récupérer l'article du jour / aléatoire de Wikipédia et le poster sur un autre site
Télécharger un site complet - aspirateur de site - robot crawler
Conversion de fichiers xx to PDF, PDF to xx
Editeur de PDF

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

## 4. Installation et utilisation du projet

### 4.1 Récupération du projet

Lancer la commande 
```bash
$ git clone https://github.com/MaximeRCD/Appli_alerte.git
 ```    

Créer un environnement virtuel afin de tester le projet
```bash
$ python -m venv .venv
```
Activer le venv : 
```bash
$ source .venv/bin/activate 
 ```    
ou 
 ```bash
$ source .venv/Script/activate
 ```    
Verifier l'activation du venv :
    
    (venv) doit apparaitre dans le terminal

Insatller les dépendances : 
```bash
$ pip install -r ./requierements.txt
 ```    
Lancer le programme:
```bash
$ python ./main.py
 ```    

# 5. Parcours Utilisateur
## 5.1 Register

Please click on register button to register yourself and choose the iphone you want.

## 5.2 Get an email

Please click on send an email button and enter the email you used to register !

## 5.3 Perform a scrap

Please click on update database button to perform scrapping and get fresh data !


