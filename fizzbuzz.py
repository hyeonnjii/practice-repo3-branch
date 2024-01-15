def get_fizzbuzz() -> str:
    for i in range(1, 16):
        if i % 3 == 0:
            print('fizz')
        else:
            print(f'{i}')

if __name__ == '__main__':
    get_fizzbuzz()
