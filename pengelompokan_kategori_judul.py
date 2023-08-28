import sys


def main():
    # TODO list kategori di tambah seperlunya
    category={
        'entertainment':['youtube', 'game', 'music'],
        'politik':['dpr', 'ekonomi', 'negara'],
        'kriminal':['pembunuhan', 'pencurian', 'perampokan']
    }

    for category_name, categories_word in category.items():
        with open(f'{category_name}.txt', 'w') as f:
            for word in categories_word:
                f.writelines(word+'\n')
        
    # TODO ganti dengan loop: ambil judul dari file JSON hasil webscraping
    judul = input('Masukan judul berita anda: ').split(' ')

    print(f'{" ".join(judul)}\n Kategori: ')
    # TODO baca kategori dari file text
    for category_name, categories_word in category.items():
        for word in judul:
            for category_word in categories_word:
                if word == category_word:
                    print(f'{category_name}')



if __name__ == "__main__":
    main()