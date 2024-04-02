# Fasta Duplicate Removal and BLAST Sequence Retrieval

This Python script performs the following tasks:

1. Reads a FASTA file and removes duplicate sequences.
2. Creates a BLAST database from the processed FASTA file.
3. Performs a BLAST search with a user-defined query sequence.
4. Parses the BLAST results to extract identifiers.
5. Retrieves sequences associated with the identifiers from the original FASTA file.
6. Writes the retrieved sequences to a new FASTA file.

The user can specify the input FASTA file, the name of the BLAST database, the output file for BLAST results, and the output file for retrieved sequences. Additionally, the user can input the query sequence and the number of sequences to retrieve.

This script is useful for sequence analysis and retrieval tasks, particularly when working with large genomic or protein datasets.

## Requirements

- Python 3.x
- BLAST command-line tools installed and accessible in the system path

## Usage

1. Clone the repository or download the script `fasta_duplicate_removal_blast_sequence_retrieval.py`.
2. Run the script in a Python environment.
3. Follow the prompts to input the necessary information:
   - FASTA file path
   - Name for the BLAST database
   - Name for the BLAST results output file
   - Query sequence
   - Number of sequences to retrieve
4. The script will perform the specified tasks and provide information about the results.

## License

This project is licensed under the BSD License - see the [LICENSE] file for details.
