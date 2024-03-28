**Student Score Analysis README**

This Python script generates random student names along with their scores in Georgian, Mathematics, English, History, and Geography subjects. It then performs several analyses on the generated data. Below is an explanation of what the script does and how to use it:

**1. Dependencies:**
   - The script uses the NumPy library for numerical operations. Make sure you have NumPy installed (`pip install numpy`).

**2. Script Overview:**
   - The script starts by defining lists of Georgian first names, last names, and subjects.
   - It then generates random student names and scores for each subject.
   - Next, it calculates the average score for each student using NumPy.
   - It identifies the student with the highest average score and the students with scores higher than the average score in English.
   - Finally, it prints out various analysis results including the student with the highest average score, the student with the lowest math score, the student with the highest math score, the average English score, and the students with English scores higher than the average.

**3. How to Use:**
   - Simply run the script in a Python environment where NumPy is installed.
   - Adjust the number of students or subjects by changing the parameters in the script as needed.
   - The script will print the analysis results to the console.

**4. Example Output:**
   ```
   სტუდენტი უმაღლესი საშუალო ქულით: როინ, შელია, 90.64
   მათემატიკის ყველაზე დაბალი ქულის მქონე მოსწავლე: თეა, კევლიშვილი, ქულა: 1
   მათემატიკის უმაღლესი ქულის მქონე მოსწავლე: თეა, კევლიშვილი, ქულა: 1
   ინგლისური ენის საშუალო ქულები: 50.28
   სტუდენტი რომლის ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე: 
   ტატიანა, სალუქვაძე, ქულა: 92
   გოგუა, ბერიანიძე, ქულა: 95
   შენგელია, კევლიშვილი, ქულა: 91
   ლიანა, ჯოხაძე, ქულა: 76
   ლიპარტელიანი, იობიძე, ქულა: 86
   ---------------------------------------------------------------------------------------------------------
   სტუდენტები	                	ქართული       	მათემატიკა    	ინგლისური		ისტორია	   	გეოგრაფია
   ---------------------------------------------------------------------------------------------------------
   ...
   ```

**5. Note:**
   - The script generates random data for demonstration purposes. In a real-world scenario, you would replace the random data generation with actual data sources.

Feel free to modify the script according to your needs and contribute to its improvement!
