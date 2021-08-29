def scoring(array):
    if len(array) == 0:
        return []
    
    tot = {}
    for i in array:
        tot[i["name"]] = 0
    
    for i in array:
        tot[i["name"]] = (i["norm_kill"] * 100) + (i["assist"] * 50) + (i["damage"] * 0.5) + (i["healing"]) + (2**i["streak"]) + (i["env_kill"] * 500)

    names = []
    scores = []

    for i in array:
        names.append(i["name"])
        scores.append(tot[i["name"]])
    
    # Sort both the names and scores arrays in descending order uisng Modified Bubble Sort
    for i in range(len(scores)):
        flag = 0
        for j in range(len(scores) -i - 1):
            if scores[j] < scores[j+1]:
                tempS = scores[j]
                tempN = names[j]
                scores[j] = scores[j+1]
                names[j] = names[j+1]
                scores[j+1] = tempS
                names[j+1] = tempN
                flag = 1
        if flag == 0:
            break

    return names



p1 = {
  "name": "JuanPablo",
  "norm_kill": 5,
  "assist": 12,
  "damage": 3200,
  "healing": 0,
  "streak": 4,
  "env_kill": 1
}
p2 = {
  "name": "ProfX",
  "norm_kill": 2,
  "assist": 14,
  "damage": 600,
  "healing": 1500,
  "streak": 0,
  "env_kill": 0
}
p3 = {
  "name": "Ajna",
  "norm_kill": 1,
  "assist": 8,
  "damage": 900,
  "healing": 30,
  "streak": 3,
  "env_kill": 5
}

p4 = {
  "name": "PaulMaurice",
  "norm_kill": 3,
  "assist": 0,
  "damage": 0,
  "healing": 20,
  "streak": 2,
  "env_kill": 0
}


try:
    assert scoring([p3, p2]) == ['Ajna', 'ProfX']
    print("Passed Test 1")
except AssertionError:
    print("Failed Test 1")

try:
    assert scoring([p1, p2, p3, p4]) == ['Ajna', 'JuanPablo', 'ProfX', 'PaulMaurice']
    print("Passed Test 2")
except AssertionError:
    print("Failed Test 2")