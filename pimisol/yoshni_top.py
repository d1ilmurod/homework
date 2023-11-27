with open("pi_million_digits.txt") as fil:
    pi = fil.read()
pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = pi.replace(" ", "")


bdate = "04052004"
print(bdate in pi)
