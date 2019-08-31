# 실행 : Ctrl + F5
# 디버깅 : F5

def _(c='=', n=20):
    print(c * n)


print('Hello', 'World', sep=', ', end='!\n')
print('%s * %s = %s' % (2, 9, 2 * 9))
print('{} * {} = {}'.format(2, 9, 2 * 9))
print('{a} * {b} = {c}'.format(a=2, b=9, c=2*9))
_()
# ==================== #
import simplejson as sj

test_dict = {'a': 95, 'b': 77, 'c': 65, 'd': 100}
print(sj.dumps(test_dict, sort_keys=True, indent=2))
_()
# ==================== #
for i in range(1, 10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i * j))
    _()
# ==================== #
class Test:
    def __init__(self):
        pass

    def print(self, msg):
        print('IN Test: ' + msg)

t = Test()
t.print('Hello, world')
_()
