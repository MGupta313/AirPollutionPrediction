import numpy as np
import pandas as pd
from pandas import datetime
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler

#Function to calculate so2 individual pollutant index(si)
def calculate_si(so2):
	si=0
	if (so2<=40):
	 si= so2*(50/40)
	if (so2>40 and so2<=80):
	 si= 50+(so2-40)*(50/40)
	if (so2>80 and so2<=380):
	 si= 100+(so2-80)*(100/300)
	if (so2>380 and so2<=800):
	 si= 200+(so2-380)*(100/800)
	if (so2>800 and so2<=1600):
	 si= 300+(so2-800)*(100/800)
	if (so2>1600):
	 si= 400+(so2-1600)*(100/800)
	return si

#Function to calculate no2 individual pollutant index(ni)
def calculate_ni(no2):
	ni=0
	if(no2<=40):
	 ni= no2*50/40
	elif(no2>40 and no2<=80):
	 ni= 50+(no2-14)*(50/40)
	elif(no2>80 and no2<=180):
	 ni= 100+(no2-80)*(100/100)
	elif(no2>180 and no2<=280):
	 ni= 200+(no2-180)*(100/100)
	elif(no2>280 and no2<=400):
	 ni= 300+(no2-280)*(100/120)
	else:
	 ni= 400+(no2-400)*(100/120)
	return ni

#Function to calculate no2 individual pollutant index(rpi)
def calculate_(rspm):
	rpi=0
	if(rpi<=30):
	 rpi=rpi*50/30
	elif(rpi>30 and rpi<=60):
	 rpi=50+(rpi-30)*50/30
	elif(rpi>60 and rpi<=90):
	 rpi=100+(rpi-60)*100/30
	elif(rpi>90 and rpi<=120):
	 rpi=200+(rpi-90)*100/30
	elif(rpi>120 and rpi<=250):
	 rpi=300+(rpi-120)*(100/130)
	else:
	 rpi=400+(rpi-250)*(100/130)
	return rpi

#Function to calculate no2 individual pollutant index(spi)
def calculate_spi(spm):
	spi=0
	if(spm<=50):
	 spi=spm
	if(spm<50 and spm<=100):
	 spi=spm
	elif(spm>100 and spm<=250):
	 spi= 100+(spm-100)*(100/150)
	elif(spm>250 and spm<=350):
	 spi=200+(spm-250)
	elif(spm>350 and spm<=450):
	 spi=300+(spm-350)*(100/80)
	else:
	 spi=400+(spm-430)*(100/80)
	return spi

# function to calculate the air quality index (AQI) of every data value as per Indian govt standards
def calculate_aqi(si,ni,spi,rpi):
	aqi=0
	if(si>ni and si>spi and si>rpi):
	 aqi=si
	if(spi>si and spi>ni and spi>rpi):
	 aqi=spi
	if(ni>si and ni>spi and ni>rpi):
	 aqi=ni
	if(rpi>si and rpi>ni and rpi>spi):
	 aqi=rpi
	return aqi

def gradient_descent(x, y, theta, iterations, alpha):
	m = y.size # No. of data points
	past_costs = []
	past_thetas = [theta]
	for i in range(iterations):
		prediction = np.dot(x, theta)
		error = prediction - y
		cost = 1/(2*m) * np.dot(error.T, error)
		past_costs.append(cost)
		theta = theta - (alpha * (1/m) * np.dot(x.T, error))
		past_thetas.append(theta)
	return past_thetas, past_costs

def rmse(y, y_pred):
	rmse = np.sqrt(sum(y - y_pred))
	return rmse


def get_predictions_helper(data_og, col_name):

	# do some preprocessing
	df = data_og[[col_name,'date']]
	df = df.set_index('date').resample('M')[col_name].mean()
	data = df.reset_index(level=0, inplace=False)
	data = data[np.isfinite(data[col_name])]
	data = data[data.date != '1970-01-31']
	data = data.reset_index(drop=True)

	# make year column
	data['year'] = data['date'].dt.year
	df = data[[col_name,'year']].groupby(["year"]).mean().reset_index().sort_values(by='year',ascending=False)
	df = df[np.isfinite(df[col_name])]

	# set up x and y vars for linear regression
	cols = ['year']
	y = df[col_name]
	x = df[cols]
	x = (x - x.mean()) / x.std()
	x = np.c_[np.ones(x.shape[0]), x]

	# hyper parameters
	alpha = 0.1
	iterations = 100
	theta = np.random.rand(2) #Picking random values to start with

	# perform SGD
	past_thetas, past_costs = gradient_descent(x, y, theta, iterations, alpha)
	theta = past_thetas[-1]
	y_pred = x.dot(theta)
	print("Gradient Descent: {:.2f}, {:.2f}".format(theta[0], theta[1]))
	print("RMSE is", np.sqrt(metrics.mean_squared_error(y,y_pred)))

	# get training cost curve
	plt.figure(figsize=(10, 10))
	plt.title('Linear Regression - ' + col_name)
	plt.xlabel('No. of iterations')
	plt.ylabel('Cost')
	plt.plot(past_costs)
	plt.savefig('Linear Regression Training - ' + col_name)
	plt.clf()

	# print actual vs predicted
	dt = pd.DataFrame({'Actual': y, 'Predicted': y_pred})
	x = pd.concat([df, dt], axis=1)
	x_axis = x.year
	y_axis = x.Actual
	y1_axis = x.Predicted
	plt.plot(x_axis, y_axis)
	plt.plot(x_axis, y1_axis)
	plt.title("Actual vs Predicted " + col_name,fontsize=20)
	plt.legend(["actual ","predicted"])
	plt.xlabel("Year", fontsize=20)
	plt.ylabel(col_name, fontsize=20)
	plt.tick_params(labelsize=20)
	plt.savefig('Actual vs Predicted ' + col_name)
	plt.clf()

	# make future predictions
	data=[[-1,2016], [-1, 2017], [-1, 2018], [-1, 2019], [-1, 2020], [-1,2021], [-1,2022], [-1,2023], [-1,2024], [-1,2025], [-1,2026], [-1,2027], [-1,2028], [-1,2029], [-1,2030]]
	scaler = MinMaxScaler(feature_range=(-1,1)) # normalization
	scaler.fit(data)
	x = scaler.transform(data)
	print("Predictions", - (x.dot(theta)))


# read data
data = pd.read_csv('../data/pollution-data.csv', encoding="ISO-8859-1")
data.fillna(0, inplace=True)

# create new columns for pollutant indexes and AQI
data['ni'] = data['no2'].apply(calculate_ni)
data['spi'] = data['spm'].apply(calculate_spi)
data['si'] = data['so2'].apply(calculate_si)
data['rpi'] = data['rspm'].apply(calculate_si)
data['AQI'] = data.apply(lambda x:calculate_aqi(x['si'],x['ni'],x['spi'],x['rpi']),axis=1)

data['date'] = pd.to_datetime(data['date'],format='%Y-%m-%d') # date parse
data['year'] = data['date'].dt.year # year
data['year'] = data['year'].fillna(0.0).astype(int)
data_og = data[(data['year']>0)]

for state in data_og.state.unique():
	print("state" + state)
	data = data_og[(data_og['state'] == state)]


# get_predictions_helper(data_og, 'AQI')
# get_predictions_helper(data_og, 'no2')
# get_predictions_helper(data_og, 'spm')
# get_predictions_helper(data_og, 'so2')
# get_predictions_helper(data_og, 'rspm')





def fit_polynomial():
	import operator
	import numpy as np
	import matplotlib.pyplot as plt
	from sklearn.linear_model import LinearRegression
	from sklearn.metrics import mean_squared_error, r2_score
	from sklearn.preprocessing import PolynomialFeatures

	np.random.seed(0)
	x = 2 - 3 * np.random.normal(0, 1, 20)
	y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)

	# transforming the data to include another axis
	x = x[:, np.newaxis]
	y = y[:, np.newaxis]

	polynomial_features= PolynomialFeatures(degree=2)
	x_poly = polynomial_features.fit_transform(x)

	model = LinearRegression()
	model.fit(x_poly, y)
	y_poly_pred = model.predict(x_poly)

	rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
	r2 = r2_score(y,y_poly_pred)
	print(rmse)
	print(r2)

	plt.scatter(x, y, s=10)
	# sort the values of x before line plot
	sort_axis = operator.itemgetter(0)
	sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
	x, y_poly_pred = zip(*sorted_zip)
	plt.plot(x, y_poly_pred, color='m')
	plt.show()
