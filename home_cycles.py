school_scores_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                    {'school_class': '4a', 'scores': [3,4,4,3,2]},
                    {'school_class': '5a', 'scores': [3,4,1,2,2]},
                    {'school_class': '6a', 'scores': [2,2,2,2,2]},
                    {'school_class': '7a', 'scores': [5,5,5,5,5,4,2]},
                    {'school_class': '8a', 'scores': [3,4,4,5,2]},
                    {'school_class': '9a', 'scores': [4,4,4,4,4]},
                    {'school_class': '10a', 'scores': [3,3,3,5,3]}
                      ]

def middle_count (scores_list):
    sum = 0
    for score in scores_list:
        sum += score
    middle = sum/len(scores_list)
    return middle

for clas in school_scores_list:
    middle_score_list = []
    clas['middle_score'] = middle_count(clas['scores'])
    middle_score_list.append(clas['middle_score'])

print (school_scores_list)
print (middle_count(middle_score_list))