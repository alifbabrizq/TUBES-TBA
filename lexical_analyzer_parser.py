# Lexical Analyzer
# Tugas Besar Teori Bahasa Automata
from pickle import FALSE
import string
# print("Tugas Besar Teori Bahasa Automata")
# print("Kelompok 4 Tugas Besar Mata Kuliah Teori Bahasa dan Automata")
# print("Muhammad Rafi Yanaputeranto (1301204352)\n Alif Babrizq Kuncara (1301204228)\n Noval Dzaki ()")
# print("IF-44-12")
# print("==================================")

# inputting string
# print("Bahasa yang digunakan merupakan bahasa Madura")
# print("Lexical Analyzer")
# print("Simbol Terminal: anom | embu | sate | kaju | sape | ajam | koncel | tono | keba | tompa")
# kalimat = input("Masukkan kalimat/kata yang ingin diperiksa: ")


def lexicalAnalyzer(kalimat):
    input_string = kalimat.lower() + "#"

    # initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
        "q0",
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "q8",
        "q9",
        "q10",
        "q11",
        "q12",
        "q13",
        "q14",
        "q15",
        "q16",
        "q17",
        "q18",
        "q19",
        "q20",
        "q21",
        "q22",
        "q23",
        "q24",
    ]

    transition_table = {}

    for i in state_list:
        for alphabet in alphabet_list:
            transition_table[(i, alphabet)] = "ERROR"
        transition_table[(i, "#")] = "ERROR"
        transition_table[(i, " ")] = "ERROR"

    # Context Free Grammar
    # s -> NN VB NN
    # NN -> anom | embu | sate | kaju | sape | ajam | koncel
    # VB -> tono | keba | tompa

    # For starting node (q0)
    transition_table[("q0", " ")] = "q0"

    # Final state
    transition_table[("q23", "#")] = "ACCEPT"
    transition_table[("q23", " ")] = "q24"

    transition_table[("q24", "#")] = "ACCEPT"
    transition_table[("q24", " ")] = "q24"

    # string "anom"
    transition_table[("q24", "a")] = "q1"
    transition_table[("q0", "a")] = "q1"
    transition_table[("q1", "n")] = "q2"
    transition_table[("q2", "o")] = "q3"
    transition_table[("q3", "m")] = "q23"

    # string "embu"
    transition_table[("q24", "e")] = "q5"
    transition_table[("q0", "e")] = "q5"
    transition_table[("q5", "m")] = "q6"
    transition_table[("q6", "b")] = "q7"
    transition_table[("q7", "u")] = "q23"

    # string "sate"
    transition_table[("q24", "s")] = "q20"
    transition_table[("q0", "s")] = "q20"
    transition_table[("q20", "a")] = "q21"
    transition_table[("q21", "t")] = "q22"
    transition_table[("q22", "e")] = "q23"

    # string "kaju"
    transition_table[("q24", "k")] = "q8"
    transition_table[("q0", "k")] = "q8"
    transition_table[("q8", "a")] = "q9"
    transition_table[("q9", "j")] = "q7"
    transition_table[("q7", "u")] = "q23"

    # string "sape"
    transition_table[("q24", "s")] = "q20"
    transition_table[("q0", "s")] = "q20"
    transition_table[("q20", "a")] = "q21"
    transition_table[("q21", "p")] = "q22"
    transition_table[("q22", "e")] = "q23"

    # string "ajam"
    transition_table[("q24", "a")] = "q1"
    transition_table[("q0", "a")] = "q1"
    transition_table[("q1", "j")] = "q4"
    transition_table[("q4", "a")] = "q3"
    transition_table[("q3", "m")] = "q23"

    # string "koncel"
    transition_table[("q24", "k")] = "q8"
    transition_table[("q0", "k")] = "q8"
    transition_table[("q8", "o")] = "q10"
    transition_table[("q10", "n")] = "q11"
    transition_table[("q11", "c")] = "q12"
    transition_table[("q12", "e")] = "q13"
    transition_table[("q13", "l")] = "q23"

    # string "tono"
    transition_table[("q24", "t")] = "q16"
    transition_table[("q0", "t")] = "q16"
    transition_table[("q16", "o")] = "q17"
    transition_table[("q17", "n")] = "q19"
    transition_table[("q19", "o")] = "q23"

    # string "keba"
    transition_table[("q24", "k")] = "q8"
    transition_table[("q0", "k")] = "q8"
    transition_table[("q8", "e")] = "q14"
    transition_table[("q14", "b")] = "q15"
    transition_table[("q15", "a")] = "q23"

    # string "tompa"
    transition_table[("q24", "t")] = "q16"
    transition_table[("q0", "t")] = "q16"
    transition_table[("q16", "o")] = "q17"
    transition_table[("q17", "m")] = "q18"
    transition_table[("q18", "p")] = "q15"
    transition_table[("q15", "a")] = "q23"

    # lexical Analysis
    idx_char = 0
    state = "q0"
    current_token = ""
    while state != "ACCEPT":
        current_char = input_string[idx_char]
        current_token += current_char
        # print(state, current_char)
        # print(f"{state, current_char}")
        state = transition_table[(state, current_char)]
        if state == "q23":
            # print(f"current token: {current_token} is valid")
            # print("current token: {} is valid".format(current_token))
            current_token = ""
        if state == "ERROR":
            # print("error")
            return False
        idx_char += 1

    # Conclusion
    if state == "ACCEPT":
        # print(f"semua token yang di input: {input_string} valid")
        return True
    else:
        return False
        #print("semua token yang di input: {} valid".format(input_string))


def parser(kalimat):
    input_string = kalimat.lower().split()
    input_string.append('EOS')

    non_terminals = ['S', 'NN', 'VB']
    terminals = ["anom", "embu", "sate", "kaju", "sape",
                 "ajam", "koncel", "tono", "keba", "tompa"]

    # Parse Table Definition
    parse_table = {}

    parse_table[('S', 'anom')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'embu')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'sate')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'kaju')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'sape')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'ajam')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'koncel')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'tono')] = ['error']
    parse_table[('S', 'keba')] = ['error']
    parse_table[('S', 'tompa')] = ['error']
    parse_table[("S", "EOS")] = ["error"]

    parse_table[('NN', 'anom')] = ['anom']
    parse_table[('NN', 'embu')] = ['embu']
    parse_table[('NN', 'sate')] = ['sate']
    parse_table[('NN', 'kaju')] = ['kaju']
    parse_table[('NN', 'sape')] = ['sape']
    parse_table[('NN', 'ajam')] = ['ajam']
    parse_table[('NN', 'koncel')] = ['koncel']
    parse_table[('NN', 'tono')] = ['error']
    parse_table[('NN', 'keba')] = ['error']
    parse_table[('NN', 'tompa')] = ['error']
    parse_table[("NN", "EOS")] = ["error"]

    parse_table[('VB', 'anom')] = ['error']
    parse_table[('VB', 'embu')] = ['error']
    parse_table[('VB', 'sate')] = ['error']
    parse_table[('VB', 'kaju')] = ['error']
    parse_table[('VB', 'sape')] = ['error']
    parse_table[('VB', 'ajam')] = ['error']
    parse_table[('VB', 'koncel')] = ['error']
    parse_table[('VB', 'tono')] = ['tono']
    parse_table[('VB', 'keba')] = ['keba']
    parse_table[('VB', 'tompa')] = ['tompa']
    parse_table[("VB", "EOS")] = ["error"]

    # stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # input reading initialization
    idx_string = 0
    symbol = input_string[idx_string]

    # parsing process
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        # print('top - ', top)
        # print('symbol - ', symbol)
        if top in terminals:
            # print('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_string = idx_string + 1
                symbol = input_string[idx_string]
                if symbol == "EOS":
                    # print('isi stack:', stack)
                    stack.pop()
            else:
                return False
        elif top in non_terminals:
            # print('top adalah simbol non-terminal')
            if parse_table[(top, symbol)][0] != "error":
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_pushed) - 1, -1, -1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                return False
        else:
            return False
        # print('isi stack', stack)
        # print()

    # kesimpulan
    # print()
    if symbol == "EOS" and len(stack) == 0:
        # print('Input string', input_string, '', 'diterima, sesuai Grammar')
        return True
    else:
        return False
        # print('Error, input string', input_string,
        #       'tidak diterima, tidak sesuai grammar')
