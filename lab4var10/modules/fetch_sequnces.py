from Bio import Entrez 
from Bio import SeqIO

#1.1 скачивание файлов
def download_records(term, n, out_file):
    Entrez.email = 'sk173619@gmail.com'
    handle = Entrez.esearch(db="nucleotide", term=term, retmax=n)
    ids = Entrez.read(handle)["IdList"]
    handle.close()
    try:
        records = []
        for id_ in ids:
            gb = Entrez.efetch(db="nucleotide", id=id_, rettype="gb", retmode="text")
            rec = SeqIO.read(gb, "genbank")
            gb.close()
            records.append(rec)
    except Exception as e:
        print(f"ошибка скачивания: {e}")
        return

    SeqIO.write(records, out_file, "genbank")
    print(f"Скачано {len(records)} записей в {out_file}")

#1.2объединение файлов
def unite_files(files, out_file):
    all_records = []
    for f in files:
        all_records.extend(list(SeqIO.parse(f, "genbank")))
    SeqIO.write(all_records, out_file, "genbank")
    print(f"Объединено {len(all_records)} записей в {out_file}")
    
#данные варианта
#1
download_records('"Prunus persica"[Organism] complete cds', 5, "prunus.gb")
download_records('"Arabidopsis thaliana"[Organism] complete cds', 5, "arabidopsis.gb")
unite_files(["prunus.gb", "arabidopsis.gb"], "all_species.gb")
