from collections import Counter


def is_valid_pt1(num):
    return len(set(str(num))) < len(str(num)) and sorted(str(num)) == list(str(num))


def is_valid_pt2(num):
    cnt = Counter(str(num))
    return any(cnt[val] == 2 for val in str(num)) and sorted(str(num)) == list(str(num))


if __name__ == "__main__":
    print(sum(is_valid_pt2(num) for num in range(147981, 691424)))
