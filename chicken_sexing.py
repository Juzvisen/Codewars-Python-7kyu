# https://www.codewars.com/kata/57ed40e3bd793e9c92000fcb/train/python


def correctness(bobs_decisions, expert_decisions):
	return sum(b==e or 0.5 * (b=="?" or e=="?") for b,e in zip(bobs_decisions,expert_decisions))





