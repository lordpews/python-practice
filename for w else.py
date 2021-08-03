koko = ["bharta", "bengan", "parantha"]
for items in koko:
    print(items)
    # break
    """
    When we use else with for loop the compiler will only go into the else block of code
    when two conditions are satisfied:

    1. The loop normally executed without any error. using break statements or jump statement will not execute
       the else block.
    2. We are trying to find an item that is not present inside the list or
       data structure on which we are implementing our loop.
       
    Except for these conditions, the program will ignore the else part of the program.
    For example, if we are just partially executing the loop using a break statement,
    then the else part will not execute.
    So, a break statement is a must if we do not want our compiler to execute the else part of the code.
    """
else:
    print("balle balle lmao")
