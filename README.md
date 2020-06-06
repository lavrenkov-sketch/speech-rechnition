### Особенности
offline распознавание русской речи на базе PocketSphinx и WebSocket


### Требования
Python 3.3+ или Python 2.7 [pickle,fnmatch,face_recognition,cv2,numpy]
Linux

файлы словаря и пр.:
```
zero_ru.cd_cont_4000
calc2.jsgf
vocabular.dict
```
закинуть по пути:

/usr/local/lib/python3.8/dist-packages/pocketsphinx/model

### Варианты установки:
```bash
pip3 install -r reguiments.txt
```
## Применение
```bash
python3 speech_to_text.py known/
```
