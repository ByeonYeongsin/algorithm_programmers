# def solution(cacheSize, cities):
#     for i in range(len(cities)):
#         cities[i] = cities[i].lower()
        
#     answer = 0
#     if len(cities) < cacheSize:
#         return 5 * len(cities)
#     else:
#         answer = 5 * cacheSize
        
#     for i in range(cacheSize, len(cities)):
#         for j in range(cacheSize, 0, -1):
#             if cities[i] == cities[i-j]:
#                 answer += 1
#                 break
#         else: answer += 5
#     return answer




cache_hit = 1
cache_miss = 5

def solution(cacheSize, cities):
    answer = 0
    cache = []
    old = 0
    for city in cities:
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            answer += cache_hit
        else:
            answer += cache_miss
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city.lower())
    return answer