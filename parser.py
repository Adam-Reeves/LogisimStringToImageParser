file_name = input("Enter a file name: ")
file_name += ".img"
doc = open(file_name, "w")
to_convert = input("Enter string: ")
logi_string = "v2.0 raw\n"

convert_flag = True

count = 0

while convert_flag:
    try:
        # print(to_convert[count])
        if to_convert[count] == "\\":
            ascii_char = "0a"
            logi_string += ascii_char + "\n"
            count += 1
        else:
            ascii_char = str(hex(ord(to_convert[count])))
            ascii_char = ascii_char[2:]
            logi_string += ascii_char + "\n"
        count += 1
    except IndexError:
        convert_flag = False

doc.write(logi_string)