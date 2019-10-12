import base64
import hashlib
#there are two main hash: one is the file hash when read from the binary and the second one is the file hash after the base64 encoding
def oddeven():
    with open("binary.txt", "r") as outfile:
        x = outfile.read()
        check = int(len(x))
    if (check % 2) == 0:
        print("Even")
        global dhck
        dhck = input("Choose a even number: ")        
    else:
        print("Odd")
        dhck = input("Choose a odd number: ")

#opens the file encodes with base64 and then saves the encodes to a txt file 
def spliting():
    with open(file_name, "rb") as outfile: 
        x = outfile.read()
        fullfile_hash = hashlib.sha256(x) #calculates the hash of the entire file to check the output in the end
        fullfile_hash = fullfile_hash.hexdigest()
        x_encoded = base64.b64encode(x)
        with open("binary.txt", "wb") as txtfile:
            txtfile.write(x_encoded)
 #accepts command from the user and splits the file        
    with open("binary.txt", "r") as outfile:
        x = outfile.read()
        file_hash = hashlib.sha256(x.encode()) #calculates the hash of the entire file of the b64 to check the output in the end
        base64_file_hash = file_hash.hexdigest()
        print(file_hash)
        #print(len(x))
        
        oddeven()
        global check
        check = int(len(x))
        global dhck
        dhck = int(dhck)
        chunks, chunk_size = int(len(x)), int(len(x)/int(dhck))
        res = [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        #print(res)
        

    #finds the hash of the res[] i.e. data of the individual file  and prints it into a new file
    hash_value = []
    for item in res:
        hash_result = hashlib.sha256(item.encode())
        hash_result = hash_result.hexdigest()
        hash_value.append(hash_result)

    with open("hash.txt", "w") as outfile:
        outfile.write(fullfile_hash + "\n" + base64_file_hash)

    for item in (hash_value):
        with open("hash.txt", "a") as outfile:
            
            outfile.write("\n" + item)
        
    #gets the hash of the data and created the name of the files
    small_hash = []
    for item in hash_value:
        sub_string = item[0:5]
        small_hash.append(sub_string)

    print(small_hash)
    #creates series of txt file
    file_list = []
    for item in small_hash:
        new_file = item + ".txt"
        file_list.append(new_file)
        with open(new_file, "w") as outfile:
            print("{} File Created....".format(item)) 

    #writing res[] data to the txt files created 
    for item, filename in zip(res, file_list):
        with open(filename, "w") as outfile:
            outfile.write(item + "\n")
    print("The file has been split succesfully")
    input()
    #encoding,spliting and hashing of files end here

def joining():
    #This starts the decoding process 
    #This reads the hash of the data and orders it into position
    first_two = []
    files_check = []
    with open("hash.txt", "r") as outfile:
        x = outfile.readlines()
        y = int(len(x))
        for data in x[0:2]:
            first_two.append(data.strip())
            
        for i in x[2:y]:
            files_check.append(i.strip())
        

    file_namesdecode = []
    #joins the files together
    for elements in files_check:
        print(elements)
        sub_string = elements[0:5]
        file_namesdecode.append(sub_string)
    #print(file_namesdecode)


    all_data = []
    b2_data = []
    all_together = []
    with open('binary2.txt', 'w') as outfile:
        for fname in file_namesdecode:
            with open(fname + '.txt') as infile:
                a = infile.read()
                all_data.append(a)
        for line in all_data:
            abc = line.strip().split('\n')
            b2_data.append(abc)
            print('done')
        for i in b2_data:
            all_together.extend(i)
        for i in all_together:
            i = str(i)
            outfile.write(i)
    
    with open('binary2.txt', 'r') as otf:
        check_file = otf.read()
        check_hash = hashlib.sha256(check_file.encode()) #calculates the hash of the entire file to check the output in the end
        check_hash = check_hash.hexdigest()
        if check_hash == first_two[1]:
            print("File is proper")
        else:
            print("File is tampered")

    def create_file():
    #Creates the new file with original base64
        with open("binary2.txt", "rb") as readtxtfile:
            txt_str = readtxtfile.read()  
            with open(file_name2, "wb") as infile:
                infile.write(base64.decodebytes(txt_str))

    create_file()


print("Welcome !")
print("This code allows you to split a file and then retrieve it later.\nThis makes it more secure for transferring secret information. ")
print("Do you want to split a file or retrieve a file?")
print("For splitting a file press 1 and for retrieving a file press 2")
a = input("Type here: ")
if a == "1":
    file_name = input("Specify the file and even the extension. for eg. 1.png: ")
    spliting()
elif a == "2":
    file_name2 = input("What do you want to save the file as? Also add the extension: ") 
    joining()
else:
    print("Doesn't seem to work. Try again")






