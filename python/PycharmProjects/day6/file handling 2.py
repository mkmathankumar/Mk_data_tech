with open('data_set.csv', 'r') as infile, open('data_set_op.csv','w') as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)
