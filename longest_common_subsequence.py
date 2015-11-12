import sys
def main():
    X ="AGGTAB"
    Y = "GXTXAYB"
    m = len(X)
    n = len(Y)
    print lcss_algorithm(X,Y)

def lcss_algorithm(text,pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    lcs_matrix = [[0]*(pattern_length+1) for i in range(text_length+1)]
    print_matrix(lcs_matrix,text_length,pattern_length)
    for i in range(0,text_length+1):
        for j in range(0,pattern_length+1):
            if i==0 or j == 0:
                lcs_matrix[i][j] = 0
            elif text[i-1] == pattern[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] +1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j],lcs_matrix[i][j-1])
    print_matrix(lcs_matrix,text_length,pattern_length)
    sequence = get_longest_sequence(lcs_matrix,text,pattern)
    return sequence

def get_longest_sequence(matrix,text,pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    index = matrix[text_length][pattern_length]
    sequence= ['0']*index
    i = text_length
    j = pattern_length
    while(i >0 and j>0):
        if text[i-1] == pattern[j-1]:
            sequence[index-1] = text[i-1]
            i= i-1
            j = j-1
            index = index-1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i = i-1
        else:
            j = j-1
    return "".join(sequence)

def print_matrix(matrix,rows,cols):
    for i in range(0,rows):
        sys.stdout.write("\n")
        for j in range(0,cols):
            sys.stdout.write(str(matrix[i][j]))
            sys.stdout.write('\t')

    sys.stdout.write('\n')

main()
