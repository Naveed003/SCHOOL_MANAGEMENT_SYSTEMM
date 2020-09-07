def hell():
    a="hello"
    def naveed():
        print(a)
        global b
        b=a
    
    naveed()
    print(b)


