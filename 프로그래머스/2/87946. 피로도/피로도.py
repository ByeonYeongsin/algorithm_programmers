def solution(k, dungeons):
    import itertools
    orders = list(itertools.permutations([i for i in range(len(dungeons))]))
    max_count = 0
    for order in orders:
        count, now_k = 0, k
        now_dungeon = [dungeons[i] for i in order]
        for dungeon in now_dungeon:
            if dungeon[0] <= now_k:
                now_k -= dungeon[1]
                count += 1
        if max_count < count:
            max_count = count
            if max_count == len(dungeons):
                break
    return max_count