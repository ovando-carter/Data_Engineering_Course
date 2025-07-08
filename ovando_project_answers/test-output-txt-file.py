import numpy as np

a_test_list = [2,4,5,6]
b_test_array = np.array(a_test_list)

np.savetxt('tot_yearly_loans.txt', b_test_array, fmt='%s', delimiter =';')


new_list = [['Tot. Loans: Jan', 'Tot. Loans: Feb', 'Tot. Loans: Mar', 'Tot. Loans: Apr', 'Tot. Loans: May'],['181', '164', '139', '138', '172']]
new_array = np.array(new_list)
print(new_array)

np.savetxt("sample7.txt", new_array, fmt='%s',delimiter =", ")

#content = np.loadtxt("sample7.txt")
#print(content)