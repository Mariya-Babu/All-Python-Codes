# import random
# for i in range(1,50):
#     x = random.randrange(1,1000)
#     print(x," = ")
#     y = int(input())
#     if(x==y):
#         continue
#     else:
#         print("Wrong")
rand_text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque amet veritatis aliquid neque odio similique incidunt praesentium nisi cupiditate minus ea explicabo, quod tempore quo laudantium inventore impedit alias assumenda tempora atque sit optio, beatae maxime. Debitis vitae consectetur tempore, ducimus saepe est accusamus? Aliquid voluptas corrupti maxime officia similique? Amet, animi fugit optio quae earum ab dolorem totam veritatis, dolores officia, sequi ducimus quidem quam neque corporis at eveniet debitis impedit dignissimos dolor reprehenderit quo consequatur eligendi? Quidem nemo aperiam dolor non, fugit molestias laboriosam eligendi obcaecati dolores sequi dolorem delectus sit eum in maiores necessitatibus, commodi vitae laborum."
li = list(rand_text.split())
for i in li:
    x = print(i," = ")
    y = input()
    if(x==y):
        continue
    else:
        print('wrong')