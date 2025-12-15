import json
import csv

country_data = {
    "название": "Великобритания",
    "столица": "Лондон",
    "население": 89900000 
}

with open('country.json', 'w', encoding='utf-8') as file:
    json.dump(country_data, file, ensure_ascii=False, indent=2)

print("Файл country.json успешно создан!")

try:
    age_sum_by_city = {}  
    count_by_city = {}    
    salary_sum_by_position = {}  

    with open('employees_with_salary.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            city = row['Город']
            position = row['Должность']
            age = int(row['Возраст'])      
            salary = float(row['Зарплата'])  
            
            if city not in age_sum_by_city:
                age_sum_by_city[city] = age      
                count_by_city[city] = 1          
            else:
                age_sum_by_city[city] += age     
                count_by_city[city] += 1    

            if position not in salary_sum_by_position:
                salary_sum_by_position[position] = salary 
            else:
                salary_sum_by_position[position] += salary
    
    avg_age_by_city = {}  
    for city in age_sum_by_city:
        avg_age = age_sum_by_city[city] / count_by_city[city]
        
        avg_age_by_city[city] = round(avg_age)
    
    result = {
        "Средний_возраст_по_городам": avg_age_by_city,
        "Сумма_зарплат_по_должностям": salary_sum_by_position,
        "Количество_по_городам": count_by_city  
    }
    
    with open('stats.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
   
    print("Результат обработки данных:")
    print("Средний возраст по городам:")
    for city, avg_age in avg_age_by_city.items():
        print(f"  {city}: {avg_age} лет")
    print("\n Сумма зарплат по должностям:")
    for position, total_salary in salary_sum_by_position.items():
        print(f"  {position}: {total_salary:.2f} руб.") 
    
    print("\n Количество сотрудников по городам:")
    for city, count in count_by_city.items():
        print(f"  {city}: {count} чел.")

except FileNotFoundError:
    print("Ошибка: Файл 'employees_with_salary.csv' не найден!")
    print("Пожалуйста, убедитесь, что файл находится в той же папке, что и программа.")
    
except KeyError as e:
    print(f"Ошибка: В файле отсутствует необходимый столбец: {e}")
    print("Убедитесь, что в CSV-файле есть столбцы: Имя, Возраст, Город, Должность, Зарплата")
    
except ValueError as e:
    print(f"Ошибка преобразования данных: {e}")
    print("Проверьте, что в столбцах 'Возраст' и 'Зарплата' только числа")
    
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
    print("Проверьте формат данных в CSV-файле")
