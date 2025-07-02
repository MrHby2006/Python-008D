
for i in range(1, 31):
    if i  % 3 == 0 and i % 5 == 0:
        print(f"{i} es múltiplo de 3 y de 5")
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} es múltiplo de 5")
    else:
        print(f"{i} es otro número")