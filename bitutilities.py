def chooseBitIcon(bits):
    if bits > 99999:
        return ["bitimagefiles/bit100000.png"]
    elif bits > 9999:
        return ["bitimagefiles/bit10000.png"]
    elif bits > 4999:
        return ["bitimagefiles/bit5000.png"]
    elif bits > 999:
        return ["bitimagefiles/bit1000.png"]
    elif bits > 99:
        return ["bitimagefiles/bit100.png"]
    else:
        return ["bitimagefiles/bit10.png"]
