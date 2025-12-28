import os
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

class InvalidAnswerError(Exception):
    """A custom exception for specific error conditions."""
    pass
def blind_auction():
    print(logo)
    print('WELCOME TO THE SECRET AUCTION PROGRAMME!!!')
    blind_auction_result = {

    }
    name = input("What is your name: \n").strip().upper()
    print(f"Hey {name}!!!! your bid for the art work is live!")
    print(f"{name} start bidding on this artwork now")
    while True:    
        
        try:
            bid = input(f"{name} What is your bid?\n")
            check_bid = bid.isdigit()
            if check_bid == False:
                raise ValueError(f"Ooops {name}, Data must be a float or an integer. Try again")
            elif check_bid == True:
                blind_auction_result[name] = float(bid)
                print(blind_auction_result)
            
        except ValueError as e:
            print(f"Error:{e}")
            continue
        while True:
            try:
                question = input("Are there other users who want to bid? \n").strip().upper()
                if question == "YES" or question == "Y":
                    os.system("cls")
                    name2 = input("What is your name: \n").strip().upper()
                    
                    print(f"Hey {name2}!!!! your bid for the art work is live!")
                    print(f"{name2} start bidding on this artwork now")
    
                    try:
                        
                        bid2 = input(f"{name2} What is your bid?\n")
                        check_bid2 = bid2.isdigit()
                        if check_bid2 == False:
                            raise ValueError(f"Ooops {name2}, Data must be a float or an integer. Try again")
                        elif check_bid2 == True:
                            blind_auction_result[name2] = float(bid2)
                            print(blind_auction_result)
                            
                    except ValueError as e:
                            print(f"Error:{e}")
                        
                elif question == "NO" or question == "N":
                        highest_bid = max(blind_auction_result.values())
                        for key,value in blind_auction_result.items(): 
                            if blind_auction_result[key] == highest_bid:
                                os.system("cls")
                                logo1 = '''
                                                ,,,,,,,,,,,,,                                                        ,,,,,,,,,,,,,            
                                            .;;;;;;;;;;;;;;;;;;;,.                                              .;;;;;;;;;;;;;;;;;;;,.
                                        .;;;;;;;;;;;;;;;;;;;;;;;;,                                            .;;;;;;;;;;;;;;;;;;;;;;;;,
                                        .;;;;;;;;;;;;;;;;;;;;;;;;;;;;.                                      .;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
                                        ;;;;;@;;;;;;;;;;;;;;;;;;;;;;;;' .............                       ;;;;;@;;;;;;;;;;;;;;;;;;;;;;;;' .............
                                        ;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'.................                    ;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'.................
                                        ;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'...................                  ;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;'...................
                                        `;;;;@;;;;;;;;;;;;;;;@;;;;;;;'.....................                 `;;;;@;;;;;;;;;;;;;;;@;;;;;;;'.....................
                                        `;;;;;;;;;;;;;;;;;;;@@;;;;;'..................;....                 `;;;;;;;;;;;;;;;;;;;@@;;;;;'..................;....
                                        `;;;;;;;;;;;;;;;;@@;;;;'....................;;.....                   `;;;;;;;;;;;;;;;;@@;;;;'....................;;.....
                                            `;;;;;;;;;;;;;@;;;;'...;.................;;....                      `;;;;;;;;;;;;;@;;;;'...;.................;;....
                                                `;;;;;;;;;;;;'   ...;;...............;.....                         `;;;;;;;;;;;;'   ...;;...............;.....
                                                `;;;;;;'          ...;;..................                            `;;;;;;'          ...;;..................
                                                    ;;              ..;...............                                   ;;              ..;...............
                                                    `                  ............                                      `                  ............
                                                    `                    ........                                        `                    ........
                                                    `                     .....                                          `                     .....
                                                    `                       '                                            `                       '
                                                    `                       '                                            `                       '
                                                    `                       '                                            `                       '
                                                    `                       `                                            `                       `
                                                    `                       `,                                           `                       `,
                                                    `                                                                    `
                                                    `                                                                    `
                                                    `.                                                                   `.
                                '''
                                print(logo1 * 3)
                                print(f"Congratulations {key}!!!")
                                print(f"Dear bidders, {key} has successfully secured the winning bid.")
                                break
                        print("Dear all, the bid summary is as follows:")
                        for index, (key,value) in enumerate(blind_auction_result.items(),start=1):
                            print(f"{index}. {key} - ${value:.2f}")
                        break
                    
                else:
                    raise InvalidAnswerError
                                            
            except InvalidAnswerError:
                print(f"Please enter a valid answer")
                continue
        break
            
if __name__  == "__main__":
    blind_auction()
