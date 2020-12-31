# According to the incoming changes next year, this program will attempt to automate
# the tedious task of adding prefixes
import re
# This deals with the mobile prefixes
moovmobile = ['01', '02', '03', '40','41', '42', '43', '50', '51', '52', '53', '70', '71', '72', '73']
mtnmobile = ['04', '05', '06', '44', '45', '46', '54', '55', '56' , '64', '65', '66', '74', '75','76', '84', '85', '86', '94', '95', '96']
orangemobile = ['07', '08', '09', '47', '48', '49', '57', '58', '59', '67', '68', '69', '77', '78', '79', '87', '88', '89', '97' , '98']
moovfixe = ['208', '218', '228', '238']
mtnfixe = ['200', '210', '220', '230', '240', '300', '310', '320', '330', '340', '350', '360']
orangefixe = ['202', '203', '212', '213', '215', '217', '224', '225','234', '235', '243', '244', '245', '306', '316', '319', '327', '337', '347', '359', '368']
pattern = re.compile(r'CELL:([0-9]{8}|\+225.*)')

def flipp(matchobj):
   # This processes the cellphone numbers
    number = matchobj.group(1).replace(' ','')
    number = number.replace('+225','') 
    for string in orangemobile:
        if number[:2] == string:
            number = "07" + number
    for string in mtnmobile:
        if number[:2] == string:
            number = "05" + number
    for string in moovmobile:
        if number[:2] == string:
            number = "01" + number
    # This processes the fixed lines
    for string in orangefixe:
        if number[:3] == string:
            number = "27" + number
    for string in mtnfixe:
        if number[:3] == string:
            number = "25" + number
    for string in moovfixe:
        if number[:3] == string:
            number = "21" + number
    number = ' '.join(a+b for a,b in zip(number[::2], number[1::2]))
    number = "+225 " + number
    print(number)
    return number

# The VCF file usually can be exported from all phones
with open('contacts.vcf','r',encoding='utf-8') as f:
    contents = f.read()
    contents = re.sub(r'CELL:([0-9]{8}|\+225.*)',flipp,contents)

with open('contacts_output.vcf','w',encoding='utf-8') as of:
    of.write(contents)
    

        



