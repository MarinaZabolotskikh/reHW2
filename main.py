import re
import csv
from pprint import pprint

def open_contact_list(file_name: str):
    with open("phonebook_raw.csv", "r", encoding = "utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def get_new_contacts_list(contact_list: list):
    new_contacts_list = []
    for info in contacts_list:
        full_name = " ".join(info[:3]).split(' ')
        number = re.sub(r'(\+7|8)?[\(\s]*(\d+)[\)\s]*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})([\(\s]*(\w+)[\.\s]\s*(\d+)\)*)?',
               r'+7(\2)\3-\4-\5 \7.\8', info[5])
        result = [full_name[0], full_name[1], full_name[2], info[3], info[4],
                  number.strip(' .'), info[6]]
        new_contacts_list.append(result)
    return new_contacts_list

def unit_lists(contact_list: list):
    for contact in contact_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contact_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
    result_list = []
    for i in contact_list:
        if i not in result_list:
            result_list.append(i)
    return result_list

def write_contact_list(file_name, contact_list: list):
    with open(file_name, "w", encoding = "utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contact_list)

if __name__ == '__main__':
    contacts_list = open_contact_list("phonebook_raw.csv")
    new_contacts_list = get_new_contacts_list(contacts_list)
    result_list = unit_lists(new_contacts_list)
    write_contact_list("phonebook.csv", result_list)

