import requests
import sys

API_KEY="bb09998cf8e9178bd0184f02c712c27c"
WEATHER_API_KEY="bb09998cf8e9178bd0184f02c712c27c"  

def news(query="python",language="ru",page_size=10):
    url="https://newsapi.org/v2/everything"
    params={
        "q":query,
        "language":language,  
        "sortBy":"publishedAt",
        "pageSize":page_size,
        "apiKey":API_KEY,
    }
    try:
        response=requests.get(url,params=params,timeout=10)
        response.raise_for_status()
        data=response.json()
        if data["status"] != "ok":
            print(f"Ошибка API {data.get('message', 'Неизвестная ошибка')}")
            return None
        return data["articles"]
    except requests.exceptions.RequestException as e:
        print(f"Ошибка http {e}")
        return None

def get_weather(city):
    url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city,
        "appid":WEATHER_API_KEY,
        "units":"metric",
        "lang":"ru"
    }
    try:
        response=requests.get(url,params=params,timeout=5)
        
        if response.status_code == 401:
            return {"error": "неверный ключ", "status_code": 401}
        elif response.status_code == 404:
            return {"error": "город не найден", "status_code": 404}
        
        response.raise_for_status()
        data=response.json()
        
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
    except requests.exceptions.Timeout:
        return {"error": "таймаут 5 секунд", "status_code": 408}
    except requests.exceptions.RequestException as e:
        return {"error": f"ошибка запроса: {e}", "status_code": 500}

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "weather":
        if len(sys.argv) > 2:
            city = sys.argv[2]
        else:
            city = input("Введите город: ").strip()
        
        print(f"GET /weather?city={city}")
        result = get_weather(city)
        
        if "error" in result:
            print(f"Ошибка: {result['error']}")
        else:
            print(f"Город: {result['city']}")
            print(f"Температура: {result['temperature']}°C")
            print(f"Описание погоды: {result['description']}")
            print(f"Влажность: {result['humidity']}%")
            print(f"Ветер: {result['wind']} м/с")
        return
    

if __name__ == "__main__":
    main()