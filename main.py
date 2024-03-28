import numpy as np
import random

# Define lists of Georgian first names, last names, and subjects
georgian_first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ',
                        'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია',
                        'ემა', 'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან',
                        'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა',
                        'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']

georgian_last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური',
                       'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა',
                       'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია',
                       'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი',
                       'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე',
                       'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე',
                       'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']

subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ისტორია', 'გეოგრაფია']

# Generate student names
student_names = [((random.choice(georgian_first_names), random.choice(georgian_last_names))) for _ in range(100)]

# Generate random scores for each subject for each student
scores = np.random.randint(1, 101, size=(100, 5))

# Combine student names and scores into a single table
table = np.hstack((np.array(student_names), scores))

# Calculate average score for each student using NumPy
average_scores = np.mean(table[:, 2:].astype(int), axis=1)

# Find student with highest average score
highest_avg_index = np.argmax(average_scores)
student_highest_avg = table[highest_avg_index]
highest_avg_score = max(average_scores)

# Find student with highest and lowest math score
highest_math_score = 101  # Initialize to the highest possible score
lowest_math_score = 1  # Initialize to the lowest possible score
student_highest_math = None
student_lowest_math = None

for student in table:
    math_score = int(student[3])  # Convert math score to integer
    if math_score < highest_math_score:
        highest_math_score = math_score
        student_highest_math = student
    if math_score > lowest_math_score:
        lowest_math_score = math_score
        student_lowest_math = student

# Find average English score
english_scores = [int(student[4]) for student in table]  # Convert English scores to integers
english_avg = sum(english_scores) / len(english_scores)

# Find students with English score greater than average English score
students_higher_english = [student for student in table if int(student[4]) > english_avg]

# Print results
print(f"სტუდენტი უმაღლესი საშუალო ქულით: {student[0]}, {student[1]}, {highest_avg_score}")
print(f"მათემატიკის ყველაზე დაბალი ქულის მქონე მოსწავლე: {student_lowest_math[0]}, "
      f"{student_lowest_math[1]}, {student_lowest_math[3]} ქულა")
print(f"მათემატიკის უმაღლესი ქულის მქონე მოსწავლე: {student_lowest_math[0]}, "
      f"{student_lowest_math[1]}, {student_lowest_math[3]} ქულა")
print("ინგლისური ენის საშუალო ქულები:", english_avg)
print("სტუდენტი რომლის ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე: ")
for student in students_higher_english:
    print(f'{student[0]}, {student[1]}, ქულა: {student[4]}')


# Print the table
print('---------------------------------------------------------------------------------------------------------')
print("სტუდენტები\t                 \tქართული       \tმათემატიკა    \tინგლისური\t\tისტორია\t    \tგეოგრაფია")
print('---------------------------------------------------------------------------------------------------------')
for row in table:
    print('\t'.join(str(item).ljust(14) for item in row))
