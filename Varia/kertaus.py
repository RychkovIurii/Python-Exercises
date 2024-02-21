import json

def label_to_grade(label):
    if label == "K5":
        return 5
    elif label == "H4":
        return 4
    elif label == "H3":
        return 3
    elif label == "T2":
        return 2
    else:
        return 1

def grade_to_label(grade):
    if grade == 5:
        return "K5"
    elif grade >= 4:
        return "H4"
    elif grade >= 3:
        return "H3"
    elif grade >= 2:
        return "T2"
    else:
        return "T1"

def analyze_grades(grades):
    subject_grades = {}
    passed_subjects = []
    for subject, grade in grades.items():
        if grade:
            if label_to_grade(grade) >= 3:
                passed_subjects.append(subject)
            subject_grades[subject] = grade
    
    if not subject_grades:
        print("Student doesn't have grades.")
        return

    max_grade = max([label_to_grade(grade) for grade in subject_grades.values()])
    min_grade = min([label_to_grade(grade) for grade in subject_grades.values()])
    average_grade = sum([label_to_grade(grade) for grade in subject_grades.values()]) / len(subject_grades)

    print("MAX grade:", grade_to_label(max_grade))
    print("MIN grade:", grade_to_label(min_grade))
    print("AVERAGE grade:", grade_to_label(average_grade))

    failed_subjects = []
    for subject, grade in grades.items():
        if grade == "null":
            failed_subjects.append(subject)

    for subject in failed_subjects:
        print("RASTI:", subject)


with open('kertaus.json', 'r') as kertaus:
    kertaus_dict = json.load(kertaus)

analyze_grades(kertaus_dict)