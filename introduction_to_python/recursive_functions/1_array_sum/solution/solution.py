def sum_array(num_list):
        if not num_list:
            return 0
        return num_list.pop() + sum_array(num_list)