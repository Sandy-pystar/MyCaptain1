import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Mobile no.","Email-id"])

        writer.writerow(info_list)

if __name__== '__main__':
    cond=True
    student_num=1
    
    while(cond):
        student_info=input("Enter the #{} student information in this format-'Name ,Age ,Mobile no. ,Email-id ':-".format(student_num))
        
        student_info_list=student_info.split(',')

        print("\nThe entered information is:- \nName: {}\nAge: {}\nMobile no.: {}\nEmail-id: {}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        correction=input("Is the entered information correct (y/n): ")
        if correction=="y":
            write_into_csv(student_info_list)
            
            cond_check=input("Do you want information of more students(y/n):-")
            if cond_check=="y":
                cond=True
                student_num+=1
            elif cond_check=="n":
                cond=False
            
        elif correction=="n":
            print("Please re-enter the values!")
