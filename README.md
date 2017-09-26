# Pygenere  
Chiffrement/déchiffrement de Vigenère en Python3.  

# How-to  
Cloner le dépot et penser à rendre le script exécutable.  
```shell
git clone https://github.com/aoikeiichi/Pygenere
cd Pygenere; chmod u+x vigenere.py
```  

# Usage  
```
./vigenere.py -h  
usage: vigenere.py [-h] (-e | -d) (-k KEY | -K KEYFILE) (-m MESSAGE | -M FILE)  
                   [-o OUTPUT] [-s] [-U]  
  
optional arguments:  
  -h, --help                       Affiche l'aide.  
  -e, --encrypt                    Chiffrement.  
  -d, --decrypt                    Déchiffrement.  
  
  -k KEY, --key KEY                Clé du message à chiffrer/déchiffrer.  
  -K KEYFILE, --keyfile KEYFILE    Chemin du fichier contenant la clé du message à chiffrer/déchiffrer.

  -m MESSAGE, --message MESSAGE                Message à chiffrer/déchiffrer.
  -M MESSAGEFILE, --messagefile MESSAGEFILE    Chemin du fichier à considérer comme message.

  -o OUTPUT, --output OUTPUT       Chemin du fichier dans lequel écrire.

  -s, --strip                      Enlever les espaces préalablement au traitement.  
  -U, --uppercase                  Message chiffré/déchiffré en Majuscule.  
```

# Exemples  
Exemple avec le fichier fourni sur Moodle.
```shell
# Déchiffrement
./vigenere.py -d -F exampleKeyFile -f exampleEncryptedFile -o decryptedTemp
# Chiffrement
./vigenere.py -e -F exampleKeyFile -f decryptedTemp -o encryptedTemp -U
# Vérification
diff encryptedTemp exampleEncryptedFile
```  

###### Si vous n'avez pas confiance, lisez le code, si vous avez confiance, lisez le code quand même.  
