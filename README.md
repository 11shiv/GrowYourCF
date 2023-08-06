# GrowYourCF

# Title: GrowYourCF : Codeforces Problem Recommendation

# Objective:
The main objective of the Codeforces Problem Predictor project is to help Codeforces users discover appropriate programming problems that match their skill level and interests. By providing their Codeforces handle, users can receive personalized problem recommendations based on their past performance and current rating.

# Tools and Technologies:
1. Python: Python is the programming language chosen for the project due to its versatility, ease of use, and extensive libraries for data manipulation and analysis.

2. Pandas: Pandas is a powerful data manipulation library in Python that allows efficient handling and analysis of tabular data structures, such as DataFrames.

3. NumPy: NumPy is a fundamental library for numerical computing in Python, providing support for arrays and matrices, making it suitable for mathematical operations.

4. Requests: The Requests library facilitates handling HTTP requests in Python, enabling the application to communicate with the Codeforces API.

5. Streamlit: Streamlit is an open-source Python library that enables developers to create web applications for data science and machine learning with ease.

6. Scikit-learn: Scikit-learn is a popular machine learning library in Python, offering various algorithms and tools for tasks like clustering, classification, regression, etc.

7. Codeforces API: The Codeforces API is an external service provided by Codeforces, a well-known competitive programming platform. It offers access to various data related to Codeforces, including user information, solved problems, contests, and more.

# Functionalities:

1. User Input:
   - The user provides their Codeforces handle as input to the application.

2. Fetch User Information:
   - The application makes an API call to the Codeforces API to retrieve essential user information for the given handle. This includes the user's rating, which indicates their current skill level on the platform.

3. Fetch User Solved Problems:
   - Another API call is made to fetch the user's solved problems from Codeforces. The application filters out successful submissions to get the list of problems the user has solved.

4. Calculate User Accuracy:
   - The user's accuracy is calculated as the ratio of successful submissions to total submissions.

5. Preprocess Problem Data:
   - The application fetches a list of Codeforces problems and associated statistics using the Codeforces API. The data is processed and prepared for problem recommendation.

6. Nearest Neighbors Algorithm:
   - The Scikit-learn library's Nearest Neighbors algorithm is used to find problems that closely match the user's current rating and accuracy. This algorithm calculates the similarity between the user and other problems in terms of rating and points.

7. Filter Recommended Problems:
   - The application filters out problems with high difficulty (rating >= 2500) to ensure that the recommended problems are appropriate for the user's skill level.

8. Surprise Problems:
   - The application adds a surprise element by presenting some unexpected problems in addition to the tailored recommendations.

9. Display Recommendations:
   - The application displays the user's Codeforces rating, accuracy, and a curated list of recommended Codeforces problems. Each recommended problem is accompanied by its name and a link to the respective contest page on Codeforces for further details.

10. User Interface:
   - The user interface for the application is created using Streamlit, allowing users to interact with the application through a web-based interface.

# Project Shots:
## 1 ![Screenshot 2023-08-06 034337](https://github.com/11shiv/GrowYourCF/assets/103626079/174d5139-56cd-463e-9d3d-3cd4df82e235)
## 2 ![Screenshot 2023-08-06 034454](https://github.com/11shiv/GrowYourCF/assets/103626079/419b1e54-628d-4824-9300-0f0c9df72775)
## 3 ![Screenshot 2023-08-06 034527](https://github.com/11shiv/GrowYourCF/assets/103626079/02e848f7-5b4b-4601-ade2-d0fc43bd6179)



# The Algorithm:
The algorithm used in the GrowYourCF project is the Nearest Neighbors algorithm, specifically the k-nearest neighbors (k-NN) algorithm. The k-NN algorithm is a simple and intuitive machine learning algorithm used for both classification and regression tasks.

In this project, the k-NN algorithm is employed to recommend Codeforces problems that closely match the user's current rating and accuracy. The algorithm identifies the k most similar problems based on their rating and points and recommends them to the user.

Here's how the algorithm works in the context of the Codeforces Problem Predictor project:

1. Data Preprocessing:
   - The application retrieves a list of Codeforces problems and their associated statistics using the Codeforces API. The data is organized and processed into a suitable format for the k-NN algorithm.

2. Feature Selection:
   - For the k-NN algorithm, the relevant features (attributes) are selected to represent each problem. In this case, the two key features chosen are the "rating" and "points" of the problem.

3. User's Data:
   - The user's Codeforces rating and accuracy are obtained from the Codeforces API.

4. Finding Nearest Neighbors:
   - The k-NN algorithm calculates the distance (similarity) between the user's rating and accuracy and all the problems' rating and points in the dataset. The similarity metric used in this project is the correlation metric.
   - The k-NN algorithm then selects the k problems with the closest similarity to the user's rating and accuracy.

5. Filtering and Recommendation:
   - The application filters out problems with high difficulty (rating >= 2500) to ensure that the recommended problems are appropriate for the user's skill level.
   - The algorithm then recommends the filtered set of k problems to the user as Codeforces problems that are well-suited to their skill level and interests.

6. Surprise Problems:
   - In addition to the tailored recommendations, the application also presents some surprise problems to offer users a variety of challenges and keep the experience interesting.

Overall, the k-NN algorithm in this project helps make personalized and relevant recommendations by identifying Codeforces problems that are most similar to the user's current skill level, as represented by their rating and accuracy. By using the correlation metric and filtering the results, the algorithm ensures that the recommended problems are well-matched to the user's proficiency, helping them find appropriate challenges to further improve their competitive programming skills on the Codeforces platform.





# Instructions for Users:
The application provides clear instructions for users to follow:
1. Enter your Codeforces handle.
2. Click the 'Get Recommendations' button.
3. The application will display your user information, including rating and accuracy, along with a list of recommended Codeforces problems based on your performance.

# Conclusion:
The Codeforces Problem Predictor is a useful tool for Codeforces users who want personalized recommendations for programming problems based on their skill level and performance. The application's user-friendly interface and accurate problem recommendations make it a valuable asset for competitive programmers seeking the right challenges to enhance their skills on the Codeforces platform.

# Certainly! Keep an eye out for updates and enhancements coming your way. Stay tuned for more exciting features and functionalities to be added in the future!
