import sys


def form_empty_json():
    return {
        "id": "",
        "name": {
            "first": None,
            "middle": None,
            "last": None
        },
        "dob": None,
        "locations": [],
        "imageId": None
    }


def get_location_object():
    return {
        "name": None,
        "coords": {
            "long": None,
            "lat": None
        }
    }


def extract(input):
    return input.replace('><', '+').replace('<', '').replace('>', '').split('+')


def form_json(s):
    ans = form_empty_json()
    arr = s.split('|')
    if arr[0] != "new_profile":
        return None
    if arr[1] and len(arr[1]) > 0:
        ans["id"] = arr[1]
    name_arr = extract(arr[2])
    for idx, name in enumerate(name_arr):
        if name and len(name) > 0:
            if idx == 0:
                ans["name"]["first"] = name
            elif idx == 1:
                ans["name"]["middle"] = name
            else:
                ans["name"]["last"] = name
    if arr[3] and len(arr[3]) > 0:
        ans["dob"] = arr[3]
    loc_obj = arr[4].split(',')
    for loc in loc_obj:
        loc_arr = extract(loc)
        obj = get_location_object()
        for idx, data in enumerate(loc_arr):
            if data and len(data) > 0:
                if idx == 0:
                    obj["name"] = data
                elif idx == 1:
                    obj["coords"]["long"] = data
                else:
                    obj["coords"]["lat"] = data
        if obj["name"]:
            ans["locations"].append(obj)
    if arr[5] and len(arr[5]) > 0:
        ans["imageId"] = arr[5]
    return ans


if __name__ == "__main__":

    if len(sys.argv) > 1:
        result = form_json(sys.argv[1])
        if result:
            print result
        else:
            print 'Invalid input.Json could not be created'
    else:
        print "Please provide an argument"
