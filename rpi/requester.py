import os

def send_data(url, access_token, data, time, lat, lng):
    data = 'curl -X \'POST\' \'%s\' -H \'accept: application/json\'  -H \'Authorization: Bearer %s\' -H \'Content-Type: application/json\' -d \'{\"owner_id\": 0, \"my_date\": \"%s\",\"time\": \"%s\", \"longitude\": %s, \"latitude\": %s}\'' %(url, access_token, data, time, lng, lat)
    return os.system(data)

def my_base(data, time, lng, lat):
    return '{\"my_date\": \"%s\", \"time\": \"%s\", \"longitude\": %s, \"latitude\": %s, \"owner_id\": 0}' %(data, time, lng, lat)

def send_more_data(url, access_token, my_list):
    my_string = 'curl -X \'POST\' \'%s\' -H \'accept: application/json\'  -H \'Authorization: Bearer %s\' -H \'Content-Type: application/json\' -d \'{\"my_list\": [' %(url, access_token)
    end_string = ']}\''
    for element in my_list:
        # print element['time']
        # print element['longitude']
        # print element['my_date']
        # print element['latitude']
        my_string += my_base(element['my_date'], element['time'], element['longitude'], element['latitude'])
        my_string += ", "
    my_string = my_string[:-2]
    my_string += end_string
    # print my_string
    return os.system(my_string)
        # print my_base(element['my_date'], element['time'], element['longitude'], element['latitude'])
