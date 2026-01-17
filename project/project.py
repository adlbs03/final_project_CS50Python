#!/usr/bin/env python3
# Projet final Python pour CS50

"""
Un chatbot simple et autonome pour tests et développement.

Fonctionnalités :
- mode interactif (entrée utilisateur répétée)
- mode non-interactif (passer le message en argument CLI)

Pas de dépendances externes : facile à exécuter dans n'importe quel environnement.
"""

import sys
from typing import Optional


def get_user_input() -> Optional[str]:
    # Si des arguments CLI sont fournis, les concatène et retourne la phrase
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    try:
        return input("Vous: ")
    except (EOFError, KeyboardInterrupt):
        print('\nSortie.')
        return None


def get_response(message: str) -> str:
    """Répond de façon simple selon quelques règles basiques."""
    if not message:
        return "Je n'ai rien reçu."

    m = message.lower().strip()
    # salutations
    if any(x in m for x in ("bonjour", "salut", "hello", "hi")):
        return "Bonjour ! Comment puis-je vous aider ?"
    if any(x in m for x in ("ça va", "ça va ?", "comment ça va", "how are you")):
        return "Je vais bien, merci. Et vous ?"
    if any(x in m for x in ("au revoir", "bye", "a bientôt", "à plus")):
        return "Au revoir ! Passez une bonne journée."
    # petites conversations
    if "ton nom" in m or "tu t'appelles" in m or "comment tu t'appelles" in m:
        return "Je m'appelle ANA, votre assistant simple."
    # si contient un point d'interrogation, répondre générique
    if "?" in m:
        return "C'est une bonne question — je n'ai pas (encore) la réponse exacte."
    # fallback: écho poli
    return "Je ne comprends pas complètement, pouvez-vous reformuler ?"


def main():
    # Si un argument CLI est fourni, on fait une seule réponse non-interactive
    if len(sys.argv) > 1:
        msg = get_user_input()
        if msg is None:
            return
        print("ANA:", get_response(msg))
        return

    # Mode interactif
    print("ANA — Chatbot simple. Tapez 'quit' ou 'au revoir' pour sortir.")
    while True:
        msg = get_user_input()
        if msg is None:
            break
        if msg.strip().lower() in ("quit", "exit", "au revoir", "bye", "a bientôt", "à plus"):
            print("ANA: Au revoir !")
            break
        response = get_response(msg)
        print("ANA:", response)


if __name__ == "__main__":
    main()


