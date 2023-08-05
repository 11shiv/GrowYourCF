import pandas as pd
import numpy as np
import requests
import streamlit as st
from sklearn.neighbors import NearestNeighbors

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def getLength(n):
    return len(str(n))

def calculate_sum(number):
    total_sum = 0
    position = 0

    while number > 0:
        digit = number % 10
        total_sum += digit * (2 ** position)
        position += 1
        number //= 10

    return total_sum

def user_data(handle):
    res2 = requests.get("https://codeforces.com/api/user.status?handle=" + handle)

    if res2.json()['status'] == 'FAILED':
        return []

    df = pd.DataFrame(res2.json()['result'])

    mask = df['verdict'] == 'OK'
    new_df = df[mask]

    x = new_df['problem']

    solved_problem_by_user = []

    for i in x:
        solved_problem_by_user.append([i['contestId'], i['index'], i['name'], i['tags']])

    return solved_problem_by_user

def user_accuracy(handle):
    res2 = requests.get("https://codeforces.com/api/user.status?handle=" + handle)
    df1 = pd.DataFrame(res2.json()['result'])

    mask = df1['verdict'] == 'OK'
    x = df1[mask].shape[0]
    y = df1.shape[0]
    return x * 100 / y

def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    data = response.json()
    if 'result' in data and data['result']:
        return data['result'][0]
    else:
        return None

def get_user_rating(user_info):
    if 'rating' in user_info:
        return user_info['rating']
    else:
        return "Rating not available"

def problem_predictor(df, new_df, target_rating, target_points):
    df_distance_columns = ['rating', 'points']
    filter_columns = ['contestId', 'index']

    X_df = df[df_distance_columns].values
    X_new_df = new_df[filter_columns].values

    n_neighbors = 6

    knn = NearestNeighbors(n_neighbors=n_neighbors, metric='correlation')
    knn.fit(X_df)

    distances, indices = knn.kneighbors([[target_rating, target_points]])

    closest_points = df.iloc[indices[0]]

    filtered_closest_points = closest_points[~closest_points[filter_columns].apply(tuple, axis=1).isin(new_df[filter_columns].apply(tuple, axis=1))]

    points_not_in_new_df = df[~df[filter_columns].apply(tuple, axis=1).isin(new_df[filter_columns].apply(tuple, axis=1))]
    points_not_in_new_df = points_not_in_new_df.sample(n=min(n_neighbors, len(points_not_in_new_df)))

    final_8_points = pd.concat([filtered_closest_points, points_not_in_new_df])

    return final_8_points

def generate_problem_link(contest_id, index):
    return f"https://codeforces.com/contest/{contest_id}/problem/{index}"

def main():
    st.title("Codeforces Problem Predictor")

    handle = st.text_input("Enter Codeforces Handle:", "")

    if st.button("Get Recommendations"):
        if handle:
            user_info = get_user_info(handle)
            if user_info:
                user_rating = get_user_rating(user_info)
                user_accuracy_value = user_accuracy(handle)

                column_names = ['contestId', 'index', 'name', 'tags']
                new_df = pd.DataFrame(user_data(handle), columns=column_names)
                new_df = new_df.drop('tags', axis=1)

                st.write(f"User Rating: {user_rating}")
                st.write(f"User Accuracy: {user_accuracy_value:.2f}%")
                res = requests.get('https://codeforces.com/api/problemset.problems')
                df1 = pd.DataFrame(res.json()['result']['problems'])
                df2 = pd.DataFrame(res.json()['result']['problemStatistics'])
                df = pd.merge(df1, df2)
                df = df.dropna()
                column_to_drop = 'type'
                df = df.drop(columns=column_to_drop)
                df = df.reset_index(drop=True)

                for index in df.index :
                    if df['rating'][index] >= 2500:
                        df = df.drop(index)

                df = df.reset_index(drop=True)

                user_info = get_user_info(handle)
                user_rating = get_user_rating(user_info)

                your_problems = problem_predictor(df, new_df, user_rating , user_accuracy_value)

                st.write("Recommended Problems:")
                for index, row in your_problems.iterrows():
                    problem_link = generate_problem_link(row['contestId'], row['index'])
                    st.write(f"{row['name']} - {problem_link}")
            else:
                    st.write("User not found. Please enter a valid Codeforces handle.")

    st.write("-------------------------------------------------------")
    st.write("Instructions:")
    st.write("1. Enter your Codeforces handle.")
    st.write("2. Click the 'Get Recommendations' button.")
    st.write("3. The app will display your user information and recommended Codeforces problems.")
    st.write("4. There are some surprise problems .")
    st.write("-------------------------------------------------------")

if __name__ == "__main__":
    main()

