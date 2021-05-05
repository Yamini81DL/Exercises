data =[]

def store(number_1,number_2):
    result = int(number_1) + int(number_2)
    data.append(number_1)
    data.append(number_2)
    data.append(result)
    return result
