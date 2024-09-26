#For developing your own program, customize just the first line of the program "product".
#You can replace any product you want in the first line "bat","ball", etc & their prices.
#Make sure your products should be singular form and in between the double quotations.
#For an example- "Bat": 1200, you can replace it with "Badminton": 2000,
product={"Bat": 1200,"Ball": 250,"Stump": 400,"Jersey":550}
order=[]
item_num=[]
count=0
price=0
print("-----------------MANU--------------------")
for key, value in product.items():
    print(f"{key:<8}: {value:>6.2f} taka")
print("-----------------------------------------")
while True:
    item=input("Enter a product to add to cart or press 'q/Q' to quit: ").capitalize()
    if product.get(item) is not None:
        order.append(item)
        if item.find("s")==len(item)-1 or item.find("S")==len(item)-1:
            number=int(input(f"Ho many {item}es: "))
        else:
            number=int(input(f"Ho many {item}s: "))
        for num in range(number):
            price+=product.get(item)
        item_num.append(number)
    elif item.lower()=="q":
        break
    else:
        print(f"Sorry! {item} is not in the list.")
print("-------------CART---------------")
print()
print("You've orderded: ")
for item in order:
    repeat=item_num[count]
    print(end=" ")
    print(str(count+1)+"."+item+"("+str(repeat)+")")
    count+=1
print()
print(f"Total number of products: {len(order)}")
print(f"Total prices: {price:.2f} taka")
print("-----------------Thanks--------------------")
