# def day_of_week(day):
    # if day == 1:
    #     return "it's sunday"
    # elif day == 2:
    #     return "it's monday"
    # elif day == 3:
    #     return "it's tuesday"
    # elif day == 4:
    #     return "it's wednesday"
    # elif day == 5:
    #     return "it's thursday"
    # elif day == 6:
    #     return "it's friday"
    # elif day == 7:
    #     return "it's staturday"
    # else:
    #     return "not a valid day"
#     match day:
#         case 1:
#             return "it's sunday"
#         case 2:
#             return "it's monday"
#         case 3:
#             return "it's tuesday"
#         case 4:
#             return "it's wednesday"
#         case 5:
#             return "it's thursday"
#         case 6:
#             return "it's friday"
#         case 7:
#             return "it's saturday"
#         case _:
#             return "not a valid day"
# print(day_of_week(1))

# def is_weekend(day):
#     match day:
    #     case "sunday":
    #         return True
    #     case "monday":
    #         return False
    #     case "tuesday":
    #         return False
    #     case "wednesday":
    #         return False
    #     case "thursday":
    #         return False
    #     case "friday":
    #         return False
    #     case "saturday":
    #         return True
    #     case _:
    #         return False
        
def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return False
print(is_weekend("saturday"))
