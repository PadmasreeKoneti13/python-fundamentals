# scores = list(map(int, input().split()))
scores = [13,92,75,95,83,95,83,75,88]
highest = scores[0]
second_largest = scores[0]
for curr_score in scores:
    if curr_score > highest:
        second_largest = highest
        highest = curr_score
    elif curr_score < highest :
        if curr_score > second_largest and curr_score!=highest:
            second_largest = curr_score
print(highest)
print(second_largest)





