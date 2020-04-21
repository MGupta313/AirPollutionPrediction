This is an interactive visualization for prediction of air pollution trends in India.
We hope this can be an useful tool for environmentalists and the government of India to see air pollution trends at various levels of
city and state granularity.

References:
- India state and city map data was created after referencing this blog: https://gist.github.com/palerdot/a10570161fc6907f717b.
- The code for Polynomial Regression code was created after referencing this blog: https://towardsdatascience.com/polynomial-regression-bbe8b9d97491
- The pre-processing/calculation of AQI is based upon on the following post: https://www.kaggle.com/anbarivan/indian-air-quality-analysis-prediction-using-ml


TODO:
- [ ] Add the yearly split into the pre-processed data.  
- [ ] Add Year picker at the bottom of the map. Only display selected year's data.  

- [ ] Zooming in should show all the cities (as icons).  
- [ ] Hovering over these cities should pull up their respective AQI values. (data is data/pollution-stats-city.json).  

- [ ] Show trendline during hover. Need to create mock data for this first.  
