def towers_of_hanoi(n,A,C,B):
    if n==1:
        print("Disc" , n , "is moved from", A ,"to", C)
        return
    towers_of_hanoi(n-1,A,B,C)
    print("Disc", n , "is moved from", A, "to",C)
    towers_of_hanoi(n-1,B,C,A)

towers_of_hanoi(3,'A','C','B')
