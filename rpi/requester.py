import os

def send_data(url, access_token, data, time, lat, lng):
    data = 'curl -X \'POST\' \'%s\' -H \'accept: application/json\'  -H \'Authorization: Bearer %s\' -H \'Content-Type: application/json\' -d \'{\"owner_id\": 0, \"my_date\": \"%s\",\"time\": \"%s\", \"longitude\": %s, \"latitude\": %s}\'' %(url, access_token, data, time, lng, lat)
    return os.system(data)