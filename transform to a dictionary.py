import statistical_tests as st
from pandas import DataFrame
import numpy as np

metrics_values = {}
mts = {}

teacher_accu=st.transf2gaussian(95.77 , 3.96,36)#ACCU
teacher_dice=st.transf2gaussian(87.29 , 11.18,36)#DICE
teacher_jac=st.transf2gaussian(78.82 , 14.43,36)#JAC
teacher_mcc=st.transf2gaussian(85.38 , 11.85,36)#MCC
teacher_sen=st.transf2gaussian(97.68, 3.45,36)#SEN
teacher_hd=st.transf2gaussian(8.23 , 2.91,36)#HAUSS
# teacher_spc=st.transf2gaussian(90.53 , 21.31,100)#SPC
# teacher_pre=st.transf2gaussian(99.32 , 02.99,100)#PRE

metrics_values[0]=teacher_accu
metrics_values[1]=teacher_dice
metrics_values[2]=teacher_jac
metrics_values[3]=teacher_mcc
metrics_values[4]=teacher_sen
metrics_values[5]=teacher_hd
# metrics_values[5]=teacher_spc
# metrics_values[6]=teacher_pre


# tr.save_results('teacher_accu',teacher_accu)
# tr.save_results('teacher_dice',teacher_dice)
# tr.save_results('teacher_jac',teacher_jac)
# tr.save_results('teacher_mcc',teacher_mcc)
# tr.save_results('teacher_sen',teacher_sen)
# tr.save_results('teacher_spc',teacher_spc)
# tr.save_results('teacher_pre',teacher_pre)

def get_metrics(metrics_lst, dict_values):

    if not dict_values:
        for metric in metrics_lst:
            dict_values[metric] = list()

    for metric in metrics_lst:
        if metric in dict_values:
            dict_values[metric].append(str(metrics_lst), dict_values)


    return dict_values



# values= [metrics_values[0], metrics_values[1], metrics_values[2], metrics_values[3], metrics_values[4], metrics_values[5], metrics_values[6]
mats = get_metrics(mts, metrics_values)

df = DataFrame(mats)
df.columns = ['acc', 'dice', 'jac', 'mcc', 'sen', 'hd']
df.to_csv('multi.csv')

# tr.read_results('accuracia','teacher_accu', 3)
