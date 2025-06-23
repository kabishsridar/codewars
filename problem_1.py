def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3 # calculating the average
    if avg <= 100 and avg >= 90: # checks the range of the calculated score and returns the corresponding grade
        print("A")
    elif avg <= 90 and avg >= 80:
        print("B")
    elif avg <= 80 and avg >= 70:
        print("C")
    elif avg <= 70 and avg >= 60:
        print("D")
    elif avg <= 60 and avg >= 0:
        print("F")
get_grade(70, 60, 100)