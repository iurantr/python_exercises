import re
pattern = r"[0-9]{2}"
print(re.findall(pattern, "Marc a27 ans"))
print(re.findall(pattern, "27,est son age"))
print(re.findall(pattern, "Je ne connais pas son age"))


