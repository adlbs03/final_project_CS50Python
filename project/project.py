#Projet final Python pour CS50

import sys
import torch

def main():
    print(f"ANA : {modele()}")

def user_chat():
    try:
        input("Ask anything")
    except IndexError:
        sys.exit

def modele():
    ...

if __name__ == "__main__":
    main()
