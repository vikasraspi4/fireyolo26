import os

folder_path = "night/valid/labels"   # folder containing txt files
c=0
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r") as file:
            lines = file.readlines()

        modified_lines = []

        for line in lines:
            parts = line.strip().split()

            if parts:
                if parts[0] == "1":
                    parts[0] = "2"
                elif parts[0] == "2":
                    parts[0] = "1"
           
            modified_lines.append(" ".join(parts) + "\n")

        with open(file_path, "w") as file:
            file.writelines(modified_lines)
            print(modified_lines,"\n")

print("Class IDs swapped successfully.")
