import torch.nn as nn
import torch
    # return res_new
# 最长回文子串

if __name__ == '__main__':

    a = 'ababaaaaaaaaab'

    l = len(a)
    M = [[0] * l for _ in range(l)]

    for i in range(l):
        M[i][i] = 1
        start_idx = i
        maxLength = 1
        if i < l-2:
            if a[i] == a[i+1]:
                M[i][i+1] = 1
                end_idx = i + 1
                maxLength = 2

    for length in range(3, l+1):
        for j in range(l-length+1):
            k = j + length - 1
            if a[j] == a[k]:
                M[j][k] = M[j+1][k-1]

                if M[j][k] == 1:
                    maxLength = length
                    start_idx = j
    
    answer = a[start_idx:start_idx+maxLength]
    print(M)


    # cv2.namedWindow('output2', cv2.WINDOW_NORMAL)
    # cv2.imshow('output2', res)
    # cv2.waitKey()