import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

pk1 = 21
pk2 = 20
pk3 = 16
pk4 = 26

gpio.setup(pk1, gpio.OUT)
gpio.setup(pk2, gpio.OUT)
gpio.setup(pk3, gpio.OUT)
gpio.setup(pk4, gpio.OUT)


true_dict = {"pk1value": False, "pk2value": False, "pk3value": False, "pk4value": False}


def check_status():
    if gpio.input(pk1) == 1:
        true_dict["pk1value"] = True
    if gpio.input(pk2) == 1:
        true_dict["pk2value"] = True
    if gpio.input(pk3) == 1:
        true_dict["pk3value"] = True
    if gpio.input(pk4) == 1:
        true_dict["pk4value"] = True


def pk1(mode):
    if mode == "On":
        gpio.output(pk1, gpio.HIGH)
        true_dict["pk1value"] = True
    if mode == "Off":
        gpio.output(pk1, gpio.LOW)
        true_dict["pk1value"] = False


def pk2(mode):
    if mode == "On":
        gpio.output(pk2, gpio.HIGH)
        true_dict["pk2value"] = True
    if mode == "Off":
        gpio.output(pk2, gpio.LOW)
        true_dict["pk2value"] = False


def pk3(mode):
    if mode == "On":
        gpio.output(pk3, gpio.HIGH)
        true_dict["pk3value"] = True
    if mode == "Off":
        gpio.output(pk3, gpio.LOW)
        true_dict["pk3value"] = False


def pk4(mode):
    if mode == "On":
        gpio.output(pk4, gpio.HIGH)
        true_dict["pk4value"] = True
    if mode == "Off":
        gpio.output(pk4, gpio.LOW)
        true_dict["pk4value"] = False
