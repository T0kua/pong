#получения значения в словаре по ключу
def get(key: str) -> str:
    file = open("json.txt","r",encoding="UTF-8")
    diction = {}
    text = [{i.split("=")[0]:i.split("=")[1].replace("\n","")} for i in file.readlines()]
    file.close()
    for i in text:
        diction.update(i)
    if key in diction.keys(): 
        return diction[key]
    raise TypeError(f"unvalid key: \"{key}\" is not such")

#изменение значения в словаре по ключу
def set(key: str, value: str) -> None:
    file = open("json.txt","r",encoding="UTF-8")
    text = file.readlines()
    file.close()
    tremor = True
    for i in range(len(text)):
        if key in text[i]:
            text[i] = f'{key}={value}\n'
            tremor = False
    if tremor:
        raise TypeError(f"unvalid key: \"{key}\" is not such")
    file = open("json.txt","w",encoding="UTF-8")
    file.writelines(text)
    file.close()





#тест
if (__name__ == "__main__"):
    set("automessage","ок")
    print(get("automessage"))
