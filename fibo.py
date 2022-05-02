def recursive_nth_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    number = recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)
    return number


def main():
    print(recursive_nth_fibo(7))


if __name__ == "__main__":
    main()