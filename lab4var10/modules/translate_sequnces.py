from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#3. название, место, белок
def extract_info(genbank_file, out_file):
    try:
        with open(out_file, "w") as out:
            for record in SeqIO.parse(genbank_file, "genbank"):
                organism = record.annotations.get("organism", "Unknown organism")
                description = record.description
                
                for feature in record.features:
                    if feature.type == "CDS":
                        
                        location = feature.location
                        protein = feature.qualifiers.get("translation")
                        out.write(f">{record.id}\n")
                        out.write(f"Organism: {organism}\n")
                        out.write(f"Definition: {description}\n")
                        out.write(f"CDS location: {location}\n")
                        out.write(f"Protein:\n{protein}\n\n")
    except Exception as e:
        print(f"Проверьте файл. ошибка: {e}")
        return
    
#данные варианта
#3
extract_info('all_species.gb', 'all_speciesFINAL3.gb')
with open ('all_speciesFINAL3.gb', 'r') as f:
    ff = f.read()
print(ff)