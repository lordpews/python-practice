list2 = ["paani","joos","chay","kaafi"]
# i=1
# for items in list2:
#     if i%2 !=0:
#         print(f"please buy {items}")
#     i= i+1
for index,item in enumerate(list2):
    if index%2==0:
        print(f"please buy {item}")