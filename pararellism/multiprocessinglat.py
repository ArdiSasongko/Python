import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    # Buat proses multiprocessing
    pool = multiprocessing.Pool()

    # Jalankan fungsi square secara paralel untuk setiap elemen dalam numbers
    results = pool.map(square, numbers)

    # Tunggu hingga semua proses selesai
    pool.close()
    pool.join()

    print(results)
