import statistics


def display_main_menu():
    print("Enter some numbers seperated by commas (eg.5,67,32)")


def get_user_input():
    num_list=input("Enter some numbers: ")
    num_list=num_list.split(",")
    num_list=[float(num) for num in num_list]
    return num_list


def calc_average_temperature(list):
    average=sum(list)/len(list)
    return average


def calc_min_max_temperature(list):
    min_temp=min(list)
    max_temp=max(list)
    return min_temp,max_temp


def sort_temperature(list):
    sorted_list=sorted(list)
    return sorted_list


def calc_median_temp(list):
    median_temp=statistics.median(list)
    return median_temp


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average=calc_average_temperature(num_list)
    min_temp,max_temp=calc_min_max_temperature(num_list)
    sorted_list=sort_temperature(num_list)
    median_temp=calc_median_temp(num_list)
    print("Average = "+str(average))
    print("Min temperature = "+str(min_temp))
    print("Max temperature = "+str(max_temp))
    print("Sorted in ascending order = "+str(sorted_list))
    print("Median temperature = "+str(median_temp))

if __name__=="__main__":
    main()




