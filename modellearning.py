from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")


f = data[["mileage"]]
t = data["vehicle_score"]

nayanmodel = LinearRegression()

nayanmodel.fit(f,t)

x = 9
y =   nayanmodel.predict([[x]]) 
newt = nayanmodel.predict(f)

plt.plot(f,t)
plt.plot(f,newt)
plt.scatter(x,y)
plt.show()