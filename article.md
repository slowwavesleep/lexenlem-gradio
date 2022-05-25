## Description

The idea is to utilize the input of an external resource (a `lexicon` — Vabamorf morphological analyzer in this 
particular case) as an additional input to improve the results of a neural lemmatizer model. Said additional input 
is a concatenation of one or more lemma candidates provided by Vabamorf. Morphological features and the part of 
speech are provided by Stanza in this demo, although it's possible to use native Vabamorf features as well 
(the results, however, are going to be slightly worse).

The lexicon-enhanced lemmatizer itself is based on an older version of Stanza. The models were trained on the 
EstonianDependency Treebank version 2.7.

Two variants of lemmatization are provided in the demo: regular lemmatization and lemmatization with
special symbols, which are `=` and `_`, denoting morphological derivation and separating parts of
compound words respectively. The latter was trained on the original data with Vabamorf set to output
these special symbols, while the latter was trained with `=` and `_` removed from the data and
vabamorf output.

<p align="center">
    <img alt="Scheme" src="https://raw.githubusercontent.com/slowwavesleep/lexicon-enhanced-lemmatization/master/img/StanfordNLP_Lemmatizer-Overall_Modified.jpg" >
</p>

