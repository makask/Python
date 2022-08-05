# Ülesanne nr.159
# Printida ainult need kahekohalised arvud, mis jaguvad 4-ga, kuid ei jagu 6-ga.

print("Kahekohalised arvud, mis jaguvad 4-ga kuid ei jagu 6-ga: ")
for number in range(10,100):
    x = number % 4
    y = number % 6
    if x == 0 and y > 0: 
        print(number, end=" ")