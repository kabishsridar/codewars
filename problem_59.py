"""
You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
"""
def most_money(students):
    if len(students) == 1:
        return students[0].name

    totals = []
    amounts = []

    for student in students:
        total = student.fives * 5 + student.tens * 10 + student.twenties * 20
        totals.append((student.name, total))
        amounts.append(total)

    max_amount = max(amounts)

    same_count = 0
    for amount in amounts:
        if amount == max_amount:
            same_count += 1

    if same_count == len(students):
        return "all"

    for name, total in totals:
        if total == max_amount:
            return name
