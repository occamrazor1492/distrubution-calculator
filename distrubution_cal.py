import csv


def run(n):
    topn = read_n_tolist(n)
    dict_array = read_all_order()
    order_count = len(dict_array)
    result, result_test_dict_object = check_in_top_n(dict_array,topn)
    result_len = len(result)

    test(result_test_dict_object, topn)

    print(result_len," Order only contain", "Top", n, " SPU", "among ",order_count, "orders. The ration is ",result_len/order_count*100, "%" )
    # print(topn)
    # print("-------------")
    # for i in result:
    #     print(str(i))
    read_all_order_test(dict_array)


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
    all_order_sku_is_topn_object_test = []
    for order_dict in dict_array:
        flag = 0
        temp_list = list(order_dict.values())[0]
        for sku in temp_list:
            if sku not in top_n:
                flag += 1
        if flag == 0:
            all_order_sku_is_topn.append(order_dict.keys())
            all_order_sku_is_topn_object_test.append(order_dict)
    return all_order_sku_is_topn, all_order_sku_is_topn_object_test


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

def test(a_dict, topn):
    for i in a_dict:
        for k in i.values():
            for j in k:
                if j not in topn:
                    print("fuck you, you made mistakes")
                    break

def read_all_order_test(dict_obj):
    with open('test_all_order.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in dict_obj:
            for k in i.values():
                for j in k:
                    spamwriter.writerow([str(i.keys()), j])






if __name__ == '__main__':
    # for i in range(5,115,5):
    #     run(i)
    run(5)

