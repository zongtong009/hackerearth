# Akash and Vishal are quite fond of travelling. They mostly travel by railways.
# They were travelling in a train one day and they got interested in the seating
# arrangement of their compartment. The compartment looked something like
# 1 2   3   ||  ||  4   5   6
# ||    ||
# 12    11  10  ||  ||  9   8   7
# WS    MS  AS   过道 AS  MS  WS
# So they got interested to know the seat number facing them and the seat type
# facing them. The seats are denoted as follows :

# Window Seat : WS
# Middle Seat : MS
# Aisle Seat : AS

# INPUT:                        OUPUT:
# 2                     19 WS
# 18                        45 AS
# 40
a = eval(input())
test_dict = {
    1: 'WS', 6: 'WS', 7: 'WS', 12: 'WS',
    2: 'MS', 5: 'MS', 8: 'MS', 11: 'MS',
    3: 'AS', 4: 'AS', 9: 'AS', 10: 'AS',
}
for i in range(a):
    m = eval(input())
    quotient = m//12  # 商
    remainder = m % 12  # 余数
    if remainder==0:
      remainder=12
      quotient-=1
    m_value=test_dict[remainder]
    m_correspond = quotient*12+13-remainder
    print(m_correspond, m_value)

print(1)
