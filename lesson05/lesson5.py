# Lesson 5
initial_money = int(input())
big_normal = input()
cookies_sold = big_normal.len()
big_sold = big_normal.count("b")
normal_sold = big_normal.count("c")

profit = 1.25*big_sold + 0.75*normal_sold

print(f"You sold {big_sold + normal_sold} cookies today!")
print(f"Today, you profited ${profit}")
print(f"You got {profit + initial_money} after selling the cookies!")
