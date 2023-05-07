# https://www.codewars.com/kata/56baeae7022c16dd7400086e/train/python
# ugly code D:

import re

def phone(strng, num):
    if strng.count(str(num)) == 0:
        return f"Error => Not found: {num}"

    if strng.count(str(num)) > 1:
        return f"Error => Too many people: {num}"

    contacts = [contact for contact in strng.split('\n') if contact != '"' and len(contact) != 0]
    # loop through list
    i = 0
    for contact in contacts:
        phone_number = re.search(r"[+][0-9]{1,2}-[0-9]{3,3}-[0-9]{3,3}-[0-9]{4,4}", contact).group()
        if phone_number[1:] == num:

            break
        else:
            i += 1
    
    phone = num
    name_regex = r"<.*>"

    name = re.search(name_regex, contact).group().replace(">", "").replace("<", "")
    address_regex = re.sub(r"[+][0-9]{1,2}-[0-9]{3,3}-[0-9]{3,3}-[0-9]{4,4}", "", contact)
    address_regex = re.sub(r"<.*>", "", address_regex)
    tmp_address = re.sub(r"[^a-zA-Z0-9-_. ]", "", address_regex).split(" ")
    address = ""
    for text in tmp_address:
        if text == "_":
            address += " "
        elif len(text) > 0:
            address += text + " "
    address = address.replace("_", " ")
    return f"Phone => {phone.strip()}, Name => {name.strip()}, Address => {address.strip()}"

dr = """/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n"""

print(phone(dr, "1-908-512-2222"))