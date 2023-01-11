# Write a Python function to reverses a string if its length is a multiple of 4.

def multiply(multiply_of4):
    

    if len(multiply_of4) ==4==8==12==16==20==24==28==32==36==40  :
        print(list(reversed(multiply_of4)))

    else:
        print("try again :" ,end="\nLENGTH SIZE IS NOT MATCH TO OUR DATABASE.YOUR LENGTH SIZE IS :-->>")
        print(len(multiply_of4))



user_input=(input("enter list or string->>><<<::>>>PLEASE NOTE THAT YOUR ENTERED STRING IS MUST BE MULTIPLY OF 4 :"))

multiply(user_input)