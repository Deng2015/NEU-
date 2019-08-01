storage = {}
storage["first"] = {}
storage["middle"] = {}
storage["last"] = {}

me = "Magnus Lie Hetland"
storage["first"]["Magus"] = [me]
storage["middle"]["Lie"] = [me]
storage["last"]["Hetland"]  = [me]

print(storage["middle"]["Lie"])

my_sister = "Anna Lie Hetland"
storage["first"].setdefault("Anna",[]).append(my_sister)
storage['middle'].setdefault('Lie',[]).append(my_sister)
storage['last'].setdefault("Hetland",[]).append(my_sister)

print(storage['middle']["Lie"])