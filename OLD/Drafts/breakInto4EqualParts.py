
#https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
def split_string(string):
    length = len(string)
    part_length = length // 4
    return [string[i:i + part_length] for i in range(0, length, part_length)]

string = "atntawtkaAcD"
print(split_string(string))
