strs = ["flower","flow","flight"]

output_str = ''

for i in range(len(strs)):
    prefix_list = []
    for j in range(3):
        prefix_list.append(strs[j][i])
    if prefix_list.count(strs[0][i]) < len(strs):
        break
    else:
        output_str += strs[0][i]

print(output_str)