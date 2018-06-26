# Classificatie op de Iris-dataset
Tensorflow example on the Iris dataset. A basic neural network with one hidden layer is created and the programmer can change the parameters in order to get to a better understanding of what the parameters do.

This code is loosly based on https://github.com/EdoVaira/Iris-Neural-Network

### For a translation in Dutch, please scroll down.

If you have installed PyCharm, Python 3 and TensorFlow correctly, continue with this readme. Otherwise, if one or more of these elements are not yet installed correctly, first finish the instructions in [installation.md ](https://github.com/assetinsightnl/course_iris/blob/master/installation.md).

Walk through the next steps in order to train and test neural network v0.00001:
1. Open iris.py in PyCharm.
2. Scroll through the code. It is not neccesary to understand the all the code.
3. Select the correct interpreter (Python 3) and make sure the following packages are installed: tensorflow, pandas, numpy and opencv-python. In [installation.md ](https://github.com/assetinsightnl/course_iris/blob/master/installation.md) an explanation is provided how a interpreter can be selected in PyCharm.
4. Right-click on the tab 'iris.py' in PyCharm and click on 'Run iris' (near the bottom).
5. The output generated can contain a TensorFlow-warning; this most likely can be ignored. The rest of the output should be similar to:

Training the model...

Epoch 50 | Loss: 51.33775

Epoch 100 | Loss: 49.221706

Epoch 150 | Loss: 44.0493

Epoch 200 | Loss: 32.334545

Epoch 250 | Loss: 27.743769

| Real / Predicted | Iris-setosa | Iris-versicolor | Iris-virginica |
|------------------|-------------|-----------------|----------------|
| Iris-setosa      | 2           | 0               | 0              |
| Iris-versicolo   | 2           | 0               | 2              |
| Iris-virginica   | 1           | 0               | 3              |

For every 50th epoch the loss will be printed; the loss should decrease when the number of runned epochs increase. When the network is fully trained, the confusion matrix will be printed, which compares the actual classes of the test data against the predicted classes of the same test data. The left side of the confusion matrix contains the actual classes, and the column names represent the predicted classes.

### Research questions
By editing the parameters between lines 129 and 148, the trained network can improve or worsen. Try to answer the following questions:
- What is the effect of shuffling of not shuffling the data? (Try to figure out what part of the data will be used for training, and what part will be used for testing)
- What is a reasonable size for the train set (and hence the test set)?
- What is the effect of varying the number of hidden nodes in the hidden layer?
- What is the effect of varying the learning rate and, if at all, how does this relate to the number of epochs?
- Which two columns combined will provide the best prediction?
- What is your best parameter configuration and why?

When all these question have been answered, more complex questions can be considered:
- Which other optimizers can be used and what is the effect of using another optimizer? (Go to the line 'optimizer = tf.train.GradientDescentOptimizer(...)' in the code)
- Which other loss functions can be used and what is the effect of using another loss function? (Go to the line 'loss = tf.reduce_mean(...)' in the code)
- Which other activation functions can be used and what is the effect of using other activation functions? (Go to the lines 'hidden_output = tf.nn.relu(...)' and 'final_output = tf.nn.softmax(...)' in the code)

## Nederlandse vertaling
Indien PyCharm, Python 3 en TensorFlow allemaal correct zijn geinstalleerd, ga dan verder met deze readme. Indien minstens een van deze drie onderdelen niet correct is geinstalleerd, doorloop dan eerst de stappen in installation.md

Doorloop de volgende stappen om neural network v0.00001 te trainen en te testen:
1. Open iris.py in PyCharm.
2. Scroll door het bestand en bekijk hoe de code een beetje in elkaar zit. Het is niet nodig om het in detail door te nemen.
3. Selecteer de juiste interpreter (Python 3) als dat nog niet het geval is. In installation.md staat uitgelegd hoe de interpreter in PyCharm in te stellen is.
4. Klik met de rechtermuisknop op het tabblad 'iris.py' in PyCharm en klik vrijwel helemaal onderaan op het groene driehoekje 'Run iris'
5. De output die wordt gegenereerd kan in eerste instantie een warning bevatten van TensorFlow; dit kan genegeerd worden. De verdere output zal lijken op:

Training the model...

Epoch 50 | Loss: 51.33775

Epoch 100 | Loss: 49.221706

Epoch 150 | Loss: 44.0493

Epoch 200 | Loss: 32.334545

Epoch 250 | Loss: 27.743769

| Real / Predicted | Iris-setosa | Iris-versicolor | Iris-virginica |
|------------------|-------------|-----------------|----------------|
| Iris-setosa      | 2           | 0               | 0              |
| Iris-versicolo   | 2           | 0               | 2              |
| Iris-virginica   | 1           | 0               | 3              |

Voor elke 50e epoch wordt de loss geprint; in principe moet de loss afnemen naarmate het aantal epoch toeneemt. Als het netwerk helemaal is getraind wordt de confusion matrix getoond met de uitkomst van de testdata. Aan de linker kant staan de daadwerkelijke klassen, en bovenaan staan de voorspelde klassen.

### Onderzoeksvragen
Door de parameters tussen regels  129 en 148 aan te passen, kan het netwerk beter of slechter worden getraind. Probeer de onderstaande vragen te beantwoorden:
- Wat is het effect van wel/niet shuffelen van de data?
- Wat is een verstandige grootte voor de testset?
- Wat is het effect van minder of juist meer hidden nodes?
- Wat is het effect van de learning rate en hoe hangt dat samen met het aantal epochs?
- Welke twee kolommen hebben gecombineerd de best voorspellende waarde?
- Wat is jouw beste configuratie en waarom?

Mochten deze vragen allemaal beantwoord zijn, bekijk dan de volgende vragen:
- Welke optimizers zijn er nog meer en heeft een andere optimizer effect op het resultaat? Zie 'optimizer = tf.train.GradientDescentOptimizer(...)' in de code)
- Welke loss functies zijn er nog meer en heeft een andere loss functie effect op het resultaat? (Zie 'loss = tf.reduce_mean(...)' in de code)
- Wat is een activation function en heeft een andere activation function effect op het resultaat? (Zie 'hidden_output = tf.nn.relu(...)' en 'final_output = tf.nn.softmax(...)' in de code)
