def chooseBitIcon(bits):
    if bits > 99999:
        return ["bitimagefiles/bit100000reduced.png"]
    elif bits > 9999:
        return ["bitimagefiles/bit10000reduced.png"]
    elif bits > 4999:
        return ["bitimagefiles/bit5000reduced.png"]
    elif bits > 999:
        return ["bitimagefiles/bit1000reduced.png"]
    elif bits > 99:
        return ["bitimagefiles/bit100reduced.png"]
    else:
        return ["bitimagefiles/bit10reduced.png"]
