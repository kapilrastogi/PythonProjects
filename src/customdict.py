class CustomDict:

    # Takes an input list with duplicate data, store the frequency of each item in a dictionary
    def frequency_map(self, data):
        my_dict = {}
        for x in data:
            val = my_dict.get(x, 0)
            my_dict[x] = val + 1
        return my_dict

    def frequency_map_ex(self, data):
        my_dict = {}
        for x in data:
            my_dict[x] = my_dict.get(x, 0) + 1
        return my_dict
