from PIL import Image


#base_filename_string = 'bulb_exp000'
def create_image_filename_list(base_filename_string = 'bulb_exp00'):
    file_list = []
    for i in range(10, 38):
        file_name = base_filename_string + str(i) + '.png'
        file_list.append(file_name)
    return file_list

        

#img_file = 'test60001.png'
def convert_to_transparent(image_filename, cycle_number):
    img = Image.open(image_filename)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 64 and item[1] == 64 and item[2] == 64:
            newData.append((255, 255, 255, 0))
        else:
           newData.append(item)
           print(item)

    new_file_string = 'bulb_transparent' + str(cycle_number) + '.png'
    img.putdata(newData)
    img.save(new_file_string, "PNG")

file_list = create_image_filename_list()
print(file_list)

cycle_number = 10
for image_filename in file_list:
    convert_to_transparent(image_filename=image_filename, 
                           cycle_number=cycle_number)
    cycle_number += 1
