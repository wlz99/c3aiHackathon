## Inspiration
The human cost of coronavirus has continued to mount, with more than 40.3m cases confirmed globally and more than 1.11m people known to have died. Building an intuitive dashboard visualization tracking the most updated status of Covid is beneficial to the public at large.

## What it does
CovidML is a web application that visualizes the trend of COVID-19 worldwide with future spread prediction. It allows users to effectively visualize current and upcoming situations of the pandemic spread.

## How We built it
Our web app is based on the Flask python framework. We obtained multiple datasets from c3.ai datalake. The visualizations on the plots page display the status quo of infection cases and fatalities across the world using Datawrapper tool. We produced geo-referenced plots using a combination of libraries. We used pandas to generate a data-frame for the dataset, and then tried different models to forecast the infection trends.

## Challenges We ran into
Mining and analyzing the data to build the data visualizations was a hard step. Even with perfect reporting, there are fundamental delays in what such data can tell us. For example, new infections today reflect virus activity as of 9 to 13 days ago (which depends, in turn, on social distancing interventions from up to 17 days prior), as derived from the lag correlation analysis. Not factoring in such considerations have led to significant over-estimation of hospitalization needs nationwide.

## What's next for CovidML
We hope to expand our web application to cover countries all around the world, add a page that visualized the multiplex impacts of Covid, and try more modeling techniques to forecast the future trend of the pandemic.
