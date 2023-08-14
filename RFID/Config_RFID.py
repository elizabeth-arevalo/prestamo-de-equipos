import RPi.GPIO as GPIO
import MFRC522

RST_PIN = 22   # Configurable, RST Pin
SS_PIN = 24    # Configurable, SDA Pin

# Create MFRC522 instance
mfrc522 = MFRC522.MFRC522(SS_PIN, RST_PIN)

def Escribir():
    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # Prepare key

    while not mfrc522.MFRC522_Request(mfrc522.PICC_REQIDL):  # Look for new cards
        pass

    status, uid = mfrc522.MFRC522_Anticoll()  # Select one of the cards

    if status == mfrc522.MI_OK:
        print("Card UID:", uid)  # Dump UID
        piccType = mfrc522.PICC_GetType(uid[0])  # Dump PICC type
        print("PICC type:", mfrc522.PICC_GetTypeName(piccType))

        block = 1
        buffer = [0] * 18
        for i in range(18):
            buffer[i] = ord(' ')

        print("Enter code ending with #")
        input_data = input()
        len_data = min(len(input_data), 30)
        for i in range(len_data):
            buffer[i] = ord(input_data[i])

        status = mfrc522.MFRC522_Auth(mfrc522.PICC_CMD_MF_AUTH_KEY_A, block, key, uid)
        if status == mfrc522.MI_OK:
            print("Authentication success")

            status = mfrc522.MFRC522_Write(block, buffer)
            if status == mfrc522.MI_OK:
                print("Write success")
            else:
                print("Write failed:", mfrc522.GetStatusCodeName(status))

            mfrc522.MFRC522_StopCrypto1()
        else:
            print("Authentication failed:", mfrc522.GetStatusCodeName(status))
        
        mfrc522.MFRC522_Halt()

def Leer():
    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

    while not mfrc522.MFRC522_Request(mfrc522.PICC_REQIDL):  # Look for new cards
        pass

    status, uid = mfrc522.MFRC522_Anticoll()  # Select one of the cards

    if status == mfrc522.MI_OK:
        print("**Card Detected:**")
        mfrc522.MFRC522_DumpDetails(uid)  # Dump some details about the card

        len_data = 18
        buffer = [0] * len_data
        block = 1

        status = mfrc522.MFRC522_Auth(mfrc522.PICC_CMD_MF_AUTH_KEY_A, block, key, uid)
        if status == mfrc522.MI_OK:
            print("Authentication success")

            status, buffer = mfrc522.MFRC522_Read(block, len_data)
            if status == mfrc522.MI_OK:
                print("Read success")
                last_name = ''.join(chr(byte) for byte in buffer)
                print("Last Name:", last_name)
            else:
                print("Read failed:", mfrc522.GetStatusCodeName(status))

            mfrc522.MFRC522_StopCrypto1()
        else:
            print("Authentication failed:", mfrc522.GetStatusCodeName(status))

        print("**End Reading**")

try:
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    mfrc522.MFRC522_Init()

    while True:
        print("1. Escribir")
        print("2. Leer")
        choice = input()
        if choice == '1':
            Escribir()
        elif choice == '2':
            Leer()

except KeyboardInterrupt:
    GPIO.cleanup()
