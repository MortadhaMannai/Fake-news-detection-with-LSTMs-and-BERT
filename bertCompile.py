#Compile model on adam optimizer, binary_crossentropy loss, and accuracy metrics
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#Train model on 5 epochs
model.fit(title_train,y_train,epochs=5)

#Evaluate model on test data
model.evaluate(title_test,y_test)