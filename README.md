# Socioeconomic Privilege and Political Ideology are Associated with Racial Disparity in COVID-19 Vaccination: Methods and Materials

This public repository contains the materials for reproducing the results described in Agarwal et al. (2021) _Socioeconomic Privilege and Political Ideology Are Associated with Racial Disparity in COVID-19 Vaccination_ and additional supplementary analyses. 


## Table of Contents

- [Content Description](#materials)

- [Data Sources for COVID-19 Racial Vaccination by States](#covid_race_data_by_state)

    * [COVID-19 Vaccination Disparity Map](#covid_map)

- [Definition of Vaccination Rate Disparity](#vax_rate_disparity)

- [Missingness](#missing)

- [Summary Statistics for Final Data](#summary_statistics)

    * [Correlation Matrix Heatmap for Final Data](#correlation_map)

- [Main Regression Result](#main_reg)

    * [Base Model Regression Table](#base_model)

 
- [Robustness Checks](#robustness_checks)

    * [Age Group Controls](#age_control)
    
    * [Different Disparity Operationalizations](#disparity_measure)
    
    * [Different Dates and Full Vaccination Rate](#date_ratetype)
    
    * [Residential Mobility](#exodus_test)
    
    * [Recent Positive Rate per COVID-19 Test](#positivity)


<a name="materials"/>

## Content Description
Materials for reproducibility include:

1. [COVID-19 vaccination rate data](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/tree/main/CountyVaccine) and Python code to reproduce the data collection, including:<br>

    a) The notebook [1.CountyVaccine_Automation](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/blob/main/1.CountyVaccine_Automation.ipynb) includes the code to collect the county-level vaccination information by race from the States whose vaccination data is oragnized in a downlable table. In this notebook, the Python code can automatically scrape the data. The States include： Illinois, Texas, Pennsylvania, Indiana, and Virginia. <br>
    
    b) The notebook [1.CountyVaccine_Tableau](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/blob/main/1.CountyVaccine_Tableau.ipynb) is designed to collect the county-level vaccination information by race from the States whose vaccination information is present in a Tableau Dashboard format. In this notebook, the Python code can also automatically scrape the data. The States include：New York, Wisconsin, Ohio, South Carolina, and Oregon.<br>
    
    c) The notebook [1.CountyVaccine_Manual](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/blob/main/1.CountyVaccine_Manual.ipynb) is developed to collect the county-level racial vaccination information from the States whose vaccination information needs to be collected manually before running the code. These States include: California, Tennessee, North Carolina, West Virginia, Maine, and New Jersey. The instructions on manual collections are documented [here](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/tree/main/CountyVaccine/Documents/Part1).<br> 
    
2. [Data](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/tree/main/DataMerge) and [Python code](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/blob/main/2.DataMerge.ipynb) to merge information from the various sources cited in our Supplementary Information (SI) Appendix.

3. Python code for [cleaning the data](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/blob/main/2.DataClean.ipynb). 

4. [Clean data](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/tree/main/StataReg) and [code](https://github.com/CHIDS-UMD/Covid19-Vaccination-Race-Disparity/blob/main/3.StataCode.ipynb) to reproduce our main regression analyses (reported in main text) and robustness checks (reported in SI Appendix) as well as  additional supplementary analyses reported here. 

Below, we also provide additional summary statistics, exploratory data analysis, and full results for the robustness checks described in the SI appendix. 



<a name="covid_race_data_by_state"/>

## Data Sources for COVID-19 Racial Vaccination by States

| State          | # of Counties | Population (million) | # of Valid Counties | Population in Analysis (million) | Data Source                                                                                                                                                   |
|----------------|---------------|----------------------|---------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| California     | 54            | 39.45                | 43                  | 39.09                            | https://covid19.ca.gov/vaccines/#California-vaccines-dashboard                                                                                                |
| Illinois       | 100           | 12.46                | 41                  | 11.41                            | https://www.dph.illinois.gov/covid19/vaccinedata?county=Illinois                                                                                              |
| Indiana        | 88            | 6.62                 | 37                  | 5.31                             | https://www.coronavirus.in.gov/vaccine/2680.htm                                                                                                               |
| Maine          | 16            | 1.34                 | 8                   | 1.01                             | https://www.maine.gov/covid19/vaccines/dashboard                                                                                                              |
| New Jersey     | 21            | 8.88                 | 21                  | 8.88                             | https://www.nj.gov/health/cd/topics/covid2019_dashboard.shtml                                                                                                 |
| New York       | 62            | 19.45                | 48                  | 18.79                            | https://covid19vaccine.health.ny.gov/covid-19-vaccine-tracker                                                                                                 |
| North Carolina | 43            | 8.56                 | 43                  | 8.56                             | https://covid19.ncdhhs.gov/dashboard/data-behind-dashboards                                                                                                   |
| Ohio           | 88            | 11.69                | 57                  | 10.57                            | https://coronavirus.ohio.gov/wps/portal/gov/covid-19/dashboards/covid-19-vaccine/covid-19-vaccination-dashboard                                               |
| Oregon         | 23            | 4.05                 | 11                  | 3.22                             | https://public.tableau.com/profile/oregon.health.authority.covid.19#!/vizhome/OregonCOVID-19VaccinationTrends/OregonCountyVaccinationTrends                   |
| Pennsylvania   | 60            | 12.68                | 40                  | 11.66                            | https://www.health.pa.gov/topics/disease/coronavirus/Vaccine/Pages/Vaccine.aspx                                                                               |
| South Carolina | 46            | 5.15                 | 46                  | 5.15                             | https://scdhec.gov/covid19/covid-19-vaccination-dashboard                                                                                                     |
| Tennessee      | 90            | 6.77                 | 62                  | 6.11                             | https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html                                                                                          |
| Texas          | 236           | 27.66                | 137                 | 26.71                            | https://tabexternal.dshs.texas.gov/t/THD/views/COVID-19VaccineinTexasDashboard/Summary?%3Aorigin=card_share_link&%3Aembed=y&%3AisGuestRedirectFromVizportal=y |
| Virginia       | 132           | 8.53                 | 111                 | 8.21                             | https://www.vdh.virginia.gov/coronavirus/covid-19-vaccine-demographics/                                                                                       |
| West Virginia  | 55            | 1.79                 | 23                  | 1.27                             | https://dhhr.wv.gov/COVID-19/Pages/default.aspx                                                                                                               |
| Wisconsin      | 72            | 5.82                 | 28                  | 4.69                             | https://www.dhs.wisconsin.gov/covid-19/vaccine-data.htm#day                                                                                                   |
| Sum            | 1186          | 180.92               | 756                 | 170.65                           |                                                                                                                                                               |

_Note_. Valid counties are those that were included in our main regression analyses, following the exclusion criteria outlined below in the sample construction figure. 

<a name="covid_map"/>

### COVID-19 Vaccination Disparity Map

![](_img/map.png)


**Figure S1.** Map represents COVID-19 vaccination disparities across 1,186 counties with data by race as of April 19, 2021. Red indicates higher vaccination rates among Whites, and blue indicates higher vaccination rates among Blacks. The vaccination rate in some counties with small numbers of Blacks or Whites exceeded 100%. We exclude those counties in Figure 1. In the regression using data from 756 counties, the range of vaccination disparity is between -52.0% and 66.2%. 


<a name="vax_rate_disparity"/>


<a name="missing"/>

## Missingness


![](_img/missing.png)
**Figure S2.** Patterns of missingness in predictor and outcome variables where white lines indicate values are missing.



<a name="sample_construction"/>

## Sample Construction

The filtering of the data collected for all counties on April 19, 2021. The same method is also applied to the data on March 27 2021, April 07 2021, May 20 2021.

![](_img/Workflow.png)


**Figure S3.** Flowchart depicting sample construction.


<a name="summary_statistics"/>

## Summary Statistics for Final Data

We present descriptive statistics of the variables in our regression analysis in non-standardized units. The table below presents rate and proportion data as percentages for ease of interpretation.  	

| Variable                                 | Description                                                                                            | Source                                                                                                                                                                                                                                            | Data Field             | count | mean   | std    | min     | 0.250  | 0.500  | 0.750  | max     |
|------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|-------|--------|--------|---------|--------|--------|--------|---------|
| CVD                                      | Covid vaccination disparity between White and Black populations in county i.                           | Department of Health in each state                                                                                                                                                                                                                | Vax_DisparityY         | 756   | 12.119 | 10.355 | -18.168 | 4.922  | 10.451 | 17.757 | 53.842  |
| FVD                                      | Flu vaccination disparity between White and Black populations in county i.                             | CMS Mapping Medical Disparity Tool (https://data.cms.gov/mapping-medicare-disparities)                                                                                                                                                            | FluVax_DisparityY      | 756   | 15.185 | 6.445  | -12.000 | 12.000 | 16.000 | 19.000 | 37.000  |
| Median Income                            | Household median income (in thousands) in county i.                                                    | 2019 ACS 5-Year Estimates Subject Tables                                                                                                                                                                                                          | MedianIncome           | 756   | 58.448 | 16.597 | 27.063  | 48.006 | 54.517 | 64.081 | 142.299 |
| Median Income Disparity                  | Household median income disparity (in thousands) between White and Black populations in county i.      | 2019 ACS 5-Year Estimates Subject Tables                                                                                                                                                                                                          | MedianIncome_Disparity | 756   | 21.003 | 16.109 | -67.705 | 13.660 | 21.828 | 29.514 | 112.332 |
| High School Graduation Rate              | Rate of high school or above education attainment in county i.                                         | 2019 ACS 5-Year Estimates Subject Tables                                                                                                                                                                                                          | HighSchool_Rate        | 756   | 86.931 | 5.305  | 61.800  | 83.975 | 87.900 | 90.900 | 96.800  |
| High School Disparity                    | High school or above education attainment disparity between White and Black populations in county i.   | 2019 ACS 5-Year Estimates Subject Tables                                                                                                                                                                                                          | HighSchool_Disparity   | 756   | 6.762  | 7.881  | -30.300 | 2.400  | 6.200  | 10.700 | 42.200  |
| Health Facilities Per Capita             | Number of potential health facilities which provide COVID-19 vaccine per person in county i.           | VaxMap 2.0 (https://www.westhealth.org/resource/vaxmap-potential-covid-19-vaccine-locations/)                                                                                                                                                     | FacNumRate             | 756   | 0.024  | 0.012  | 0.000   | 0.017  | 0.021  | 0.026  | 0.098   |
| COVID-19 Cases Per Capita                | Number of COVID-19 cases per person in county i by April 19th, 2021                                    | The Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (https://github.com/CSSEGISandData/COVID-19)                                                                                                                    | CaseRate               | 756   | 9.469  | 2.657  | 2.235   | 7.720  | 9.527  | 11.116 | 24.159  |
| Home IT Rate                             | Rate of computer ownership and internet in the home in county i.                                       | 2019 ACS 5-Year Estimates Subject Tables                                                                                                                                                                                                          | IT_Rate                | 756   | 82.684 | 7.053  | 55.600  | 78.775 | 83.400 | 87.600 | 97.000  |
| Home IT Disparity                        | Computer ownership and internet in the home disparity between White and Black populations in county i. | 2019 ACS 5-Year Estimates Subject Tables                                                                                                                                                                                                          | IT_Disparity           | 756   | 8.308  | 10.520 | -21.900 | 2.100  | 7.700  | 14.000 | 72.300  |
| Urban                                    | Dummy variable that equals 1 if county i is located in an urban area.                                  | CMS Mapping Medical Disparity Tool (https://data.cms.gov/mapping-medicare-disparities)                                                                                                                                                            | urban                  | 756   | 0.603  | 0.490  | 0.000   | 0.000  | 1.000  | 1.000  | 1.000   |
| Rate of Vehicle Ownership                | Rate of households with vehicles in county i.                                                          | CDC Social Vulnerability Index (https://www.atsdr.cdc.gov/placeandhealth/svi/index.html)                                                                                                                                                          | vehicle                | 756   | 92.914 | 4.962  | 23.000  | 91.800 | 93.700 | 95.200 | 98.600  |
| Political Ideology                       | Rate of people who voted Republican in 2020 presidential election in county i.                         | USA Today (https://www.usatoday.com/in-depth/graphics/2020/11/10/election-maps-2020-america-county-results-more-voters/6226197002/)                                                                                                               | republican_rate        | 756   | 58.749 | 16.065 | 11.249  | 48.080 | 60.414 | 71.550 | 89.324  |
| Segregation Index                        | The degree to which Black and White groups live separately from one another in county i.               | 2021 County Health Rankings (https://www.countyhealthrankings.org/explore-health-rankings/measures-data-sources/county-health-rankings-model/health-factors/social-and-economic-factors/family-social-support/residential-segregation-blackwhite) | Segregation            | 756   | 44.852 | 16.125 | 0.041   | 33.277 | 45.831 | 56.441 | 86.159  |
| Racial Bias                              | Weighted implicit racial bias in county i.                                                             | Data from Riddle and Sinclair (2019; https://osf.io/pu79a/)                                                                                                                                                                                       | racial_weighted_bias   | 756   | 39.993 | 1.879  | 31.156  | 39.199 | 40.177 | 40.888 | 44.453  |
| Vaccine Hesitancy                        | COVID-19 vaccine hesitancy in county i.                                                                | Department of Health and Human Services, Office of the Assistant Secretary for Planning and Evaluation (https://aspe.hhs.gov/pdf-report/vaccine-hesitancy)                                                                                        | hesitancy              | 756   | 17.677 | 3.798  | 7.000   | 15.000 | 18.000 | 20.000 | 27.000  |
| Proportion of Black Residents            | Proportion of black residents in county i.                                                             | County Population by Characteristics: 2010-2019 (https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)                                                                                                           | Black_Prop             | 756   | 12.397 | 13.136 | 0.541   | 3.103  | 7.429  | 16.913 | 76.973  |
| Flu Vaccination Rate                     | Rate of flu vaccination among Medicare beneficiaries in county i.                                      | CMS Mapping Medical Disparity Tool (https://data.cms.gov/mapping-medicare-disparities)                                                                                                                                                            | FluVax_Rate            | 756   | 47.622 | 7.552  | 19.000  | 43.000 | 49.000 | 53.000 | 65.000  |
| Flu Vaccination Disparity                | Flu vaccination disparity between White and Black Medicare beneficiaries in county i.                  | CMS Mapping Medical Disparity Tool (https://data.cms.gov/mapping-medicare-disparities)                                                                                                                                                            | FluVax_Disparity       | 756   | 15.185 | 6.445  | -12.000 | 12.000 | 16.000 | 19.000 | 37.000  |
| Proportion of Pop. Above Age 75          | Rate of  Age >=75 population in county i.                                                              | County Population by Characteristics: 2010-2019 (https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)                                                                                                           | Above75_Rate           | 756   | 7.680  | 1.844  | 3.515   | 6.469  | 7.697  | 8.758  | 17.853  |
| Above Age 75 Disparity                   | Age >= 75 population disparity between white and black people in county i.                             | County Population by Characteristics: 2010-2019 (https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)                                                                                                           | Above75_Disparity      | 756   | 4.583  | 2.452  | -4.481  | 3.099  | 4.717  | 5.966  | 17.401  |
| Proportion of Pop. Above Age 15 Below 74 | Rate of  15 <= age <= 74 population in county i.                                                       | County Population by Characteristics: 2010-2019 (https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)                                                                                                           | A15T74_Rate            | 756   | 74.389 | 2.144  | 65.922  | 73.190 | 74.299 | 75.436 | 83.149  |
| Age 15 <= Age <= 74 Disparity            | 15 <= age <= 74 population disparity between white and black people in county i.                       | County Population by Characteristics: 2010-2019 (https://www.census.gov/data/tables/time-series/demo/popest/2010s-counties-detail.html)                                                                                                           | A15T74_Disparity       | 756   | -0.433 | 4.311  | -20.894 | -1.974 | 0.064  | 1.996  | 17.110  |
| Test Positivity                          | Rate of Nucleic Acid Amplification Tests (NAATs) positivity in county i.                                | CDC COVID-19 Integrated County View (https://covid.cdc.gov/covid-data-tracker/#county-view)                                                                                                                                                       | Positivity             | 756   | 6.334  | 3.765  | 0.000   | 3.828  | 5.760  | 8.433  | 26.080  |


<a name="correlation_map"/>

### Correlation Matrix Heatmap for Final Data

![](_img/correlation.png)

**Figure S4.** A correlation matrix heatmap illustrate bivariate relationships among all variables in our main regression results and robustness checks.

<a name="main_reg"/>

## Main Regression Result


<a name='base_model'>
   
### Base Model Regression Table

Below, we provide the regression table presented in Agarwal et al. (2021) for comparison to the robustness checks. 

   |                                    | CVD (April 19, 2021)         |  FVD 2019    |
|------------------------------------|------------------------------|--------------|
| Economic Stability                 |                              |              |
| Median Income                      | -2.196*                      | 1.135+       |
|                                    | (0.987)                      | -0.611       |
| Median Income Disparity            | 0.888+                       | 0.884+       |
|                                    | (0.439)                      | -0.431       |
| Education Access and Quality       |                              |              |
| High School Graduation Rate        | 1.219                        | 1.115        |
|                                    | (1.191)                      | -1.089       |
| High School Disparity              | 2.013***                     | 1.905***     |
|                                    | (0.408)                      | -0.378       |
| Healthcare Access and Quality      |                              |              |
| Health Facilities Per Capita       | 0.782                        | 0.812        |
|                                    | (0.762)                      | -0.698       |
| COVID-19 Cases Per Capita          | -0.0764                      | -0.11        |
|                                    | (0.751)                      | -0.669       |
| Neighborhood and Built Environment |                              |              |
| Home IT Rate                       | 0.514                        | 0.424        |
|                                    | (0.772)                      | -0.833       |
| Home IT Disparity                  | 0.199                        | 0.0151       |
|                                    | (0.989)                      | -0.901       |
| Urban                              | 0.185                        | 0.0214       |
|                                    | (1.226)                      | -1.15        |
| Rate of Vehicle Ownership          | 2.069                        | 1.934        |
|                                    | (1.284)                      | -1.152       |
| Social and Community Context       |                              |              |
| Political Ideology                 | -6.451**                     | -5.959**     |
|                                    | (1.728)                      | -1.663       |
| Segregation                        | 1.426+                       | 1.219+       |
|                                    | (0.692)                      | -0.673       |
| Racial Bias                        | 1.431+                       | 1.297*       |
|                                    | (0.733)                      | -0.58        |
| Covariates                         |                              |              |
| Vaccine Hesitancy                  | 1.905                        | 2.109        |
|                                    | (1.764)                      | -1.619       |
| Proportion of Black Pop.           | -5.243*                      | -5.245*      |
|                                    | (2.057)                      | -1.995       |
| Constant                           | 8.286***                     | 13.46***     |
|                                    | (1.437)                      | (0.916)      |
|                                    |                              |              |
| Observations                       | 756                          | 756          |
| Covered Population (million)       | 170.65                       | 170.65       |
| Covered Population (proportion)    | 0.515                 | 0.515 |
| R-squared                          | 0.673                        | 0.463        |
| State Dummies                      | TRUE                         | TRUE         |
| Robust Standard Error              | TRUE                         | TRUE         |
| Clustered at State Level           | TRUE                         | TRUE         |
| Weighted with County Population    | TRUE                         | TRUE         |


<a name="robustness_checks"/>

## Detailed Regression Results and Robustness Checks

    
    
 
<a name="age_control"/>
    
 ### Different Age Group Controls
  
Below, we report regression tables controlling for proportion of population above age 75 and disparities in the proportion of population above age 75 for the White and Black population. We add this variable as a control to account for the fact that older adults were prioritized early on in the vaccine rollout. In addition, we add additional control variables to account for the population that was eligible for the vaccines. Based on available demographic data, we approximate the vaccine eligible population by controlling for the proportion of population ages 15-74 in one set of analyses and the proportion of population ages 20-74 in a second set of analyses.
    
|                                    | CVD (April 19, 2021)         |                                    | CVD (April 19, 2021)         |
|------------------------------------|------------------------------|------------------------------------|------------------------------|
| Economic Stability                 |                              | Economic Stability                 |                              |
| Median Income                      | -1.126*                      | Median Income                      | -0.924                       |
|                                    | (0.506)                      |                                    | (0.543)                      |
| Median Income Disparity            | 0.875+                       | Median Income Disparity            | 0.888                        |
|                                    | (0.436)                      |                                    | (0.436)                      |
| Education Access and Quality       |                              | Education Access and Quality       |                              |
| High School Graduation Rate        | 1.431                        | High School Graduation Rate        | 1.334                        |
|                                    | (1.156)                      |                                    | (1.115)                      |
| High School Disparity              | 1.859**                      | High School Disparity              | 1.991***                     |
|                                    | (0.490)                      |                                    | (0.481)                      |
| Healthcare Access and Quality      |                              | Healthcare Access and Quality      |                              |
| Health Facilities Per Capita       | 0.650                        | Health Facilities Per Capita       | 0.633                        |
|                                    | (0.730)                      |                                    | (0.728)                      |
| COVID-19 Cases Per Capita          | -0.389                       | COVID-19 Cases Per Capita          | -0.307                       |
|                                    | (0.556)                      |                                    | (0.591)                      |
| Neighborhood and Built Environment |                              | Neighborhood and Built Environment |                              |
| Home IT Rate                       | -0.370                       | Home IT Rate                       | -0.317                       |
|                                    | (0.886)                      |                                    | (0.807)                      |
| Home IT Disparity                  | -0.130                       | Home IT Disparity                  | -0.252                       |
|                                    | (0.589)                      |                                    | (0.602)                      |
| Urban                              | -0.980                       | Urban                              | -0.812                       |
|                                    | (0.798)                      |                                    | (0.875)                      |
| Rate of Vehicle Ownership          | 1.233                        | Rate of Vehicle Ownership          | 1.151                        |
|                                    | (1.217)                      |                                    | (1.205)                      |
| Social and Community Context       |                              | Social and Community Context       |                              |
| Political Ideology                 | -5.163**                     | Political Ideology                 | -5.133*                      |
|                                    | (1.730)                      |                                    | (1.761)                      |
| Segregation                        | 1.391+                       | Segregation                        | 1.332                        |
|                                    | (0.792)                      |                                    | (0.815)                      |
| Racial Bias                        | 0.551                        | Racial Bias                        | 0.632                        |
|                                    | (0.485)                      |                                    | (0.427)                      |
| Covariates                         |                              | Covariates                         |                              |
| Vaccine Hesitancy                  | 1.574                        | Vaccine Hesitancy                  | 1.718                        |
|                                    | (1.605)                      |                                    | (1.591)                      |
| Proportion of Black Pop.           | -4.873*                      | Proportion of Black Pop.           | -4.770*                      |
|                                    | (1.927)                      |                                    | (1.874)                      |
| FluVax_WholeRate                   | -0.136                       | FluVax_WholeRate                   | -0.124                       |
|                                    | (0.687)                      |                                    | (0.711)                      |
| FluVax_Disparity                   | 1.582*                       | FluVax_Disparity                   | 1.664**                      |
|                                    | (0.544)                      |                                    | (0.543)                      |
| Proportion of Pop. Above Age 75    | -0.763                       | Proportion of Pop. Above Age 75    | -0.606                       |
|                                    | (0.884)                      |                                    | (0.917)                      |
| Above Age 75 Disparity             | 2.742*                       | Above Age 75 Disparity             | 2.539*                       |
|                                    | (1.026)                      |                                    | (1.050)                      |
| A15T74_WholeRate                   | -0.389                       | A20T74_WholeRate                   | -0.281                       |
|                                    | (0.588)                      |                                    | (0.608)                      |
| A15T74_Disparity                   | 2.319***                     | A20T74_Disparity                   | 2.472***                     |
|                                    | (0.250)                      |                                    | (0.360)                      |
| Constant                           | 11.84***                     | Constant                           | 11.97***                     |
|                                    | (1.213)                      |                                    | (1.276)                      |
|                                    |                              |                                    |                              |
| Observations                       | 756                          | Observations                       | 756                          |
| Covered Population (million)       | 170.65                       | Covered Population (million)       | 170.65                       |
| Covered Population (proportion)    | 0.515                 | Covered Population (proportion)    | 0.515                 |
| R-squared                          | 0.728                        | R-squared                          | 0.730                        |
| State Dummies                      | TRUE                         | State Dummies                      | TRUE                         |
| Robust Standard Error              | TRUE                         | Robust Standard Error              | TRUE                         |
| Clustered at State Level           | TRUE                         | Clustered at State Level           | TRUE                         |
| Weighted with County Population    | TRUE                         | Weighted with County Population    | TRUE                         |
    
 
<a name="disparity_measure"/>
    
 ### Different Disparity Operationalizations
 
  As additional robustness checks, we also model alternative operationlizations of disparity. Specifically, we model a ratio-based definition (White Vaccination Rate/Black Vaccination Rate), the log of that ratio, and an outcome that scales the absolute disparity by the overall vaccination rate of the White and Black populations in a given county.
 
   
|                                    | Ratio Disparity | Log Ratio Disparity | Scaled Absolute Disparity |
|------------------------------------|-----------------|---------------------|---------------------------|
| Economic Stability                 |                 |                     |                           |
| Median Income                      | -0.224*         | -0.249*             | -0.260*                   |
|                                    | (0.0786)        | (0.112)             | (0.113)                   |
| Median Income Disparity            | 0.0635          | 0.0525              | 0.0829                    |
|                                    | (0.0698)        | (0.0461)            | (0.0584)                  |
| Education Access and Quality       |                 |                     |                           |
| High School Graduation Rate        | 0.0108          | 0.0433              | 0.0467                    |
|                                    | (0.0907)        | (0.123)             | (0.152)                   |
| High School Disparity              | 0.258***        | 0.256***            | 0.197***                  |
|                                    | (0.0463)        | (0.0464)            | (0.0430)                  |
| Healthcare Access and Quality      |                 |                     |                           |
| Health Facilities Per Capita       | 0.0140          | 0.0321              | 0.0173                    |
|                                    | (0.0792)        | (0.0938)            | (0.0952)                  |
| COVID-19 Cases Per Capita          | 0.0146          | 0.0343              | 0.0223                    |
|                                    | (0.0666)        | (0.0766)            | (0.0620)                  |
| Neighborhood and Built Environment |                 |                     |                           |
| Home IT Rate                       | 0.0325          | 0.0676              | 0.105                     |
|                                    | (0.0564)        | (0.0796)            | (0.101)                   |
| Home IT Disparity                  | -0.181          | -0.0636             | 0.00680                   |
|                                    | (0.150)         | (0.103)             | (0.0793)                  |
| Urban                              | 0.00423         | -0.00179            | -0.00382                  |
|                                    | (0.152)         | (0.178)             | (0.167)                   |
| Rate of Vehicle Ownership          | 0.130           | 0.211               | 0.262+                    |
|                                    | (0.147)         | (0.164)             | (0.148)                   |
| Social and Community Context       |                 |                     |                           |
| Political Ideology                 | -0.387*         | -0.493**            | -0.537**                  |
|                                    | (0.131)         | (0.152)             | (0.167)                   |
| Segregation                        | 0.188**         | 0.241**             | 0.256**                   |
|                                    | (0.0521)        | (0.0638)            | (0.0713)                  |
| Racial Bias                        | 0.0536          | 0.0793              | 0.106                     |
|                                    | (0.0849)        | (0.0919)            | (0.0840)                  |
| Covariates                         |                 |                     |                           |
| Vaccine Hesitancy                  | 0.120           | 0.173               | 0.202                     |
|                                    | (0.163)         | (0.195)             | (0.209)                   |
| Proportion of Black Pop.           | -0.348*         | -0.414*             | -0.353                    |
|                                    | (0.159)         | (0.188)             | (0.206)                   |
| Constant                           | -0.482**        | -0.484**            | -0.374*                   |
|                                    | (0.147)         | (0.163)             | (0.149)                   |
|                                    |                 |                     |                           |
| Observations                       | 756             | 756                 | 756                       |
| Covered Population (million)       | 170.65          | 170.65              | 170.65                    |
| Covered Population (proportion)    | 0.515           | 0.515               | 0.515                     |
| R-squared                          | 0.552           | 0.551               | 0.563                     |
| State Dummies                      | True            | True                | True                      |
| Robust Standard Error              | True            | True                | True                      |
| Clustered at State Level           | True            | True                | True                      |
| Weighted with County Population    | True            | True                | True                      |   
    
    
 
<a name="date_ratetype"/>
    
### Different Dates and Full Vaccination Rate Types
 
   
  
|                                    | CVD (March 27, 2021)         | CVD (April 07, 2021)         | CVD (May 20, 2021) | CVD - Full Dose (May 20, 2021) |
|------------------------------------|------------------------------|------------------------------|--------------------|--------------------------------|
| Economic Stability                 |                              |                              |                    |                                |
| Median Income                      | -1.862*                      | -2.209*                      | -1.519*            | -2.797**                       |
|                                    | -0.698                       | -0.902                       | (0.683)            | (0.742)                        |
| Median Income Disparity            | 0.135                        | 0.509                        | 1.422*             | 1.240*                         |
|                                    | -0.378                       | -0.381                       | (0.577)            | (0.478)                        |
| Education Access and Quality       |                              |                              |                    |                                |
| High School Graduation Rate        | 1.43                         | 1.358                        | 0.623              | -0.472                         |
|                                    | -1.144                       | -1.181                       | (1.305)            | (0.808)                        |
| High School Disparity              | 1.707**                      | 1.868***                     | 1.935**            | 1.057+                         |
|                                    | -0.468                       | -0.386                       | (0.611)            | (0.478)                        |
| Healthcare Access and Quality      |                              |                              |                    |                                |
| Health Facilities Per Capita       | 0.14                         | 0.569                        | 0.351              | -0.967                         |
|                                    | -0.421                       | -0.626                       | (0.862)            | (0.772)                        |
| COVID-19 Cases Per Capita          | 0.536                        | 0.0487                       | 0.727+             | 0.981                          |
|                                    | -0.388                       | -0.759                       | (0.408)            | (0.679)                        |
| Neighborhood and Built Environment |                              |                              |                    |                                |
| Home IT Rate                       | -0.383                       | -0.322                       | 0.279              | 1.649***                       |
|                                    | -0.528                       | -0.577                       | (0.729)            | (0.326)                        |
| Home IT Disparity                  | 0.269                        | 0.0619                       | 0.721              | -0.395                         |
|                                    | -0.666                       | -0.855                       | (0.939)            | (0.547)                        |
| Urban                              | -1.142*                      | 0.0583                       | -0.529             | -0.356                         |
|                                    | -0.457                       | -1.088                       | (0.833)            | (0.329)                        |
| Rate of Vehicle Ownership          | 1.514+                       | 2.705*                       | 1.246              | 0.183                          |
|                                    | -0.845                       | -1.027                       | (1.632)            | (1.601)                        |
| Social and Community Context       |                              |                              |                    |                                |
| Political Ideology                 | -4.694***                    | -5.529**                     | -7.413***          | -4.060***                      |
|                                    | -1.07                        | -1.374                       | (1.353)            | (0.644)                        |
| Segregation                        | 1.157*                       | 1.496*                       | 1.459+             | 0.503                          |
|                                    | -0.523                       | -0.59                        | (0.751)            | (0.760)                        |
| Racial Bias                        | 1.031+                       | 1.416*                       | 1.681*             | -0.118                         |
|                                    | -0.49                        | -0.631                       | (0.733)            | (0.476)                        |
| Covariates                         |                              |                              |                    |                                |
| Vaccine Hesitancy                  | 0.734                        | 1.487                        | 2.207              | -1.081                         |
|                                    | -1.249                       | -1.599                       | (1.548)            | (0.649)                        |
| Proportion of Black Pop.           | -4.211*                      | -4.603*                      | -7.212**           | -3.263+                        |
|                                    | -1.453                       | -1.776                       | (2.089)            | (1.747)                        |
| Constant                           | 4.937**                      | 6.126*                       | -1.078             | 5.825**                        |
|                                    | (1.411)                      | (2.155)                      | (2.606)            | (1.614)                        |
|                                    |                              |                              |                    |                                |
| Observations                       | 734                          | 758                          | 738                | 534                            |
| Covered Population (million)       | 156.46                       | 171.71                       | 156.06             | 84.96                          |
| Covered Population (proportion)    | 0.472                        | 0.518                        | 0.471              | 0.256                          |
| R-squared                          | 0.822                        | 0.655                        | 0.748              | 0.706                          |
| State Dummies                      | TRUE                         | TRUE                         | True               | True                           |
| Robust Standard Error              | TRUE                         | TRUE                         | True               | True                           |
| Clustered at State Level           | TRUE                         | TRUE                         | True               | True                           |
| Weighted with County Population    | TRUE                         | TRUE                         | True               | True                           |
    
    

<a name="exodus_test"/>

   
   
### Residential Mobility
   
|                                    | CVD (April 19, 2021)         |
|------------------------------------|------------------------------|
| Economic Stability                |                              |
| Median Income                      | -2.584*                      |
|                                    | (0.996)                      |
| Median Income Disparity            | 1.074                        |
|                                    | (0.724)                      |
| Education Access and Quality       |                              |
| High School Graduation Rate        | -0.583                       |
|                                    | (0.754)                      |
| High School Disparity              | 1.463***                     |
|                                    | (0.282)                      |
| Healthcare Access and Quality      |                              |
| Health Facilities Per Capita       | 0.283                        |
|                                    | (0.642)                      |
| COVID-19 Cases Per Capita          | 0.469                        |
|                                    | (0.419)                      |
| Neighborhood and Built Environment |                              |
| Home IT Rate                       | 1.446+                       |
|                                    | (0.777)                      |
| Home IT Disparity                  | -0.515                       |
|                                    | (0.770)                      |
| Urban                              | -0.372                       |
|                                    | (0.487)                      |
| Rate of Vehicle Ownership          | 0.721                        |
|                                    | (1.399)                      |
| Social and Community Context       |                              |
| Political Ideology                 | -6.399***                    |
|                                    | (0.977)                      |
| Segregation                        | 1.438*                       |
|                                    | (0.550)                      |
| Racial Bias                        | 0.152                        |
|                                    | (0.543)                      |
| Covariates                         |                              |
| Vaccine Hesitancy                  | 0.172                        |
|                                    | (1.398)                      |
| Proportion of Black Pop.           | -4.625*                      |
|                                    | (1.700)                      |
| Constant                           | 9.265***                     |
|                                    | (1.309)                      |
|                                    |                              |
| Observations                       | 744                          |
| Covered Population (million)       | 146.00                       |
| Covered Population (proportion)    | 0.440                        |
| R-squared                          | 0.750                        |
| State Dummies                      | True                         |
| Robust Standard Error              | True                         |
| Clustered at State Level           | True                         |
| Weighted with County Population    | True                         |
   
   
 
<a name="positivity"/>
   
### Recent Positive Rate per COVID-19 Test
|                                    | CVD (April 19, 2021)         |
|------------------------------------|------------------------------|
| Economic Stability                 |                              |
| Median Income                      | -2.128*                      |
|                                    | (0.968)                      |
| Median Income Disparity            | 0.914                        |
|                                    | (0.434)                      |
| Education Access and Quality       |                              |
| High School Graduation Rate        | 1.398                        |
|                                    | (1.125)                      |
| High School Disparity              | 2.041***                     |
|                                    | (0.423)                      |
| Healthcare Access and Quality      |                              |
| Health Facilities Per Capita       | 0.864                        |
|                                    | (0.750)                      |
| COVID-19 Cases Per Capita          | 0.0534                       |
|                                    | (0.748)                      |
| Neighborhood and Built Environment |                              |
| Home IT Rate                       | 0.362                        |
|                                    | (0.737)                      |
| Home IT Disparity                  | 0.244                        |
|                                    | (0.971)                      |
| Urban                              | 0.0242                       |
|                                    | (1.278)                      |
| Rate of Vehicle Ownership          | 2.097                        |
|                                    | (1.277)                      |
| Social and Community Context       |                              |
| Political Ideology                 | -6.552**                     |
|                                    | (1.722)                      |
| Segregation                        | 1.378                        |
|                                    | (0.697)                      |
| Racial Bias                        | 1.321                        |
|                                    | (0.759)                      |
| Covariates                         |                              |
| Vaccine Hesitancy                  | 1.857                        |
|                                    | (1.778)                      |
| Proportion of Black Pop.           | -5.249*                      |
|                                    | (2.030)                      |
| Test Positivity                    | 0.713                        |
|                                    | (0.385)                      |
| Constant                           | 8.224***                     |
|                                    | (1.450)                      |
|                                    |                              |
| Observations                       | 756                          |
| Covered Population (million)       | 170.65                       |
| Covered Population (proportion)    | 0.515                 |
| R-squared                          | 0.674                        |
| State Dummies                      | TRUE                         |
| Robust Standard Error              | TRUE                         |
| Clustered at State Level           | TRUE                         |
| Weighted with County Population    | TRUE                         |


   
