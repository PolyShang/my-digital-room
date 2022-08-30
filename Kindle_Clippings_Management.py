'''
This is a program to standardize the Kindle annotations and make them
acceptable for my Obsidian note input.
'''

# Get book annotation input file and prepare the receiving file.

original_annotation = open('E:/My_Clippings.txt', 'r', encoding='UTF-8')
interim_doc = open('E:/Interim_document.txt', 'a', encoding='UTF-8')
standard_annotation = open('E:/Kindle_annotation.txt', 'a', encoding='UTF-8')

input_lines = original_annotation.readlines()   # Read the original clippings into a list.

# Extract certain book's notes into an interim document.

book_title = input('Please input the book title in the clipping file: ')

i = 0
while i < len(input_lines):
    if input_lines[i] == f'{book_title}\n':
        interim_doc.write(input_lines[i + 1])
        interim_doc.write(input_lines[i + 3])
    i += 1

# Convert the highlights and notes into OB note format.

interim_doc.close()      # Close the interim file to flush the content so that it could be read again.
interim_doc = open('E:/Interim_document.txt', 'r', encoding='UTF-8')
input_lines = interim_doc.readlines()   # Open the interim file and read its content.

'''
Organize the book notes into the OB note format. Two steps as below.
1. If a note is made following a highlight, the first if cycle and the sub if cycle identify
and input the content accordingly. In the case of a single highlight is available, the sub if
cycle identify it (no 'Note' available) and handles it.
2. If only a note is made, the 'elif' part take over and input the content.
'''

j = 0
while j < len(input_lines):
    if input_lines[j][0] == '-' and input_lines[j][2:6] == 'High':
        line_highlight = input_lines[j] + '\n' + '> \n' + '> ' + input_lines[j + 1] + '> \n'
        standard_annotation.write(line_highlight)
        if input_lines[j + 2][0] == '-' and input_lines[j + 2][2:6] == 'Note':
            input_lines[j + 3] = input_lines[j + 3].strip()
            line_note = '\n<font color=\'33beff\'>' + input_lines[j + 3] + '</font>\n' + '\n---\n\n'
            standard_annotation.write(line_note)
            j += 4
            continue
        standard_annotation.write('\n---\n\n')
        j += 2
        continue
    elif input_lines[j][0] == '-' and input_lines[j][2:6] == 'Note':
        standard_annotation.write(input_lines[j])
        input_lines[j + 1] = input_lines[j + 1].strip()
        line_note = '\n<font color=\'33beff\'>' + input_lines[j + 1] + '</font>\n' + '\n---\n\n'
        standard_annotation.write(line_note)
        j += 2
    else:
        j += 1

# Close all open files.

standard_annotation.close()
original_annotation.close()
interim_doc.close()

# End.