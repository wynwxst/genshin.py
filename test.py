import genshin

g = genshin.Genshin(local=False)

c = g.api("characters")
print(c.values)
print(g.types)
print()