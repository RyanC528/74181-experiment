import sys
import time
from class_dec import lang_info
import subprocess
from gui import GUI

def invoke(lang:lang_info, in_file: str) -> bool:
    err = subprocess.run([lang.path,in_file, lang.outfile], capture_output= True)

    if err == 0x00:
        return False
    elif err == 0x01:
        print("subrocess control returned error value")
        sys.exit()
        return True
    else:
        print("subprocess somehow return not 0 or 1, something majorly broke up")
        sys.exit()
        return True


def run_progam(langs: list[lang_info], in_file: str, gui: GUI) -> None:
    start_time: float = 0
    end_time: float = 0

    err: bool = False

    for lang in langs:
        start_time = time.time()

        err = invoke(lang, in_file)

        if err == False:
            end_time = time.time()

            lang.time = end_time - start_time

            gui.mainloop()
        else:
            print("SHIT BROKE")
            sys.exit()
