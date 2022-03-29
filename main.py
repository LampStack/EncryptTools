import os, time, string , pyfiglet

class EncryptTools:
    def clearScreen() -> None:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    
    def LettersCheck(key:str) -> bool:
        keywords = string.printable.strip() + ' ' + '\n'
        for char in key:
            if char not in keywords:
                return False
        return True

    def shift(message:str, number:int, type:str) ->str:
        keywords = string.printable.strip() + ' ' + '\n'
        result = ''
        for char in message:
            if type == 'Encrypt':
                result += keywords[(keywords.find(char) + number) % len(keywords)]
            else:
                result += keywords[(keywords.find(char) - number) % len(keywords)]
        return result

    def Encrypt(message:str, key:str) -> str:
        for letter in key:
            message = EncryptTools.shift(message, ord(letter), 'Encrypt')
        return message

    def Decrypt(message:str, key:str) -> str:
        key = key[::-1]
        for letter in key:
            message = EncryptTools.shift(message, ord(letter), 'Decrypt')
        return message


if __name__ == '__main__':
    __red, __green, __yellow, __white = '\033[1;31m', '\033[32;1m', '\033[1;33m', '\033[1;37m'
    self = EncryptTools()
    while True:
        EncryptTools.clearScreen()
        print(f'{__red}{pyfiglet.figlet_format("Encrypt Tools", font="slant")}')
        print(f'{__yellow}1- {__white}Encrypt Message')
        print(f'{__yellow}2- {__white}Decrypt Message')
        try:
            option = int(input(f'{__green}\n- Choose an option (1/2) : '))
        except ValueError:
            print(f'{__red}You Have To Choose A Number !')
            time.sleep(1.7)
        else:
            if option not in [1, 2]:
                print(f'{__red}You Have To Choose 1 or 2 !')
                time.sleep(1.7)
        EncryptTools.clearScreen()
        key = str(input(f'{__green}- Please Enter Your Key : {__white}'))
        if not EncryptTools.LettersCheck(key):
            print(f'{__red}Key Letters Should Be English Letters, Numbers OR Characters !')
            time.sleep(1.7)
            continue
        message = str(input(f'{__green}- Please Enter Your Message : {__white}'))
        if not EncryptTools.LettersCheck(message):
            print(f'{__red}Message Letters Should Be English Letters, Numbers OR Characters !')
            time.sleep(1.7)
            continue

        match option:
            case 1:
                result = EncryptTools.Encrypt(message, key)
                print(f'\n{__yellow}- Your Encrypted Message -> {__white}{result}')
            case 2:
                result = EncryptTools.Decrypt(message, key)
                print(f'\n{__yellow}- Your Decrypted Message -> {__white}{result}')
        input(f'{__red}\nPress on any key to continue')
