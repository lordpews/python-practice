def searcher():
    import time

    poplu = "this task takes 4 sec to execute"
    time.sleep(4)

    while True:
        text = (yield)
        if text in poplu:
            print("your text is in poplu")
        else:
            print("lol noob haha no wrong text")


search = searcher()
next(search)
search.send("to")
input()
search.send("this task ")