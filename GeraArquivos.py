arq = open('processos.in', 'w')

arq.writelines('0 PROG01 1 20' + '\n')
arq.writelines('0 PROG02 1 10 5 10\n')
arq.writelines('5 PROG10 1 5 3 15 5 10\n')
arq.writelines('3 PROG03 2 30\n')
arq.writelines('10 PROG15 1 5 1 15 1 20')

arq.close()




# timeAdmission = []
# nameProcess = []
# priority = []
# time = []

# for i in range(0, len(processos)):
#     timeAdmission.append(aux[i][0])
#     nameProcess.append(aux[i][1])
#     priority.append(aux[i][2])


# print(timeAdmission)
# print(nameProcess)
# print(priority)

