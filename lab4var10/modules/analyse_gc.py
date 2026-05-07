from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#1.3 проверка количества cds
def count_cds(file):
    try:
        cds_count = 0
        for record in SeqIO.parse(file, "genbank"):
            for feature in record.features:
                if feature.type == "CDS":
                    cds_count += 1
        return cds_count
    except Exception as e:
        print(f"ошибка счета CDS: {e}")
        return

#2.сортировка по gc 
def sort_gc(input_file, output_file):
    try:
        records = list(SeqIO.parse(input_file, "genbank"))
        records.sort(key=lambda r: gc_fraction(r.seq))
    except Exception as e:
        print(f"ошибка сортировки по CDS: {e}")
        return

    with open(output_file, "w") as out:
        for r in records:
            gc = gc_fraction(r.seq)
            out.write(f"{r.id}: {r.description}, GC = {gc}\n")

#данные варианта
cds= count_cds("all_species.gb")
if cds >= 10:
    print(f"Условие соблюдается (всего {cds} CDS)")
else:
    print(f"CDS меньше 10 {cds}")
#2
sort_gc('all_species.gb','all_speciesfinal.gb')
with open ('all_speciesfinal.gb', 'r') as f:
    ff = f.read()
print(ff)