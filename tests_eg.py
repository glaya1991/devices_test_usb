# 3.1.1. Тестирование компонентов устройств
msg_components = [
    "/get/memory?address=26&|"
]

#3.2.1 Тест: “Инициализация и обнаружение устройства”
msg_device = [
    "/device&|"
]

# 3.2.2 Тест «Инициализация и обнаружение устройства по Wi-Fi»
msg_wifi_init = [
    "/put/wifi?login=LenovoTAB2A7_30HC&pass=229ce9bd3843&|"
]

# 3.2.3. Тест “Импеданс ЭЭГ”
msg_impedance = [
    "/put/memory?address=52&value=6&|",
    "/get/memory?address=81&|",
    "/get/memory?address=82&|",
    "/get/memory?address=83&|",
    "/get/memory?address=84&|",
    "/get/memory?address=85&|",
    "/get/memory?address=86&|",
    "/get/memory?address=87&|",
    "/get/memory?address=88&|",
    "/get/memory?address=89&|",
    "/get/memory?address=90&|"
]

# 3.2.5. Тест “Начало потока ЭЭГ”
msg_thread_eeg = [
    "/put/memory?address=52&value=7&|",
    "/put/memory?address=23&value=0&|",
    "/put/memory?address=161&value=4&|",
    "/put/memory?address=162&value=4&|",
    "/put/memory?address=163&value=10&|",
    "/put/memory?address=164&value=400&|",
    "/put/memory?address=165&value=500&|",
    "/put/memory?address=166&value=2000&|",
    "/put/memory?address=22&value=32&|",
    "/put/memory?address=39&value=214&|",
    "/put/memory?address=40&value=194&|",
    "/put/memory?address=41&value=96&|",
    "/put/memory?address=42&value=0&|",
    "/put/memory?address=43&value=0&|",
    "/put/memory?address=44&value=0&|",
    "/put/memory?address=45&value=0&|",
    "/put/memory?address=46&value=0&|",
    "/put/memory?address=47&value=0&|",
    "/put/memory?address=48&value=112&|",
    "/put/memory?address=49&value=0&|",
    "/put/memory?address=50&value=0&|",
    "/put/memory?address=51&value=0&|",
    "/put/memory?address=91&value=1985229328&|",

    "/put/memory?address=92&value=64&|",
    "/put/memory?address=93&value=64&|",
    "/put/memory?address=94&value=64&|",
    "/put/memory?address=95&value=64&|",
    "/put/memory?address=96&value=64&|",
    "/put/memory?address=97&value=64&|",
    "/put/memory?address=98&value=64&|",
    "/put/memory?address=99&value=64&|",

    "/put/memory?address=23&value=1&|",
    "/put/memory?address=52&value=1&|"
]

# 3.2.8. Тест “Режим P300 для ЭЭГ”
msg_p300 = [
    "/device&|"
    "/put/memory?address=52&value=7&|",
    "/put/memory?address=23&value=0&|",
    "/put/memory?address=161&value=4&|",
    "/put/memory?address=162&value=4&|",
    "/put/memory?address=163&value=10&|",
    "/put/memory?address=164&value=400&|",
    "/put/memory?address=165&value=500&|",
    "/put/memory?address=166&value=2000&|",
    "/put/memory?address=22&value=32&|",
    "/put/memory?address=39&value=214&|",
    "/put/memory?address=40&value=194&|",
    "/put/memory?address=41&value=96&|",
    "/put/memory?address=42&value=0&|",
    "/put/memory?address=43&value=0&|",
    "/put/memory?address=44&value=0&|",
    "/put/memory?address=45&value=0&|",
    "/put/memory?address=46&value=0&|",
    "/put/memory?address=47&value=0&|",
    "/put/memory?address=48&value=112&|",
    "/put/memory?address=49&value=0&|",
    "/put/memory?address=50&value=0&|",
    "/put/memory?address=51&value=0&|",
    "/put/memory?address=91&value=1985229464&|",

    "/put/memory?address=92&value=64&|",
    "/put/memory?address=93&value=64&|",
    "/put/memory?address=94&value=64&|",
    "/put/memory?address=95&value=64&|",
    "/put/memory?address=96&value=64&|",
    "/put/memory?address=97&value=64&|",
    "/put/memory?address=98&value=64&|",
    "/put/memory?address=99&value=64&|",

    "/put/memory?address=23&value=1&|",
    "/put/memory?address=52&value=1&|"
]