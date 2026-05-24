import os
import time
from PIL import Image
from multiprocessing import Pool
from pathlib import Path
from urllib.request import Request, urlopen

def download_your_images():
    os.makedirs("images", exist_ok=True)
    
    urls = [
        ("https://i.pinimg.com/1200x/29/fd/b0/29fdb0915539f739df8c8a4a773178fa.jpg", "img_0.jpg"),
        ("https://avatars.mds.yandex.net/i?id=046b62221019e5ef9711a04b798700d5e01b7829-5874640-images-thumbs&n=13", "img_1.jpg"),
        ("https://avatars.mds.yandex.net/i?id=cecdc713794e4fa2faf54f03733179ca7cd2a785-4467645-images-thumbs&n=13", "img_2.jpg")
    ]
    
    print("Попытка скачать ВАШИ изображения...")
    downloaded = 0
    
    for url, filename in urls:
        filepath = os.path.join("images", filename)
        
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            print(f"  Скачано: {filename}")
            downloaded += 1
        except Exception as e:
            print(f"  Не удалось скачать {filename}: {e}")
            print(f"    Ссылка: {url}")
    
    if downloaded == 0:
        print("\nНЕ УДАЛОСЬ СКАЧАТЬ ИЗОБРАЖЕНИЯ АВТОМАТИЧЕСКИ!")
        print("Сделайте вручную:")
        for i, (url, filename) in enumerate(urls):
            print(f"  {i+1}. Откройте в браузере: {url}")
            print(f"     Сохраните как: images/{filename}")
        print("\nПосле скачивания запустите программу снова.")
        
        print("\nСоздаю временные заглушки для демонстрации...")
        for i in range(3):
            img = Image.new('RGB', (800, 600), color=(150, 150, 150))
            img.save(f"images/img_{i}.jpg")
            print(f"  Создана заглушка: images/img_{i}.jpg")
    else:
        print(f"\nСкачано {downloaded} из 3 изображений")
    
    print()

def process_image(image_path, output_dir="processed"):
    try:
        img = Image.open(image_path)
        original_size = img.size
        print(f"  Обработка: {os.path.basename(image_path)} (размер: {original_size[0]}x{original_size[1]})")
        
        img = img.rotate(-90, expand=True)
        
        img = img.resize((800, 600), Image.LANCZOS)
        
        img = img.convert('L')
        
        base_name = os.path.basename(image_path)
        output_name = f"out_{base_name}"
        output_path = os.path.join(output_dir, output_name)
        
        img.save(output_path, 'JPEG', quality=95)
        print(f"    Сохранено: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"  Ошибка при обработке {image_path}: {e}")
        return None

def process_sequential(images_list, output_dir):
    print("\nНачинаю последовательную обработку...")
    results = []
    for i, img_path in enumerate(images_list, 1):
        print(f"\n[{i}/{len(images_list)}]")
        result = process_image(img_path, output_dir)
        results.append(result)
    return results

def process_parallel(images_list, output_dir):
    print("\nНачинаю параллельную обработку...")
    with Pool() as pool:
        args = [(img_path, output_dir) for img_path in images_list]
        results = pool.starmap(process_image, args)
    return results

def main():
    print("ПРОГРАММА ОБРАБОТКИ ВАШИХ ИЗОБРАЖЕНИЙ")
    
    os.makedirs("processed", exist_ok=True)
    os.makedirs("images", exist_ok=True)
    
    download_your_images()
    
    images_list = [str(p) for p in Path("images").glob("*.jpg")]
    
    if not images_list:
        print("Ошибка: Нет изображений для обработки!")
        return
    
    print(f"Найдено изображений: {len(images_list)}")
    
    print("РЕЖИМ 1: Последовательная обработка (без распараллеливания)")
    
    start_time = time.time()
    results_seq = process_sequential(images_list, "processed")
    sequential_time = time.time() - start_time
    
    processed_seq_count = len([r for r in results_seq if r])
    print(f"\nОбработано: {processed_seq_count} из {len(images_list)} изображений")
    print(f"Время выполнения: {sequential_time:.4f} секунд")
    
    print("РЕЖИМ 2: Параллельная обработка (multiprocessing.Pool)")
    
    start_time = time.time()
    results_par = process_parallel(images_list, "processed")
    parallel_time = time.time() - start_time
    
    processed_par_count = len([r for r in results_par if r])
    print(f"\nОбработано: {processed_par_count} из {len(images_list)} изображений")
    print(f"Время выполнения: {parallel_time:.4f} секунд")
    
    print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ")
    print(f"Последовательная обработка: {sequential_time:.4f} сек")
    print(f"Параллельная обработка:    {parallel_time:.4f} сек")
    
    if parallel_time > 0:
        speedup = sequential_time / parallel_time
        print(f"Ускорение: {speedup:.2f}x")
    
    print("\nРезультаты сохранены в папке: processed/")
    print("Файлы: out_img_0.jpg, out_img_1.jpg, out_img_2.jpg")
    print("\nГотово!")

if __name__ == "__main__":
    main()