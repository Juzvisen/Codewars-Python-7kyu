# https://www.codewars.com/kata/5b043e3886d0752685000009/train/python


def micheal_pays(costs):
	kate_pays = costs / 100 * 33.33 if costs /100 *33.33 < 10 else 10
	if costs < 5:
		return costs
	else:
		return round(costs - kate_pays,2)

print(micheal_pays(5.9181))