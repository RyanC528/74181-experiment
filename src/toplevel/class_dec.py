#idk where this should have FloatingPointError
from dataclasses import dataclass

@dataclass
class lang_info:
    #input vars
    name: str
    path: str

    #prefined vars
    time: float = 0
    is_running: bool = False

#PYTHON DECS
python: lang_info = lang_info(
    "python",
    "src/lowlevel/python/control.py",
)


#C DECS
c: lang_info = lang_info(
    "C",
    "src/lowlevel/c/control.c"
)

#KOTLIN DECS
kotlin: lang_info = lang_info(
    "Kotlin",
    "src/lowlevel/kotlin/control.kt"
)
