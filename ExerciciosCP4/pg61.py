"""
1. Given a text file that contains only alphabet characters [A-Za-z], digits [0-9], spaces,
and periods (‘.’), write a program to read this text file line by line until we encounter
a line that starts with seven periods (“.......”). Concatenate (combine) each line
into one long string T. When two lines are combined, give one space between them so
that the last word of the previous line is separated from the first word of the current
line. There can be up to 30 characters per line and no more than 10 lines for this input
block. There are no trailing spaces at the end of each line and each line ends with a
newline character. Note that the sample input is shown inside a box after question
1.(d) and before task 2.
(a) Do you know how to store a string in your favorite programming language?
(b) How to read a given text input line by line?
(c) How to concatenate (combine) two strings into a larger one?
(d) How to check if a line starts with a string “.......” to stop reading input?

Input:
I love CS3233 Competitive
Programming. i also love
AlGoRiThM
.......you must stop after reading this line as it starts with 7 dots
after the first input block, there will be one loooooooooooong line...
"""

T = ""
pegaInput = True

while(True):
    try:
        str = input()
    except:
        break

    if(pegaInput):
        if(str[0:7:1] == "......."):
            pegaInput = False
        else:
            T += str

print(T)

"""
Suppose that we have one long string T. We want to check if another string P can
be found in T. Report all the indices where P appears in T or report -1 if P cannot
be found in T. For example, if T = “I love CS3233 Competitive Programming. i
also love AlGoRiThM” and P = “I”, then the output is only {0} (0-based indexing)
because uppercase ‘I’ and lowercase ‘i’ are considered di↵erent and thus the character
‘i’ at index {39} is not part of the output. If P = “love”, then the output is {2, 46}.
If P = “book”, then the output is {-1}.

(a) How to find the first occurrence of a substring in a string (if any)?
Do we need to implement a string matching algorithm (e.g., Knuth-Morris-Pratt
algorithm discussed in Book 2, etc) or can we just use library functions?

(b) How to find the next occurrence(s) of a substring in a string (if any)?

Input:
I love CS3233 Competitive Programming. i also love AlGoRiThM
I

output
0

Input
I love CS3233 Competitive Programming. i also love AlGoRiThM
i

output
9

Input
I love CS3233 Competitive Programming. i also love AlGoRiThM
love

Output
2, 46

Input
I love CS3233 Competitive Programming. i also love AlGoRiThM
book

Output
-1
"""

# # T = input()
# T = "I love CS3233 Competitive Programming. i also love AlGoRiThM"

# # palavra = input()
# palavra = "love"

# if(palavra in T):
#     indexes = []
#     for i in range(len(T)):
#         try:
#             if(T[i:len(palavra) + i: 1] == palavra):
#                 indexes.append(i)
#         except:
#             break

#     print(indexes)

#     for i in range(len(indexes)):
#         if(i < len(indexes) - 1):
#             print(f"{indexes[i]}, ", end="")
#         else:
#             print(f"{indexes[i]}.")

# else:
#     print(-1)



# T = input()
T = "I love CS3233 Competitive Programming. i also love AlGoRiThM"

# palavra = input()
palavra = "love"

pos = 0

ind = []

pos = T.find(palavra, pos + 1)

while(pos != -1):
    ind.append(pos)
    pos = T.find(palavra, pos + 1)

if(len(ind) > 0):
    for i in range(len(ind)):
        if(i < len(ind) - 1):
           print(f"{ind[i]}, ", end="")
        else:
            print(f"{ind[i]}.")
else:
    print(-1)

"""
Suppose we want to do some simple analysis of the characters in T and also to transform
each character in T into lowercase. The required analysis are: How many digits, vowels
[aeiouAEIOU], and consonants (other lowercase/UPPERCASE alphabet characters
that are not vowels) are there in T? Can you do all these in O(n) where n is the length
of the string T?
"""