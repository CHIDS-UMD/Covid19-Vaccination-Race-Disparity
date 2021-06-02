



reg CvdVax_DisparityY MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias hesitancy Black_Prop state_dummy1-state_dummy16  [pweight=org_WholeNum] , r cluster(State)
estimates store COVID


reg FluVax_DisparityY MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias hesitancy Black_Prop state_dummy1-state_dummy16  [pweight=org_WholeNum] , r cluster(State)
estimates store Flu



grstyle init
grstyle set plain, horizontal grid
grstyle set color #44b9db: p#bar p#barline 
coefplot COVID, bylabel(COVID-19 Vaccination Disparity) || Flu, bylabel(Flu Vaccination Disparity) ||, keep(MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias hesitancy Black_Prop) xline(0) ciopts(recast(rcap)) citop bgcolor(white) levels(95) rename(MedianInc_WholeAvg="Median Income" MedianInc_Disparity="Median Income Disparity" HighSchool_WholeRate="High School Graduation Rate" HighSchool_Disparity="High School Disparity" FacNumRate="Health Facilities Per Capita" CaseRate="COVID-19 Cases Per Capita" IT_WholeRate="Home IT Rate" IT_Disparity="Home IT Disparity" urban="Urban" vehicle="Rate of Vehicle Ownership" republican_rate="Political Ideology" Segregation="Segregation Index" racial_weighted_bias="Racial Bias" hesitancy="Vaccine Hesitancy" Black_Prop="Proportion of Black Residents" ) note("")
*Percentage point change in disparities associated with 1 standard deviation increase in predictor variables. Error bars represent 95% confidence intervals.
