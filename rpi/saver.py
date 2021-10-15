def data_to_save(time, lat, lon):
    return str(time) + "," + str(lat) + "," + str(lon)


def save_to_file(filename, data):
    f = open("data/%s" %(filename), "a")
    f.write(str(data) + "\n")
