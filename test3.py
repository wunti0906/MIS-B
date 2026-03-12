def life(y):
    # 第一步：將所有數字加總
    # 例如 19951231 -> 1+9+9+5+1+2+3+1 = 31
    total = sum(int(digit) for digit in y)
    
    # 第二步：如果結果大於 9，就繼續把位數相加（直到剩下個位數）
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    
    print(f"您的生命靈數為：{total}")

x = input("請輸入西元生日(8位數，如19951231): ")

# 檢查輸入長度是否正確，避免出錯
if len(x) == 8 and x.isdigit():
    life(x)
else:
    print("輸入格式錯誤，請輸入8位數字。")