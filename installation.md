# Installation of the software required for this tutorial

#### For a translation in Dutch, please scroll down.

### Validate that PyCharm, Python and TensorFlow are installed correctly
- Open PyCharm
- Open a new, empty Python-file
- Check at File -> Settings -> Project: ... -> Project Interpreter that Python 3.x has been installed. If this is not the case, follow the steps of 'Select Python interepreter' below.
- As first line of the empty Python-file, type 'import tensorflow as tf'
- When the import statement is not underlined by a red line, everything is installed correctly!
- When the import statement is underlined by a red line, TensorFlow has not been installed correctly. At the time of writing, Python 3.5 is the highest version which can be used with TensorFlow (on Windows). It is best to follow the steps of 'Install Python and TensorFlow' below.

### Install PyCharm
- Go to https://www.jetbrains.com/pycharm/download/#section=windows and download and install the Community version of PyCharm (64-bit)

### Install Python and TensorFlow
At the time of writing, TensorFlow cannot be used with Python 3.6.x on Windows, and hence Python 3.5 will be downloaded.
- Go to https://www.python.org/downloads/windows/
  - Make sure you download the 64-bit executable installer, not the 32-bit!
  - Download Python 3.5.4
  - Install Python in a folder which is easy to go to
- Open cmd.exe and go the the folder in which Python is installed (this is a fail-safe; if other python version are installed as well, we know for sure that the correct Python interpreter is selected)
- Upgrade pip: 'python.exe -m pip install --upgrade pip'
- Install the packages tensorflow, numpy, pandas and opencv: 'python.exe -m pip install tensorflow numpy pandas opencv-python'

### Select the correct Python interpreter in PyCharm
- Open a .py-file in PyCharm or create a new .py file
- When the installed Python version is the standard Python interpreter on the computer, this will automatically become the interpreter. Otherwise:
- Go to File -> Settings -> Project: ...
- Select 'Python interpreter'
- Top-right, klick the wheel and select 'Add local'
- Select 'Existing environment' and click on the three dots on the right
- Go the the folder where Python 3.5 was installed and select 'python.exe'
- Click 'Ok' and click 'Ok' once more
- Wait until on the bottom right the wheel is no longer spinning, with the text 'x processes running'

## Nederlandse vertaling
### Controleer of PyCharm, Python en TensorFlow juist op je laptop zijn geinstalleerd:
- Open PyCharm
- Open een nieuw leeg Python-bestand (noem het b.v. test.py)
- Controleer bij File -> Settings -> Project: ... -> Project Interpreter dat Python 3.x is geselecteerd (zo niet; volg de stappen van 'Selecteer Python interpreter' hieronder)
- Type bovenaan 'import tensorflow as tf'
- Als er geen rood kringeltje onder dit statement komt te staan, is alles correct geinstalleerd!
- Als er wel een rood kringeltje onder dit statement komt te staan, is Tensorflow niet (correct) geinstalleerd. Op dit moment werkt TensorFlow onder Windows alleen met Python 3.5 en lager, en nog niet met 3.6. Volg de stappen van 'Installeer Python en Tensorflow' om het allemaal correct te installeren.

### Installeer PyCharm:
- Ga naar https://www.jetbrains.com/pycharm/download/#section=windows en download en installeer de Community versie van PyCharm

### Installeer Python en Tensorflow:
Op dit moment werkt TensorFlow nog niet met Python 3.6.x onder Windows, vandaar dat Python 3.5 wordt gedownload.
- Ga naar https://www.python.org/downloads/windows/
  - Let bij het kiezen op dat je voor de 64-bit executable installer gaat (niet de 32-bit!)
  - Kies Python 3.5.4
  - Installeer het in een map die je makkelijk terug kan vinden
- Open cmd.exe en ga naar de map waar python is geinstalleerd (dit is voor de zekerheid; als er ook andere Python versies zijn geïnstalleerd, weten we nu zeker dat de juiste Python interpreter is geselecteerd)
- Upgrade pip: 'python.exe -m pip install --upgrade pip'
- Installeer tensorflow, numpy, pandas en opencv: 'python.exe -m pip install tensorflow numpy pandas opencv-python'

### Selecteer Python interpreter in PyCharm
- Open een code-bestand in PyCharm of maak een nieuw bestand aan als je dat nog niet hebt gedaan
- Als de geinstalleerde Python versie de standaard Python is op de computer, wordt dit automatisch de interpreter. Anders:
- Ga naar File -> Settings -> Project: ...
- Klik op Python interpreter
- Rechtsboven, klik op het wieltje en klik op 'Add local'
- Vink 'Existing environment' aan en klik op de drie puntjes aan de rechterkant
- Ga naar de map waar je net Python 3 hebt geinstalleerd en klik 'python.exe' aan, klik op Ok en klik nogmaals op Ok
- Wacht tot rechts onderaan het wieltje niet meer draait en er niet meer staat 'x processes running'
