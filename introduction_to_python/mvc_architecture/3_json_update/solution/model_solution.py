import json

match_data = {"Hockey":"India", "Cricket":"England", "Gymnastics":"Russia", "Football":"Spain","Baseball":"USA"}
data_match = json.dumps(match_data)

def get_list():
    return match_data

class Sports:

    def __init__(self, sport, country):
        self.sport = sport
        self.country = country

    def retrive_match(self):
        match_data[self.sport] = self.country
        return match_data



