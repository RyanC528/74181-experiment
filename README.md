# 74181-experiment

Working on an experiment comparing preformence of a few languages when interopted with python.
Basic idea is to have 2 halves of the program, one python control program and a compiled 74181 emulator


PYTHON CONTROL PROGRAM

high level portion of the program

Gui to show what is happening

takes text file input full of random four bit number

times each execution


Compiled language psuedo

takes two text file inputs as an arg

reads 3 random 4 bit numbers in a line of input txt

pipe into an implimentation of a 74181

emulator returns output

write to output txt file

close itself. 

LOOP NEEDS TO BE IN COMPILED LANUGAGE TO AVOID PYTHON BOTTLENECK


LM4181 

ref -> https://www.righto.com/2017/03/inside-vintage-74181-alu-chip-how-it.html

avoid conditional work, instead use bitwise when ever possible


TARGET LANGUAGES
  Min - i know these languages comfertably
  normal python - control
  c
  kotlin

  likely - i know the basics
  c++
  go
  pypi - or another compiled python version

  if i have time and intress - I don't really know these languages
  rust
  zig


dirt structure

main
  src
    toplevel
      gui.py
      invoke.py
      main.py
    74818
      python
        control.py
        chip.py
      c
        c.exe
        control.c
        control.h
        chip.c
        chip.h
        makefile
      kotlin
        kotlin.exe
        control.kt
        chip.kt
        build.kts
  test
  files
    input.txt
    python.txt
    c.txt
    kotlin.txt
  myproject.toml
  .env - idk if needed
  venv
  .gitignore
  requirments.txt
  read.me
