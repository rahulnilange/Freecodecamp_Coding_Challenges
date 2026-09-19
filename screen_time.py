
"""
Given an input array of seven integers, representing a 
week's time, where each integer is the amount of hours
spent on your phone that day, determine if it is too 
much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.

If the average of any three days in a row is greater 
than or equal to 8 hours, it’s too much.

If the average of the seven days is greater
than or equal to 6 hours, it's too much.

too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) should return False
too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) should return False
too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) should return False
too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) should return True
too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) should return True
too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) should return True
too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) should return True
"""

def too_much_screen_time(hours):
    check_1 = any(num >= 10 for num in hours)

    result = [sum(hours[i:i+3])/3 for i in range(0, len(hours) - 3)]
    check_2 = any(num > 8 for num in result)
    check_3 = (sum(hours) / 7) >= 6

    return check_1 or check_2 or check_3
