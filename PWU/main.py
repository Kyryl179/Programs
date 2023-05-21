from subprocess import call

try:
    call(["python", "game.py"])
except Exception as e: 
    print(e)
    input()