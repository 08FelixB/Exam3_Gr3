messages_gr3 = {
    "pseudo" : "DebugWoman",
    "messages" : ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
    "cryptes" : ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", "Oh frgh pdîwuh hvw 4567"]
}




def dechiffrer_message():
    """
    Déchiffre un message codé à l’aide de la clé fournie.
    """
    message_cryptes1 = "Uhqghc yrxv dx srlqw 1 à plgl"
    message_decrypter = ""
    clef1 = {'d': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g',
            'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n',
            'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u',
            'y': 'v', 'z': 'w', 'a': 'x', 'b': 'y', 'c': 'z', '1': "4", '2': "5", "3": "6", '4': "7", '5': "8", '6': "9", '7': '10'}
    clef2 = {'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G',
            'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N',
            'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
            'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y', 'C': 'Z',}

    for mot in message_cryptes1:
        if mot in clef1:
                message_decrypter += clef1[mot]
        elif mot in clef2:
                message_decrypter += clef2[mot]
        else:
            message_decrypter += mot

    return message_decrypter
def dechiffrer_message2():
    """
    Déchiffre un message codé à l’aide de la clé fournie.
    """
    message_cryptes2 = "Sodq E dfwlyhu hq fdv gh sureoèph"
    message_decrypter2 = ""
    clef1 = {'d': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g',
            'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n',
            'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u',
            'y': 'v', 'z': 'w', 'a': 'x', 'b': 'y', 'c': 'z', '1': "4", '2': "5", "3": "6", '4': "7", '5': "8", '6': "9", '7': '10'}
    clef2 = {'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G',
            'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N',
            'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
            'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y', 'C': 'Z',}

    for mot in message_cryptes2:
        if mot in clef1:
                message_decrypter2 += clef1[mot]
        elif mot in clef2:
                message_decrypter2 += clef2[mot]
        else:
            message_decrypter2 += mot

    return message_decrypter2

def dechiffrer_message3():
    """
    Déchiffre un message codé à l’aide de la clé fournie.
    """
    message_cryptes3 = "Oh frgh pdîwuh hvw 4567"
    message_decrypter3 = ""
    clef1 = {'d': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g',
            'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n',
            'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u',
            'y': 'v', 'z': 'w', 'a': 'x', 'b': 'y', 'c': 'z', '1': "4", '2': "5", "3": "6", '4': "7", '5': "8", '6': "9", '7': '10'}
    clef2 = {'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G',
            'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N',
            'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
            'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y', 'C': 'Z',}

    for mot in message_cryptes3:
        if mot in clef1:
                message_decrypter3 += clef1[mot]
        elif mot in clef2:
                message_decrypter3 += clef2[mot]
        else:
            message_decrypter3 += mot

    return message_decrypter3

def verifier_message():
    """
    fonction qui vérifie si le message déchiffré est pareil que le message decrypter
    """
    #Si le premier message n'égale pas à "Rendez vous au point 8 à midi" -> print("Attention, le message 1 a été intercepté, car il ne correspond pas.")
    if dechiffrer_message() != "Rendez vous au point 8 à midi":
        print("Attention, le message 1 a été intercepté, car il ne correspond pas.")
    # Si le deuxième message n'égale pas à "Plan B activer en cas de problème" -> print("Attention, le message 1 a été intercepté, car il ne correspond pas.")
    if dechiffrer_message2() != "Plan B activer en cas de problème":
        print("Attention, le message 2 a été intercepté, car il ne correspond pas.")
    # Si le troisième message n'égale pas à "Le code maître est 2345" -> print("Attention, le message 1 a été intercepté, car il ne correspond pas.")
    if dechiffrer_message3() != "Le code maître est 2345":
        print("Attention, le message 3 a été intercepté, car il ne correspond pas.")


verifier_message()
print(dechiffrer_message())
print(dechiffrer_message2())
print(dechiffrer_message3())