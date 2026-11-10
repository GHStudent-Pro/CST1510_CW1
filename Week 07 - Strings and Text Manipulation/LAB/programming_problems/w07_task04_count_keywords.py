# Task 4: Count Keywords in Feedback

feedback = [
    "The product quality is great",
    "Fast delivery but poor quality",
    "Great product and great delivery",
    "Quality could be better"
]

keywords = ['great', 'quality', 'delivery']

all_feedback = " ".join(feedback).lower()

for keyword in keywords:
    print(f"{keyword}: {all_feedback.count(keyword)}")
