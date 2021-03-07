import collections


class Mode:
    @staticmethod
    def mode(data):
        data_m = collections.Counter(data)
        data_list = dict(data_m)

        max_value = max(list(data_m.values()))
        mode_val = [num for num, freq in data_list.items() if freq == max_value]
        if len(mode_val) == len(data):
            return "no mode"
        else:
            return int(''.join(map(str, mode_val)))
