# Pandas11

# 1 Problem 1 : Replace Employee ID with the Unique Identifier(	https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, on = 'id', how ='left')
    return df[['unique_id','name']]

# 2 Problem 2 : Students and Examinations	(https://leetcode.com/problems/students-and-examinations/ )

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    grouped = examinations.groupby(['student_id','subject_name']).size().reset_index(name = 'attended_exams')
    
    all_rows = pd.merge(students,subjects, how ='cross')

    result = pd.merge(all_rows, grouped, on = ['student_id','subject_name'], how ='left')
    result['attended_exams'] = result['attended_exams'].fillna(0)
    result.sort_values(by =['student_id','subject_name'], inplace = True)
    return result[['student_id','student_name','subject_name','attended_exams']]