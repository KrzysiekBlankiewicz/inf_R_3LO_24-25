def to_bin(dec):	#dec jest liczbą
	wynik = ""
	while dec != 0:
		x = dec % 2
		dec = (dec - x) / 2
		if x == 0:
			wynik = "0" + wynik
		if x == 1:
			wynik = "1" + wynik
	return wynik
    
def to_dec(bin):	#bin jest napisem
	wynik = 0
	for i in range(0, len(bin)):
		if bin[i] == "1":
			wynik += 2**(len(bin)-i-1)	
	return wynik
