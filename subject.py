import sys

args = sys.argv
first_arg = int(args[1])
second_arg = int(args[2])
third_arg = int(args[3])

def is_passed(math_point, japanese_point, english_point) -> bool:
    total_point = math_point + japanese_point + english_point
    return (total_point >= 220 or (math_point >= 70 and japanese_point >= 70 and english_point >= 70)) and (math_point >= 50 and japanese_point >= 50 and english_point >= 50)

print("合格" if is_passed(first_arg, second_arg, third_arg) else "不合格")
