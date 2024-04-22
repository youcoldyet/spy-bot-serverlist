import os

def compile_html_files(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.htm'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as html_file:
                    output.write(html_file.read())
                    output.write('\n')  # Add a newline between each file

# Usage example
folder_path = r'yourfolderpathhere'
output_file = 'compiled_output.html'
compile_html_files(folder_path, output_file)
print(f'HTML files in {folder_path} compiled into {output_file}')
