def single(single_numbers_):
    all_single_numbers = []
    for index , value in single_numbers_:
            all_single =  list(value.text.strip())
            if(len(all_single)==1):
                all_single.extend("*")
            all_single_numbers.extend(all_single)

    return all_single_numbers # returns all_single_numbers











