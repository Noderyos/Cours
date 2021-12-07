def caesar_encode(text : str, key : int) -> str:
    base = 65 if ord(text[0]) <= 90 else 97
    return ''.join([chr(((ord(i) - base + key) % 26) + base) for i in text if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)])

def caesar_decode(text : str, key : int) -> str:
    base = 65 if ord(text[0]) <= 90 else 97
    return ''.join([chr(((ord(i) - base - key) % 26) + base) for i in text if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)])

def caesar(text : str, key : int) -> str:
    base = 65 if ord(text[0]) <= 90 else 97
    return ''.join([chr(((ord(i) - base + key) % 26) + base) for i in text if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)])





def caesar_encode_detail(text : str, key : int) -> str:
    base = 65 if ord(text[0]) <= 90 else 97
    out = ""
    for i in text:
    	if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
    		out += chr(((ord(i) - base + key) % 26) + base)
    	else:
    		out += i
    return out

def caesar_decode_detail(text : str, key : int) -> str:
    base = 65 if ord(text[0]) <= 90 else 97
    out = ""
    for i in text:
    	if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
    		out += chr(((ord(i) - base - key) % 26) + base)
    	else:
    		out += i
    return out
def caesar_detail(text : str, key : int) -> str:
    if not text == "":
        out = ""
        for i in text:
        	if (ord(i) >= 65 and ord(i) <= 90):
        		out += chr(((ord(i) - 65 + key) % 26) + 65)
        	else:
        		out += i
        return out
    return ""


def caesar_custom_alphabet(text : str, key : int, alpha = "éèàù'?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") -> str:
    if not text == "":
        out = ""
        for i in text:
            if isinstance(alpha,str) and i in alpha:
                out += alpha[(alpha.find(i)+ key) % len(alpha)]
            else:
                out += i
        return out
    return ""
    #return ''.join([alpha[(alpha.find(letter) + key) % len(alpha)] for letter in text])