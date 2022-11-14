rent = int(input())

statuette = rent - ( rent * 0.30)
catering = statuette - (statuette * 0.15)
music = catering / 2

total_sum = rent + statuette + catering + music
print(f"{total_sum:.2f}")
