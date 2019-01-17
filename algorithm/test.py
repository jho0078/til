def my_languages(dic):
    key_list = []
    for value in dic.values():
        if value >= 60:
            key_list.append(value)
    key_list.sort(reverse=True)

    result = []
    for i in key_list:
        for key, value in dic.items():
            if i == value:
                result.append(key)
    return result

print(my_languages({"Java": 10, "Ruby": 67, "Python": 89, "PHP": 61}))
