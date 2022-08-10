# BA1C
# http://rosalind.info/problems/ba1c/
# Find a Profile-most Probable k-mer in a String


def comp(text):
    pattern=""
    for i in range(0,len(text)):
        if text[i]== "A":
            pattern = "T" + pattern
        elif text[i]== "C":
            pattern = "G" + pattern
        elif text[i]=="G":
            pattern = "C" + pattern
        elif text[i]== "T":
            pattern = "A" + pattern
        else:
            return "Greška pri unosu"
    return pattern

print(comp("AAAACCCGGT"))
