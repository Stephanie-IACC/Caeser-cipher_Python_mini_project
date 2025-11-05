def calculate_love_score():
    name1 = input("Enter your name:").strip().upper()
    first_partner = list(name1)
    name2 = input("Enter your partners name:").strip().upper()
    second_partner = list(name2)
    test1 = ('T','R','U','E')
    test2 = ('L','O','V','E')

    total_count =[]
    for each_letter in test1:
        count = 0
        if each_letter in first_partner:
            count += 1  
        if each_letter in second_partner:
            count += 1               
        if first_partner.count(each_letter) > 1:
            count += 1
        if second_partner.count(each_letter) > 1:
            count += 1
            
        total_count.append(count)
        Total1 = sum(total_count)
        
        if count > 1: 
            print(f"{each_letter} occurs {count} times")
        if count == 0: 
            print(f"{each_letter} occurs {count} times")
        if count == 1: 
            print(f"{each_letter} occurs {count} time")

    print(f"Total={Total1}\n")

    total_count2 =[]
    for each_letter in test2:
        count = 0
        if each_letter in first_partner:
            count += 1  
        if each_letter in second_partner:
            count += 1                
        if first_partner.count(each_letter) > 1:
            count += 1
        if second_partner.count(each_letter) > 1:
            count += 1
            
        total_count2.append(count)
        Total2 = sum(total_count2) 
        if count > 1: 
            print(f"{each_letter} occurs {count} times")
        if count == 0: 
            print(f"{each_letter} occurs {count} times")
        if count == 1: 
            print(f"{each_letter} occurs {count} time")
    print(f"Total={Total2}\n")

    Love_score = str(Total1) + str(Total2)
    print(f"Love score={Love_score}")

if __name__ == "__main__":

    calculate_love_score()