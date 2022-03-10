def printPattern(n):
    line_no = 1
    curr_star = 0
    line_no = 1
    while(line_no <= n ):
        if (curr_star < line_no):
            print("* ", end = "")
            curr_star += 1
            continue
        if (curr_star == line_no):
            print("")
            line_no += 1
            curr_star = 0
printPattern(7)
