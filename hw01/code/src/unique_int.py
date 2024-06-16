'''
    This script reads a list of integers from an input file. 
    Generates an output file having a list of unique integers present in the 
    input file
'''

#Import Operating system
import os


def process_file(input_file_path, output_file_path):
    """Process the input file to find unique integers and write them to the output file."""
    unique_integers = set()

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.isdigit() or (line.startswith('-') and line[1:].isdigit()):
                unique_integers.add(int(line))

    sorted_integers = sorted(unique_integers)

    with open(output_file_path, 'w') as file:
        for integer in sorted_integers:
            file.write(f"{integer}\n")


def main():
    """Main function to handle directory paths and file processing."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.abspath(os.path.join(
        base_dir, '..', '..', 'sample_inputs'))
    output_dir = os.path.abspath(os.path.join(
        base_dir, '..', '..', 'sample_results'))

    if not os.path.exists(input_dir):
        print(f"Input directory does not exist: {input_dir}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Base directory: {base_dir}")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")

    for input_file in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, input_file)
        output_file_path = os.path.join(
            output_dir, f"{input_file}_results.txt")
        process_file(input_file_path, output_file_path)
        print(f"Processed {input_file} -> {input_file}_results.txt")


if __name__ == "__main__":
    main()
