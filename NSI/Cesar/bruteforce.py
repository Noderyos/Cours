def caesar_encode_detail(text : str, key : int) -> str:
    base = 65
    out = ""
    for i in text:
    	if ord(i) >= 65 and ord(i) <= 90:
    		out += chr(((ord(i) - base + key) % 26) + base)
    	else:
    		out += i
    return out
INPUT = "AV WRZJ JFLMVEK TV IVMV VKIREXV VK GVEVKIREK U'LEV WVDDV ZETFEELV, VK HLV A'RZDV, VK HLZ D'RZDV, VK HLZ E'VJK, TYRHLV WFZJ, EZ KFLK R WRZK CR DVDV EZ KFLK R WRZK LEV RLKIV, VK D'RZDV VK DV TFDGIVEU"
OUT = []
for i in range(26):
	#print(f"With key {str(i)} we found : {caesar_encode_detail(INPUT,i)}")
	OUT.append(str(i) + " " + str(caesar_encode_detail(INPUT,i).count("E") / len(INPUT)))
	#print("Chance : " + str(caesar_encode_detail(INPUT,i).count("E") / len(INPUT)))
key = int(sorted(OUT)[::-1][0].split(" ")[0])
print(f'\nValid key is {key} with {str(caesar_encode_detail(INPUT,key).count("E") / len(INPUT))[:5]}% of the letter E in the sentence\n')
print(f'Decoded : ' + caesar_encode_detail(INPUT,key) + "\n")