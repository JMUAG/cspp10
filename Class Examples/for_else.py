for i in range(5):
    if i > 8:
        print("breaking out of loop")
        break
    print(i)
else: #only happens if we did NOT break out of loop
    print("completed entire for loop")

print("end")