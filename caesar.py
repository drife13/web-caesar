def alphabet_position(letter):
    upletter = letter.upper()

    return ord(upletter)-ord('A')

def rotate_character(char, rot):
    apc = alphabet_position(char)
    rot = rot % 26
    if char.isalpha():
        if (25-apc)>=rot: rot_up = apc+rot
        else: rot_up = rot-(25-apc)-1

        if char<'a': rot_ord = ord('A')+rot_up
        else: rot_ord = ord('a')+rot_up
    else: return char

    return chr(rot_ord)

def encrypt(text, rot):
    rot_text = ""
    for char in text:
        rot_text += rotate_character(char,rot)

    return rot_text
