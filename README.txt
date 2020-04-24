README
 

DESCRIPTION:
For the visualization tool front-end we used HTML (Hypertext Markup Language) to set up the core building blocks of the visualization tool. We used CSS (Cascading Style Sheets) to design the appearance of the pop-up boxes, text and various features of the tool.

We preprocessed air quality statistics in addition to using various models to predict future air quality trends and stored this metadata in JSON files. We used D3.js to load the data for our tool. D3 is a JavaScript library for producing dynamic, interactive data visualizations in web browsers. We also used D3 to create and connect tools such as: the bar graph, the trend line graph, the pop-up text boxes, to the visualization tool.

We widely used the JavaScript version 5 package as well. JavaScript enables interactive web pages. It is a multi-paradigm language and supports event-driven and functional styles. It has standard APIs for working with text, dates, regular expressions and document object models. We used JavaScript to implement various integral functions such as: onclick, onhover, generating the color for different states etc.

Our tool relies heavily on displaying geographical data on India and having interactive components. We used Mapbox, which is an open source mapping platform for custom designed maps. We found the polygon data for drawing different states of India on top of the Mapbox map. Their API helped us enable interactive components as well. 

The prediction models are built using Python 3.7, along with a few libraries that support data processing and machine learning. In particular, we use Numpy and Pandas for quickly accessing, storing, and processing pollution data. The pyplot module from matplotlib is used to draw all the graphs, and the Scikit-Learn library is used for building the model, as it includes algorithms such as linear regression and polynomial regression, as well as metrics for evaluation.

INSTALLATION:
Download our code repository and save it in your local directory.
Install Firefox or a similar browser to view the visualization tool.
Disable CORS in your Firefox browser. Cross-Origin Resource Sharing (CORS) is a standard that allows a server to relax the same-origin policy. CORS needs to be disabled in order for the visualization tool to access metadata that has been preprocessed and stored in the code directory.
To disable CORS in Firefox -
Open Firefox, and on the address bar, type about:config.
Click on I'll be careful,I promise! ".
Search for security. fileuri. strict_origin_policy.
Right-click and select Toggle to change the value from false to true.
Close the browser and launch it again.

EXECUTION:
We recommend viewing our visualization with Firefox. Open the code directory. Right-click on the “map.html” file and click on “Open With” and select “Firefox”.
