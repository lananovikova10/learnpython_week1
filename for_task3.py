"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_scores = [{'school_class': '1a', 'scores': [5, 5, 5, 5, 5]},
                 {'school_class': '1b', 'scores': [3, 4, 5, 5, 5]},
                 {'school_class': '1c', 'scores': [3, 2, 4, 5, 2]}]

avg_school_scores = []

for class_scores in school_scores:
    for item in class_scores['scores']:
        avg_school_scores.append(item)

calculate_avg_school_scores = sum(avg_school_scores) / len(avg_school_scores)
print(calculate_avg_school_scores)

for class_scores in school_scores:
    avg_score = sum(class_scores['scores']) / len(class_scores['scores'])
    print(avg_score)
