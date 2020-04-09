
def transf2gaussian(average, std, n):

    """
    average:
    std:
    n:
    """

    import numpy as np

    np.random.seed(12345678)

    value = np.random.normal(average, std, n)
    return value

#paramétrico: para dados com distribuição normal
def kolmogorov(data1, data2, alpha, flag):

    
    """
    Kolmogorov-Smirnov test

    data1: Receive the file to be compared.
    data2: Receive file for comparison with main file.
    alpha: Threshold value for hypothesis testing.
    flag: Receives a boolean value for saving or not saving the results to a text file.

    """

    import scipy.stats as st
    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    import tkinter as tk


    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('kolmogorov_results')
    # text = np.asarray((10),np.uint8)
    # texto = None
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/Kolmogorov-Smirnov-results.txt', 'w') as f:
            f.write('   --- Kolmogorov-Smirnov test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100
        newarray1[newarray1 < 0] = 0
        newarray2[newarray2 < 0] = 0


        _, ks_value = st.ks_2samp(newarray1, newarray2)


        if (ks_value * 100) > alpha:
            print('Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(ks_value, data_columns[col]))
            text[col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares\n'.format(ks_value, data_columns[col])

        else:
            print('Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(ks_value, data_columns[col]))
            text[col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares\n'.format(ks_value, data_columns[col])


        # Save results
        if flag == True:
            with open('database/Kolmogorov-Smirnov-results.txt', 'a') as f:
                if (ks_value * 100) > alpha:
                    f.write('Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(ks_value, data_columns[col]))
                else:
                     f.write('Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(ks_value, data_columns[col]))
                f.write('\n')
        # texto[col] = text
        # text.append(text)
    root = tk.Tk()
    root.title('kolmogorov_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

    # return ks_value

#paramétrico: para dados com distribuição normal
def studentst(data1, data2, alpha, flag):


    """
    Student’s t-test

    data1: 
    data2: 
    alpha: 
    flag: Receives a boolean value for saving or not saving the results to a text file.

    """

    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    from scipy import stats as st
    from scipy.stats import ttest_ind
    import tkinter as tk


    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('T_student_results')
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/Students-t-test-results.txt', 'w') as f:
            f.write('   --- Student’s t-test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose())*100)

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)

        # newarray1=np.asarray([635,704,662,560,603,745,698,575,633,669],np.uint8)
        # newarray2=np.asarray([640,712,681,558,610,740,707,585,635,682],np.uint8)

        _stat, p = ttest_ind(newarray1, newarray2)

        
        if (p * 100) > alpha:
            print('Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
            text[col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares\n'.format(p, data_columns[col])
        else:
            print('Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
            text[col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares\n'.format(p, data_columns[col])

        # Save results
        if flag == True:
            with open('database/Students-t-test-results.txt', 'a') as f:
                if (p * 100) > alpha:
                    f.write('Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
                else:
                     f.write('Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
                f.write('\n')
    root = tk.Tk()
    root.title('student_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

#não paramétrico: para dados sem presuposta distribuição específica
def friedman(data1, data2, alpha, flag):

    """
    The Friedman test tests the null hypothesis that repeated measurements of the same individuals have the same distribution.
    It is often used to test for consistency among measurements obtained in different ways.
    For example, if two measurement techniques are used on the same set of individuals, the Friedman test can be used
    to determine if the two measurement techniques are consistent.
    """

    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    from scipy import stats as st
    from scipy.stats import friedmanchisquare
    import tkinter as tk


    data_columns = []
    alpha = float(alpha)


    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('Friedman_results')
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/Friedman-test-results.txt', 'w') as f:
            f.write('   --- Friedman test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100
        newarray1[newarray1 < 0] = 0
        newarray2[newarray2 < 0] = 0

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)


        stat, p = friedmanchisquare(newarray1, newarray1, newarray2, newarray2)

        
        if (p * 100) > alpha:
            print('Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
            text[col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares\n'.format(p, data_columns[col])
        else:
            print('Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
            text[col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares\n'.format(p, data_columns[col])

        # Save results
        if flag == True:
            with open('database/Friedman-test-results.txt', 'a') as f:
                if (p * 100) > alpha:
                    f.write('Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
                else:
                     f.write('Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(p, data_columns[col]))
                f.write('\n')
    root = tk.Tk()
    root.title('friedman_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

#teste paramétrico: para dados com distribuição normal
def bartlett_test(data1,data2,alpha,flag):
    """
    Perform Bartlett’s test for equal variances

    Bartlett’s test tests the null hypothesis that all input samples are from populations with equal variances.
    or samples from significantly non-normal populations, Levene’s test levene is more robust.

    """



    import scipy.stats as st
    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    import tkinter as tk

    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('Bartlett_results')
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/bartlett test-results.txt', 'w') as f:
            f.write('   --- bartlett test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100
        newarray1[newarray1 < 0] = 0
        newarray2[newarray2 < 0] = 0

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)

        _, P_value = st.bartlett(newarray1, newarray2)


        if (P_value * 100) > alpha:
            print(
                'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(P_value, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem variâncias iguais\n'.format(
                P_value, data_columns[col])
        else:
            print(
                'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(P_value, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem variâncias iguais\n'.format(
                P_value, data_columns[col])

        # Save results
        if flag == True:
            with open('database/bartlett-results.txt', 'a') as f:
                if (P_value * 100) > alpha:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(
                            P_value, data_columns[col]))
                else:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(
                            P_value, data_columns[col]))
                f.write('\n')

    root = tk.Tk()
    root.title('bartlett_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

#teste não paramétrico: para dados sem presuposta distribuição específica
def levene_test(data1,data2,alpha,flag):
    """
    The Levene test tests the null hypothesis that all input samples are from populations with equal variances.
     Levene’s test is an alternative to Bartlett’s test bartlett in the case where there are significant deviations from normality.

    """



    import scipy.stats as st
    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    import tkinter as tk

    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('Levene_results')
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/levene test-results.txt', 'w') as f:
            f.write('   --- levene test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100
        newarray1[newarray1 < 0] = 0
        newarray2[newarray2 < 0] = 0

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)

        _, P_value = st.bartlett(newarray1, newarray2)


        if (P_value * 100) > alpha:
            print(
                'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(P_value, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem variâncias iguais\n'.format(
                P_value, data_columns[col])


        else:
            print(
                'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(
                    P_value, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem variâncias iguais\n'.format(
                P_value, data_columns[col])

        # Save results
        if flag == True:
            with open('database/levene-results.txt', 'a') as f:
                if (P_value * 100) > alpha:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(
                            P_value, data_columns[col]))
                else:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem variâncias iguais'.format(
                            P_value, data_columns[col]))
                f.write('\n')
    root = tk.Tk()
    root.title('levene_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

#testa a distribuição dos dados
def normal_test(data1,alpha,flag):
    """
        This function tests the null hypothesis that a sample comes from a normal distribution.
         It is based on D’Agostino and Pearson’s [1], [2] test that combines skew and kurtosis to produce an omnibus test of normality.

        """

    import scipy.stats as st
    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    import tkinter as tk

    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    # array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    # array2 = fo.transform2array(array2)
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/normal test-results.txt', 'w') as f:
            f.write('   --- normal test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        # newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        # newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        # newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray1[newarray1 < 0] = 0
        # newarray2[newarray2 < 0] = 0
        # newarray2[newarray2 > 100] = 100

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)

        _, P_value = st.normaltest(newarray1)

        if (P_value * 100) > alpha:
            print(
                'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem distribuição normal'.format(
                    P_value, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem distribuição normal\n'.format(
                P_value, data_columns[col])

        else:
            print(
                'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem distribuição normal'.format(
                    P_value, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem distribuição normal\n'.format(
                P_value, data_columns[col])

        # Save results
        if flag == True:
            with open('database/normal-results.txt', 'a') as f:
                if (P_value * 100) > alpha:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] possuem distribuição normal'.format(
                            P_value, data_columns[col]))
                else:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] possuem distribuição normal'.format(
                            P_value, data_columns[col]))
                f.write('\n')
    root = tk.Tk()
    root.title('normal_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

#teste não paramétrico
def Mann_Whitney_test(data1,data2,alpha,flag):
    """
    Compute the Mann-Whitney rank test on samples x and y.
    for more informations see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html#scipy.stats.mannwhitneyu
    """

    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    from scipy import stats as st
    from scipy.stats import friedmanchisquare
    import tkinter as tk

    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('Man_Whitney_results')
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/Mann_Whitney-test-results.txt', 'w') as f:
            f.write('   --- Mann_Whitney test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100
        newarray1[newarray1 < 0] = 0
        newarray2[newarray2 < 0] = 0

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)

        stat, p = friedmanchisquare(newarray1, newarray1, newarray2, newarray2)


        if (p * 100) > alpha:
            print(
                'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(
                    p, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares\n'.format(
                p, data_columns[col])

        else:
            print(
                'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(
                    p, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares\n'.format(
                p, data_columns[col])

        # Save results
        if flag == True:
            with open('database/Mann_Whitney-test-results.txt', 'a') as f:
                if (stat * 100) > p:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] são similares'.format(
                            p, data_columns[col]))
                else:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] são similares'.format(
                            p, data_columns[col]))
                f.write('\n')
    root = tk.Tk()
    root.title('Mann_Whitney_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()

#teste não paramétrico
def ranksums_test(data1,data2,alpha,flag):
    """
        Compute the Wilcoxon rank-sum statistic for two samples.

        The Wilcoxon rank-sum test tests the null hypothesis that two sets of measurements are drawn from the same distribution.
        The alternative hypothesis is that values in one sample are more likely to be larger than the values in the other sample.
        This test should be used to compare two samples from continuous distributions. It does not handle ties between measurements in x and y.
        For tie-handling and an optional continuity correction see scipy.stats.mannwhitneyu.
       """

    import file_operations as fo
    import pandas as pd
    import numpy as np
    from pandas import DataFrame as df
    from scipy import stats as st
    from scipy.stats import friedmanchisquare
    import tkinter as tk

    data_columns = []
    alpha = float(alpha)

    array1 = fo.loading_file(data1)
    array2 = fo.loading_file(data2)

    _rows, cols = array1.shape[:2]
    data_columns = array1.columns.values

    array1 = fo.transform2array(array1)
    array2 = fo.transform2array(array2)
    print('Ranksmus_results')
    text = ["" for x in range(cols)]

    if flag == True:
        with open('database/ranksums-test-results.txt', 'w') as f:
            f.write('   --- ranksums test results --- \n\n')

    for col in range(cols):

        newarray1 = np.asarray(array1[:, col], np.float)
        newarray2 = np.asarray(array2[:, col], np.float)

        newarray1 = ((newarray1.transpose()))
        newarray2 = ((newarray2.transpose()))

        newarray1 = np.float64(newarray1)
        newarray2 = np.float64(newarray2)

        newarray1[newarray1 > 100] = 100
        newarray2[newarray2 > 100] = 100
        newarray1[newarray1 < 0] = 0
        newarray2[newarray2 < 0] = 0

        # newarray1 = newarray1.reshape(-1)
        # newarray2 = newarray2.reshape(-1)

        stat, p = st.ranksums(newarray1, newarray2)


        if (p * 100) > alpha:
            print(
                'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] tem a mesma distribuição'.format(
                    p, data_columns[col]))

            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] tem a mesma distribuição\n'.format(
                p, data_columns[col])

        else:
            print(
                'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] tem a mesma distribuição'.format(
                    p, data_columns[col]))
            text[
                col] = 'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] tem a mesma distribuição\n'.format(
                p, data_columns[col])

        # Save results
        if flag == True:
            with open('database/ranksums-test-results.txt', 'a') as f:
                if (stat * 100) > p:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para confirmar a hipótese de que os dados para [{}] tem a mesma distribuição'.format(
                            p, data_columns[col]))
                else:
                    f.write(
                        'Com um p de {:.4f}, há evidências suficientes para negar a hipótese de que os dados para [{}] tem a mesma distribuição'.format(
                            p, data_columns[col]))
                f.write('\n')
    root = tk.Tk()
    root.title('ranksums_test_results')
    T = tk.Text(root, height=15, width=130)
    T.pack()
    T.insert(tk.END, text)
    tk.mainloop()


