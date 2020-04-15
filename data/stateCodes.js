var mapCodeToState = {
  "AP": "Andhra Pradesh",
  "AR": "Arunachal Pradesh",
  "AS": "Assam",
  "BR": "Bihar",
  "CT": "Chhattisgarh",
  "DL": "Delhi",
  "GA": "Goa",
  "GJ": "Gujarat",
  "HR": "Haryana",
  "HP": "Himachal Pradesh",
  "JK": "Jammu & Kashmir",
  "JH": "Jharkhand",
  "KA": "Karnataka",
  "KL": "Kerala",
  "MP": "Madhya Pradesh",
  "MH": "Maharashtra",
  "MN": "Manipur",
  "ML": "Meghalaya",
  "MZ": "Mizoram",
  "NL": "Nagaland",
  "OR": "Odisha",
  "PB": "Punjab",
  "RJ": "Rajasthan",
  "SK": "Sikkim",
  "TN": "Tamil Nadu",
  "TR": "Tripura",
  "UP": "Uttar Pradesh",
  "UT": "Uttaranchal",
  "WB": "West Bengal",
  "AN": "Andaman and Nicobar",
  "LD": "Lakshadweep",
};

var state_pollution = 0;
var city_pollution = 0;
d3.json("./data/pollution-stats-state.json", function(data) {
  state_pollution = data;
});
d3.json("./data/pollution-stats-city.json", function(data) {
  city_pollution = data;
});
