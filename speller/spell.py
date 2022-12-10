import pandas as pd
def similarity(s1: str, s2: str)->float:
	"""Computes the similarity score between s1 and s2."""
	return len(set(s1) & set(s2)) / len(set(s1) | set(s2))

def capit(lis):
    new = []
    for a in lis:
        a=str(a)
        a=a.capitalize()
        new.append(a)
    lis = new
    return(lis)


# sheet location and column locations
mysheet = 'distat.csv'
df = pd.read_csv(mysheet)

incorrect = df["tobe_Correct"].tolist()
incorrect = capit(incorrect)
correct = df["Correct"].tolist()
correct = capit(correct)
new = []
dict = {'k' : 0}
import pandas as pd

for word in incorrect:
    if word in correct:
        new.append(word)
    elif word not in correct:
        for tale in correct:
            sim = similarity(str(word), str(tale))
            dict[tale] = sim
        #print(dict)
        Keymax = max(zip(dict.values(), dict.keys()))[1]
        new.append(Keymax)
    else:
        new.append("123")
                #if word in correct:
          #  new.append(word)  

df["corrected"] = pd.Series(new)
df.to_excel("vasu2.xlsx")

print(df)
