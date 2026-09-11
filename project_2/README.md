# Iris Flower Classification Using SVM

Iris Flower Classification is a machine learning project that classifies Iris flowers into different species using a Support Vector Machine (SVM) model.

## Features

- Classifies Iris flowers into different species
- Uses four flower measurements as input features
- Splits the dataset into training and testing sets
- Applies feature scaling using StandardScaler
- Uses an SVM classifier with an RBF kernel
- Evaluates the model using accuracy
- Generates a classification report
- Generates a confusion matrix

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Support Vector Machine (SVM)
- StandardScaler

## How It Works

The model uses four measurements of Iris flowers:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The dataset is divided into **70% training data and 30% testing data** using stratified sampling.

The training features are scaled using `StandardScaler` so that the features are on a similar scale.

An SVM model with an **RBF kernel** is then trained on the scaled training data.

After training, the model predicts the species of flowers in the test dataset. The predictions are compared with the actual labels to evaluate the model's performance.

## Model Evaluation

The model performance is evaluated using:

- Accuracy
- Classification Report
- Confusion Matrix
