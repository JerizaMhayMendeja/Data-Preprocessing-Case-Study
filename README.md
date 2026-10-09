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

### 👭Members

| Name | Student Number | Section |
| :--- | :--- | :--- |
| Mendeja, Jeriza Mhay | 23-05104 | MEXE 4101 |
| Santiago, Maria Kirsten E. | 23-02413 | MEXE 4101|

### 📚Notebook links

| Chapter | MENDEJA, Jeriza Mhay| SANTIAGO, Kirsten|
| :--- | :--- | :--- |
| Ch1_2_3 |(https://colab.research.google.com/drive/11xehpsrqn9JxIIoqWu2lmDY16n17e2vd?usp=sharing) | [link](#) |
| Ch4 |(https://colab.research.google.com/drive/1s2B7yzj-R1blcwmq4ACz8th2M9KM0OOh?usp=sharing) | [link](#) |
| Ch5 |(https://colab.research.google.com/drive/1QuUONdlGkP_kiNfhqYksFf6nJt88bFsU?usp=sharing)| [link](#) |
| Ch6 |(https://colab.research.google.com/drive/1u2qrcEAzBzlc3S2UjMLdaQbNYJKgXOh0?usp=sharing) | [link](#) |
| Ch7 |(https://colab.research.google.com/drive/1Y4iga3lTRZ0YqsuzlnlUEAS9w-1WYCbM?usp=sharing) | [link](#) |
| Ch8 |(https://colab.research.google.com/drive/1tgFI2v62dOXUl1xZuu1yVJ6UR0h2tqS_?usp=sharing) | [link](#) |
| Ch9 |(https://colab.research.google.com/drive/1oZRGhEAj9Ng57pVFags5VZY9lo82oyka?usp=sharing)| [link](#) |

## 💡What we learned

### Chapter 1_2_3
Through chapters 1-3, we learned that cleaning and preparing raw data is totally necessary because real-world information is always messy, and we were actually surprised to find out that doing this prep work saves computer memory and makes our final results way more accurate. Moving into Python, we figured out how to check data types and print the first few rows, and it was super cool to see how fast Pandas calculates averages and max sales for thousands of items almost instantly. We also learned how to fix missing pieces by filling them in with average values instead of deleting whole rows, and we were really surprised that throwing away useless columns on purpose actually makes the data better and less distracting for the model.

### Chapter 4
In Chapter 4, we learned all about feature engineering, which is basically just making brand new columns out of the info we already have to make our dataset way more useful. For example, instead of dealing with a bunch of confusing numbers for temperature, we can group them into super simple labels like "hot" or "cold" so it's easier to work with. The most mind-blowing part was finding out that computers are actually totally blind to normal words like "Rainy" or "Sunny", they don't get language at all. We literally have to convert all those text words into numbers, like 1s and 0s, just so the machine can finally read and understand what's going on.

### Chapter 5
Then, for Chapter 5, we learned about data scaling. If we have one column with really big numbers, like student test grades in the 90s, and another column with super small numbers, like hours spent studying from 1 to 5, the computer gets totally confused and thinks the big numbers are way more important just because they're bigger. We were super surprised by how easy it is to fix this problem, we just shrink all the numbers down so they all fit neatly between 0 and 1. That way, the computer is totally fair and treats every single column equally, but the actual meaning and relationship of the data doesn't change at all.

### Chapter 6
Chapter 6 was about outliers. These are just weird numbers that don't match the rest of the group, like a student claiming they study 100 hours a week when everyone else studies 10. We learned how to use math like Z-scores and IQR to find them automatically. It really surprised us that one single bad number can completely mess up all your results if you forget to remove it or change it.

### Chapter 7
Completing the Chapter 7 notebook taught us concepts regarding feature selection, which simply is determining the most relevant features for ML modelling, and the use of correlation to achieve this process. Furthermore, it made us recall different types of correlation which are the positive, negative, and zero correlation which also had coefficients. However, unlike correlation which was familiar to us since it has been taught since high school, this chapter taught us the basics of feature selection especially in terms of methods that are used under this process. The filter method essentially works by using statistical processes, the wrapper method works by trying different combinations of features and see what combinations perform well, and the embedded method selects important features while training the model by identifying which features are useful then, it reduces or removes those that are not. 

### Chapter 8
The Chapter 8 notebook introduced us all about Preprocessing Pipeline construction. It taught us that a preprocessing pipeline simply works like a conveyor belt where the data is loaded, goes through several stations for further processing as a preparation for ML models, then is unloaded, ready to be used by machine learning (ML) models. Moreover, this chapter showed us that, to build a preprocessing pipeline, imputation and scaling must be done first so as to handle missing data and standardize features.

### Chapter 9
Chapter 9, the final notebook. Unlike the previous chapters where steps for data preprocessing were introduced and taught, in this one, it made us integrate them and execute a complete data preprocessing operation. Aside from the steps taught from the previous chapters, chapter 9 taught us that preprocessing for features undergo a different process depending on what type or group of features they are. Numerical features go through imputation then scaling while categorical features go through imputation then one-hot encoding. This chapter also taught us that it is important to choose the appropriate plotting method or graph to present data depending on what they want to show or analyze. For example, bar plot or chart is used to compare categorical data while histogram shows data distribution.

## ❌Errors we found

### Chapter 3
* The Useless Import Mistake
<img width="1748" height="58" alt="image" src="https://github.com/user-attachments/assets/40fe4b00-7b18-4b0e-bd84-03b685f4c9f1" />
We never actually use np anywhere in the rest of the code.<br><br>
* The Fix: Just delete the cell entirely.<br><br>

* The FutureWarning Mistake
<img width="1730" height="73" alt="image" src="https://github.com/user-attachments/assets/8a2f0ce2-7010-450d-85f7-0f65effac892" />
This triggered a big warning message block because Pandas is changing how inplace=True works in future updates.<br><br>
* The Fix:<br><br>
<img width="879" height="84" alt="image" src="https://github.com/user-attachments/assets/35c26e98-ece6-43de-9f66-ace4a6e798ef" /><br><br>

* The Useless Deletion Mistake
<img width="1749" height="78" alt="image" src="https://github.com/user-attachments/assets/d6b070bd-30cf-4af7-9ad1-dfed3559cba6" />
It just filled all the empty publisher blanks in the cell right above this one. Because there are no empty spots left, this deletion line does absolutely nothing.<br><br>
* The Fix:<br><br>
<img width="851" height="44" alt="image" src="https://github.com/user-attachments/assets/d7034cc2-149e-4849-aba1-9ad51e159559" /><br><br>

* The Impossible Decimal Year Mistake
<img width="1741" height="36" alt="image" src="https://github.com/user-attachments/assets/e9096d71-180c-4512-909d-eae9b204e6ad" />
Earlier in the notebook, the describe() function showed that the mean for the Year column is 2006.4. A video game cannot be released in the year 2006.4.<br><br>
* The Fix:<br><br>
<img width="854" height="57" alt="image" src="https://github.com/user-attachments/assets/8b07bf5e-366a-4a30-9ddf-40672f80eac3" /><br><br>

### Chapter 4
* Ordinal Counting Mismatch
<img width="1800" height="288" alt="image" src="https://github.com/user-attachments/assets/d9baea31-37b9-479c-8dac-b689866df806" />
Python programs almost always start counting at zero. As shown in the output box right below it, OrdinalEncoder actually changed the words to 0.0, 1.0, and 2.0. The lesson notes are contradicting what the code is actually doing.<br><br>
* The Fix:<br><br>
<img width="812" height="135" alt="image" src="https://github.com/user-attachments/assets/47c51f91-4ed4-41e7-976b-ab2329d58b3c" /><br><br>


### Chapter 5
* The Double Import Redundancy
<img width="1736" height="164" alt="image" src="https://github.com/user-attachments/assets/467d244a-3fda-4aed-8459-30a34610eb23" />
In the code cell introducing MinMaxScaler, the exact same library import (from sklearn.preprocessing import MinMaxScaler) is typed twice in a row, separated by just one comment. Loading the exact same tool twice in the same cell is completely unnecessary.:<br><br>
* The Fix: Just delete the code under the example data since it's redundant.<br><br>


### Chapter 6
* Z-Score Contradiction
<img width="1742" height="138" alt="image" src="https://github.com/user-attachments/assets/f4d17527-3fad-4abb-a961-654c620bef15" />
The code outputs [], meaning the Z-score method found exactly zero outliers. The number 100 only reached a Z-score of 2.61, which is less than 3. However, the text immediately below it says, "In this example, the number 100 is a clear outlier..." and later claims "In this scenario, again, the number 100 is identified as an outlier". The Z-score method completely failed to catch it because the dataset is too small.<br><br>
* The Fix:<br><br>
<img width="869" height="90" alt="image" src="https://github.com/user-attachments/assets/3a833b03-d718-46fd-a77c-096ab4a198ef" /><br><br>



* Hiding Outlier Mistake
<img width="1740" height="98" alt="image" src="https://github.com/user-attachments/assets/83c16b59-1c7d-491b-a8ad-4dd5aabffef0" />
The head() function defaults to showing only the first 5 rows of data. Because the dataset only has 8 numbers, and the outlier (100) is at the very end of the list, using .head() completely hides the outlier from view. This defeats the purpose of previewing the data to see the outlier problem.<br><br>
* The Fix:<br><br>
<img width="880" height="106" alt="image" src="https://github.com/user-attachments/assets/fb7dc152-88ca-4ef3-81ea-7d33884e1c85" /><br><br>


### Chapter 7


### Chapter 8


### Chapter 9

## 🤖Note on AI tools

Say whether you used an AI tool, and what for. This is not a penalty.
Hiding it is.

## 🔗References

McKinney, W. (2021). Python for Data Analysis, 3rd ed. O'Reilly.
VanderPlas, J. Python Data Science Handbook.
