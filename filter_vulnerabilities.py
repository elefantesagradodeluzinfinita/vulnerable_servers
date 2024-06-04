import sys
import os

def find_vulnerabilities(input_filename):
    output_filename = 'coincidences.txt'
    keywords = ['Vulnerability', 'Vulnerable']
    
    if not os.path.isfile(input_filename):
        print(f"El archivo {input_filename} no existe.")
        return
    
    with open(output_filename, 'a') as outfile:
        with open(input_filename, 'r') as infile:
            for line in infile:
                if any(keyword in line for keyword in keywords):
                    outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_archivo>")
    else:
        input_filename = sys.argv[1]
        find_vulnerabilities(input_filename)

