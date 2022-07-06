data = []
count = 0
with open ('reviews.txt','r') as f :
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 :
			print(len(data))
print('檔案讀取完了, 總共有', len(data),'筆資料')

sum_len = 0 

for d in data :
	sum_len = sum_len + len(d)
print('留言的平均長度', sum_len/len(data))

new = []

for d in data:
	if len(d)< 100:
		new.append(d)

print('一共有',len(new),'筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print ('一共有',len(good) , '留言提到幾筆')
print(good[0])

	

#文字計數
data = []
count = 0
with open ('reviews.txt','r') as f :
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 :
			print(len(data))
print('檔案讀取完了, 總共有', len(data),'筆資料')

print(data[0])

wc = {} #word_count 

for d in data: #ｄ是100萬留言的每一個清單
	words = d.split (' ')#將每個分成字串
	for word in words :#讀取每一個字串的字
		if word in wc :
			wc[word] +=1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
 	word = input('請問你想查什麼字:')
 	if word == 'q':
 		break
 	if word in wc:
 		print(word, '出現過幾次:',wc[word])
 	else:
 		print('這字查詢不到')