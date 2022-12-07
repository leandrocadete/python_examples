import json

def SomatoriaPrize(dictArrayPrizes):
    total = 0
    for prize in dictArrayPrizes:
        total += prize["prize"]
    return total

stream = open("Prize22.json", "rb")
j = json.load(stream)

array_prizes = j["ticket"]["play"]["prizes"]
totalPrize_direto = j["ticket"]["ticket"]["total_prize"]

sumPrize = SomatoriaPrize(array_prizes)
print(sumPrize) # com somatória
print(totalPrize_direto) # direto de total_prize
stream.close()
