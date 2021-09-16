def read(path):
    f = open(path, "r")
    file = f.read()
    lines = file.split("\n")
    for line in lines:
        words = line.split(" ")
        if words[0] == "power":
            power = float(words[1])
        if words[0] == "layer":
            layer = float(words[1])
        if words[0] == "time":
            time = float(words[1])
    return power , layer, time
