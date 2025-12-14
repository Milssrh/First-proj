import json
import csv
from collections import defaultdict

country_data = {
    "название": "Великобритания",
    "столица": "Лондон",
    "население": 899000000
}

with open('country.json', 'w', encoding='utf-8') as f:
    json.dump(country_data, f, ensure_ascii=False, indent=2)

try:
    age_sum_by_city = defaultdict(float)
    count_by_city = defaultdict(int)
    salary_sum_by_position = defaultdict(float)
    employee_count_by_city = defaultdict(int)

    with open('employees_with_salary.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            city = row['Город']
            position = row['Должность']
            age = int(row['Возраст'])
            salary = float(row['Зарплата'])
            
            age_sum_by_city[city] += age
            count_by_city[city] += 1
            
            salary_sum_by_position[position] += salary
            
            employee_count_by_city[city] += 1

    avg_age_by_city = {}
    for city in age_sum_by_city:
        avg_age = age_sum_by_city[city] / count_by_city[city]
        avg_age_by_city[city] = round(avg_age)

    result = {
        "Средний_возраст_по_городам": avg_age_by_city,
        "Сумма_зарплат_по_должностям": salary_sum_by_position,
        "Количество_по_городам": employee_count_by_city
    }
    
    with open('stats.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("\n Содержимое stats.json:")
    print(json.dumps(result, ensure_ascii=False, indent=2))

except FileNotFoundError:
    print("Ошибка: Файл employees_with_salary.csv не найден!")
except Exception as e:
    print(f"Произошла ошибка: {e}")