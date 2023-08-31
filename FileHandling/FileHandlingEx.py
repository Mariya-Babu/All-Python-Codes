try:
    print("File Operations Example!")

    with open('file_1.txt','x'):
        print("File Created Successfully!")

except:
    print('File already exist')

finally:
    print("Programme Completed! Successfully!")
