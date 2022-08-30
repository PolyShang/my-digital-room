"""
This is a program to standardize the book annotations from my Boox reader and make them
acceptable for my Obsidian note input.
"""

from os import mkdir

# Define the inputting file path and the annotation color. R: red; B: Blue; LB: Light Blue； Y: Yellow.

file_in_path = input('Please input the document path: ')
color_input = input('The annotation color should be Blue, Light Blue, Green, or Yellow? ')
color_dict = {'Blue': '33beff', 'Light Blue': '00d7ec', 'Green': '81ff6e', 'Yellow': 'f6f996'}
color_selection = color_dict[color_input]

# Read input file, get the title and prepare the output file with it.

original_annotation = open(file_in_path, 'r', encoding='UTF-8')

lines = original_annotation.readlines()
p = lines[0].index('>')                       # Get the ">" marker where the title ends in the line.
book_title = lines[0][9: p - 12]              # Strip out the full title.
title_list = book_title.split(' ')            # Split the title string with 'space'.

annotation_name = ''
i = 0
while i < 3:
    if i >= len(title_list):
        break
    else:
        annotation_name += title_list[i]       # Use the first three words or Chinese strings as file title.
        i += 1

mkdir(f'E:\OneDrive\Books\Book Annotations\{annotation_name}')

# Prepare the output file.

final_annotation = open(f'E:/OneDrive/Books/Book Annotations/'
                        f'{annotation_name}/{annotation_name}.txt', 'a', encoding='UTF-8')

i = 0
while i < len(lines):
    # Remove empty lines and the annotation head with marker '读书笔记'.
    if lines[i] == '\n' or '读书笔记' in lines[i]:
        i += 1
        continue
    # Identify the separator and copy it with an extra line end marker.
    # Remove the unnecessary lines between the separator and the highlight header.
    elif '---------' in lines[i]:
        j = i
        temp_line = lines[i] + '\n'
        final_annotation.write(temp_line)
        while j < len(lines):
            if j + 1 < len(lines) and '页码' in lines[j + 1]:
                break
            j += 1
        i = j + 1
    # Identify and convert the highlight header.
    elif '页码' in lines[i]:
        temp_line = lines[i] + '\n'
        final_annotation.write(temp_line)
        i += 1
    # Identify and convert the annotation with selected color.
    # Remove the empty lines until hitting the next separator.
    elif '【批注】' in lines[i]:
        temp_line = lines[i].strip()
        temp_line = '\n' + '<font color=\'' + color_selection + '\'>' + temp_line + '</font>' + '\n\n'
        j = i + 1
        while j < len(lines):
            if lines[j] == '\n':
                j += 1
                continue
            if '---------' in lines[j]:
                i = j
                break
            else:
                lines[j].strip()
                temp_line = temp_line + '<font color=\'' + color_selection + '\'>' + lines[j] + '</font>' + '\n\n'
                j += 1
        final_annotation.write(temp_line)
        i = j
    # This part is to convert the highlighted content and put them under quotation mode.
    else:
        j = i + 1
        lines[i] = lines[i].strip()
        temp_line = '> \n' + '> ' + lines[i]
        while j < len(lines):
            if '【批注】' in lines[j] or '---------' in lines[j]:
                temp_line = temp_line + '\n> \n'
                i = j
                break
            else:
                lines[j] = lines[j].strip()
                temp_line = temp_line + lines[j]
                j += 1
        final_annotation.write(temp_line)
        i = j

# Close the two files.
final_annotation.close()
original_annotation.close()