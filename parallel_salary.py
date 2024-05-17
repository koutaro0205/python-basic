import sys
import math
from module.func_salary import calcAmount

args = sys.argv

def parallel_salary(salary_list):
  for salaryStr in salary_list:
    result = calcAmount(int(salaryStr))
    allowance = result["allowance"]
    tax_amount = result["tax_amount"]
    print(f"給与:{salaryStr}、支給額:{math.floor(allowance)}、税額:{math.floor(tax_amount)}")

parallel_salary(args[1:len(args)])
