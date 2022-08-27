import csv, re


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", newline='', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
def right_naming(contacts_list):
  for man in contacts_list:
    fio = re.findall('[А-Я]?[а-я]+', man[0]+man[1]+man[2])
    man[0:len(fio)] = fio

def formating_phone(contacts_list):
  for phone in contacts_list:
    pattern_phone = r'(\+7|8)\s*\(?(\d{3})\)?(\s|-)*(\d{3})(\s|-)*(\d{2})(\s|-)*(\d{2})'
    dob = r'\s*\(?доб\.\s(\d+)\)?'
    repl = r'+7(\2)\4-\6-\8'
    dob_r = r' доб.\9'
    if 'доб' in phone[5]:
      phone[5] = re.sub(pattern_phone + dob, repl + dob_r, phone[5])
    else:
      phone[5] = re.sub(pattern_phone, repl, phone[5])

def remove_dublicate(contacts_list):
  dist_man = {}
  for man in contacts_list:
    if man[0] in dist_man:
      for index, data in enumerate(man):
        if data:
          man[index] = data
        else:
          man[index] = dist_man[man[0]][index]
      contacts_list.remove(dist_man[man[0]])
    else:  
      dist_man[man[0]] = man


right_naming(contacts_list)
formating_phone(contacts_list)
remove_dublicate(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)