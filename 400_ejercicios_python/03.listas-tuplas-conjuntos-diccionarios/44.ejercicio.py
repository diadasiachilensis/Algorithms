def mean_class(students):
    average=round(sum(students.values())/len(students),2)
    print(f"📘 El promedio del curso es: {average} ⭐")


students = {
    "Student_1": 6.5, "Student_2": 5.9, "Student_3": 6.2, "Student_4": 4.8, "Student_5": 5.5,
    "Student_6": 6.7, "Student_7": 5.1, "Student_8": 4.3, "Student_9": 6.0, "Student_10": 5.8,
    "Student_11": 6.3, "Student_12": 5.6, "Student_13": 6.9, "Student_14": 4.7, "Student_15": 5.2,
    "Student_16": 6.1, "Student_17": 5.0, "Student_18": 4.5, "Student_19": 6.8, "Student_20": 5.7,
    "Student_21": 6.4, "Student_22": 5.3, "Student_23": 6.6, "Student_24": 4.9, "Student_25": 5.4,
    "Student_26": 6.2, "Student_27": 5.9, "Student_28": 6.0, "Student_29": 4.6, "Student_30": 6.3,
    "Student_31": 5.1, "Student_32": 6.5, "Student_33": 6.8, "Student_34": 4.4, "Student_35": 5.0,
    "Student_36": 6.6, "Student_37": 5.7, "Student_38": 6.9, "Student_39": 4.8, "Student_40": 5.3,
    "Student_41": 6.1, "Student_42": 5.2, "Student_43": 6.4, "Student_44": 4.9, "Student_45": 5.8
}

mean_class(students)