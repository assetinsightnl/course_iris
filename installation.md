# Installation of the software required for this tutorial

#### For a translation in Dutch, please scroll down.

### Validate that PyCharm, Python and TensorFlow are installed correctly
- Open PyCharm
- Open a new, empty Python-file
- Check at File -> Settings -> Project: ... -> Project Interpreter that Python 3.x has been installed. If this is not the case, follow the steps of 'Select Python interepreter' below.
- As first line of the empty Python-file, type 'import tensorflow as tf'
- When the import statement is not underlined by a red line, everything is installed correctly!
- When the import statement is underlined by a red line, TensorFlow has not been installed correctly. At the time of writing, Python 3.5 is the highest version which can be used with TensorFlow (on Windows). It is best to follow the steps of 'Install Python and TensorFlow' below.


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
- Ga naar https://www.python.org/downloads/windows/
  - Let bij het kiezen op dat je voor de 64-bit executable installer gaat (niet de 32-bit!)
  - Kies Python 3.5.4 - 2017-08-08
  - Installeer het in een map die je makkelijk terug kan vinden
- Open command.exe en ga naar de map waar python is geinstalleerd
- Upgrade pip: python.exe -m pip install --upgrade pip
- Installeer tensorflow, numpy, pandas en opencv: python.exe -m pip install tensorflow numpy pandas opencv-python


### Selecteer Python interpreter in PyCharm
- Open een code-bestand in PyCharm of maak een nieuw bestand aan als je dat nog niet hebt gedaan
- Als de geinstalleerde python versie de standaard python is op de computer, wordt dit automatisch de interpreter. Anders:
- Ga naar File -> Settings -> Project: ...
- Klik op Python interpreter
- Rechtsboven, klik op het wieltje en klik op 'Add local'
- Vink 'Existing environment' aan en klik op de drie puntjes aan de rechterkant
- Ga naar de map waar je net Python 3 hebt geinstalleerd en klik 'python.exe' aan, klik op Ok en klik nogmaals op Ok
- Wacht tot rechts onderaan het wieltje niet meer draait en er niet meer staat 'x processes running'
