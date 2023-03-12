inp = input("what do you want to calc:  ").strip()

inp = inp.split()

if inp[1] == "+":
    print("{:.1f}".format(float(int(inp[0]) + int(inp[2])))) 
elif inp[1] == "-":
    print("{:.1f}".format(float(int(inp[0]) - int(inp[2])))) 
elif inp[1] == "*":
    print("{:.1f}".format(float(int(inp[0]) * int(inp[2])))) 
elif inp[1] == "/":
    print("{:.1f}".format(float(int(inp[0]) / int(inp[2])))) 
