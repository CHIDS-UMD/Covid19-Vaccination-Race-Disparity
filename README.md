# Racial COVID-19 Vaccination Data Source

| State          | # of Counties | # of Valid Counties | Link                                                                                                                                                          |
|----------------|---------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| California     | 54            | 43                  | https://covid19.ca.gov/vaccines/#California-vaccines-dashboard                                                                                                |
| Illinois       | 102           | 42                  | https://www.dph.illinois.gov/covid19/vaccinedata?county=Illinois                                                                                              |
| Indiana        | 89            | 37                  | https://www.coronavirus.in.gov/vaccine/2680.htm                                                                                                               |
| Maine          | 16            | 8                   | https://www.maine.gov/covid19/vaccines/dashboard                                                                                                              |
| New Jersey     | 21            | 21                  | https://www.nj.gov/health/cd/topics/covid2019_dashboard.shtml                                                                                                 |
| New York       | 62            | 48                  | https://covid19vaccine.health.ny.gov/covid-19-vaccine-tracker                                                                                                 |
| North Carolina | 43            | 43                  | https://covid19.ncdhhs.gov/dashboard/data-behind-dashboards                                                                                                   |
| Ohio           | 88            | 57                  | https://coronavirus.ohio.gov/wps/portal/gov/covid-19/dashboards/covid-19-vaccine/covid-19-vaccination-dashboard                                               |
| Oregon         | 23            | 11                  | https://public.tableau.com/profile/oregon.health.authority.covid.19#!/vizhome/OregonCOVID-19VaccinationTrends/OregonCountyVaccinationTrends                   |
| Pennsylvania   | 60            | 40                  | https://www.health.pa.gov/topics/disease/coronavirus/Vaccine/Pages/Vaccine.aspx                                                                               |
| South Carolina | 46            | 43                  | https://scdhec.gov/covid19/covid-19-vaccination-dashboard                                                                                                     |
| Tennessee      | 90            | 62                  | https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html                                                                                          |
| Texas          | 245           | 139                 | https://tabexternal.dshs.texas.gov/t/THD/views/COVID-19VaccineinTexasDashboard/Summary?%3Aorigin=card_share_link&%3Aembed=y&%3AisGuestRedirectFromVizportal=y |
| Virginia       | 133           | 111                 | https://www.vdh.virginia.gov/coronavirus/covid-19-vaccine-demographics/                                                                                       |
| West Virginia  | 55            | 23                  | https://dhhr.wv.gov/COVID-19/Pages/default.aspx                                                                                                               |
| Wisconsin      | 72            | 28                  | https://www.dhs.wisconsin.gov/covid-19/vaccine-data.htm#day                                                                                                   |
| Sum            | 1296          | 759                 |                                                                                                                                                               |




# Descriptive Statistics

We present descriptive statistics of the variables in our regression analysis. Each variable is at the county level, where the subscript `i` represents county `i`.									

|                        | count | mean   | std    | min     | 25%    | 50%    | 75%    | max     |
|------------------------|-------|--------|--------|---------|--------|--------|--------|---------|
| Vax_DisparityY         | 759   | 9.021  | 10.435 | -18.168 | 1.502  | 6.756  | 15.192 | 48.640  |
| FluVax_DisparityY      | 759   | 15.211 | 6.449  | -12.000 | 12.000 | 16.000 | 19.000 | 37.000  |
| MedianIncome           | 759   | 58.412 | 16.584 | 27.063  | 47.796 | 54.489 | 64.032 | 142.299 |
| MedianIncome_Disparity | 759   | 19.217 | 15.671 | -67.671 | 12.325 | 20.119 | 28.221 | 106.200 |
| HighSchool_Rate        | 759   | 60.159 | 5.403  | 33.605  | 57.727 | 60.988 | 63.597 | 73.273  |
| HighSchool_Disparity   | 759   | 4.470  | 8.789  | -32.600 | -0.500 | 4.200  | 9.000  | 41.000  |
| FacNumRate             | 759   | 0.024  | 0.012  | 0.000   | 0.017  | 0.021  | 0.026  | 0.098   |
| CaseRate               | 759   | 9.260  | 2.650  | 2.092   | 7.486  | 9.286  | 10.924 | 24.131  |
| IT_Rate                | 759   | 82.652 | 7.070  | 55.600  | 78.700 | 83.400 | 87.600 | 97.000  |
| IT_Disparity           | 759   | 7.543  | 10.496 | -21.700 | 1.250  | 7.100  | 13.050 | 73.700  |
| urban                  | 759   | 0.605  | 0.489  | 0.000   | 0.000  | 1.000  | 1.000  | 1.000   |
| vehicle                | 759   | 92.914 | 4.952  | 23.000  | 91.800 | 93.700 | 95.200 | 98.600  |
| republican_rate        | 759   | 58.688 | 16.066 | 11.249  | 47.915 | 60.317 | 71.514 | 89.324  |
| Segregation            | 759   | 44.941 | 16.163 | 0.041   | 33.305 | 45.875 | 56.490 | 86.159  |
| racial_weighted_bias   | 759   | 39.989 | 1.877  | 31.156  | 39.192 | 40.176 | 40.884 | 44.453  |
| hesitancy              | 759   | 17.673 | 3.792  | 7.000   | 15.000 | 18.000 | 19.500 | 27.000  |
| Black_Prop             | 759   | 12.367 | 13.124 | 0.541   | 3.042  | 7.429  | 16.784 | 76.973  |
| FluVax_Rate            | 759   | 47.610 | 7.549  | 19.000  | 43.000 | 49.000 | 53.000 | 65.000  |
| FluVax_Disparity       | 759   | 15.211 | 6.449  | -12.000 | 12.000 | 16.000 | 19.000 | 37.000  |
| Above75_Rate           | 759   | 7.671  | 1.848  | 3.515   | 6.457  | 7.683  | 8.753  | 17.853  |
| Above75_Disparity      | 759   | 3.638  | 2.310  | -4.910  | 2.215  | 3.515  | 5.074  | 12.933  |