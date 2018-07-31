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
