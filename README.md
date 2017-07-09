# Sensitivity-Analysis
Sensitivity Analysis of movie review and classifying them as either positive or negative using Python

# What I did
I tried sensitivity analysis of movie reviews and classified them as either positive or negative. I am using <b>nltk</b> library for the natural language processing. Since natural language processing uses machine learning so it programs might not yeild a right result every time. So these are the steps I followed:-<br>
  1. <b>Acquire a raw dataset</b>- The nltk library offers a huge range of datasets mainly for natural language processing. One of them is movie reviews and it can be downloaded using the <b>nltk.download()</b> from the Python prompt. You will have the dataset depending on the path you seleceted during download. For me it was <b>/root/nltk_data/corpora/movie_reviews/</b>
  2. <b>Process the raw dataset</b>- Since we cannot use the raw dataset directly, I extracted every word from the txt files in /root/nltk_data/corpora/movie_reviews/pos/ and /root/nltk_data/corpora/movie_reviews/neg/ and associated them with "pos" or "neg" depending on which directory it is found and stored it in a list of tuples where each tuple contained the list of words of a single file and the name of the directory. E.g (<list of words of cv000_29416.txt>, "neg") etc. I called it documents.
  3. <b>A little bit more processing</b>- Along with the above processing I also removed the stop words and puctuations and shuffled the list documents.
  4. <b>Create a list of every word in the movie_reviews folder</b>- I created another list called all_words where I stored every word in the files. Then I arranged it according to the frquency of each word.
  5. <b>Create feature set using all_words and documents</b>- The documents and the all_words list is used to create a new list called featureset which is actually a list of tuples where each tuple consists of a dictionary and the name of a folder.
  6. <b>Create a training set and testing set from feature set</b>- The training set contains 3/4 th of the feature set whereas the testing set contains the latter 1/4 th.
  7. <b>Train and test algorithms</b>- I used a total of 8 algorithms. I trained and tested all of them against same training and testing set
  
 # Note
 I have saved all those classifiers to the classifiers folder with their respective names using the pickle library.
 
 # Usage
    python create_classifiers.py
    python test.py
   
