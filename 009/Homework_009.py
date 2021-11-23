###################################################################################################
import os
import codecs
###################################################################################################
PATH = os.getcwd()
###################################################################################################


def create_file(full_path):
    with open(full_path, 'w'):
        pass


def get_data_of_file(full_path):
    result = []
    with codecs.open(full_path, 'r', "utf_8_sig") as file_object:
        for person in file_object.readlines():
            person_data_dict = {
                "name": person.split()[0],
                'surname': person.split()[1],
                'appraisals': list(map(int, person.split()[2:]))
            }
            result.append(person_data_dict)
        return result


def get_average_score_of_person(person_data_in: dict):
    try:
        average_score_out = round(sum(person_data_in['appraisals'])/len(person_data_in['appraisals']), 2)
        person_data_out = f"{person_data_in['surname']} {person_data_in['name'][0]}" \
                          f"{'.'.ljust(20 - len(person_data_in['surname']))}"
    except ZeroDivisionError:
        person_data_out = 'Error'
        average_score_out = 0
    return person_data_out, average_score_out


def get_data_to_file(full_path: str, data_in='', score_in=0):
    if os.path.isfile(full_path):
        with open(full_path, 'a') as file_person_data:
            if score_in > 0:
                file_person_data.write(f"{data_in}{score_in}\n")
            else:
                file_person_data.write(f"{data_in}\n")
    return


###############################################################################
# 1.
name_of_file_read01 = 'List_of_student.txt'
name_of_file_write01 = 'List_of_student_average.txt'
full_path_read01 = f"{PATH}/{name_of_file_read01}"
full_path_write01 = f"{PATH}/{name_of_file_write01}"
create_file(full_path_write01)
list_average_score_class01 = []
for data01 in get_data_of_file(full_path_read01):
    person_data01, average_score01 = get_average_score_of_person(data01)
    get_data_to_file(full_path=full_path_write01, data_in=person_data01, score_in=average_score01)
    list_average_score_class01.append(average_score01)
    if person_data01 == 'Error':
        print("|1.|>>>", person_data01)
    elif average_score01 < 5:
        print("|1.|>>>", person_data01, average_score01)
average_score_class01 = round(sum(list_average_score_class01)/len(list_average_score_class01), 2)
print("|1.|>>>", 'Средний бал по классу:'.ljust(44 - len('Средний бал по классу:')),
      average_score_class01)

###############################################################################
# 2.
name_of_file_create02 = 'New_file.txt'
full_path_create02 = f"{PATH}/{name_of_file_create02}"
create_file(full_path_create02)
for _ in range(1000):
    input_text02 = input('Введи текст:')
    get_data_to_file(full_path=full_path_create02, data_in=input_text02)
    if input_text02 == '':
        break

###############################################################################
