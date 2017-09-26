#!/usr/bin/python3
"""
J'ai finalement écrit ce script, originellement pour un challenge de stégano de root-me.org
mais j'avais eu plus vite fait de trouver sur le net.

Chaînes de test
#key = "EYJFRGTT"
#message = "EPCQFBXKWURQCTXOIPMNV"
"""

import argparse
import unicodedata

# Enlever les accents (thx to https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string)
def remove_accents(input_str):
  nfkd_form = unicodedata.normalize('NFKD', input_str)
  only_ascii = nfkd_form.encode('ASCII', 'ignore')
  return only_ascii

"""
Parser
"""
# Parser
parser = argparse.ArgumentParser(description='Chiffrement et Déchiffrement de Vigenère')
# Chiffrement / Déchiffrement
encryptGroup = parser.add_mutually_exclusive_group(required=True)
encryptGroup.add_argument('-e','--encrypt', action='store_true', help='Chiffrement.')
encryptGroup.add_argument('-d','--decrypt', action='store_true', help='Déchiffrement.')
# Clé
keyGroup = parser.add_mutually_exclusive_group(required=True)
keyGroup.add_argument('-k', '--key', help='Clé du message à chiffrer/déchiffrer.')
keyGroup.add_argument('-K', '--keyfile', help='Chemin du fichier contenant la clé du message à chiffrer/déchiffrer.')
# Message
messageGroup = parser.add_mutually_exclusive_group(required=True)
messageGroup.add_argument('-m', '--message', help='Message à chiffrer/déchiffrer.')
messageGroup.add_argument('-M', '--messagefile', help='Chemin du fichier à considérer comme message.')
# Format
parser.add_argument('-o', '--output', help='Chemin du fichier dans lequel écrire.')
parser.add_argument('-s', '--strip', action='store_true', help='Enlever les espaces préalablement au traitement.')
parser.add_argument('-U', '--uppercase', action='store_true', help='Message chiffré/déchiffré en Majuscule.')

# Parsing des arguments
args = parser.parse_args()

"""
Algo
"""
# Vars
i = 0
offset = ord('a')
final = ""

# Clé
if(args.key):
  key = remove_accents(args.key.lower()).decode("utf-8")
else:
  with open(args.keyfile, 'r', encoding='utf-8') as kf:
    key = remove_accents(kf.read().rstrip("\n").lower()).decode("utf-8")

# Message
if(args.message):
  message = remove_accents(args.message.lower()).decode("utf-8")
else:
  with open(args.file, 'r', encoding='utf-8') as mf:
    message = remove_accents(mf.read().rstrip("\n").lower()).decode("utf-8")

# Trimming des espaces
if(args.strip):
  message = message.strip()

# Itération sur le message
for char in message:

  # Si c'est une lettre
  if(char.isalpha()):
    k = ord(key[i]) - offset
    m = ord(char) - offset

    # Chiffrement
    if(args.encrypt):
      c = (m + k) % 26
    
    # Déchiffrement
    if(args.decrypt):
      c = (m - k) % 26

    final += chr(c + offset)

    # Incrémentation de la clé
    i = (i + 1) % len(key)

  # Sinon si c'est genre un point, on ne change pas et on n'incrémente pas
  else:
    final += char

# On convertit en majuscule
if(args.uppercase):
  final = final.upper()

# Écriture dans le fichier
if(args.output):
  with open(args.output, 'w', encoding='utf-8') as outFile:
    outFile.write("".join([final, "\n"]))

# Ou affichage sur la sortie standard
else:
  print(final)
