import sys

def isBraille(text):
    return all(c in 'O.' for c in text)

def translate_braille_eng(text):
    braille_eng_map = {}
    braile_num_map={}
    braille_eng_map["O....."]="a"
    braille_eng_map["O.O..."]="b"
    braille_eng_map["OO...."]="c"
    braille_eng_map["OO.O.."]="d"
    braille_eng_map["O..O.."]="e"
    braille_eng_map["OOO..."]="f"
    braille_eng_map["OOOO.."]="g"
    braille_eng_map["O.OO.."]="h"
    braille_eng_map[".OO..."]="i"
    braille_eng_map[".OOO.."]="j"
    braille_eng_map["O...O."]="k"
    braille_eng_map["O.O.O."]="l"
    braille_eng_map["OO..O."]="m"
    braille_eng_map["OO.OO."]="n"
    braille_eng_map["O..OO."]="o"
    braille_eng_map["OOO.O."]="p"
    braille_eng_map["OOOOO."]="q"
    braille_eng_map["O.OOO."]="r"
    braille_eng_map[".OO.O."]="s"
    braille_eng_map[".OOOO."]="t"
    braille_eng_map["O...OO"]="u"
    braille_eng_map["O.O.OO"]="v"
    braille_eng_map[".OOO.O"]="w"
    braille_eng_map["OO..OO"]="x"
    braille_eng_map["OO.OOO"]="y"
    braille_eng_map["O..OOO"]="z"
    braile_num_map["O....."]="1"
    braile_num_map["O.O..."]="2"
    braile_num_map["OO...."]="3"
    braile_num_map["OO.O.."]="4"
    braile_num_map["O..O.."]="5"
    braile_num_map["OOO..."]="6"
    braile_num_map["OOOO.."]="7"
    braile_num_map["O.OO.."]="8"
    braile_num_map[".OO..."]="9"
    braile_num_map[".OOO.."]="0"
    #decimal follows corresponds period in number context
    braile_num_map[".O...O"]="."
    #in english context, period is period
    braille_eng_map["..OO.O"]="."
    
    braille_eng_map["..O..."]=","
    braille_eng_map["..O.OO"]="?"
    braille_eng_map["..OOO."]="!"
    braille_eng_map["..OO.."]=":"
    braille_eng_map["..O.O."]=";"
    braille_eng_map["....OO"]="-"
    braille_eng_map[".O..O."]="/"
    braille_eng_map[".OO..O"]="<"
    #greater than and o have the same braille symbol
    braile_num_map["O..OO."]=">"
    braille_eng_map["O.O..O"]="("
    braille_eng_map[".O.OO."]=")"
    braille_eng_map["......"]=" "
    braille_eng_map[".....O"]="capital follows"
    braille_eng_map[".O...O"]="decimal follows"
    braille_eng_map[".O.OOO"]="number follows"
    letters=[text[i:i+6] for i in range(0, len(text), 6)]
    num=False
    upperCase=False
    answer=''
    for letter in letters:
        if letter in braille_eng_map and braille_eng_map[letter] ==' ':
            #if space found, no longer number context
            answer+=braille_eng_map[letter]
            num=False
            continue
        elif letter in braille_eng_map and braille_eng_map[letter] == "capital follows":
            #if capital follows, next letter is upperCase
            upperCase=True
            continue
        elif letter in braille_eng_map and braille_eng_map[letter] == "number follows":
            #if number follows, number context starts
            num=True
            continue
        if(num):
            #if number context
            answer+=braile_num_map[letter]
        else:
            #if alphabet/character context
            if upperCase:
                #if upperCase
                answer+=braille_eng_map[letter].upper()
                upperCase=False
            else:
                #if lowercase/character
                answer+=braille_eng_map[letter]
    print(answer)
    return answer 
                        
def translate_eng_braille(text):
    eng_braille_map = {}
    num_braille_map={}
    eng_braille_map["a"]="O....."
    eng_braille_map["b"]="O.O..."
    eng_braille_map["c"]="OO...."
    eng_braille_map["d"]="OO.O.."
    eng_braille_map["e"]="O..O.."
    eng_braille_map["f"]="OOO..."
    eng_braille_map["g"]="OOOO.."
    eng_braille_map["h"]="O.OO.."
    eng_braille_map["i"]=".OO..."
    eng_braille_map["j"]=".OOO.."
    eng_braille_map["k"]="O...O."
    eng_braille_map["l"]="O.O.O."
    eng_braille_map["m"]="OO..O."
    eng_braille_map["n"]="OO.OO."
    eng_braille_map["o"]="O..OO."
    eng_braille_map["p"]="OOO.O."
    eng_braille_map["q"]="OOOOO."
    eng_braille_map["r"]="O.OOO."
    eng_braille_map["s"]=".OO.O."
    eng_braille_map["t"]=".OOOO."
    eng_braille_map["u"]="O...OO"
    eng_braille_map["v"]="O.O.OO"
    eng_braille_map["w"]=".OOO.O"
    eng_braille_map["x"]="OO..OO"
    eng_braille_map["y"]="OO.OOO"
    eng_braille_map["z"]="O..OOO"
    num_braille_map["1"]="O....."
    num_braille_map["2"]="O.O..."
    num_braille_map["3"]="OO...."
    num_braille_map["4"]="OO.O.."
    num_braille_map["5"]="O..O.."
    num_braille_map["6"]="OOO..."
    num_braille_map["7"]="OOOO.."
    num_braille_map["8"]="O.OO.."
    num_braille_map["9"]=".OO..."
    num_braille_map["0"]=".OOO.."
    num_braille_map["."]=".O...O"
    eng_braille_map["."]="..OO.O"
    eng_braille_map[","]="..O..."
    eng_braille_map["?"]="..O.OO"
    eng_braille_map["!"]="..OOO."
    eng_braille_map[":"]="..OO.."
    eng_braille_map[";"]="..O.O."
    eng_braille_map["-"]="....OO"
    eng_braille_map["/"]=".O..O."
    eng_braille_map["<"]=".OO..O"
    eng_braille_map[">"]="O..OO."
    eng_braille_map["("]="O.O..O"
    eng_braille_map[")"]=".O.OO."
    eng_braille_map[" "]="......"
    eng_braille_map["capital follows"]=".....O"
    eng_braille_map["decimal follows"]=".O...O"
    eng_braille_map["number follows"]=".O.OOO"
    answer=''
    num=False
    for i in range(0,len(text)):
        char = text[i]
        if char.isupper():
            answer+= eng_braille_map["capital follows"]
        if char.isdigit():
            if not num:
                answer+= eng_braille_map["number follows"]
                num=True
            answer+=num_braille_map[char]
        else:
            if char=='.':
                if num:
                    answer+=num_braille_map[char]
                elif i+1<len(text) and text[i+1].isdigit():
                    answer+= eng_braille_map["number follows"]
                    answer+= eng_braille_map["decimal follows"]
                    num=True
                else:
                    answer+= eng_braille_map[char]
            else:
                answer+= eng_braille_map[char.lower()]
                num=False
    print(answer)
    return answer
            
    
def translatOr(text):
    if(isBraille(text)):
        return translate_braille_eng(text)
    else:
        return translate_eng_braille(text)

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("No arguments specified")
    text=''
    for i in range(1, len(sys.argv)):
        text+=sys.argv[i]
        if i!=len(sys.argv)-1:
            text+=' '
    translatOr(text)
