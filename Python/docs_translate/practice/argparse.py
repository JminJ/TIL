import argparse

# 인자들을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser()

# 입력받을 인자값을 등록
parser.add_argument('--target', required=True)
parser.add_argument('--env',required=False, default='dev')

# 입력받은 인자값을 args에 저장
args = parser.parse_args()

# 인자값 출력
print(args.target)
print(args.env)