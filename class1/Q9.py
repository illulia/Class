# 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a = dict()
print(a)
a['name'] = 'python' # 1번
a[('a',)] = 'python' # 2번
# a[[1]] = 'python' 3번
a[250] = 'python' # 4번
print(a)