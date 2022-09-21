# 54. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Run Length Encoding (RLE) Compression Algorithm in Python

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):   
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def display():
    # the original string
    our_message = "AuuBBBCCCCCCcccccCCCCCCCCCA"
    encoded_message=encode_message(our_message)
    
    print("Original string: [" + our_message + "]")
    print("Encoded string: [" + encoded_message +"]")
    
