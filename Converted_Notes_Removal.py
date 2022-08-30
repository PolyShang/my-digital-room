'''
This is a tool to remove the notes that I already handled.
'''

# Get book annotation input file and prepare the receiving file.

original_annotation = open('E:/My_Clippings_1.txt', 'r', encoding='UTF-8')
modified_annotation = open('E:/My_Clippings.txt', 'a', encoding='UTF-8')

input_lines = original_annotation.readlines()  # Read the original clippings into a list.

# Extract certain book's notes into an interim document.

book_titles = ['Thinking, Fast and Slow (Daniel Kahneman)\n', 'Fire and Fury (Michael Wolff)\n',
               '丹尼尔斯经典跑步训练法：世界最佳跑步教练的跑步公式 (湛庐乐跑人生系列图书) (杰克•丹尼尔斯)\n',
               'The Ultimate Guide to Kink (Tristan Taormino)\n', 'How the Mind Works (Steven Pinker)\n',
               'Sapiens: A Brief History of Humankind (Yuval Noah Harari)\n',
               'Catch-22 - Joseph Heller (Shahid Riaz)\n',
               'The Beginning of Infinity: Explanations That Transform the World (David Deutsch)\n',
               'The Intelligent Investor, Rev. Ed (Benjamin Graham)\n', 'On Tyranny (Timothy Snyder)\n',
               '嫌疑人X的献身 (东野圭吾)\n', '同級生 (东野圭吾)\n', 'Guns, Germs, and Steel (Jared Diamond)\n',
               'Zero to One: Notes on Startups, or How to Build the Future (Peter Thiel, Blake Masters)\n',
               'The Goal: A Process of Ongoing Improvement (Eliyahu Goldratt)\n', 'Switch (Chip Heath)\n',
               'Positive Discipline for Teenagers (Jane Nelsen)\n', '叫魂：1768年中国妖术大恐慌 (孔飞力)\n',
               'Why is Sex Fun?: the evolution of human sexuality (Jared Mason Diamond)\n',
               'BDSM 101 (Rev. Jen)\n', 'The Easiest Way to Meet and Pick Up Girls...ever!! (Dusty White)\n']

i = 0
while i < len(input_lines):
    if input_lines[i] in book_titles:
        i += 5
        continue
    else:
        for j in range(5):
            modified_annotation.write(input_lines[i + j])
    i += 5
#
modified_annotation.close()
original_annotation.close()

# End.
