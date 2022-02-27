from sklearn.model_selection import train_test_split

#Split data into training and testing dataset
title_train, title_test, y_train, y_test = train_test_split(titles, labels, test_size=0.2,\
                                                            random_state=1000)