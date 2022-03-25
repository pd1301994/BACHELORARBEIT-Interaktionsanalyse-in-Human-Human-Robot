# Naive Bayes analiser

This program aims to analyse texts using Naive Bayes Algorithms, including the naive basics algorithm, including Multibinomial and Bernoulli data distribution.

#            1st!

````
pip install -r requirements.txt
````

## This program is not yet trained!!!

Because of the amount of space that a .pickle file occupies, the model is not yet trained but the usage is very simple: 

1. Run the file "naive_bayes_train.py" -- This will take a while depending on the type of computer you have. Normally it takes around 5 mins, but not worry if it takes a bit longer. 
2. Run the program "converting_sents.py". This will just read all the already trained algorithm and compare it, so it won´t take long. 
3. The first two steps are just needed to be done the first time! YOU DO NOT HAVE TO TRAIN IT EVERY TIME YOU USE IT!! Now, use the file "main.py" and insert the title of the file you want to analyse. The program is thought to analyse a .txt file, with simple modifications you can analyse any kind of string. 

Now the program is trained and ready to be used. The analyse doesn´t take much time to be done, it depends on the size of your file and the power of your computer, but a file with around 5Kb takes less than 5secs to give a result. 

The result you will obtained is the percentage of the text you introduced which matches with the cathegory (instructions / small_talk). Consider the program does a binar categorization, this means, if the text contains a 60% of "instructions" the other 40% would be cathegorized as "small_talk"




