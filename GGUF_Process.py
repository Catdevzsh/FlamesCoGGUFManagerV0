import sys
import glob

def merge_files(output_file="fused.gguf"):
    file_pattern = "*.gguf"
    files_to_merge = glob.glob(file_pattern)
    with open(output_file, 'w') as outfile:
        for fname in files_to_merge:
            with open(fname) as infile:
                outfile.write(infile.read())
                outfile.write("\n")  # Optionally, add a newline between files if needed.
    print(f"Merged {len(files_to_merge)} files into {output_file}")

def display_copyright():
    copyright_text = """
    [Flames Co. Systems [C] 20XX]
    All rights reserved. Unauthorized reproduction, distribution, or use of this software is prohibited.
    """
    print(copyright_text)

def main():
    print("Welcome to the CLI File Manager. Type /help for a list of commands.")
    while True:
        command = input("Enter command: ").strip()
        if command == "/merge":
            merge_files()  # You can add functionality to specify the output file.
        elif command == "/copyright":
            display_copyright()
        elif command == "/exit":
            print("Exiting the program.")
            sys.exit(0)
        elif command == "/help":
            print("/merge: Merge all .gguf files into a single file named fused.gguf")
            print("/copyright: Display copyright information.")
            print("/exit: Exit the program.")
        else:
            print("Unknown command. Type /help for a list of commands.")

if __name__ == "__main__":
    main()
