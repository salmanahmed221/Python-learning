import pandera as pa
from pandera.typing import Series
from datetime import datetime
import pandas as pd

# Data for 10 students
students_data = [
    {
        "roll_no": 1,
        "name": "Alice",
        "father": "Bob",
        "course": "Physics",
        "date_of_admission": "2023-01-10",
        "fee": 10000,
    },
    {
        "roll_no": 2,
        "name": "Brian",
        "father": "Steve",
        "course": "Chemistry",
        "date_of_admission": "2023-02-12",
        "fee": 11000,
    },
    {
        "roll_no": 3,
        "name": "Chloe",
        "father": "Tim",
        "course": "Biology",
        "date_of_admission": "2023-03-14",
        "fee": 12000,
    },
    {
        "roll_no": 4,
        "name": "David",
        "father": "Rick",
        "course": "Physics",
        "date_of_admission": "2023-04-10",
        "fee": 13000,
    },
    {
        "roll_no": 5,
        "name": "Eva",
        "father": "John",
        "course": "Physics",
        "date_of_admission": "2023-05-16",
        "fee": 14000,
    },
    {
        "roll_no": 6,
        "name": "Frank",
        "father": "Tom",
        "course": "Economics",
        "date_of_admission": "2023-06-21",
        "fee": 15000,
    },
    {
        "roll_no": 7,
        "name": "Grace",
        "father": "Harry",
        "course": "History",
        "date_of_admission": "2023-07-25",
        "fee": 16000,
    },
    {
        "roll_no": 8,
        "name": "Henry",
        "father": "Charles",
        "course": "Geography",
        "date_of_admission": "2023-08-17",
        "fee": 17000,
    },
    {
        "roll_no": 9,
        "name": "Isabel",
        "father": "Oliver",
        "course": "English",
        "date_of_admission": "2023-09-10",
        "fee": 18000,
    },
    {
        "roll_no": 10,
        "name": "Jack",
        "father": "Noah",
        "course": "Art",
        "date_of_admission": "2023-10-05",
        "fee": 19000,
    },
]

# Create the DataFrame
students_df = pd.DataFrame(students_data)

# Convert 'date_of_admission' to datetime
students_df["date_of_admission"] = pd.to_datetime(students_df["date_of_admission"])


for group in list(students_df.groupby(["course"])):
    print(group[0])
    print(group[1])
    print("================================")
