import os
products = []
if os.path.isfile('products.csv') :
	print('讀取中...')
	with open('products.csv', 'r', encoding='utf-8') as f :
		for line in f:
			if '商品,價格' in line :
				continue
			s = line.strip().split(',')
			name = s[0]
			price = s[1]
			products.append([name,price])
	print(products)	
else :
	print('檔案建立中')
while True : 
	 name = input('請輸入商品名: ')
	 if name == 'q' :
	 	break
	 price = input('請輸入價錢: ')
	 p = []
	 p.append(name)
	 p.append(price)
	 products.append(p)

for pp in products :
	print(pp[0], '價錢為', pp[1])

with open('products.csv', 'w', encoding='utf-8') as f :
	f.write('商品,價格\n')
	for pp in products :
		f.write(pp[0]+','+pp[1]+'\n')

