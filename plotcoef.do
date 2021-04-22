



reg Vax_DisparityY MedianIncome MedianIncome_Disparity HighSchool_Rate HighSchool_Disparity FacNumRate CaseRate IT_Rate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias hesitancy Black_Prop state_dummy1-state_dummy16  [pweight=org_Total_Whole] , r cluster(State)
estimates store covid


reg FluVax_DisparityY MedianIncome MedianIncome_Disparity HighSchool_Rate HighSchool_Disparity FacNumRate CaseRate IT_Rate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias hesitancy Black_Prop state_dummy1-state_dummy16  [pweight=org_Total_Whole] , r cluster(State)
estimates store flu



grstyle init
grstyle set plain, horizontal grid
grstyle set color #44b9db: p#bar p#barline 
coefplot covid, bylabel(COVID-19 Vaccination Disparity) || flu, bylabel(Flu Vaccination Disparity) ||, keep(MedianIncome MedianIncome_Disparity HighSchool_Rate HighSchool_Disparity FacNumRate CaseRate IT_Rate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias hesitancy Black_Prop ) xline(0) recast(bar) ciopts(recast(rcap)) citop barwidt(0.3) bgcolor(white) levels(95) rename(MedianIncome="Median Income" MedianIncome_Disparity="Median Income Disparity" HighSchool_Rate="High School Graduation Rate" HighSchool_Disparity="High School Disparity" FacNumRate="Health Facilities Per Capita" CaseRate="COVID-19 Cases Per Capita" IT_Rate="Home IT Rate" IT_Disparity="Home IT Disparity" urban="Urban" vehicle="Rate of Vehicle Ownership" republican_rate="Political Ideology" Segregation="Segregation Index" racial_weighted_bias="Racial Bias" hesitancy="Vaccine Hesitancy" Black_Prop="Proportion of Black Residents" ) note("")
*Percentage point change in disparities associated with 1 standard deviation increase in predictor variables. Error bars represent 95% confidence intervals.





