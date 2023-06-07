import base64


def encoding_decoding_password():
    data = input("Enter a string to encode : ")
    print("String to be encoded : \n" + data)

    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print("Encoded String : " + encodedStr)
    decodedBytes = base64.b64decode(encodedStr)
    decodedStr = str(decodedBytes, "utf-8")
    print("Decoded String : " + decodedStr)