from fuzzywuzzy import fuzz
opts = {
    "greetings": ('привет', "здарова", "салам"),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты')
    }
}
def recognize_cmd(cmd):
    RC = {'greetings': '','cmd': '', 'percent': 50}
    for c,v in opts['cmds'].items():
        print("COMMAND:", c), print("PERCENT:", v)
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            print(vrt)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
            print("FUZZ:", vrt)
    
    return RC

recognize_cmd(input(""))