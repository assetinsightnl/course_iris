## Controleer of PyCharm, Python en TensorFlow juist op je laptop zijn geïnstalleerd:
- Open PyCharm
- Open een nieuw leeg Python-bestand (noem het b.v. test.py)
- Controleer bij File -> Settings -> Project: ... -> Project Interpreter dat Python 3.x is geselecteerd (zo niet; volg de stappen van 'Selecteer Python interpreter' hieronder)
- Type bovenaan 'import tensorflow as tf'
- Als er geen rood kringeltje onder dit statement komt te staan, is alles correct geinstalleerd!
  - Open het bestand iris.py en ga aan de slag!
- Als er wel een rood kringeltje onder dit statement komt te staan, is Tensorflow niet (correct) geinstalleerd.
  - Ga naar het configuratiescherm en verwijder Python 3.6.x en volg de stappen van 'Installeer Python en Tensorflow' (ja, Python moet verwijderd worden helaas)


## Installeer PyCharm:
- Ga naar https://www.jetbrains.com/pycharm/download/#section=windows en download en installeer de Community versie van PyCharm


## Installeer Python en Tensorflow:
- Ga naar https://www.python.org/downloads/windows/
  - Let bij het kiezen op dat je voor de 64-bit executable installer gaat (niet de 32-bit!)
  - Kies Python 3.5.4 - 2017-08-08
  - Installeer het in een map die je makkelijk terug kan vinden
- Open command.exe en ga naar de map waar python is geinstalleerd
- Upgrade pip: python.exe -m pip install --upgrade pip
- Installeer tensorflow, numpy, pandas en opencv: python.exe -m pip install tensorflow numpy pandas opencv-python


## Selecteer Python interpreter in PyCharm
- Open een code-bestand in PyCharm of maak een nieuw bestand aan als je dat nog niet hebt gedaan
- Als de geinstalleerde python versie de standaard python is op de computer, wordt dit automatisch de interpreter. Anders:
- Ga naar File -> Settings -> Project: ...
- Klik op Python interpreter
- Rechtsboven, klik op het wieltje en klik op 'Add local'
- Vink 'Existing environment' aan en klik op de drie puntjes aan de rechterkant
- Ga naar de map waar je net Python 3 hebt geinstalleerd en klik 'python.exe' aan, klik op Ok en klik nogmaals op Ok
- Wacht tot rechts onderaan het wieltje niet meer draait en er niet meer staat 'x processes running'
