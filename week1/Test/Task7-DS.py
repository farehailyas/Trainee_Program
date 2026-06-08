def top_three(scores):
    return sorted(list(set(scores)), reverse=True)[:3]

scores = [12 , 13 , 14 , 15 , 16 , 17, 12 , 12 , 12]
print(top_three(scores))
