import os
import time
from PIL import Image
import multiprocessing

def create_test_images():
    os.makedirs("images", exist_ok=True)
    
    sizes = [(1920, 1080), (2560, 1440), (1280, 720), (2048, 1536), (1600, 1200)]
    colors = [(73, 109, 137), (255, 100, 100), (100, 255, 100), (100, 100, 255), (255, 200, 100)]
    
    print("Создание тестовых изображений...")
    for i in range(20):
        size = sizes[i % len(sizes)]
        color = colors[i % len(colors)]
        img = Image.new('RGB', size, color=color)
        filename = f"images/img_{i}.jpg"
        img.save(filename)
        print(f"  Создано: {filename} ({size[0]}x{size[1]})")
    
    print()

def process_image(image_path, output_dir="processed"):
    try:
        img = Image.open(image_path)
        
        img = img.rotate(-90, expand=True)
        
        img = img.resize((800, 600), Image.LANCZOS)
        
        img = img.convert('L')
        
        base_name = os.path.basename(image_path)
        output_name = f"out_{base_name}"
        output_path = os.path.join(output_dir, output_name)
        img.save(output_path, 'JPEG', quality=95)
        
        return output_path
    except Exception as e:
        print(f"  Ошибка: {image_path} - {e}")
        return None

def process_sequential(images_list, output_dir):
    print("\nПоследовательная обработка...")
    results = []
    for img_path in images_list:
        results.append(process_image(img_path, output_dir))
    return results

def process_parallel(images_list, output_dir):
    print("\nПараллельная обработка...")
    with multiprocessing.Pool() as pool:
        args = [(img_path, output_dir) for img_path in images_list]
        return pool.starmap(process_image, args)

def main():
    print("ОБРАБОТКА ИЗОБРАЖЕНИЙ")
    
    os.makedirs("processed", exist_ok=True)
    
    create_test_images()
    
    images_list = []
    for file in os.listdir("images"):
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            images_list.append(os.path.join("images", file))
    
    if not images_list:
        print("Ошибка: Нет изображений для обработки!")
        return
    
    print(f"\nНайдено изображений: {len(images_list)}")
    
    print("РЕЖИМ 1: Последовательная обработка")
    
    start = time.time()
    results_seq = process_sequential(images_list, "processed")
    seq_time = time.time() - start
    
    print("РЕЖИМ 2: Параллельная обработка (multiprocessing.Pool)")
    
    start = time.time()
    results_par = process_parallel(images_list, "processed")
    par_time = time.time() - start
    
    print("РЕЗУЛЬТАТЫ")
    print(f"Последовательная обработка: {seq_time:.4f} сек")
    print(f"Параллельная обработка:     {par_time:.4f} сек")
    
    if par_time > 0:
        print(f"Ускорение: {seq_time/par_time:.2f}x")
    
    seq_success = len([r for r in results_seq if r])
    par_success = len([r for r in results_par if r])
    print(f"\nУспешно обработано (последовательно): {seq_success} из {len(images_list)}")
    print(f"Успешно обработано (параллельно):     {par_success} из {len(images_list)}")
    
    print("\nРезультаты сохранены в папке: processed/")

if __name__ == "__main__":
    main()
