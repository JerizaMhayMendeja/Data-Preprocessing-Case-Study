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

## Chapter 1
Chapter 1 showed me that we can't just throw raw data into a model right away. We have to clean it up first because real-world data is usually super messy or missing some parts. I honestly didn't expect that doing this prep work is actually a big deal for saving money and computer memory later, plus it just makes the final results way more accurate.

## Chapter 2
In Chapter 2, we learned how to actually bring datasets into Python and check what kind of data we have, like numbers or categories. It taught me to always print out the first few rows just to see what I'm dealing with. The most surprising part was seeing how fast Pandas can do all the basic math. It spit out the average and max sales for thousands of games almost instantly.

## Chapter 3
Chapter 3 was about fixing missing values. Instead of just deleting a whole row because one thing is blank, I learned we can just fill it in with the average or the most common answer. I was really surprised that deleting things on purpose is sometimes a good thing. Like dropping a useless "Rank" column actually makes the data better and less distracting for the model.

## Chapter 4
Chapter 4 taught me about feature engineering, which is basically creating new columns from the stuff you already have to make the data more useful. Like changing a bunch of different temperatures into simple labels like "hot" or "cold". It was crazy to learn that computers completely ignore words like "Rainy". We actually have to turn those text words into 1s and 0s just so the machine can read them.

## Chapter 5
For Chapter 5, we talked about data scaling. If one column has really big numbers (like grades in the 90s) and another has small ones (like studying for 5 hours), the computer might get confused and think the big numbers are way more important. I was surprised by how easy it is to fix. We just shrink all the numbers to fit perfectly between 0 and 1. That way, the computer treats everything equally but the data still means the same thing.

## Chapter 6
Chapter 6 was about outliers. These are just weird numbers that don't match the rest of the group, like a student claiming they study 100 hours a week when everyone else studies 10. We learned how to use math like Z-scores and IQR to find them automatically. It really surprised me that one single bad number can completely mess up all your results if you forget to remove it or change it.

## Errors we found

List any mistake you found in the original notebooks, and the correct version.
There are real ones in there. Finding them earns points.

## Note on AI tools

Say whether you used an AI tool, and what for. This is not a penalty.
Hiding it is.

## References

McKinney, W. (2021). Python for Data Analysis, 3rd ed. O'Reilly.
VanderPlas, J. Python Data Science Handbook.
Any other page or article you used.
