import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')


import mytest as te

dispatcher = {}

def prob1():
    def prob1_mine(n):
        pass
    
    def prob1_db(h):
        pass

    dispatcher["prob1_mine"] = prob1_mine
    dispatcher["prob1_db"] = prob1_db


def prob2():
    def prob2_mine(n):
        pass
    
    def prob2_db(h):
        pass

    dispatcher["prob2_mine"] = prob2_mine
    dispatcher["prob2_db"] = prob2_db


def prob3():
    def prob3_mine(n):
        pass
    
    def prob3_db(h):
        pass

    dispatcher["prob3_mine"] = prob3_mine
    dispatcher["prob3_db"] = prob3_db



def prob4():
    def prob4_mine(n):
        pass
    
    def prob4_db(h):
        pass

    dispatcher["prob4_mine"] = prob4_mine
    dispatcher["prob4_db"] = prob4_db



def prob5():
    def prob5_mine(n):
        pass
    
    def prob5_db(h):
        pass

    dispatcher["prob5_mine"] = prob5_mine
    dispatcher["prob5_db"] = prob5_db


dispatcher["prob1"] = prob1
dispatcher["prob2"] = prob2
dispatcher["prob3"] = prob3
dispatcher["prob4"] = prob4
dispatcher["prob5"] = prob5


def get_prob_input(prob_num):
    # return 값은 반드시 list나 tuple 형태로
    if prob_num == 1:
        return 1
    elif prob_num == 2:
        return 2
    elif prob_num == 3:
        return 3
    elif prob_num == 4:
        return 4
    else: 
        return 5
    pass

num_probs = 5
num_test = 10
test_res = list()
for i in range(1, num_probs+1):
    i, e = te.test_probs_ntimes(te.test_prob, num_test, prob_num=i, dispatcher=dispatcher, get_input=get_prob_input, show_input_info=False)
    test_res.append({"info":i, "exec_time":e})
    print("-------")


# import json
# 0번째 문제 1, 2번째 테스트 케이스 확인
# cases = [1, 2]
# for case_info in test_res[0]['info'][cases]:
#     print(json.dumps(case_info, sort_keys=True, indent=4))
