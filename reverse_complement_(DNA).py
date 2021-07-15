# https://www.codewars.com/kata/574a7d0dca4a8a0fbe000100/train/python


def reverse_complement(dna):
	if not set("ACTG").issuperset(dna):
		return "Invalid sequence"
	return dna[::-1].translate(dna.maketrans("ACTG", "TGAC"))   
    

