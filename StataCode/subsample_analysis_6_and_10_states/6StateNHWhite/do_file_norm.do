clear all
set more off
use "/Users/floydluo/Desktop/Covid19-Vaccination-Race-Disparity/StataCode/subsample_analysis_6_and_10_states/6StateNHWhite/DataNorm.dta"


drop if ReportNH == 0


tab State, generate(state_dummy)


winsor2 MedianInc_Disparity, replace cuts (5,95)
winsor2 racial_weighted_bias, replace cuts (5,95)
winsor2 A15T74_Disparity, replace cuts (5,95)
winsor2 republican_rate, replace cuts (5,95)
winsor2 MedianInc_WholeAvg, replace cuts (5,95)
winsor2 IT_WholeRate, replace cuts (5,95)
winsor2 A15T74_WholeRate, replace cuts (5,95)
winsor2 Above75_WholeRate, replace cuts (5,95)
winsor2 FacNumRate, replace cuts (5,95)
winsor2 Segregation, replace cuts (5,95)
winsor2 Black_Prop, replace cuts (5,95)
winsor2 HighSchool_Disparity, replace cuts (5,95)
winsor2 FluVax_Disparity, replace cuts (5,95)
winsor2 FluVax_WholeRate, replace cuts (5,95)
winsor2 Above75_Disparity, replace cuts (5,95)
winsor2 CvdVax_DisparityY, replace cuts (5,95)
winsor2 CaseRate, replace cuts (5,95)
winsor2 vehicle, replace cuts (5,95)
winsor2 IT_Disparity, replace cuts (5,95)
winsor2 urban, replace cuts (5,95)
winsor2 HighSchool_WholeRate, replace cuts (5,95)



reg CvdVax_DisparityY MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop state_dummy1-state_dummy6  [pweight=org_WholeNum] , r cluster(State)

outreg2 using StataCode/subsample_analysis_6_and_10_states/6StateNHWhite/RegResult.doc, replace ctitle(CvdVax_D) addtext(SD, True, R, True, C, True, W, True)  keep (MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop) excel alpha(0.001, 0.01, 0.05, 0.10) symbol(***, **, *, +)


reg CvdVax_DisparityY MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop FluVax_WholeRate FluVax_Disparity state_dummy1-state_dummy6  [pweight=org_WholeNum] , r cluster(State)

outreg2 using StataCode/subsample_analysis_6_and_10_states/6StateNHWhite/RegResult.doc, append ctitle(CvdVax_D) addtext(SD, True, R, True, C, True, W, True)  keep (MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop FluVax_WholeRate FluVax_Disparity) excel alpha(0.001, 0.01, 0.05, 0.10) symbol(***, **, *, +)


reg CvdVax_DisparityY MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop FluVax_WholeRate FluVax_Disparity Above75_WholeRate Above75_Disparity state_dummy1-state_dummy6  [pweight=org_WholeNum] , r cluster(State)

outreg2 using StataCode/subsample_analysis_6_and_10_states/6StateNHWhite/RegResult.doc, append ctitle(CvdVax_D) addtext(SD, True, R, True, C, True, W, True)  keep (MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop FluVax_WholeRate FluVax_Disparity Above75_WholeRate Above75_Disparity) excel alpha(0.001, 0.01, 0.05, 0.10) symbol(***, **, *, +)


reg CvdVax_DisparityY MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop FluVax_WholeRate FluVax_Disparity Above75_WholeRate Above75_Disparity A15T74_WholeRate A15T74_Disparity state_dummy1-state_dummy6  [pweight=org_WholeNum] , r cluster(State)

outreg2 using StataCode/subsample_analysis_6_and_10_states/6StateNHWhite/RegResult.doc, append ctitle(CvdVax_D) addtext(SD, True, R, True, C, True, W, True)  keep (MedianInc_WholeAvg MedianInc_Disparity HighSchool_WholeRate HighSchool_Disparity FacNumRate CaseRate IT_WholeRate IT_Disparity urban vehicle republican_rate Segregation racial_weighted_bias Black_Prop FluVax_WholeRate FluVax_Disparity Above75_WholeRate Above75_Disparity A15T74_WholeRate A15T74_Disparity) excel alpha(0.001, 0.01, 0.05, 0.10) symbol(***, **, *, +)

