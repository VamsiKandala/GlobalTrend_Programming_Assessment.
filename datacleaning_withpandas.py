import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('EmployeeData.csv')

# Function to clean the DataFrame
def clean_dataframe(df):
    # Handle missing values
    df['Name'].fillna('Unknown', inplace=True)
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Salary'].fillna(df['Salary'].mean(), inplace=True)
    df['JoiningDate'].fillna('Unknown', inplace=True)

    # Normalize numerical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Encode categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df

# Clean the DataFrame
cleaned_df = clean_dataframe(df)

# Print the cleaned DataFrame
print(cleaned_df)
