sagol_sagol = [109, "rolan jay", "jadylyn", 463, "arl"]
choice = input(" sort or reverse :")

if choice == "sort":
    sagol_sagol.sort(key=str)
    print(sagol_sagol)
elif choice == "reverse":
    sagol_sagol.reverse()
    print(sagol_sagol)

