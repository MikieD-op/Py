import time

lights = ["🔴", "🟡", "🟢"]
loop = True
while loop == True:
    for light in lights:
        print(light)
        if light == "🔴":
            time.sleep(5)
        elif light == "🟡":
            time.sleep(2)
        elif light == "🟢 ":
            time.sleep(3)
