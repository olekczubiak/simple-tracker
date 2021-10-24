import os
def send_data(data, lat, lng):
    data = "curl -X \'POST\'   \'https://tracker.toadres.pl/add\'   -H \'accept: application/json\'   -H \'Content-Type: application/json\'   -d \'{\"time\": \"%s\", \"longitude\": \"%s\", \"latitude\": \"%s\"}\'" %(data, lng, lat)
    return os.system(data)