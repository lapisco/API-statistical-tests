import statistical_tests as st
import file_operations as fo
import numpy as np
# import cv2

# Import paths
data1 = '/home/adriell/Downloads/teste estatístico Artigo 5/TKinter_tests/database/brain/parzen_mask.csv'
data2 = '/home/adriell/Downloads/teste estatístico Artigo 5/TKinter_tests/database/brain/parzen_mask_clutering.csv'



# ---------------------------------------------------------------
# data1=np. asarray([1,90642,2,10288,1,52229,2,61826,1,42738,2,22488,1,69742,3,15435,1,98492,1,99568],np.uint8)
# data2=np. asarray([1,90642,2,10288,1,52229,2,61826,1,42738,2,22488,1,69742,3,15435,1,98492,1,99568],np.uint8)

# st.transf2gaussian()


# Kolmogorov-Smirnov test
print('resultados comogorov')
st.kolmogorov(data1, data2, 3, False)

# print('\n\nresultados students')
# # # Student's t-test
# st.studentst(data1, data2, 1, False)


# print('\n\nresultados friedman')
# # # Friedman test
# st.friedman(data1, data2, 3, False)

# #
# print('\n\nresultados bartlett')
# # # bartelett test
# st.bartlett_test(data1, data2, 3, False)

#
# print('\n\nresultados levene')
# # # levene test
# st.levene_test(data1, data2, 3, False)
#
#
# print('\n\nresultados normal')
# # # normal test
# st.normal_test(data1, 3, False)
# #
# #
# print('\n\nresultados mann_whitney ')
# # # mann_whitney test
# st.Mann_Whitney_test(data1, data2, 3, False)

#
# print('\n\nresultados ranksums ')
# # # ranksums test
# st.ranksums_test(data1, data2, 3, False)


