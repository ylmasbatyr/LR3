import os
import subprocess
import sys

def main():
    os.system("cmd.exe")
    
    print("Выполнили: Ульмашев Ислам Русланович, Духнай Николай Евгеньевич")
    print("Группа: 21-К-АС2\n")
    
    docs = os.path.join(os.environ['USERPROFILE'], 'Documents')
    print(f"Папка: {docs}\n")
    
    for item in os.listdir(docs):
        path = os.path.join(docs, item)
        if os.path.isdir(path):
            print(f"[DIR]  {item}")
        else:
            print(f"[FILE] {item}")
    
    input("\nНажмите Enter...")

if __name__ == "__main__":
    main()

