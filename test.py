import random
while True:
    print("type roll")
    answer = input()
    if answer == "roll":
        print(random.randint(1,6))
    else:
        break