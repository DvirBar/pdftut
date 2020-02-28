from pdftut import decrypter, merger
from data import numpages, chaporder, validateLookup
import random


file1 = decrypter(input("Please enter path for the pdf file: \n"), 1)
engfile = decrypter(input("Enter path for English version test: \n"), 2)
engpage = int(input("Enter number for the page you wish to extract from the English version: \n"))
chap_num = int(input("How many chapters would you like have? [6/8] \n"))


if chap_num == 6:
    chapters = list()
    temp_dict = {}
    # Split base chapters
    # Create a dictionary for each chapter and add it to the list
    start_chapt = None
    end_chapt = None
    for i in range(0, chap_num):
        temp_dict.update({'num': i,
            'start_page': numpages[chaporder[i]]["start"],
            'end_page': numpages[chaporder[i]]["end"],
            'chap_type': chaporder[i]
            })
        if temp_dict['num'] == 0:
            start_chapt = temp_dict['start_page'] - 1
        if temp_dict['num'] == 5:  
            if input("Would you like to extract the answer sheet and split it to a separate file? [y/n]") == "y":
                end_chapt = temp_dict['end_page'] + 4
            else:
                end_chapt = temp_dict['end_page'] + 1
        chapters.append(temp_dict.copy())
        temp_dict.clear()
    random.shuffle(chapters)
    merger(start_chapt, end_chapt, chapters, file1)

elif chap_num == 8:
    chapters = list()
    file2 = None
    temp_dict = {}
    # Split base chapters
    # Create a dictionary for each chapter and add it to the list
    start_chapt = None
    end_chapt = None
    answer = None
    for i in range(0, chap_num):
        if i < 6:
            temp_dict.update({'num': i,
                'start_page': numpages[chaporder[i]]["start"],
                'end_page': numpages[chaporder[i]]["end"],
                'chap_type': chaporder[i],
                })
            if i == 0:
                start_chapt = temp_dict['start_page'] - 1
            if i == 5:
                if input("Would you like to extract the answer sheet and split it to a separate file? [y/n]") == "y":
                    end_chapt = temp_dict['end_page'] + 4
                else:
                    end_chapt = temp_dict['end_page'] + 1
                file2 = decrypter(input("Please enter path for the second pdf file: \n"), 3)
        else:
            answer = input("Choose chapter: (enter '/info' for options information)")
            if answer == '/info':
                print("Information about chapter codes: \n" +
                "v1: Verbal - chapter 1 \n" +
                "v2: Verbal - chapter 2 \n" +
                "q1: Quantitive - chapter 1 \n" +
                "q2: Quantitive - chapter 2 \n" +
                "e1: English - chapter 1 \n" +
                "e2: English - chapter 2 \n")
                i -= 1
            elif validateLookup:
                temp_dict.update({'num': i,
                    'start_page': numpages[answer]["start"],
                    'end_page': numpages[answer]["end"],
                    })
            else: 
                print("Error: please enter a valid entry")
                i -= 1
        chapters.append(temp_dict.copy())
        temp_dict.clear()
    random.shuffle(chapters)
    merger(start_chapt, end_chapt, chapters, file1, engfile, engpage, file2)


else:
    print("Please enter either 6 or 8.")

#C:\Users\Dvir\Documents\simulations\psychometric_oct_2014.pdf
#C:\Users\Dvir\Documents\simulations\psychometric_dec_2014.pdf
#C:\Users\Dvir\Documents\simulations\1904-Pirsum-ENGLISH-muktan.pdf
