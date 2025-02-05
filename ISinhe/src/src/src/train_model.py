from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

df = pd.read_csv("../data/tweets_limpos.csv")
df["label"] = df["tweet_clean"].apply(lambda x: 1 if "feliz" in x else 0)

X_train, X_test, y_train, y_test = train_test_split(df["tweet_clean"], df["label"], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("nb", MultinomialNB())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
