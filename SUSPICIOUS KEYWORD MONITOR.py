

# ♡ ♡ ♡ ♡ ♡SUSPICIOUS KEYWOPRD MONITOR --- CHECKS POSTS FOR SUS KEYWORDS ♡ ♡ ♡ ♡
# 
#





# ♡ ♡ ♡DICTIONARY ♡ ♡ ♡
#
#

POSTS = [
""
"FEEL LIKE SUCH A GANGSTER THIS MORNING, HAD TO DRINK COFFEE WITH NO MILK OR SUGAR",
"SHANK OPPS IN THE FACE ON SIGHT",
"IVE GOT A KILLER HEADACHE",
"i'M GONNA KILL THEM ALL"
]


KEYWORDS = [
"STAB",
"KILL",
"BOMB",
"SHANK",
"GANG",
"RAMBO"
] 


###### ♡this bit interacts with user su[posedly ♡ ♡ ♡ ♡
#
#
print("Hello There! What's the new DANGER word?")
name = input("Enter your keyword:")
#  ♡ ♡ ♡ ♡ ♡ Check if the keyword is already in the list
if name in KEYWORDS:
    print(f"The keyword '{name}' is already in the list stupid.")
else:
    # ####  ♡  ♡ ♡ ♡ Add the new keyword to the list
    KEYWORDS.append(name)
    print(f"The keyword '{name}' has been added to the list.")
print("Updated Keywords:", KEYWORDS)






# ♡ ♡ ♡THIS IS WHERE THE LOOPTY LOOP IS ; IT SHOWS WHERE THE WORD WAS IDENT  ♡ ♡ ♡
#
#
for POST in POSTS:
    for KEYWORD in KEYWORDS:
        if KEYWORD in POST:
              print(f"WARNING DANGER DANGER: '{KEYWORDS} in {POSTS} ")