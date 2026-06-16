import pandas as pd

# 🔹 Step 1: Create initial student data as a dictionary
data = {
    'Name': ['Aryan', 'Alex', 'Riya', 'John', 'Meena', 'Rahul'],
    'Age': [20, 21, 19, 22, 20, 23],
    'Marks': [90, 85, 92, 78, 88, 95],
    'City': ['Delhi', 'London', 'Mumbai', 'New York', 'Chennai', 'Pune']
}

# 🔹 Step 2: Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print("📋 Original DataFrame created in code:")
print(df)

# 🔹 Step 3: Save to a CSV file
df.to_csv('student.csv', index=False)
print("\n💾 'student.csv' file saved successfully.")

# 🔹 Step 4: Read the CSV back
df2 = pd.read_csv('student.csv')
print("\n📂 Loaded data from 'student.csv':")
print(df2)

# 🔹 Step 5: Access specific value
print("\n👤 First student's name is:", df2.at[0, 'Name'])

# 🔹 Step 6: Create another DataFrame from df2 (optional)
df1 = pd.DataFrame(df2)
print("\n🆕 DataFrame created from loaded CSV:")
print(df1)

# 🔹 Step 7: Show first 2 rows
print("\n🔍 First 2 rows:")
print(df2.head(2))

# 🔹 Step 8: DataFrame info
print("\n📊 DataFrame Info:")
df2.info()

# 🔹 Step 9: Statistical summary
print("\n📈 Statistical Summary:")
print(df2.describe())

# 🔹 Step 10: View columns
print("\n🧾 All Names:")
print(df['Name'])

print("\n🧾 Names and Ages:")
print(df2[['Name', 'Age']])

# 🔹 Step 11: Access via loc[]
print("\n🎯 Name of 1st student using loc:")
print(df2.loc[0])

# 🔹 Step 12: Filter operations
print("\n🔎 Students older than 20:")
print(df[df['Age'] > 20])

print("\n🔎 Students aged exactly 20:")
print(df[df['Age'].isin([20])])

print("\n🔍 Using query for Age > 20:")
print(df.query('Age > 20'))

# 🔹 Step 13: Sorting and value counts
print("\n⬆️ Sorted by Age (ascending):")
print(df.sort_values(by='Age'))

print("\n🌍 Student count by City:")
print(df['City'].value_counts())

# ------------------------------------
# 🔸 FUNCTIONS AND TRANSFORMATIONS 🔸
# ------------------------------------

# 🔹 Step 14: Apply function (increase Age by 10%)
df2['Age'] = df['Age'].apply(lambda x: x * 1.1)
print("\n📈 Age after 10% increase:")
print(df2['Age'])

# 🔹 Step 15: map() function to capitalize names
df2['Name'] = df2['Name'].map(str.upper)
print("\n🔤 Names in UPPERCASE:")
print(df2['Name'])

# 🔹 Step 16: Add Grade column using apply + lambda
df2['Grade'] = df['Marks'].apply(lambda m: 'A' if m >= 90 else 'B')
print("\n🎓 DataFrame with Grades:")
print(df2)

# 🔹 Step 17: Crosstab example (City vs Name)
print("\n📊 Crosstab (City vs Name):")
print(pd.crosstab(df['City'], df['Name']))

# 🔹 Step 18: Replace city name
df2['City'] = df2['City'].replace({'Delhi': 'New Delhi'})
print("\n📍 City name 'Delhi' replaced with 'New Delhi':")
print(df2[['Name', 'City']])

# 🔹 Step 19: Add Rank column based on Marks
df['Rank'] = df['Marks'].rank(method='min', ascending=False)
print("\n🏆 Students Ranked by Marks:")
print(df)

# ------------------------------------
# 🔸 PIVOT TABLE DEMO 🔸
# ------------------------------------

# 🔹 Step 20: Create a pivot-style dataset
pivot_data = {
    'Name': ['Aryan', 'Alex', 'Riya', 'John', 'Meena', 'Aryan'],
    'City': ['Delhi', 'London', 'Mumbai', 'Delhi', 'London', 'Delhi'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Marks': [90, 85, 92, 78, 88, 95]
}

pivot_df = pd.DataFrame(pivot_data)

# 🔹 Step 21: Pivot Table: Average Marks by City and Subject
pivot_table = pivot_df.pivot_table(index='City', columns='Subject', values='Marks', aggfunc='mean')
print("\n📌 Pivot Table (Average Marks by City and Subject):")
print(pivot_table)
