import subprocess
import os

# Define file paths
input_file = '/path/to/Ecoli_Blood7.fastq.gz'
output_file = '/path/to/kaiju_output.csv'
nodes_file = '/path/to/nodes.dmp'
database_file = '/path/to/kaiju_db_fungi.fmi'

# Kaiju command to classify reads and generate the output file
kaiju_command = f"kaiju -t {nodes_file} -f {database_file} -i {input_file} -o {output_file}"

# Run the Kaiju command
subprocess.run(kaiju_command, shell=True)

print(f"Taxonomy classification completed. Results saved to {output_file}")
