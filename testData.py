#Convert each of the testing data series to a Word2Vec embedding
test = []

for i in title_test:
  temp = np.array(embed(i))
  test.append(temp)

#Accounts for the different length of words in test data
test = tf.keras.preprocessing.sequence.pad_sequences(test,dtype='float')