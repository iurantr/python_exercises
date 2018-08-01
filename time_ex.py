from datetime import datetime, timedelta

def loop_input_int(string="Enter value:"):
    verif = True
    while verif:
        try:
            result = int(input(string))
        except ValueError:
            print("Error: please enter an Integer value!")
        else:
            verif=False
    return result

print("Entrer la premier duree.")
H1 = loop_input_int("Entrer H1 : ")
M1 = loop_input_int("Entrer M1 : ")
S1 = loop_input_int("Entrer S1 : ")

print("Entrer la deuxiéme date.")
H2 = loop_input_int("Entrer H2 : ")
M2 = loop_input_int("Entrer M2 : ")
S2 = loop_input_int("Entrer S2 : ")

duree1 = timedelta(hours=H1, minutes=M1, seconds=S1)
duree2 = timedelta(hours=H2, minutes=M2, seconds=S2)
somme = duree1 + duree2

# try to format the output string
try:
    somme_str = datetime.strptime(str(somme), "%H:%M:%S")
    somme_str = somme_str.strftime("0 jours %H H %M Min %S s")
except ValueError:
    try:
        somme_str = datetime.strptime(str(somme), "%j day, %H:%M:%S")
        somme_str = somme_str.strftime("%j jours %H H %M Min %S s")
    except ValueError:
        somme_str = datetime.strptime(str(somme), "%j days, %H:%M:%S")
        somme_str = somme_str.strftime("%j jours %H H %M Min %S s")


print()

print("%d H %d Min %d s + %d H %d Min %d s = " % \
      (H1, M1, S1, H2, M2, S2) + somme_str)
