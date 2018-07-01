def getDefenseForce(DamageReduction):
    return DamageReduction*100/(1-DamageReduction)

print(getDefenseForce(0.9))
input()