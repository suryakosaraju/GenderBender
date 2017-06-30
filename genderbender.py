from sklearn import tree

#[height,weight,shoe size ]

X = [[166,60,34],[186,80,44],[170,72,40],[160,75,38],[186,88,44],[168,70,34],[193,90,48],[166,60,34],[196,100,48],[186,87,44],[176,70,32]]

Y= ['female','male','female','female','male','female','male','female','male','male','female']

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(X,Y)

prediction = classifier.predict([[185,100,43]])

print prediction