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

#### The FutureWarning Mistake
<img width="1730" height="73" alt="image" src="https://github.com/user-attachments/assets/8a2f0ce2-7010-450d-85f7-0f65effac892" />
This triggered a big warning message block because Pandas is changing how inplace=True works in future updates.<br><br>
#### The Fix: <br><br>
To fix this error, we rewrite the code cleanly to update the column directly instead, like writing df['Year'] = df['Year'].fillna(df['Year'].mean()). />
<br><br>

#### The Impossible Decimal Year Mistake
<img width="1741" height="36" alt="image" src="https://github.com/user-attachments/assets/e9096d71-180c-4512-909d-eae9b204e6ad" />
Earlier in the notebook, the describe() function showed that the mean for the Year column is 2006.4. A video game cannot be released in the year 2006.4.<br><br>
#### The Fix:<br><br>
To fix this error, we change .mean() to .median() so it uses a whole number instead. /><br><br>


### Chapter 5

#### The Double Import Redundancy
<img width="1736" height="164" alt="image" src="https://github.com/user-attachments/assets/467d244a-3fda-4aed-8459-30a34610eb23" />
In the code cell introducing MinMaxScaler, the exact same library import (from sklearn.preprocessing import MinMaxScaler) is typed twice in a row, separated by just one comment. Loading the exact same tool twice in the same cell is completely unnecessary.:<br><br>
#### The Fix:
Just delete the code under the example data since it's redundant.<br><br>


### Chapter 6

#### Z-Score Contradiction
<img width="1742" height="138" alt="image" src="https://github.com/user-attachments/assets/f4d17527-3fad-4abb-a961-654c620bef15" />
The code outputs [], meaning the Z-score method found exactly zero outliers. The number 100 only reached a Z-score of 2.61, which is less than 3. However, the text immediately below it says, "In this example, the number 100 is a clear outlier..." and later claims "In this scenario, again, the number 100 is identified as an outlier". The Z-score method completely failed to catch it because the dataset is too small.<br><br>
* The Fix:<br><br>
The code uses a Z-score threshold of 3 which outputs zero outliers because the dataset is too small, even though the text claims the number 100 is an outlier. To fix this error, we lower the threshold to 2.5 (data[np.abs(z_scores) > 2.5]) so the method can successfully catch the outlier in the small dataset.<br><br>

* Hiding Outlier Mistake
<img width="1740" height="98" alt="image" src="https://github.com/user-attachments/assets/83c16b59-1c7d-491b-a8ad-4dd5aabffef0" />
The head() function defaults to showing only the first 5 rows of data. Because the dataset only has 8 numbers, and the outlier (100) is at the very end of the list, using .head() completely hides the outlier from view. This defeats the purpose of previewing the data to see the outlier problem.<br><br>
* The Fix:<br><br>
<img width="880" height="106" alt="image" src="https://github.com/user-attachments/assets/fb7dc152-88ca-4ef3-81ea-7d33884e1c85" /><br><br>

# Chapters 7 & 8
## Case Sensitivity
Although the code runs correctly, we should avoid using different cases for variables to prevent confusion, especially when troubleshooting and debugging.

### Chapter 7: Variable X Written in Uppercase
<p>In this example, the variable 'X' is written in uppercase.</p>
  <img width="828" alt="Chapter 7 code with uppercase variable X" src="https://github.com/user-attachments/assets/97c560ad-93b3-487b-88d9-dcbfe87f1124" />
  <img width="830" alt="Chapter 7 code example" src="https://github.com/user-attachments/assets/58efdd98-f83d-4425-b3cc-886c4bdfb3fa" />

#### Consistent Variable Naming
For consistency and readability, we should use either uppercase or lowercase for the same variable throughout the code.
  <img width="738" alt="Consistent variable naming example" src="https://github.com/user-attachments/assets/30ac8b12-a798-4937-960b-821c34de88e7" />
  <img width="707" alt="Corrected variable naming example" src="https://github.com/user-attachments/assets/4e5d5a1b-aedb-4ae2-a055-c3ba5cf9c9fe" />

### Chapter 8: Variable X Written in Uppercase
In this example, the variable 'X' is also written in uppercase.
  <img width="825" alt="Chapter 8 code with uppercase variable X" src="https://github.com/user-attachments/assets/33a84848-aea3-4953-82d3-fdf4025fe580" />
  <img width="823" alt="Chapter 8 code example" src="https://github.com/user-attachments/assets/0e39f69b-92d1-4a32-b0d3-b3b8768bd973" />

#### Consistent Variable Naming
To maintain consistency, variable names should follow the same capitalization throughout the program.
  <img width="787" alt="Consistent variable naming example" src="https://github.com/user-attachments/assets/05664df9-90b4-4cd5-b55e-d5012ef90c4f" />
  <img width="557" alt="Corrected variable naming example" src="https://github.com/user-attachments/assets/4f46d7ac-f4f6-4a0b-84ea-2364ffb10717" />

## 🤖Note on AI tools
AI tools such as ChatGPT, Gemini, and Claude were used during the creation of this repository and the Google Colab notebooks. For the Google Colab notebooks, AI tools were used to identify code errors and explain how to correct them. Furthermore, they were used to teach and explain unfamiliar instructions, functions, and their purposes to help us better understand how the code works. For the Question and Answer section, AI tools were used to paraphrase our answers, check their grammar, and organize them into a clear and concise form. Lastly, for this repository, AI tools were used to organize the formatting of the contents. 


## 🔗References

McKinney, W. (2021). Python for Data Analysis, 3rd ed. O'Reilly.
VanderPlas, J. Python Data Science Handbook.
