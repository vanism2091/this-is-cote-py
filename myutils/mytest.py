import time
import numpy as np
import random
# import collections


# iterable 객체에서 elmt k개를 뽑아 list<elmt>로 반환하는 함수
def get_choices(iterable, k=1): return random.choices(iterable, k=k)


# 문제 풀이때 만든 각 case test를 위한 함수
def test_prob(prob_num, dispatcher, get_input):
    dispatcher[f"prob{prob_num}"]()
    inputs = get_input(prob_num)
    t1, res1 = exec_time_check(dispatcher[f"prob{prob_num}_mine"], *inputs)
    t2, res2 = exec_time_check(dispatcher[f"prob{prob_num}_db"], *inputs)
    # if isinstance(inputs, collections.Iterable):
    #     t1 = exec_time_check(dispatcher[f"prob{prob_num}_mine"], *inputs)
    #     t2 = exec_time_check(dispatcher[f"prob{prob_num}_db"], *inputs)
    # else:
    #     t1 = exec_time_check(dispatcher[f"prob{prob_num}_mine"], inputs)
    #     t2 = exec_time_check(dispatcher[f"prob{prob_num}_db"], inputs)
    info = {
        "input": inputs,
        "res1": res1,
        "res2": res2
    }
    return [t1, t2, res1 == res2 if res1 != None and res2 != None else None], info


# 실행 시간, return 값을 반환하는 함수
def exec_time_check(method, *params):
    start = time.time()
    if not len(params):
        res = method()
    else:
        res = method(*params)
    end = time.time()
    return end - start, res


# 알고리즘 설명 강의할 때, 처음 만든 test_ntimes 함수
def test_ntimes(test_method, ntimes, params):
    res = []
    for i in range(ntimes):
        res.append(test_method(*params))
    print(*res, sep='\n')
    res = np.array(res)
    print(np.average(res, axis=0))


# 문제 풀이때 사용하기 위해 만든 test_ntimes 함수
def test_probs_ntimes(test_method, ntimes, **params):
    # res [( case_num, [t1, t2, res1==res2], info_dict )]
    # info_dict = {"input": , "res1": , "res2": }
    # returns [info_dict], exec_avg: [avg_et_res1, avg_et_res2]
    res = np.empty((0, 3))
    for i in range(ntimes):
        res = np.vstack((res, np.array([i, *test_method(**params)], dtype=object)))

    # exec_times, results 만 따로 보고 싶다
    exec_times_results = np.array([v for v in res[:, 1]], dtype=np.float32)
    print(*exec_times_results, sep='\n')
    exec_avg = np.average(exec_times_results[:, :2], axis=0)
    # 평균 실행 시간 출력 [ mine, db ]
    print("average execution time:: ", exec_avg)

    # score == True if res1 == res2 else False
    # [score] > score == nan || 0 (False) || 1 (True)
    scores = exec_times_results[:, 2]
    if np.any(np.isnan(scores)):
        # test case 결과 중 nan이 하나라도 있는 경우
        # function 문법적 작성 문제
        print("Error:: Function returns NOTHING at some cases..!")
    elif np.any(scores == 0):
        # test case 결과 중 False가 하나라도 있는 경우
        # function 논리적 구현 문제
        false_cases = np.where(scores == 0)[0]
        print(f"Diff... at #{len(false_cases)} cases")
        print(false_cases)
    else:
        # 모든 case 결과가 True인 경우
        print("All clear--!")
    return res[:, 2].tolist(), exec_avg.tolist()
