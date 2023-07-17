import pandas as pd

import UserSchema

# バリデーション対象のデータフレームの作成
data = {
    "id": ["No_0001", "No_0002", "No_0003", "No_0004", "No_0005"],
    "age": [25, 27, 31, "45", 23],
    "income": [50000, 62000, 10000, 87000, 92000],
    "gender": ["male", "male", "female", "male", "female"],
    "job": ["engineer", "doctor", None, "engineer", "teacher"],
    "hoge": ["22", "33", "44", "55", "66"],
    "datetime": ["2023-07-17T12:39:29+0900", "2023-07-17T12:39:29+0900", "2023-07-17T12:39:29+0900", "2023-07-17T12:39:29+0900", "2023-07-17T12:39:29+0900"]
}

df = pd.DataFrame(data)

print(df.dtypes)
validated_df = UserSchema.UserSchema.validate(df)
print(validated_df.dtypes)
print(validated_df.head())