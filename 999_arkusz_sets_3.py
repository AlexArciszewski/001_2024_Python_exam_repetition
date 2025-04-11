


def main() ->None:
    # user_num = int(input("Pls give me the number: "))
    user_num = 20
    num_list = []
    for num in range(user_num):
        if num % 2 == 0:
            num_list.append(num)
    user_set = set(num_list)
    print(user_set)

    num_list2 = []
    for num2 in range(user_num):
        if num2 % 3 == 2:
            num_list2.append(num2)
    user2_set = set(num_list2)
    print(user2_set)
    print("A+B")
    c = user_set.union(user2_set)
    print(c)
    print(len(c))
    print("A & B")
    d = user_set.intersection(user2_set)
    print(d)
    print(len(d))
    print("A – B")
    e = user2_set.difference(user_set)
    print(e)
    print(len(e))
    # print("B ^ A sym. diff")
    # f = user2_set.symetric_difference(user_set)
    # print(f)
    # print(len(f))

    if user2_set in user_set:
        print("Yeah")
    else:
        print(f"set B{user2_set} is not in set A {user_set}")



if __name__ == "__main__":
    main()

