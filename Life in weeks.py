import math

def life_in_weeks(name, current_age):
    num_of_days_yr = int(365)
    num_of_days_wk = int(7)
    average_yr_lenth = (float(num_of_days_yr/num_of_days_wk))
    average_yr_lenthim = math.trunc(average_yr_lenth)
    max_yr_dperson = int(90)
    
    weeks_left = ((max_yr_dperson - current_age) * average_yr_lenthim)
    
    return f"{name}, you have {weeks_left} weeks left."
    
print(life_in_weeks("Tim",12))