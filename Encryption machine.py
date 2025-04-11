import flet as ft
import pyperclip

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': "-----", '1': ".----", '2': "..---", '3': "...--",
    '4': "....-", '5': ".....", '6': "-....", '7': "--...",
    '8': "---..", '9': "----.", ' ': '//'
}
MORSE_DECODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encrypt_morse(text):
    return ' / '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def decrypt_morse(text):
    return ''.join(MORSE_DECODE_DICT.get(char, '') for char in text.split(' / '))

def encrypt_a1z26(text):
    return ' '.join(str(ord(char.upper()) - 64) if char.isalpha() else char for char in text)

def decrypt_a1z26(text):
    return ''.join(chr(int(num) + 64) if num.isdigit() else num for num in text.split())

SUBSTITUTION_KEY = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPASDFGHJKLZXCVBNM")
REVERSE_SUBSTITUTION_KEY = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNM", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def encrypt_substitution(text):
    return text.upper().translate(SUBSTITUTION_KEY)

def decrypt_substitution(text):
    return text.upper().translate(REVERSE_SUBSTITUTION_KEY)

def main(page: ft.Page):
    page.title = "Encryption App"
    page.theme_mode = ft.ThemeMode.SYSTEM

    input_field = ft.TextField(label="Enter your message", width=400, animate_opacity=300)
    output_field = ft.TextField(label="Output", read_only=True, width=400)
    method_dropdown = ft.Dropdown(
        label="Select encryption method",
        options=[
            ft.dropdown.Option("Morse Code"),
            ft.dropdown.Option("A1Z26"),
            ft.dropdown.Option("Substitution Cipher")
        ],
    )

    def encrypt_action(e):
        text = input_field.value.strip()
        method = method_dropdown.value
        if not text or not method:
            output_field.value = "Please enter text and select a method."
        else:
            if method == "Morse Code":
                output_field.value = encrypt_morse(text)
            elif method == "A1Z26":
                output_field.value = encrypt_a1z26(text)
            elif method == "Substitution Cipher":
                output_field.value = encrypt_substitution(text)
        output_field.update()

    def decrypt_action(e):
        text = input_field.value.strip()
        method = method_dropdown.value
        if not text or not method:
            output_field.value = "Please enter text and select a method."
        else:
            if method == "Morse Code":
                output_field.value = decrypt_morse(text)
            elif method == "A1Z26":
                output_field.value = decrypt_a1z26(text)
            elif method == "Substitution Cipher":
                output_field.value = decrypt_substitution(text)
        output_field.update()

    def copy_to_clipboard(e):
        pyperclip.copy(output_field.value)
        page.snack_bar = ft.SnackBar(ft.Text("Copied to clipboard!"))
        page.snack_bar.open = True
        page.update()

    theme_toggle = ft.Switch(label="Dark Mode", on_change=lambda e: setattr(page, 'theme_mode', ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT) or page.update())

    page.add(
        theme_toggle,
        input_field,
        method_dropdown,
        ft.Row([
            ft.ElevatedButton("Encrypt", on_click=encrypt_action),
            ft.ElevatedButton("Decrypt", on_click=decrypt_action),
            ft.ElevatedButton("Copy", on_click=copy_to_clipboard)
        ]),
        output_field
    )

ft.app(target=main)
#para que no me diga que lo subi tarde, se lo subo asi porque no se como subirlo en git y si.