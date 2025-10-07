"""
1) Given a text file that contains only alphabet characters [A-Za-z], digits [0-9], spaces,
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
2) Suppose that we have one long string T. We want to check if another string P can
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
3) Suppose we want to do some simple analysis of the characters in T and also to transform
each character in T into lowercase. The required analysis are: How many digits, vowels
[aeiouAEIOU], and consonants (other lowercase/UPPERCASE alphabet characters
that are not vowels) are there in T? Can you do all these in O(n) where n is the length
of the string T?
"""

T = "Suppose we want to do some simple analysis of the characters in T and also to transform " \
    "each character in T into lowercase. The required analysis are: How many digits, vowels " \
    "[aeiouAEIOU], and consonants (other lowercase/UPPERCASE alphabet characters that are not " \
    "vowels) are there in T? Can you do all these in O(n) where n is the length of the string T?"

print(T)

mapa = {}

vogais = "aeiouAEIOU"
consoantes = "qwrtypsdfghjklçzxcvbnm"
consoantes += consoantes.upper()

qttVogal = 0
qttConsoante = 0

Tzinho = ""

for i in range(len(T)):
    if(T[i] in vogais):
        qttVogal += 1
    elif(T[i] in consoantes):
        qttConsoante += 1
    else:
        Tzinho += T[i].lower()
        continue

    try:
        mapa[T[i]] += 1
    except:
        mapa[T[i]] = 1

    Tzinho += T[i].lower()

print("\n", mapa, sep="")
print(f"Na string temos {qttVogal} vogais")
print(f"Na string temos {qttConsoante} consoantes")
print(Tzinho)

"""4) Next, we want to break this one long string T into tokens (substrings) and store them
into an array of strings called tokens. For this mini task, the delimiters of these tokens

are spaces and periods (thus breaking sentences into words). For example, if we tok-
enize the string T (in lowercase), we will have these tokens = {“i”, “love”, “cs3233”,

“competitive”, “programming”, “i”, “also”, “love”, “algorithm”}. Then, we want

to sort this array of strings lexicographically and then find the lexicographically small-
est string. That is, we have sorted tokens: {“algorithm”, “also”, “competitive”,

“cs3233”, “i”, “i”, “love”, “love”, “programming”}. Thus, the lexicographically
smallest string for this example is “algorithm”.
(a) How to tokenize a string?
(b) How to store the tokens (the shorter strings) in an array of strings?
(c) How to sort an array of strings lexicographically?"""

T = "I love CS3233 Competitive Programming. i also love AlGoRiThM"

T = T.lower().split(" ")

print(T)

print(sorted(T))


"""5) Now, identify which word appears the most in T. In order to answer this query, we
need to count the frequency of each word. For T, the output is either “i” or “love”,
as both appear twice. Which data structure should be used for this mini task?"""

mapa = {}

for i in T:
    try:
        mapa[i] += 1
    except:
        mapa[i] = 1
    finally:
        print(i,": ", mapa[i], sep="")

"""6) The given text file has one more line after a line that starts with “.......” but the
length of this last line is not constrained. Your task is to count how many characters
there are in the last line. How to read a string if its length is not known in advance?"""

T = """I love CS3233 Competitive
Programming. i also love
AlGoRiThM
.......you must stop after reading this line as it starts with 7 dots
after the first input block, there will be one loooooooooooong line..."""

dots = 0
cont = 0

for i in range(len(T)):
    if(dots == 7):
        print(T[i], end="")
        cont += 1
        continue

    if(T[i] == "."):
        dots += 1
    else:
        dots = 0

print(f"Após os \"........\" temos {cont} caracteres")