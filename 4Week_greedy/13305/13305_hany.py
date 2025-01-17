# 13305번 주유소
'''
어떤 나라에 N개의 도시가 있다. 이 도시들은 일직선 도로 위에 있다.
제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동하려고 한다.
인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있다.

도로 길이의 단위는 km를 사용한다.

처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다.

기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다.

도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다.
각 도시에는 단 하나의 주유소가 있으며, 도시 마다 주유소의 리터당 가격은 다를 수 있다.
가격의 단위는 원을 사용한다.

원 안에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격이다.
도로 위에 있는 숫자는 도로의 길이를 표시한 것이다.

제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.
'''
# 최소의 비용
n = int(input()) # 도시의 개수
roads = list(map(int, input().split())) # 두 도시를 연결하는 각 도로의 길이
prices = list(map(int, input().split())) # 각 도시의 리터당 가격
roads.append(0)

pay = 0 # 기름값

min_price = 1000000001
# roads와 prices의 인덱스가 동일하고 각 인덱스는 도시를 대표한다.
# 해당 도시의 가격이 다음 도시의 가격보다 싸다면 그 다음 도시와 비교한다.

for idx in range(n):
    if idx == n - 1:
        break

    if min_price > prices[idx]:
        min_price = prices[idx]
    pay += (min_price * roads[idx])
print(pay)