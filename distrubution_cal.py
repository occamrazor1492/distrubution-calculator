import csv


def run(n):
    topn = read_n_tolist(n)
    dict_array = read_all_order()
    order_count = len(dict_array)
    result = len(check_in_top_n(dict_array,topn))
    print(result," Order only contain", "Top", n, " SPU", "among ",order_count, "orders. The ration is ",result/order_count*100, "%" )


def read_all_order():
    dict_array_record = []
    dict_array = []
    with open('all.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            key = row[0]
            value = row[1]

            if key in dict_array_record:
                for item in dict_array:
                    if item.__contains__(key):
                        temp_list = list(item.values())[0]
                        temp_list.append(value)
                        item[key] = temp_list
            else:
                dict_array_record.append(key)
                dict_array.append({key: [value]})

    # print("order count: ", len(dict_array))
    return dict_array


def check_in_top_n(dict_array, top_n):
    all_order_sku_is_topn = []
    for order_dict in dict_array:
        flag = 0
        temp_list = list(order_dict.values())[0]
        for sku in temp_list:
            if sku not in top_n:
                flag += 1
        if flag == 0:
            all_order_sku_is_topn.append(sku)
    return all_order_sku_is_topn


def read_n_tolist(n):
    top_n_list = []
    counter = 0
    value_record = []
    with open('allsku.csv', newline='', encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            value = row[1]
            if counter >= n and value not in value_record:
                break

            if value not in value_record:
                counter += 1
                value_record.append(value)
            key = row[0]

            top_n_list.append(key)
    return top_n_list


if __name__ == '__main__':
    for i in range(5,115,5):
        run(i)

