# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python


def DNA_strand(dna):
	return dna.translate(dna.maketrans("ATCG", "TAGC"))
	
	
