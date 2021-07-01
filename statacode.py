import pandas as pd
import numpy as np
from datetime import datetime
import os
# from IPython.core.display import display, HTML
import missingno as msno
import subprocess
import os
import shutil
import argparse


# import subprocess
# new versions



def dependent_variable_construction(T2):

    ###### (0) for LeastOne Vaccination
    for col in ['CvdVax_WhiteNum', 'CvdVax_NHWhiteNum']:
        index = - T2[col].isna()
        T2.loc[index, 'CvdVax_ZWhiteNum'] = T2.loc[index, col] 

    # for Full Vaccination  
    try:
        for col in ['FullCvdVax_WhiteNum', 'FullCvdVax_NHWhiteNum']:
            index = - T2[col].isna()
            T2.loc[index, 'FullCvdVax_ZWhiteNum'] = T2.loc[index, col] 
    except:
        print('No Full Vaccine Data')


    ###### (1) Disparity
    suffix = '_Disparity'

    new_cols = []
    for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
        new_col = i+suffix
        T2[new_col] = T2[ i + '_MWhiteRate'] - T2[i+'_MBlackRate'] 
        new_cols.append(new_col)
        
    
    for i in  ['FluVax', 'HighSchool', 'Bachelor', 'IT', 'Unempl', 'A15T74', 'A20T74',  'Above75', 'Above65', 'Above15', 'Above20',]:
        new_col = i+suffix
        T2[new_col] = T2[ i + '_NHWhiteRate'] - T2[i+'_BlackRate'] 
        new_cols.append(new_col)

        
    for i in [ 'MeanInc', 'MedianInc']:
        new_col = i+suffix
        T2[new_col] = T2[ i + '_NHWhiteAvg'] - T2[i+'_BlackAvg'] 
        new_cols.append(new_col)
        

    try:
        for i in ['FullCvdVax', 'FullCvdVaxAbove15', 'FullCvdVaxAbove20']:
            new_col = i+suffix
            T2[new_col] = T2[ i + '_MWhiteRate'] - T2[i+'_MBlackRate'] 
            new_cols.append(new_col)
    except:
        print('No Full Cvd')
        
    # ZWhiteRate - MBlackRate
    try:   
        for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
            new_col ='Z' + i + suffix
            T2[new_col] = T2[ i + '_ZWhiteRate'] - T2[i+'_MBlackRate'] 
            new_cols.append(new_col)

    except:
        print('No ZCvd Info')


    ###### (2) Ratio Disparity
    new_cols = []
    suffix = '_RD'

    for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
        new_col = i+suffix
        T2[new_col] = (T2[ i + '_MWhiteRate'] + 0.0001) /( T2[i+'_MBlackRate']  + 0.0001)
        new_cols.append(new_col)
        

    for i in  ['FluVax', 'HighSchool', 'Bachelor', 'IT', 'Unempl', 'A15T74', 'A20T74',  'Above75', 'Above65', 'Above15', 'Above20',]:
        new_col = i+suffix
        T2[new_col] = (T2[ i + '_NHWhiteRate']+ 0.0001) / (T2[i+'_BlackRate']  + 0.0001)
        new_cols.append(new_col)

        
    for i in [ 'MeanInc', 'MedianInc']:
        new_col = i+suffix
        T2[new_col] = (T2[ i + '_NHWhiteAvg'] + 0.0001)/ (T2[i+'_BlackAvg']  + 0.0001)
        new_cols.append(new_col)
        

    try:
        for i in ['FullCvdVax', 'FullCvdVaxAbove15', 'FullCvdVaxAbove20']:
            new_col = i+suffix
            T2[new_col] = (T2[ i + '_MWhiteRate'] + 0.0001)/( T2[i+'_MBlackRate']  + 0.0001)
            new_cols.append(new_col)
    except:
        print('No Full Cvd')
        
        
    try:   
        for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
            new_col ='Z' + i + suffix
            T2[new_col] = (T2[ i + '_ZWhiteRate'] + 0.0001) /( T2[i+'_MBlackRate']  + 0.0001)
            new_cols.append(new_col)

    except:
        print('No ZCvd Info')
        
    T2[new_cols].describe()


    ###### (3) Log Ratio Disparity
    new_cols = []

    suffix = '_LogRD'

    for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
        new_col = i+suffix
        T2[new_col] = np.log( (T2[ i + '_MWhiteRate'] + 0.0001) /( T2[i+'_MBlackRate']  + 0.0001) )
        new_cols.append(new_col)
        
        
    for i in  ['FluVax', 'HighSchool', 'Bachelor', 'IT', 'Unempl', 'A15T74', 'A20T74',  'Above75', 'Above65', 'Above15', 'Above20',]:
        new_col = i+suffix
        T2[new_col] = np.log( (T2[ i + '_NHWhiteRate']+ 0.0001) / (T2[i+'_BlackRate']  + 0.0001) )
        new_cols.append(new_col)

        
    for i in [ 'MeanInc', 'MedianInc']:
        new_col = i+suffix
        T2[new_col] = np.log((T2[ i + '_NHWhiteAvg'] + 0.0001)/ (T2[i+'_BlackAvg']  + 0.0001) )
        new_cols.append(new_col)

    try:
        for i in ['FullCvdVax', 'FullCvdVaxAbove15', 'FullCvdVaxAbove20']:
            new_col = i+suffix
            T2[new_col] = np.log( (T2[ i + '_MWhiteRate'] + 0.0001)/( T2[i+'_MBlackRate']  + 0.0001) )
            new_cols.append(new_col)
    except:
        print('No Full Cvd')
        
        
    try:   
        for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
            new_col ='Z' + i+suffix
            T2[new_col] = np.log( (T2[ i + '_ZWhiteRate'] + 0.0001) /( T2[i+'_MBlackRate']  + 0.0001) )
            new_cols.append(new_col)
    except:
        print('No ZCvd Info')
        
        
    T2[new_cols].describe()


    ########## (4) Scaled Disparity
    new_cols = []
    suffix = '_SD'

    # LeastOne CVD
    for i in ['CvdVax', 'CvdVaxAbove15', 'CvdVaxAbove20']:
        popu_type = i.replace('CvdVax', '')
        popu_type = popu_type + '_' if len(popu_type) > 0 else popu_type
        
        new_col = i+ suffix
        AvgWBRate = (T2['CvdVax_ZWhiteNum'] + T2['CvdVax_BlackNum'])  / ( T2[popu_type + 'NHWhiteNum'] + T2[popu_type + 'BlackNum']) 
        T2[new_col] = T2[i + '_Disparity'] / (AvgWBRate * 100)
        new_cols.append(new_col)
        


    # Rate Predictors
    for i in  ['FluVax', 'HighSchool', 'Bachelor', 'IT', 'Unempl', 'A15T74', 'A20T74',  'Above75', 'Above65', 'Above15', 'Above20',]:
        new_col = i+suffix
        # T2[i + '_WhiteNum'] = T2[i + '_WhiteRate'] * T2['NHWhiteNum'] # Error here, keep here
        NHWhiteNum = T2[i + '_NHWhiteRate'] * T2['NHWhiteNum']
        BlackNum = T2[i + '_BlackRate'] * T2['BlackNum']
        AvgWBRate = (NHWhiteNum + BlackNum) / ( T2['NHWhiteNum'] + T2['BlackNum'])
        T2[new_col] = T2[i + '_Disparity'] / (AvgWBRate * 100)
        new_cols.append(new_col)


    # Income Predictors
    for i in [ 'MeanInc', 'MedianInc']:
        new_col = i+suffix
        T2[new_col] = T2[i+'_Disparity'] / T2[i+'_WholeAvg']
        new_cols.append(new_col)

        
        
    # Full CVD
    try:
        for i in ['FullCvdVax', 'FullCvdVaxAbove15', 'FullCvdVaxAbove20']:
            popu_type = i.replace('FullCvdVax', '')
            popu_type = popu_type + '_' if len(popu_type) > 0 else popu_type
            
            new_col = i+ suffix
            AvgWBRate = (T2['CvdVax_ZWhiteNum'] + T2['CvdVax_BlackNum'])  / ( T2[popu_type + 'NHWhiteNum'] + T2[popu_type + 'BlackNum'])
            T2[new_col] = T2[i + '_Disparity'] / (AvgWBRate * 100)
            new_cols.append(new_col)
    except:
        print('No Full Cvd')
        
    T2[new_cols].describe()

    return T2


def independent_variable_construction(T2):
    # How about other disparity. There unit is not meaningful. Maybe we can just leave them. 
    # Absolute
    T2['CvdVax_DisparityY'] = T2['CvdVax_Disparity']# *100
    T2['CvdVaxAbove15_DisparityY'] = T2['CvdVaxAbove15_Disparity']# *100
    T2['CvdVaxAbove20_DisparityY'] = T2['CvdVaxAbove20_Disparity']# *100
    T2['FluVax_DisparityY'] = T2['FluVax_Disparity']# *100

    # Ratio
    T2['CvdVax_RDY'] = T2['CvdVax_RD']
    T2['CvdVaxAbove15_RDY'] = T2['CvdVaxAbove15_RD']
    T2['CvdVaxAbove20_RDY'] = T2['CvdVaxAbove20_RD']
    T2['FluVax_RDY'] = T2['FluVax_RD']# *100


    # logRatio
    T2['CvdVax_LogRDY'] = T2['CvdVax_LogRD'] 
    T2['CvdVaxAbove15_LogRDY'] = T2['CvdVaxAbove15_LogRD']
    T2['CvdVaxAbove20_LogRDY'] = T2['CvdVaxAbove20_LogRD']
    T2['FluVax_LogRDY'] = T2['FluVax_LogRD']



    # Scaled 
    T2['CvdVax_SDY'] = T2['CvdVax_SD']
    T2['CvdVaxAbove15_SDY'] = T2['CvdVaxAbove15_SD']
    T2['CvdVaxAbove20_SDY'] = T2['CvdVaxAbove20_SD']
    T2['FluVax_SDY'] = T2['FluVax_SD']# *100


    try:
        T2['FullCvdVax_DisparityY'] = T2['FullCvdVax_Disparity']# *100
        T2['FullCvdVaxAbove15_DisparityY'] = T2['FullCvdVaxAbove15_Disparity']# *100
        T2['FullCvdVaxAbove20_DisparityY'] = T2['FullCvdVaxAbove20_Disparity']# *100
        
        # Ratio
        T2['FullCvdVax_RDY'] = T2['FullCvdVax_RD']
        T2['FullCvdVaxAbove15_RDY'] = T2['FullCvdVaxAbove15_RD']
        T2['FullCvdVaxAbove20_RDY'] = T2['FullCvdVaxAbove20_RD']
        
        # Scaled 
        T2['FullCvdVax_SDY'] = T2['FullCvdVax_SD']
        T2['FullCvdVaxAbove15_SDY'] = T2['FullCvdVaxAbove15_SD']
        T2['FullCvdVaxAbove20_SDY'] = T2['FullCvdVaxAbove20_SD']
        
    except:
        print('No Full Cvd')
        
    T2['ZCvdVax_DisparityY'] = T2['ZCvdVax_Disparity']# *100

    T2['FacNum'] = T2[['FQHC', 'HOPD', 'PHMCY', 'RUHC']].sum(axis = 1)
    T2['vehicle'] = 1- T2['EP_NOVEH']
    T2['logFacNum' ] = np.log(T2['FacNum' ] + 1)
    T2['logcases' ] = np.log(T2['cases' ] + 1)

    T2['FacNumRate' ] = T2['FacNum' ]/T2['WholeNum']

    T2['CaseRate' ] = T2['cases' ]/T2['WholeNum']


    T2['Black_Prop' ] = T2['BlackNum' ]/T2['WholeNum']
    T2['Segregation'] = T2['Segregation'] / 100
    T2['log_WholeNum'] = np.log(T2['WholeNum'])
    T2['org_WholeNum'] = T2['WholeNum'] + 0
    T2['Selected'] = [1]*len(T2)



    money_cols = ['MedianInc_WholeAvg', 'MedianInc_Disparity',]


    for i in money_cols:
        T2[i] = T2[i] / 1000


    rate1_cols = ['FacNumRate', 'CaseRate', 'republican_rate', 'vehicle',
                'Segregation','racial_weighted_bias','hesitancy','Black_Prop']

    for i in rate1_cols:
        T2[i] = T2[i]  * 100
        
        
    rate100_cols = ['HighSchool_WholeRate','HighSchool_Disparity', 
                    'IT_WholeRate','IT_Disparity',
                    'FluVax_WholeRate', 'FluVax_Disparity', 
                    'A15T74_WholeRate', 'A15T74_Disparity', 
                    'A20T74_WholeRate', 'A20T74_Disparity', 
                    'Above75_WholeRate', 'Above75_Disparity',
                    'Above65_WholeRate', 'Above65_Disparity',
                    'Above20_WholeRate', 'Above20_Disparity',
                    'Above15_WholeRate', 'Above15_Disparity']

    # display(HTML(T2[money_cols].describe().to_html()))
    # display(HTML(T2[rate1_cols].describe().to_html()))
    # display(HTML(T2[rate100_cols].describe().to_html()))
    # print(T2['State'].unique())
    # print('State Number:', len(T2['State'].value_counts().sort_index()))
    return T2 




def prep_process(T2, cols, path):
    # cols: Y + Xs
    prefix_cols  = ['State', 'County']
    addtion_cols = [i for i in ['org_WholeNum', 'log_WholeNum', 'Black_Prop', 'BlackNum', 'NotInHighMobility', 'ReportNH'] if i not in cols]
    addtion_cols = addtion_cols if 'IT_Disparity' in cols else addtion_cols + ['IT_Disparity']
    
    # print('prefix cols:', prefix_cols)
    # print('addition cols:', addtion_cols)
    
    T2['Selected'] = 1
    print('Original Sample:', T2['Selected'].sum())
        
    selected_columns = prefix_cols + cols + addtion_cols
    

    ### Here
    critieria_nonan = {}
    critieria_nonan_list = selected_columns
    if 'FluVax_Disparity' not in selected_columns:
        critieria_nonan_list.append('FluVax_Disparity')
    for col in critieria_nonan_list:
        # print(col)
        critieria_nonan[col] = (-T2[col].isna()).astype(int)
        
    for col in critieria_nonan:
        T2['Selected'] = T2['Selected']*critieria_nonan[col]
        print('The object after Dropping Nan:', col, T2['Selected'].sum())
        
    
    cirteria_within01 = {}
    cirteria_within01_list = ['CvdVax_MWhiteRate', 'CvdVax_MBlackRate']
    for col in cirteria_within01_list:
        cirteria_within01[col] = (T2[col] < 100).astype(int)
    
    
    ### Here
    cirteria_others = {}
    cirteria_others['LargeBlackNum'] = (T2['BlackNum'] >= 273).astype(int)
    
    for col in cirteria_others:
        T2['Selected'] = T2['Selected']*cirteria_others[col]
        print('The object after the process of:', col, T2['Selected'].sum())
        
    pathT2 = os.path.join(path, 'T2.csv')
    print('Write T2 to:', pathT2 )
    T2.to_csv(pathT2)
    
    return T2, selected_columns


def standardize_data(T2, YXcols, selected_columns, path):
    T3 = T2[T2['Selected'] == 1][selected_columns]
    
    
    pathDict = os.path.join(path, 'DataVarDict.csv')
    pathStata = os.path.join(path, 'Data.dta')
    
    T3.describe().T.to_csv(pathDict)
    T3.to_stata(pathStata)
    print('Write T3     to:', pathStata )
    
    # Do not normalize
    dummy_cols = ['republican', 'urban', 'ReportNH']
    # DependentVariables = [i for i in YXcols if i[-1] == 'Y']
    # DependentVariables = [i for i in YXcols if 'DisparityY' in i or 'RDY' in i or 'SDY' in i]
    DependentVariables = [i for i in YXcols if 'DisparityY' in i]
    
    print('Dependent Variables are:', DependentVariables)
    not_normalized_cols = DependentVariables + dummy_cols
    print('\n\nnot normalized:', not_normalized_cols, '\n\n')
    
    T3Norm = T3.copy()
    for col in YXcols:
        if col in not_normalized_cols:
            
            continue
        df = T3Norm[col]
        T3Norm[col]=(df-df.mean())/df.std()
        
    pathNormDict = os.path.join(path, 'DataNormVarDict.csv')
    pathNormStata = os.path.join(path, 'DataNorm.dta')
    
    T3Norm.describe().T.to_csv(pathNormDict)
    T3Norm.to_stata(pathNormStata)
    print('Write T3Norm to:', pathNormStata )
        
    return T3, T3Norm


def get_regression(Y, X, addText, state_dummy_num = '16'):
    # Y: string
    # X: list, including all the dependent variable
    reg_string = ' '.join(['reg', Y] + X) #+ sum([v for k, v in CV.items()], []))
    # reg_string = reg_string+'dummy

    reg_string = reg_string + ' state_dummy1-state_dummy{} '.format(state_dummy_num)
    if addText.get('W'):
        reg_string = reg_string + ' [pweight=org_WholeNum] '  ### 
    if addText.get('R'):
        reg_string = reg_string + ', r ' if ',' not in reg_string else reg_string + 'cluster(State) ' 
    if addText.get('C'):
        reg_string = reg_string + ', cluster(State) ' if ',' not in reg_string else reg_string + 'cluster(State)'
    # reg_string = reg_string + ', level()'
    
    return reg_string


def get_outreg2(Y, X, DocName, addText, replace = False):
    # Title = '_'.join(['Mdl', '.'.join([k for k, v in addText.items() if v] )])
    # Title = Title[:-1] if Title[-1] == '_' else Title
    # omit = "state_dummy1-state_dummy" + max_state + " o.state_dummy1-o.state_dummy" + max_state
    Title = Y
    TitleString = 'append ctitle({})'.format(Title) if not replace else 'replace ctitle({})'.format(Title)
    addTextString = 'addtext(SD, True, ' + ', '.join([k + ', ' + str(v) for k, v in addText.items()]) + ')' 
    d = ' '.join(['outreg2 using', 
                  DocName + ',', 
                  TitleString,  
                  addTextString, 
                  " keep (" +' '.join(X) + ') '
                  'excel',
                  "alpha(0.001, 0.01, 0.05, 0.10) symbol(***, **, *, +)"
                 ])
    return d


def gen_regression_code(YXLists,
                        additonal_stata = [], 
                        state_dummy_num = 16,
                        winsor = 95, 
                        Norm = True):
    

    # Use the dataset: Normalized or not
    if Norm == True:
        DataPath = os.path.join(os.getcwd(), path, 'DataNorm.dta')
    else:
        DataPath = os.path.join(os.getcwd(), path, 'Data.dta')

    winsor_range = '(' + str(100- winsor) + ',' +  str(winsor) + ')'
    winsor_code = 'winsor2 {}, replace cuts ' + winsor_range
    
    L1 = ['clear all', 'set more off', 'use "' + DataPath + '"', '\n']
    L2 = ['\n', "tab State, generate(state_dummy)", '\n']

    # Winsor variable
    L = L1  + additonal_stata + L2 + [winsor_code.format(i) for i in list(set(sum(YXLists, [])))] + ['\n\n']


    # Regression
    addText = {'R': True, 'C': True, 'W': True}
    DocName = os.path.join(path, 'RegResult.doc')
    
    Regression_Commands = []
    for idx,  YXCols in enumerate(YXLists):
        # print(state_dummy_num)
        Y, X_used = YXCols[0], YXCols[1:]

        # X_used = Xlist
        reg_string = get_regression(Y, X_used, addText, state_dummy_num)

        Regression_Commands.append(reg_string) 

        replace = True if idx == 0 else False
        
        Title = Y.replace('Y', '').replace('Disparity', 'D')
        out = get_outreg2(Title, X_used, DocName, addText, replace)

        L = L + [reg_string + '\n', out, '\n']
        
    # End Part
    stata_string =  '\n'.join(L)
    do_suffix = 'norm' if Norm else 'orig'
    StataCodePath = os.path.join(os.getcwd(), path, 'do_file_{}.do'.format(do_suffix))
    print(StataCodePath, '\n\n\n')
    print(stata_string)
    with open(StataCodePath, 'w') as f:
        f.write(stata_string)
            
    return StataCodePath


def prepare_YX(Vax, Disparity, Var_list):
    ##############
    # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
    # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
    # Var_list = ['Base']
    ##############
    
    Y  = Vax + '_' + Disparity + 'Y' 
    X_dict = {
        'Base': [
            'MedianInc_WholeAvg',  'MedianInc_' + Disparity,
            'HighSchool_WholeRate', 'HighSchool_' + Disparity,
            'FacNumRate', 'CaseRate',
            'IT_WholeRate', 'IT_' + Disparity, 
            'urban', 'vehicle', 
            'republican_rate', 'Segregation', 'racial_weighted_bias',
            'hesitancy', 'Black_Prop',
        ],
        'FluVax':['FluVax_WholeRate', 'FluVax_' + Disparity],
        'Above75': ['Above75_WholeRate', 'Above75_' + Disparity],
        'A15T74':['A15T74_WholeRate', 'A15T74_' + Disparity],
        'RecentPositive':['positivity'], 
    }

    X_used = sum([X_dict[var_name] for var_name in Var_list], [])
    YXcols = [Y] + X_used

    return YXcols


if __name__ =='__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, default='main_regression', help=' ')

    args = parser.parse_args()
    task = args.task
    
    if task == 'main_regression':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if not os.path.exists(path):
            os.makedirs(path)

        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax', 'FluVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base']
                        # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'main_regression_originalX':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if not os.path.exists(path):
            os.makedirs(path)

        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax', 'FluVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base']
                        # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = False
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'check_age_all':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if not os.path.exists(path):
            os.makedirs(path)

        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        ['Base', 'FluVax'],
                        ['Base', 'FluVax', 'Above75'],
                        ['Base', 'FluVax', 'Above75', 'A15T74'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'check_age_above15':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if not os.path.exists(path):
            os.makedirs(path)

        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVaxAbove15']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        ['Base', 'FluVax'],
                        ['Base', 'FluVax', 'Above75'],
                        ['Base', 'FluVax', 'Above75', 'A15T74'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'check_age_above20':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if not os.path.exists(path):
            os.makedirs(path)

        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVaxAbove20']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        ['Base', 'FluVax'],
                        ['Base', 'FluVax', 'Above75'],
                        ['Base', 'FluVax', 'Above75', 'A15T74'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'check_disparity_types':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if not os.path.exists(path):
            os.makedirs(path)

        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity', 'RD', 'LogRD', 'SD']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        # ['Base', 'FluVax'],
                        # ['Base', 'FluVax', 'Above75'],
                        # ['Base', 'FluVax', 'Above75', 'A15T74'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'diff_dates':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        
        for date in ['03-27', '04-07', '04-19', '05-20', '05-20_FullVax']:
            path = os.path.join('StataCode', folder, date)
            print('Generate Path:', path)
            if not os.path.exists(path):
                os.makedirs(path)

            # update T2
            
            RawDataPath = 'StataReg/CountyVaccine-{}.csv'.format(date.split('_')[0])

            print(RawDataPath)


            T2 = pd.read_csv(RawDataPath) 
            T2 = dependent_variable_construction(T2)
            T2 = independent_variable_construction(T2)
        
            # generate YXLists and cols
            YXLists = []
            cols = []
            Vax = 'CvdVax' if 'FullVax' not in date else 'FullCvdVax'
            Disparity = 'Disparity'
            Var_list = ['Base']
            YXcols = prepare_YX(Vax, Disparity, Var_list)
            YXLists.append(YXcols)
            cols = cols + [i for i in YXcols if i not in cols]

            # generate T3
            # print(all_variables)
            T2, selected_columns = prep_process(T2, cols, path)
            T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

            state_dummy_num = T3Norm['State'].nunique()
            additonal_stata = []
            
            # additonal_stata = ['drop if NotInHighMobility == 0']
            # for Norm in [True, False]:
            Norm = True
            StataCodePath = gen_regression_code(YXLists,
                                                additonal_stata,
                                                state_dummy_num,
                                                winsor = 95, 
                                                Norm = Norm)


            ## Do some processing in Python
            ## Set do-file information
            dofile = StataCodePath

            stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
            cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

            ## Run do-file
            # subprocess.call(cmd) 
            # pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
            #            shell=True, preexec_fn=os.setsid) 

            # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  

    elif task == 'residential_mobility':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)


        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        ['Base', 'FluVax', ],
                        ['Base', 'FluVax', 'Above75', ],
                        ['Base', 'FluVax', 'Above75', 'A15T74'],
                        # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        # additonal_stata = []
        additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'recent_positive_rate':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)


        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        ['Base', 'RecentPositive'],
                        ['Base', 'RecentPositive', 'FluVax', ],
                        ['Base', 'RecentPositive', 'FluVax', 'Above75', ],
                        ['Base', 'RecentPositive', 'FluVax', 'Above75', 'A15T74'],
                        # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        # print(list(T2.columns))
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 
    
    elif task == 'avoid_collinearity':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)


        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['CvdVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        # ['Base', 'RecentPositive'],
                        ['Base', 'FluVax', ],
                        ['Base', 'FluVax', 'Above75', ],
                        ['Base', 'FluVax', 'Above75', 'A15T74'],
                        # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    YXcols = [i for i in YXcols if i != 'hesitancy']
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        # print(list(T2.columns))
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 

    elif task == 'subsample_analysis_6_and_10_states':

        for NHReport in ['6StateNHWhite', '10StateAllWhite']:
            # create folder
            folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
            
            path = os.path.join('StataCode', folder, NHReport)
            print('Generate Path:', path)
            if os.path.exists(path):
                shutil.rmtree(path)
            os.makedirs(path)


            # update T2
            RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
            T2 = pd.read_csv(RawDataPath) 
            T2 = dependent_variable_construction(T2)
            T2 = independent_variable_construction(T2)
            
            # generate YXLists and cols
            YXLists = []
            cols = []
            # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
            for Vax in ['CvdVax']:
                # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
                for Disparity in ['Disparity']:
                    # 'Base'
                    for Var_list in [
                            ['Base'],
                            # ['Base', 'RecentPositive'],
                            ['Base', 'FluVax', ],
                            ['Base', 'FluVax', 'Above75', ],
                            ['Base', 'FluVax', 'Above75', 'A15T74'],
                            # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                        ]:
                        YXcols = prepare_YX(Vax, Disparity, Var_list)
                        YXcols = [i for i in YXcols if i != 'hesitancy']
                        YXLists.append(YXcols)
                        cols = cols + [i for i in YXcols if i not in cols]

            # generate T3
            # print(all_variables)
            # print(list(T2.columns))
            T2, selected_columns = prep_process(T2, cols, path)
            T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

            
            # additonal_stata = []

            ReportNHStates = ['Illinois', 'Texas', 'Virginia', 'California', 'New Jersey',  'Oregon']
            if NHReport == '6StateNHWhite':
                additonal_stata = ['drop if ReportNH == 0']
                state_dummy_num = len(ReportNHStates)
            else:
                additonal_stata = ['drop if ReportNH == 1']
                state_dummy_num = T3Norm['State'].nunique() - len(ReportNHStates)

            # for Norm in [True, False]:
            Norm = True
            StataCodePath = gen_regression_code(YXLists,
                                                additonal_stata,
                                                state_dummy_num,
                                                winsor = 95, 
                                                Norm = Norm)


            ## Do some processing in Python
            ## Set do-file information
            # dofile = StataCodePath

            # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
            # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

            # ## Run do-file
            # subprocess.call(cmd) 

    elif task == 'vax_rate_on_all_white':

        # create folder
        folder = task #+ str(datetime.now()).split('.')[0].replace(':', '-').replace(' ', '_')
        path = os.path.join('StataCode', folder)
        print('Generate Path:', path)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)


        # update T2
        RawDataPath = 'StataReg/CountyVaccine-04-19.csv'
        T2 = pd.read_csv(RawDataPath) 
        T2 = dependent_variable_construction(T2)
        T2 = independent_variable_construction(T2)
        
        # generate YXLists and cols
        YXLists = []
        cols = []
        # Vax = 'CvdVax' # FullCvdVax, CvdVaxAbove20, CvdVaxAbove15. 'FluVax
        for Vax in ['ZCvdVax']:
            # Disparity = 'Disparity' # 'RD', 'LogRD', 'SD'
            for Disparity in ['Disparity']:
                # 'Base'
                for Var_list in [
                        ['Base'],
                        # ['Base', 'RecentPositive'],
                        ['Base', 'FluVax', ],
                        ['Base', 'FluVax', 'Above75', ],
                        ['Base', 'FluVax', 'Above75', 'A15T74'],
                        # ['Base', 'FluVax', 'Above75', 'A15T74', 'RecentPositive'],
                    ]:
                    YXcols = prepare_YX(Vax, Disparity, Var_list)
                    # YXcols = [i for i in YXcols if i != 'hesitancy']
                    YXLists.append(YXcols)
                    cols = cols + [i for i in YXcols if i not in cols]

        # generate T3
        # print(all_variables)
        # print(list(T2.columns))
        T2, selected_columns = prep_process(T2, cols, path)
        T3, T3Norm = standardize_data(T2, cols, selected_columns, path)

        state_dummy_num = T3Norm['State'].nunique()
        additonal_stata = []
        # additonal_stata = ['drop if NotInHighMobility == 0']
        # for Norm in [True, False]:
        Norm = True
        StataCodePath = gen_regression_code(YXLists,
                                            additonal_stata,
                                            state_dummy_num,
                                            winsor = 95, 
                                            Norm = Norm)


        ## Do some processing in Python
        ## Set do-file information
        # dofile = StataCodePath

        # stata_app_path = '/Applications/Stata/StataSE.app/Contents/MacOS/StataSE'
        # cmd = [stata_app_path, "do", dofile, "mpg", "weight", "foreign"]

        # ## Run do-file
        # subprocess.call(cmd) 
    
    else:
        pass


