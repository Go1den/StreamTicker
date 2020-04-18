def chooseBitIcon(bits):
    if bits > 99999:
        return ["imagefiles/bit100000.png"]
    elif bits > 9999:
        return ["imagefiles/bit10000.png"]
    elif bits > 4999:
        return ["imagefiles/bit5000.png"]
    elif bits > 999:
        return ["imagefiles/bit1000.png"]
    elif bits > 99:
        return ["imagefiles/bit100.png"]
    else:
        return ["imagefiles/bit10.png"]
