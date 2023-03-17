from bisect import bisect

income = 0 # your salary here
fed_ref = {
    "rates": [10, 12, 22, 24, 32, 35, 37]
    , "brackets": [11000, 44725, 95375, 182100, 231250, 578125]
}
state_ref = {
    "rates": [4, 4.5, 5.25, 5.5, 6.00, 6.85, 9.65, 10.3, 10.9]
    , "brackets": [8500, 11700, 13900, 80650, 215400, 1077550, 5000000, 25000000]
}
local_ref = {
    "rates": [3.078, 3.762, 3.819, 3.876]
    , "brackets": [21600, 45000, 90000]
}

def tax(income, rates, brackets, base_tax):
    i = bisect(brackets, income)
    if not i:
        return 0
    rate = rates[i]
    bracket = brackets[i-1]
    income_in_bracket = income - bracket
    tax_in_bracket = income_in_bracket * rate / 100
    total_tax = base_tax[i-1] + tax_in_bracket
    return total_tax

if __name__ == '__main__':
    # Code to calculate base tax
    for level in [fed_ref, state_ref, local_ref]:
        # base_tax is the maximum tax paid in each bracket
        base_tax = []
        for i, bracket in enumerate(level["brackets"]):
            if i == 0:
                val = bracket * level["rates"][i] / 100
            else:
                val = ((bracket - level["brackets"][i-1]) * level["rates"][i] / 100) + base_tax[-1]
            base_tax.append(val)
        level["base_tax"] = base_tax
        # print(base_tax)
    total_tax = 0
    for level in [fed_ref, state_ref, local_ref]:
        total_tax += tax(income=income, **level)
    social_security = 6.2 /100 * income
    total_tax += social_security
    print(f"Total Tax: {total_tax}")
    print(f"Net Pay: {income - total_tax}")
    print(f"Net Monthly Pay: {(income - total_tax)/12}")
