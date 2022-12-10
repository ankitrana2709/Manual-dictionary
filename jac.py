def jaccard_similarity(s1: str, s2: str)->float:
	"""Computes the Jaccard similarity score between s1 and s2."""
	return len(set(s1) & set(s2)) / len(set(s1) | set(s2))

if __name__ == "__main__":
	s1 = "gurgaon"
	s2 = "gurugram"
	jaccard_sim = jaccard_similarity(s1, s2)
	print(f"The Jaccard similarity between {s1} and {s2} is {jaccard_sim}")
