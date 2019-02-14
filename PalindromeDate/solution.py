# Complete the find_palindromes function below.
def find_palindromes(year):
    def valid_palindrome_date(date, yy, length=8):
        if length == 8:
            mm = int(date[:2])
            dd = int(date[2:4])
        elif length == 7:
            mm = int(date[0])
            dd = int(date[1:3])
        else:
            exit('wrong length of date, either 7 or 8')
        if 1 <= mm <= 12 and 1 <= dd <= days_in_month(yy, mm):
            return True
        else:
            return False

    def is_leapyear(yy):
        return (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0 and yy % 3200 != 0)

    def days_in_month(yy, mm):
        if mm in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        if mm in {4, 6, 9, 11}:
            return 30
        if mm == 2:
            return 29 if is_leapyear(yy) else 28

    ret = 0

    def f7(x): return str(x)[::-1][:3] + str(x)

    def f8(x): return str(x)[::-1] + str(x)
    for y in range(year//100*100, (year//100+1)*100):
        if valid_palindrome_date(f7(y), y, 7):
            ret += 1
        if valid_palindrome_date(f8(y), y, 8):
            ret += 1
    return ret
