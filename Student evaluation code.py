"""
This program is design for the Student Grading System.
By : Yuvraj Yadav
Now, we will import some module which we will use in this program.
"""

import os
import datetime
from tabulate import tabulate


# below we have store the path of this program because it will help to store or write .txt file. 
path = os.getcwd()

"""
Below there are all the function which we will be using in this program.
"""

def calculate_overall_score(weight_of_all_assessment, student_marks):
    """
    This function calculate the overall score or average on the basis of Weight and mark which we enter.
    Here, we don't know that how many assessment are there so we make the list to a store the value product of mark and weight.
    And we use for loop to calculate the product of mark and weight, And append it to the list.
    In last, we will add all the item of the list which is average of all the mark.
    """
    if len(weight_of_all_assessment) == len(student_marks):
        a=[]
        for j in range (0, len(weight_of_all_assessment)):
            average_part = student_marks[j] * weight_of_all_assessment[j]
            a.append(average_part)
        average = sum(a)

        return average
    else:
        raise ValueError
    


def round_to_category(num) :
    """
    This function is for roundup the overall score as required.
    Here, Parameter is the raw overall score that we get after the calculation.
    And In last this function will roundup according to the requirement and return the roundup score.
    """

    # the list scores contain the mark that program accept as per as requirement
    scores = [0, 5, 15, 25, 32, 35, 38, 42, 45, 48, 52, 55, 58, 62, 65, 68, 72, 75, 78, 82, 85, 92, 100]
    Raw_score = num

    # here we create the empty list to store the difference to find the nearest mark that can be accepted
    difference = []
    for score in scores :
        difference.append(abs(score - Raw_score))
    min_difference = min(difference)
    if difference.count(min_difference) == 1 :
        index_of_scores = difference.index(min_difference)
    else :
        index_of_scores = difference.index(min_difference) + 1

    category = determine_category(scores[index_of_scores])

    return scores[index_of_scores],category


def determine_category(overall_score):

    """
    This function are for determine the category of student as mentioned in question or required for assessment.
    """
    if overall_score == 100:
        return "Aurum Standard"
    elif 82 <= overall_score <= 92:
        return "Upper First"
    elif 72 <= overall_score <= 78:
        return "First"
    elif 62 <= overall_score <= 68:
        return "2:1"
    elif 52 <= overall_score <= 58:
        return "2:2"
    elif 42 <= overall_score <= 48:
        return "Third"
    elif 32 <= overall_score <= 38:
        return "Condonable Fail"
    elif 5 <= overall_score <= 25:
        return "Fail"
    elif overall_score > 100 or overall_score < 0 :
        return "Ungraded"
    else :
        return "Defecit Opus"
    

def age_calculate(Date_of_Birth) :
    """
    This function is design to calculate the age of students.
    In this the parameter is date of birth.
    To use this function store dob in variable in string data type and write the variable name as parameter.
    And in last it return the age of student.
    """
    today_date = datetime.date.today()
    DOB = Date_of_Birth
    DOB_split = DOB.split("-")
	
	# Here we are using conditional statement because if dob month is greater than today then age is 1 year less else it is just (today year - birth year)
    if today_date.month < int(DOB_split[1]) or (today_date.month == int(DOB_split[1]) and today_date.day < int(DOB_split[2])) :
        age = today_date.year - int(DOB_split[0]) - 1
        return age
    else :
        age = today_date.year - int(DOB_split[0])
        return age
    
def Setup_module():
    """
    This function is for module configuration
    """
    Module_name = input("Please enter the module name : ")
    No_of_assessment = int(input("Please enter the number of assessment that the module have : "))
    name_of_all_assessment = []
    weight_of_all_assessment = []
    """
    Here, we are using loop for asking user to enter assessment name and weight.
    and in last we append it on list which we created above.
    """
    for i in range(1, No_of_assessment + 1):
        assessment_name = input(f"Please enter the name of assessment {i} : ")
        name_of_all_assessment.append(assessment_name)
        weight =input(f"Please enter the weight of assessment {i} ({assessment_name}), weight should be in percentage (0-100) and don't write \'%\' symbol : ")
        try:
            weight_in_num = int(weight)/100
            weight_of_all_assessment.append(weight_in_num)
        except:
            print("Error")
            return ValueError

    
    if sum(weight_of_all_assessment) == 1 :
        print("Module configuration complete.")
        return weight_of_all_assessment
    else:
        print("Error")
        return ValueError
    

def advanced(file_name,weight_of_all_assessment):
    
        headers = ["UID", "Name", "D.o.B", "Age", "Raw Score","Rounded Score","Category"]
        students_data =[]
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    detail = line.strip()
                    student_detail = detail.split(",")
                    student_ID = int(student_detail [0])
                    name = student_detail [1]
                    DOB = student_detail[2]
                    age = age_calculate(DOB)
                    score_string = student_detail[3:]
                    score = []
                    try:
                        for p in range (len(score_string)):
                            new_score = int(score_string[p])
                            score.append(new_score)
                    except ValueError :
                        raise ValueError
                    
                    weight = weight_of_all_assessment
                    if len(score) == len(weight):
                        raw_overall_score = calculate_overall_score(weight, score)
                        roundup= round_to_category(raw_overall_score)
                        roundup_score = roundup[0]
                        category = roundup[1]
                        student_details = [student_ID,name,DOB, age, raw_overall_score, roundup_score, category]
                        students_data.append(student_details)
                    elif len(score) > len(weight) or len(score) < len(weight):
                        raise IndexError
                    else:
                        print("Error")

        
        
            if len(score) == len(weight):
                students_data.sort()
                students_table = tabulate(students_data, headers)
                student_file = open("students.txt","w")
                student_file.write(students_table)
                student_file.close()
                return students_table
            
            else:
                student_file = open("students.txt","w")
                student_file.write("Invalid data please try again")
                student_file.close()
                raise IndexError
            

        except FileNotFoundError:
            raise FileNotFoundError
        



def main():
    # we are printiing below line --- just to separate path of program and program.

    # Welcome Message
    print("""Welcome, This program is design for the Student Grading System.
    First, let's set up the module configuration.\n""")

    
    user_choice = input("Do you want to configure a module ? (y/n) : ")
    if user_choice == "y" :

        weight_of_all_assessment = Setup_module()

        if weight_of_all_assessment != ValueError :
            print("How would like to proceed ?")
            user_choice = int(input("Do you want to (1) input manually or (2) load from file ? : "))

            if user_choice == 1 :
                # initilize
                raw_score_of_all_students = []
                roundup_overall_score_of_all_students = []
                category_of_all_students = []
                student_id = 0
                # for Table 
                headers = ["UID", "Name", "D.o.B", "Age", "Raw Score","Rounded Score","Category"]
                data_of_all_students = []
                
                # student detail 
                while(student_id != "end"):
                    student_id = input("Please enter student ID (student ID should must be 2 digit number or enter \'end\' to fihish) : ")
                    if student_id == "end":
                        break
                    try:
                        Student_ID = int(student_id)
                    except:
                        print("Error")
                        print("The input you entered was invalid")
                    student_name = input("Please enter student name : ")
                    student_DOB = input("Please enter student date of birth (YYYY-MM-DD) : ")
                    DOB_split = student_DOB.split("-")
	
                    try:
                        month = int(DOB_split[1])
                        year = int(DOB_split[0])
                        day = int(DOB_split[2])
                    except:
                        print("Error")
                        print("The input you entered was invalid")
                    student_marks = []
                    for j in range (1, len(weight_of_all_assessment)+1) :
                        mark = input(f"Please enter the mark of assessment{[j]} : ")
                        try:
                            score = int(mark)
                            student_marks.append(score)
                            
                        except ValueError:
                            print("ValueError")
                            print("The input you entered was invalid")

                    score = calculate_overall_score(weight_of_all_assessment,student_marks)
                    if score != ValueError:
                        raw_score_of_all_students.append(score)
                        overall = round_to_category(score)
                        overall_score = overall[0]
                        roundup_overall_score_of_all_students.append(overall_score)
                        category_of_student = overall[1]
                        category_of_all_students.append(category_of_student)
                        student_age = age_calculate(student_DOB)
                        student_data = [student_id, student_name, student_DOB,student_age, score, overall_score, category_of_student]
                        data_of_all_students.append(student_data)

                    else :
                        print(ValueError)


                data_of_all_students.sort()
                students_table = tabulate(data_of_all_students, headers)
                student_file = open("students.txt","w")
                student_file.write(students_table)
                student_file.close()
                print(students_table)

            elif user_choice == 2 :
                path = os.getcwd
                path_file = os.listdir()
                print(path_file)
                file_name = (input("Enter the file name from above file : "))
                students_table = advanced(file_name,weight_of_all_assessment)
                print(students_table)
                student_file = open("student detail.txt","w")
                student_file.write(students_table)
                student_file.close()
                

            else:
                print("""Please try again and enter corect number
                Thank You""")

        else:
            print("Please, Try again")
        

    elif user_choice == "n":
        print("How would like to proceed ?")
        user_choice = int(input("Do you want to (1) input manually or (2) load from file ? : "))
        if user_choice == 1:
            headers = ["UID", "Name", "D.o.B", "Age", "Raw Score","Rounded Score","Category"]
            data_of_all_students = []
            weight_of_all_assessment = [0.10,0.20,0.30,0.40]
            No_of_assessment = 4
            raw_score_of_all_students = []
            roundup_overall_score_of_all_students = []
            category_of_all_students = []
            student_id = 0
            while(student_id != "end"):
                student_id = input("Please enter student ID (student ID should must be 2 digit number or enter \'end\' to fihish) : ")
                if student_id == "end":
                    break
                student_name = input("Please enter student name : ")
                student_DOB = input("Please enter student date of birth (YYYY-MM-DD) : ")
                student_marks = []
                for j in range (1, 5) :
                    mark = float(input(f"Please enter the mark of assessment {j} : "))
                    student_marks.append(mark)
                score = calculate_overall_score(weight_of_all_assessment,student_marks)
                raw_score_of_all_students.append(score)
                overall = round_to_category(score)
                overall_score = overall[0]
                roundup_overall_score_of_all_students.append(overall_score)
                category_of_student = overall[1]
                category_of_all_students.append(category_of_student)
                student_age = age_calculate(student_DOB)
                student_data = [student_id, student_name, student_DOB,student_age, score, overall_score, category_of_student]
                data_of_all_students.append(student_data)


            data_of_all_students.sort()
            students_table = tabulate(data_of_all_students, headers)
            student_file = open("students.txt","w")
            student_file.write(students_table)
            student_file.close()
            print(students_table)

        elif user_choice == 2:
            weight_of_all_assessment = [0.10,0.20,0.30,0.40]
            path_file = os.listdir()
            print(path_file)
            file_name = (input("Enter the file name from above file : "))
            students_table = advanced(file_name,weight_of_all_assessment)
            print(students_table)
            student_file = open("student detail.txt","w")
            student_file.write(students_table)
            student_file.close()

        else:
            print("""Sorry, invalid input.
        Thank You.""")



    else:
        print("""Sorry, invalid input.
        Thank You.""")




if __name__ == "__main__" :
    main()  


