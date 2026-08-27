from sklearn.tree import DecisionTreeClassifier, export_text

# Dataset features: [Outlook (0: Sunny, 1: Overcast, 2: Rain),
#                   Humidity (0: Normal, 1: High)]
X = [
    [0, 1],  # Sunny, High
    [0, 0],  # Sunny, Normal
    [1, 1],  # Overcast, High
    [2, 0],  # Rain, Normal
    [2, 1],  # Rain, High
]

# Labels: Play Tennis (1 = Yes, 0 = No)
y = [0, 1, 1, 1, 0]

# Train the model
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)

# Predict for a new day: Sunny (0), Normal Humidity (0)
new_sample = [[0, 0]]
prediction = clf.predict(new_sample)

print("Prediction for [Sunny, Normal Humidity]:", "Play" if prediction[0] == 1 else "Do Not Play")

# Print the text representation of the decision tree rules
print("\nGenerated Tree Structure:")
print(export_text(clf, feature_names=["Outlook", "Humidity"]))