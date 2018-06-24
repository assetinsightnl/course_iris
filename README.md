# iris
Tensorflow example on the Iris dataset

This code is based on https://github.com/EdoVaira/Iris-Neural-Network

Indien PyCharm, Python 3 en TensorFlow allemaal correct zijn geinstalleerd, ga dan verder met deze readme. Indien minstens een van deze drie onderdelen niet correct is geinstalleerd, doorloop dan eerst de stappen in installation.txt

Doorloop de volgende stappen om neural network v0.00001 te trainen en te testen:
1. Open iris.py in PyCharm
2. Scroll door het bestand en bekijk hoe de code een beetje in elkaar zit. Het is niet nodig om het in detail door te nemen, maar enkele aspecten in de code zullen herkend moeten worden aangezien ze zojuist in de presentatie zijn genoemd.
3. Selecteer de juiste interpreter (Python 3) als dat nog niet het geval is. In installation.txt staat uitgelegd hoe de interpreter in PyCharm in te stellen is.
4. Klik met de rechtermuisknop op het tabblad 'iris.py' in PyCharm en klik vrijwel helemaal onderaan op het groene driehoekje 'Run iris'
5. De output die wordt gegenereerd kan in eerste instantie een warning bevatten van TensorFlow; dit kan genegeerd worden. De verdere output zal lijken op:

Training the model...

Epoch 50 | Loss: 51.33775

Epoch 100 | Loss: 49.221706

Epoch 150 | Loss: 44.0493

Epoch 200 | Loss: 32.334545

Epoch 250 | Loss: 27.743769

| Echt / Voorspeld | Iris-setosa | Iris-versicolor | Iris-virginica |
|------------------|-------------|-----------------|----------------|
| Iris-setosa      | 2           | 0               | 0              |
| Iris-versicolo   | 2           | 0               | 2              |
| Iris-virginica   | 1           | 0               | 3              |

Voor elke 50e epoch wordt de loss geprint; in principe moet de loss afnemen naarmate het aantal epoch toeneemt. Als het netwerk helemaal is getraind wordt de confusion matrix getoond met de uitkomst van de testdata. Aan de linker kant staan de daadwerkelijke klassen, en bovenaan staan de voorspelde klassen.

Door de parameters tussen regels  129 en 148 aan te passen, kan het netwerk beter of slechter worden getraind. Probeer de onderstaande vragen te beantwoorden:
- Wat is het effect van wel/niet shuffelen van de data?
- Wat is een verstandige grootte voor de testset?
- Wat is het effect van minder of juist meer hidden nodes?
- Wat is het effect van de learning rate en hoe hangt dat samen met het aantal epochs?
- Welke twee kolommen hebben gecombineerd de best voorspellende waarde?
- Wat is jouw beste configuratie en waarom?

Mochten deze vragen allemaal beantwoord zijn, bekijk dan de volgende vragen:
- Welke optimizers zijn er nog meer en heeft een andere optimizer effect op het resultaat? Zie optimizer = tf.train.GradientDescentOptimizer(...) in de code)
- Welke loss functies zijn er nog meer en heeft een andere loss functie effect op het resultaat? (Zie loss = tf.reduce_mean(...) in de code)
- Wat is een activation function en heeft een andere activation function effect op het resultaat? (Zie hidden_output = tf.nn.relu(...) en final_output = tf.nn.softmax(...) in de code)
