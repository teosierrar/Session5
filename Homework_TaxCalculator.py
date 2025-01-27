try:
    y = float(input("What is your gross income?"))
    numchild=int(input("How many children do you have?"))
    if y<float(1000):
        taxcut=.10
    elif float(2000) > y >= float(1000):
        taxcut=.12
    elif float(4000) > y >= float(2000):
        taxcut=.14
    else:
        taxcut=.18
    if numchild>=int(1) and y<float(2000):
        taxcut=(numchild*.1+taxcut)
    elif numchild>=int(1) and y>=float(2000):
        taxcut=(numchild*.05+taxcut)
    else:
        print("No extra tax cut from children")

except ValueError:
    print("only numerical values accepted")

print(f"Your taxes due are {y*taxcut}")
