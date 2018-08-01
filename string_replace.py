def remplacer_mot(to_replace, replace_by, in_what):
    if any([type(x) !=type("str") for x in [to_replace, replace_by, in_what] ]):
       print("Error: expect strings in input.")
       return -1
    return in_what.replace(to_replace, replace_by)

print( remplacer_mot("com", "cam", "coméra" ) )
print( remplacer_mot("com", "cam", 6) )

def remplacer_mot_brut_force(to_replace, replace_by, in_what):
    str_sum = sum(bytearray(to_replace))
    str_len = len(to_replace)
    pos = []
    i=0
    bytear = sum(bytearray(in_what[:str_len]))
    while i < len(in_what) - str_len:
        if bytear == str_sum:
            if in_what[i:i+in_what]==to_replace:
                pos.append(i)


def remplacer_mot(mot1, mot2, ch):
    n = len(ch)
    n1 = len(mot1)
    n2 = len(mot2)
    i=0
    while i<n-n1:
        if ch[i:i+n1]==mot1:
            ch = ch[:i] + mot2 + ch[i+n1:]
            n+=n2
            i+=n2-n1
        i+=1
    return ch

mot1="bc"
mot2="123bc456"
ch="abcbcbcbcdbc"
print(remplacer_mot(mot1, mot2, ch))