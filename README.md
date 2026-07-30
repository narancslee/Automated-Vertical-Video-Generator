#ENGLISH
-----------------------------------------------------------
# Automated Video Generator

An automated Python script designed to generate videos optimized for TikTok, YouTube Shorts, and Instagram Reels from raw text files.

## Key Features

* **Automated Text-to-Speech:** Converts input text into high-quality voiceovers using the edge-tts library.
* **Hybrid Audio Synchronization:** Implements a custom, sentence-based generation algorithm to maintain natural human intonation while precisely aligning subtitle chunks.
* **Dynamic Subtitling:** Automatically parses input text into readable, fast-paced subtitle blocks centered on the screen.
* **Smart Background Processing:** Automatically loops the source background video to match the final audio duration and trims excess footage seamlessly.

## Technologies Used

* **Python 3**
* **asyncio** (Asynchronous API handling)
* **edge-tts** (Microsoft Edge Text-to-Speech engine)
* **moviepy** (Video and audio manipulation)

## Quick Start

**1. Preparation**
Place your transcript in a file named `szoveg.txt` in the root directory. 
Place your background video in the root directory and name it `hattervidi.mp4`.

**2. Installation**
Install the required dependencies via pip:
```bash
pip install edge-tts moviepy
```
**3. Execution**
Run the main script to generate your final video:
```bash
python3 main.py
```
The final rendered output will be saved as kesz_video.mp4.
-----------------------------------------------------------
#HUN

# Automatizált Videó Generátor

Egy automatizált Python script, amely nyers szövegfájlokból készít videókat, optimalizálva TikTok, YouTube Shorts és Instagram Reels platformokra.

## Főbb funkciók

* **Automatizált Text-to-Speech:** A bemeneti szöveget kiváló minőségű hanggá alakítja az edge-tts könyvtár segítségével.
* **Hibrid hangszinkronizáció:** Egyedi, mondatalapú generáló algoritmust alkalmaz a természetes emberi hanglejtés megőrzésére, miközben elcsúszás nélkül igazítja a felirattömböket a hanghoz.
* **Dinamikus feliratozás:** A bemeneti szöveget automatikusan rövid, jól olvasható, pörgős feliratblokkokra bontja a képernyő közepén.
* **Intelligens háttérkezelés:** A megadott háttérvideót automatikusan végteleníti, hogy lefedje a generált hang hosszát, a felesleget pedig láthatatlanul levágja.

## Szakmai kihívások és megoldások

A fejlesztés során a legnagyobb technikai kihívást a feliratok és az aszinkron módon generált beszédhang tökéletes szinkronizálása jelentette. A hagyományos, átlagokon alapuló matematikai elosztás a hosszabb videóknál folyamatos elcsúszást eredményezett. Ezt egy saját, hibrid algoritmus tervezésével oldottam meg, amely mondatonként dolgozza fel a szöveget. Így a TTS motor megőrzi a természetes emberi hangsúlyozást, miközben a kód izolált, frame-pontos időzítést számol a hozzá tartozó felirattömböknek.

## Használt technológiák

* **Python 3**
* **asyncio** (Aszinkron API hívások kezelése)
* **edge-tts** (Microsoft Edge Text-to-Speech motor)
* **moviepy** (Videó- és hangfájlok renderelése)

## Használati útmutató

**1. Előkészületek**
Helyezd el a felolvasandó szöveget a `szoveg.txt` fájlba.
Helyezd el a háttérvideót a gyökérmappában `hattervidi.mp4` néven.

**2. Telepítés**
Telepítsd a programhoz szükséges csomagokat a terminálból:
```bash
pip install edge-tts moviepy
```
**3. Futtatás**
Indítsd el a generálást a következő paranccsal:
```bash
python3 main.py
```
