def main():
    order = 3  # Orde matriks 3x3
    A = [list(map(int, input(f"Masukkan elemen baris {i + 1} matriks A (pisahkan dengan spasi): ").split())) for i in range(order)]
    B = [list(map(int, input(f"Masukkan elemen baris {i + 1} matriks B (pisahkan dengan spasi): ").split())) for i in range(order)]

    # Cek apakah perkalian bisa dilakukan
    if len(A[0]) == len(B):
        C = [[sum(A[i][k] * B[k][j] for k in range(order)) for j in range(order)] for i in range(order)]
        print("Hasil Perkalian Matriks A dan B:")
        for row in C:
            print(row)
    else:
        print("Perkalian matriks tidak dapat dilakukan.")

if __name__ == "__main__":
    main()

