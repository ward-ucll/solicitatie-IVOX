data = []
testgevallen = int(input())
for test in range(1, testgevallen + 1 ):
    testgeval = dict()
    testgeval["stroomPerUur"] = [int(x) for x in input().split(" ")]
    testgeval["aantalTaken"] = int(input())
    testgeval["taken"] = list()
    for taak in range(1, testgeval["aantalTaken"] + 1):
        testgeval["taken"].append(tuple(input().split(" ")))
    data.append(testgeval)

def calculate_price(data):
    testnummer = 0
    for test in data:
        test["stroomPerUur"] = sorted(test["stroomPerUur"])
        totaal = 0
        for taak in test["taken"]:
            stroomindex = 0
            for x in range(1, int(taak[1]) + 1):
                totaal += test["stroomPerUur"][stroomindex] * int(taak[0])
                if (x % 60 == 0):
                    stroomindex += 1 
        testnummer +=1
        print(f"{(testnummer)} {totaal}")
        
calculate_price(data)
