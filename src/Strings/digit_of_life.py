bday = input('Enter your bday (YYYYMMDD or YYYYDDMM or MMDDYYYY): ')

dsum = 0

if len(bday) > 8:
        print("Entered date is too long")
else:
    list_str = [int(i) for i in bday]
    for d in list_str:
        dsum += d
        if dsum > 9:
            dsum = dsum % 10  + dsum // 10
            
print(dsum)
