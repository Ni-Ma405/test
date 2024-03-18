num = int(input("Enter the number for which you want the multiplication table"))
limit = int(input ("Enter the limit up to which you want the multiplication table generated"))
print (f"multiplication table of {num}")

for i in range(1, limit + 1): 
    print (f"{num} x {i} = {num * i}")
