
with open("dna_sample.txt", "r") as file:
    sequence = file.read().strip()

# Counting the individual nucleotide bases
count_A = sequence.count("A")
count_T = sequence.count("T")
count_C = sequence.count("C")
count_G = sequence.count("G")

print("--- DNA Analysis Report ---")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"C: {count_C}")
print(f"G: {count_G}")
