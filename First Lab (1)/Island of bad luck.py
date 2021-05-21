# Алексей Головлев, группа БСБО-07-19

int_day = int(input())
int_month = int(input())
int_year = int(input())

int_year = int_year if (int_month - 2) > 0 else int_year - 1
int_month = int_month - 2 if (int_month - 2) > 0 else 12 - abs(int_month - 2)
c = int_year // 100
int_year = int_year % 100

print((int_day + ((13 * int_month - 1) // 5) + int_year + (int_year // 4 + c // 4 - 2 * c + 777)) % 7)
