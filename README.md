<p align="center">
  <strong>COLLEGE OF ENGINEERING</strong><br>
  Department of Electronics Engineering<br>
  <strong>BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING</strong><br>
  <strong><em>1st Semester, AY 2026-2027</em></strong>
</p>

<h1 align="center">DATA PREPROCESSING CASE STUDY</h1>
<p align="center">
   <em>MExEE 402: MExE Elective 2</em>
</p>

### Members

| Name | Student Number | Section |
| :--- | :--- | :--- |
| Mendeja, Jeriza Mhay | | MEXE 4101 |
| Santiago, Kirsten | | MEXE 4101|

### Notebook links

| Chapter | MENDEJA, Jeriza Mhay| SANTIAGO, Kirsten|
| :--- | :--- | :--- |
| Ch1_2_3 |(https://colab.research.google.com/drive/11xehpsrqn9JxIIoqWu2lmDY16n17e2vd?usp=sharing) | [link](#) |
| Ch4 |(https://colab.research.google.com/drive/1s2B7yzj-R1blcwmq4ACz8th2M9KM0OOh?usp=sharing) | [link](#) |
| Ch5 |(https://colab.research.google.com/drive/1QuUONdlGkP_kiNfhqYksFf6nJt88bFsU?usp=sharing)| [link](#) |
| Ch6 |(https://colab.research.google.com/drive/1u2qrcEAzBzlc3S2UjMLdaQbNYJKgXOh0?usp=sharing) | [link](#) |
| Ch7 |(https://colab.research.google.com/drive/1Y4iga3lTRZ0YqsuzlnlUEAS9w-1WYCbM?usp=sharing) | [link](#) |
| Ch8 |(https://colab.research.google.com/drive/1tgFI2v62dOXUl1xZuu1yVJ6UR0h2tqS_?usp=sharing) | [link](#) |
| Ch9 |(https://colab.research.google.com/drive/1oZRGhEAj9Ng57pVFags5VZY9lo82oyka?usp=sharing)| [link](#) |

## What we learned

### Chapter 1
Chapter 1 showed us that we can't just throw raw data into a model right away. We have to clean it up first because real-world data is usually super messy or missing some parts. We honestly didn't expect that doing this prep work is actually a big deal for saving money and computer memory later, plus it just makes the final results way more accurate.

### Chapter 2
In Chapter 2, we learned how to actually bring datasets into Python and check what kind of data we have, like numbers or categories. It taught us to always print out the first few rows just to see what we're dealing with. The most surprising part was seeing how fast Pandas can do all the basic math. It spit out the average and max sales for thousands of games almost instantly.

### Chapter 3
Chapter 3 was about fixing missing values. Instead of just deleting a whole row because one thing is blank, We learned we can just fill it in with the average or the most common answer. We was really surprised that deleting things on purpose is sometimes a good thing. Like dropping a useless "Rank" column actually makes the data better and less distracting for the model.

### Chapter 4
Chapter 4 taught us about feature engineering, which is basically creating new columns from the stuff you already have to make the data more useful. Like changing a bunch of different temperatures into simple labels like "hot" or "cold". It was knowledgable to learn that computers completely ignore words like "Rainy". We actually have to turn those text words into 1s and 0s just so the machine can read them.

### Chapter 5
For Chapter 5, we talked about data scaling. If one column has really big numbers (like grades in the 90s) and another has small ones (like studying for 5 hours), the computer might get confused and think the big numbers are way more important. We was surprised by how easy it is to fix. We just shrink all the numbers to fit perfectly between 0 and 1. That way, the computer treats everything equally but the data still means the same thing.

### Chapter 6
Chapter 6 was about outliers. These are just weird numbers that don't match the rest of the group, like a student claiming they study 100 hours a week when everyone else studies 10. We learned how to use math like Z-scores and IQR to find them automatically. It really surprised us that one single bad number can completely mess up all your results if you forget to remove it or change it.

### Chapter 7


### Chapter 8


### Chapter 9

## Errors we found

### Chapter 3
* The Useless Import Mistake
<img width="1748" height="58" alt="image" src="https://github.com/user-attachments/assets/40fe4b00-7b18-4b0e-bd84-03b685f4c9f1" />
- We never actually use np anywhere in the rest of the code.

* The FutureWarning Mistake
<img width="1730" height="73" alt="image" src="https://github.com/user-attachments/assets/8a2f0ce2-7010-450d-85f7-0f65effac892" />
- This triggered a big warning message block because Pandas is changing how inplace=True works in future updates.

* The Useless Deletion Mistake
<img width="1749" height="78" alt="image" src="https://github.com/user-attachments/assets/d6b070bd-30cf-4af7-9ad1-dfed3559cba6" />
- It just filled all the empty publisher blanks in the cell right above this one. Because there are no empty spots left, this deletion line does absolutely nothing.

* The Impossible Decimal Year Mistake
<img width="1741" height="36" alt="image" src="https://github.com/user-attachments/assets/e9096d71-180c-4512-909d-eae9b204e6ad" />
- Earlier in the notebook, the describe() function showed that the mean for the Year column is 2006.4. A video game cannot be released in the year 2006.4.


### Chapter 4
* Ordinal Counting Mismatch
<img width="1800" height="288" alt="image" src="https://github.com/user-attachments/assets/d9baea31-37b9-479c-8dac-b689866df806" />
- Python programs almost always start counting at zero. As shown in the output box right below it, OrdinalEncoder actually changed the words to 0.0, 1.0, and 2.0. The lesson notes are contradicting what the code is actually doing.

### Chapter 5
* The Double Import Redundancy
<img width="1736" height="164" alt="image" src="https://github.com/user-attachments/assets/467d244a-3fda-4aed-8459-30a34610eb23" />
- In the code cell introducing MinMaxScaler, the exact same library import (from sklearn.preprocessing import MinMaxScaler) is typed twice in a row, separated by just one comment. Loading the exact same tool twice in the same cell is completely unnecessary.

### Chapter 6
* Z-Score Contradiction
<img width="1742" height="138" alt="image" src="https://github.com/user-attachments/assets/f4d17527-3fad-4abb-a961-654c620bef15" />
- The code outputs [], meaning the Z-score method found exactly zero outliers. The number 100 only reached a Z-score of 2.61, which is less than 3. However, the text immediately below it says, "In this example, the number 100 is a clear outlier..." and later claims "In this scenario, again, the number 100 is identified as an outlier". The Z-score method completely failed to catch it because the dataset is too small.

* Hiding Outlier Mistake
<img width="1740" height="98" alt="image" src="https://github.com/user-attachments/assets/83c16b59-1c7d-491b-a8ad-4dd5aabffef0" />
- The head() function defaults to showing only the first 5 rows of data. Because the dataset only has 8 numbers, and the outlier (100) is at the very end of the list, using .head() completely hides the outlier from view. This defeats the purpose of previewing the data to see the outlier problem.

### Chapter 7


### Chapter 8


### Chapter 9

## Note on AI tools

Say whether you used an AI tool, and what for. This is not a penalty.
Hiding it is.

## References

McKinney, W. (2021). Python for Data Analysis, 3rd ed. O'Reilly.
VanderPlas, J. Python Data Science Handbook.
Any other page or article you used.
