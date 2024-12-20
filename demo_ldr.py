from gpiozero import LightSensor

ldr = LightSensor(20)

while True:
    ldr.wait_for_light()
    print("It's Light :)")
    ldr.wait_for_dark()
    print("It's dark :(")

while True:
    print(ldr.value)