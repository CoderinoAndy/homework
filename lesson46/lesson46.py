# Lesson 46
def collatz(upper):
    kingcount = 0
    kingnum = 0
    for number in range(1, upper + 1):
        start = number
        counter = 0
        while number != 1:
            if number % 2 == 0:
                number //= 2
            else:
                number = 3*number + 1
            counter += 1
        
        if counter > kingcount:
            kingnum = start
            kingcount = counter
    return kingnum


def solo_collatz(num):
    size = 1
    start = num
    while start > 1:
        if start % 2 == 0:
            start = start//2
        else:
            start *= 3
            start += 1
        size += 1
    return size

longest = 0
best = 0
for num in range(1, 10000000):
    result = solo_collatz(num)
    if result > longest:
        longest = result
        best = num
print(f"{best} has length {longest}")

cache = {1:1}
def c_seq2(num):
    if num in cache:
        return cache[num]
    else:
        size = 1
        start = num
        while start > 1:
            if start % 2 == 0:
                start = start//2
            else:
                start *= 3
                start += 1
            if start in cache: # Oh! We found start, we did it before in a previous go!
                cache[num] = size + cache[start] # Logging in memory! Looks like we can add the size we counted and start and we can take the shortcut!
                return size + cache[start] # Okay. Here's the size of your num! I took the shortcut of cache[start].
            else:
                size += 1 # Continue adding up the size! We haven't recognized start yet in our memory!
        cache[num] = size # We got to the end of the collatz sequence and we didn't use the cache. That's okay! We can just add a new entry and move on.
        return cache[num] # Unfortunately, we were not very efficient so we can only return to you our non-shortcutted length. I am drawing upon my previous entry!
            

