from glob import glob

PYTHON_DEFAULT_CODE = '''"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!

    return


if __name__ == '__main__':
    main()
'''

C_DEFAULT_CODE = '''/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    // 이곳에 코드를 작성해주세요!

    return 0;
}'''


def make_file(filename, code):
    with open(filename, "w", encoding='UTF-8') as f:
        f.write(code)


def main():
    for i in range(1, 10):
        make_file(f'../python/{i}.py', PYTHON_DEFAULT_CODE)
        make_file(f'../c/{i}.c', C_DEFAULT_CODE)


if __name__ == '__main__':
    main()
