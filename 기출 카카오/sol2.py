from itertools import combinations


def solution(orders, course):
    temp2 = []
    for c_n in course:
        course_menu = {}

        for order_content in orders:
            new = []
            new = list(combinations(order_content, c_n))

            for j in range(len(new)):
                com_course = ''
                ordered_course = ''

                for i in range(len(new[j])):
                    com_course += new[j][i]

                temp = []
                for cha in com_course:
                    temp.append(cha)
                temp.sort()
                for o in temp:
                    ordered_course += o
                com_course = ordered_course

                if com_course != '':
                    try:
                        course_menu[com_course] += 1
                    except:
                        course_menu[com_course] = 1
        dic_max = 0
        if len(course_menu) != 0:
            dic_max = max(course_menu.values())
            temp = []
            if dic_max > 1:
                for keys in course_menu:
                    if course_menu[keys] == dic_max:
                        temp2.append(keys)
        # temp2.append(temp)
    temp2.sort()
    return temp2