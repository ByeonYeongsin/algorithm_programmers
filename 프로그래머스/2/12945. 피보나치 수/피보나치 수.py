def solution(n):
    f0, f1 = 0, 1
    fn = 0
    for i in range(2, n+1):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn % 1234567