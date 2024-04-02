### python
import subprocess
import tempfile

# Function to read sequences from a FASTA file
def read_fasta(file_path):
    sequences = {}
    current_seq = ""
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                header = line.strip()[:31]  # Limiting header length to 50 characters
                sequences[header] = ""
                current_seq = header
            else:
                sequences[current_seq] += line.strip()
    return sequences
# Function to write sequences to a FASTA file

def write_fasta(file_path, sequences):
    with open(file_path, 'w') as file:
        for header, sequence in sequences.items():
            file.write(header + '\n')
            file.write(sequence + '\n')

# Function to remove duplicate sequences from a FASTA file
def remove_duplicates(fasta_file):
    sequences = read_fasta(fasta_file)
    seen_sequences = set()
    unique_sequences = {}
    for header, sequence in sequences.items():
        if sequence not in seen_sequences:
            unique_sequences[header] = sequence
            seen_sequences.add(sequence)
        else:
            print(f"Duplicate sequence found and removed: {header}")
    write_fasta(fasta_file, unique_sequences)

# Function to create a BLAST database from a FASTA file
def makeblastdb(fasta_file, db_name):
    cmd = ['makeblastdb', '-in', fasta_file, '-dbtype', 'nucl', '-out', db_name]
    subprocess.run(cmd)

# Function to perform a BLAST search
def blastn(query_sequence, db_name, output_file):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(">Query\n" + query_sequence + "\n")
        temp_query_file = temp_file.name
    cmd = ['blastn', '-query', temp_query_file, '-db', db_name, '-out', output_file, '-outfmt', '6']
    subprocess.run(cmd)
    return temp_query_file

# Function to parse BLAST output and extract identifiers
def parse_blast_output(output_file):
    identifiers = []
    with open(output_file, 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            identifier = fields[1]
            identifiers.append(identifier)
    return identifiers

# Function to retrieve sequences associated with identifiers from a FASTA file
def get_sequences_from_fasta(fasta_file, identifiers, output_fasta_file):
    sequences = {}
    current_sequence = None
    #sequences_retrieved = 0  # Counter to track the number of sequences retrieved
    with open(fasta_file, 'r') as file:
        for line in file:
            #if sequences_retrieved >= num_sequences:  # Check if desired number of sequences have been retrieved
                #break  # Exit loop if desired number of sequences have been retrieved
            if line.startswith('>'):
                header = line.strip()[1:]  # Remove ">" from the header
                if header in identifiers:
                    current_sequence = header
                    sequences[current_sequence] = ""
                else:
                    current_sequence = None
            elif current_sequence is not None:
                sequences[current_sequence] += line.strip()
    
    # Write the sequences to the output file
    with open(output_fasta_file, 'w') as output_fasta_file:
        for header, sequence in sequences.items():
            output_fasta_file.write(">" + header + "\n")
            output_fasta_file.write(sequence + "\n")
    
    return output_fasta_file


# Example usage:
fasta_file = input("Enter the fasta file path: \n")  # Change this to your FASTA file path
db_name = "blast_database"  # Change this to desired name for BLAST database
output_file = "blast_results.txt"  # Change this to desired name for BLAST results output file
output_fasta_file = "blast_results.fasta"  # Change this to desired name for output FASTA file
#num_sequences = int(input("Enter the number of sequences to retrieve: "))  # Prompt user for number of sequences

# Pre-processing steps
remove_duplicates(fasta_file)
makeblastdb(fasta_file, db_name)

# Perform BLAST search
query_sequence = input("Enter your query sequence: ")
temp_query_file = blastn(query_sequence, db_name, output_file)
print("Temporary query file created:", temp_query_file)

# Parse BLAST output and extract identifiers
identifiers = parse_blast_output(output_file)

# Retrieve sequences associated with identifiers
sequences = get_sequences_from_fasta(fasta_file, identifiers, output_fasta_file)

# Print information about the results
print("BLAST results written to:", output_file)
#print("Extracted identifiers:", identifiers)
print("Result sequences written to:", output_fasta_file)