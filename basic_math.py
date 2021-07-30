#######################
# Basic Math          #
#######################


def get_greatest(number_list):
    number_list.sort()
    number_list.reverse()
    greatest_number = number_list[0]
    return greatest_number


def get_smallest(number_list):
    number_list.sort()
    samllest_number = number_list[0]
    return samllest_number


def get_median(number_list):
    a = 0
    for i in number_list:
       print(i)
       a += i
    median = a / int(len(number_list))
    return median


a = [95, 61, 96, 45, 27, 86, 33, 66, 4, 39]
get_greatest(a)
print(get_greatest(a))

# """
# 여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
# """


# def get_greatest(number_list):
#     """
#     주어진 리스트에서 가장 큰 숫자를 반환함

#         Parameters:
#             number_list (list): integer로 값으로만 구성된 list
#             ex - [10, 33, 22, 99, 33]

#         Returns:
#             greatest_number (int): parameter number_list 중 가장 큰 값

#         Examples:
#             >>> number_list = [39, 54, 32, 11, 99]
#             >>> import basic_math as bm
#             >>> bm.get_greatest(number_list)
#             99
#     """
#     greatest_number = None
#     return greatest_number


# def get_smallest(number_list):
#     """
#     주어진 리스트에서 제일 작은 숫자를 반환함

#         Parameters:
#             number_list (list): integer로 값으로만 구성된 list
#             ex - [10, 33, 22, 99, 33]

#         Returns:
#             smallest_number (int): parameter number_list 중 가장 작은 값

#         Examples:
#             >>> number_list = [39, 54, 32, 11, 99]
#             >>> import basic_math as bm
#             >>> bm.get_smallest(number_list)
#             11
#     """
#     smallest_number = None
#     return smallest_number



# def get_mean(number_list):
#     """
#     주어진 리스트 숫자들의 평균을 구함.

#         Parameters:
#             number_list (list): integer로 값으로만 구성된 list
#             ex - [10, 33, 22, 99, 33]

#         Returns:
#             mean (int): parameter number_list 숫자들의 평균

#         Examples:
#             >>> number_list = [39, 54, 32, 11, 99]
#             >>> import basic_math as bm
#             >>> bm.get_mean(number_list)
#             47
#     """
#     mean = None
#     return mean


# def get_median(number_list):
#     """
#     주어진 리스트 숫자들의 중간값을 구함.

#         Parameters:
#             number_list (list): integer로 값으로만 구성된 list
#             ex - [10, 33, 22, 99, 33]

#         Returns:
#             median (int): parameter number_list 숫자들의 중간값

#         Examples:
#             >>> number_list = [39, 54, 32, 11, 99]
#             >>> import basic_math as bm
#             >>> bm.get_median(number_list)
#             39
#             >>> number_list2 = [39, 54, 32, 11, 99, 5]
#             >>> bm.get_median(number_list2)
#             35.5
#     """
#     median = None
#     return median