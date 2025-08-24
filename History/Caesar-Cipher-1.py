# # Caesar Cipher 1

# https://www.programiz.com/online-compiler/7G4YL9bR9NNM1

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

def start():
    string = input("(String) Please enter text to encode or decode: ")
    
    key = int(input("(Int) Please enter a key: "))
    
    print("1) Encode")
    print("2) Decode")
    type = int(input("(Int) Would you like to Encode or Decode the string?: "))
    
    print("1) Ceaser Cypher")
    print("2) My Custom Encryption")
    method = int(input("(Int) What method would you like to Encode or Decode the string with: "))
    
    if type == 1:
        encode(string, key, method)
    if type == 2:
        decode(string, key, method)

def encode(string, key, method):
    print("\nString: "+string)
    print("Key: "+str(key)+"\n")
    
    # Alphabet
    ref = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    
    if method == 1:
        print("Ceaser Cypher, encode\n")
        string_unpacked = [*string]
        print(string_unpacked)
        
        char_ilist = []
        schar_ilist = []
        rchar_ilist = []
        
        for i in string_unpacked:
            char_index = ref.index(i)
            print("0-25: "+str(char_index))
            char_ilist.append(char_index)
        
        print(char_ilist)
        
        for i in char_ilist:
            char_index = i+key
            print("0-25: "+str(char_index))
            schar_ilist.append(char_index)
            
        print(schar_ilist)
        
        for i in schar_ilist:
            char_result = ref[i]
            print(char_result)
            rchar_ilist.append(char_result)
        
        string_result = "".join(rchar_ilist)
        print(string_result)
        
    if method == 2:
        print("My Custom Encryption, encode\n")
    
def decode(string, key, method):
    print("\nString: "+string)
    print("Key: "+str(key)+"\n")
    
    # Alphabet
    ref = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    
    if method == 1:
        print("Ceaser Cypher, decode\n")
        string_unpacked = [*string]
        print(string_unpacked)
        
        char_ilist = []
        schar_ilist = []
        rchar_ilist = []
        
        for i in string_unpacked:
            char_index = ref.index(i)
            print("0-25: "+str(char_index))
            char_ilist.append(char_index)
        
        print(char_ilist)
        
        for i in char_ilist:
            char_index = i-key
            print("0-25: "+str(char_index))
            schar_ilist.append(char_index)
            
        print(schar_ilist)
        
        for i in schar_ilist:
            char_result = ref[i]
            print(char_result)
            rchar_ilist.append(char_result)
        
        string_result = "".join(rchar_ilist)
        print(string_result)
        
    if method == 2:
        print("My Custom Encryption, decode\n")

start()


