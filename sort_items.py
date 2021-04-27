import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path,file_name)

    with open(file_name, "r") as file:
        soubor = csv.reader(file, delimiter="\t")

        for line in soubor:
            row =[int(number)for number in line]




    return row

def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    with open(file_name, "r") as file:
        soubor = csv.reader(file, delimiter="\t")

        for idx, line  in enumerate(soubor):
            if idx == row_number:

                row =[int(number)for number in line]

    return  row

def selection_sort(number_array, direction = "ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """



    for i in range(len(number_array)):
        minimum = 1
        for j in range(i+1,len(number_array)):
            if direction == "ascending":
                if number_array[j] < number_array[minimum]:
                     minimum = j
                number_array[i], number_array[minimum] = number_array[minimum], number_array[i]
            elif direction == "descending":
                if number_array[j] > number_array[minimum]:
                    minimum = j
            number_array[i], number_array[minimum] = number_array[minimum], number_array[i]

    return number_array





def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    change = False

    for i in range(len(number_array)-1):
        for j in range(len(number_array)-i-1):
            if number_array[j] > number_array[j+1]:

                number_array[j],number_array[j+1] =number_array[j+1],number_array[j]
                change = True
        if not change:
            break

    return number_array


def main():

    hodnoty = read_row("numbers_one.csv")
    print(hodnoty)

    print(selection_sort(hodnoty))


    dalsi_hodnoty = read_rows("numbers_two.csv",1)
    print(dalsi_hodnoty)

    print(bubble_sort(dalsi_hodnoty))


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

