from Bio import SeqIO
from Bio.Seq import Seq
import os

def sequences_to_protein_fasta(filename): #IN1.fasta IN 2.fasta IN3.fasta
    results = []
    try:
        for record in SeqIO.parse(filename, "fasta"):
            results.append(str(record.seq))
        print(f"найдено последовательностей: {len(results)}")  
    except Exception as e:
        print(f"ошибка чтения файла: {e}")
        return
    
    if len(results) < 2:
        print('нет интронов либо пустой файл')
        return

    if len(results[0]) > 999:
        print('слишком большая последовательность')
        return 
    
    results_1 = results[0]

    try:
        for i in range(1,len(results)): #т.к. нумерация с 0
            results_1 = results_1.replace(results[i],'') #dna_s1.replace(old, new)

        results_1 = Seq(results_1)
        protein = str(results_1.translate(to_stop = True)) #до стоп кадона и остановить не включая его
        return protein

    except Exception as e: 
        print(f"ошибка, проверьте последовательность: {e}")

protein = sequences_to_protein_fasta('IN 2.fasta')
print(protein)
with open ('OUT 2.txt','r') as file:
    check = file.read()
print(check == protein)


protein = sequences_to_protein_fasta('dna.fasta') #есть не нуклеотидные буквы
protein = sequences_to_protein_fasta('dna2.fasta') #только днк



# 
os.listdir()
os.getcwd()





