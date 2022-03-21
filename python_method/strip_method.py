

# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)


#banana

txt = "     banana     "

x = txt.strip()

print(x)



txt = ",,,,,rrttgg.....banana....rrr"

y = txt.strip(",.grt")

print(y)

