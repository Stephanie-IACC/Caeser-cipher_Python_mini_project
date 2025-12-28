def is_leap_year(year):
    '''Return True if a year is leap and Fals if it isn't
    '''
    if year % 4 != 0:
        return False
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    if  year % 100 == 0 and year % 400 == 0:
        return True
    
    if  year % 100 == 0 and year % 400 != 0:
        return False
    

if __name__ == "__main__":
    print(is_leap_year(2024))   