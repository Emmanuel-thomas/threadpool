import threading
import random

def save_file(file_number):
    with open(file_number, 'w') as f:
        f.write(file_number)
    print(f"File {file_number} saved successfully.")

def main():
    total_file_count = 5     #
    # Generate 5 random filenames
    filenames = set()
    while len(filenames) < total_file_count:
        filename_num = str(random.randint(1, 100))
        # if filename_num not in filenames
        filenames.add(f'{filename_num}.txt')

    thread_pool = []
    for file_number in filenames:
        t = threading.Thread(target=save_file, args=(file_number,))
        thread_pool.append(t)

    for t in thread_pool:
        t.start()

    for t in thread_pool:
        t.join()

if __name__ == '__main__':
    main()
