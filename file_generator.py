import date_generator as dg

dg.list_dates(dg.start_date)
n=dg.count

for i in range(1, n+1):
    filename = f"{i}.py"
    with open(filename, "w") as f:
        f.close()
    