# Simulate_hash_length_extension_attack

針對MD5模擬hash_length_extension_attack

## coding大綱:
將引用的python2 MD5模板 自己手動改成 python3

引用MD5之後 設計自己的模擬python3程式

## 解說
Hash length extension attack:
理論:
已知:1.MD5(secret+message) 2.secret+message長度
可推出=>MD5(secret+message+padding+append message)

# 理想題目設計:
給你一個md5py.py檔案、hash(secret+message1)、md5的block size、和message2(append)，再給出一個數位簽章hash(secret+message1+padding+message2)，請你偽造這個數位簽章，並且算出你第一次所修改的鏈接變量和。
send格式為” 你的偽造簽章,鏈接變量和”。server會先比對這個數位簽章，若相同再比對鏈接變量和，若鏈接變量和也相同便會噴出flag。

# 原始程式碼:
![image](https://github.com/Dennis1529/Simulate_hash_length_extension_attack/blob/master/code1.PNG)
![image](https://github.com/Dennis1529/Simulate_hash_length_extension_attack/blob/master/code2.PNG)

# 原始程式碼解釋:
md5py太長我就不貼了，由於我沒有架server所以我直接把資料和答案都寫死在同一個程式內，寫出pad然後將原始資料Padding後+上append，生成數位簽章，修改鏈接變量，這裡我是上網抓下md5 python2的code，然後自己去刻，刻成python3的code(這也是我整個花最久時間的地方)，接下來由於我把那個bytelistToLong寫在md5py內了所以我直接呼叫那個function改鏈接變量，做update的動作就能偽造出數位簽章了。

# 解題:
整個題目懂了之後其實超級簡單，因為我也把那個bytelistToLong附加在md5py內了，如果把其他我自己寫死的東西拿掉只有下面5行而已。
![image](https://github.com/Dennis1529/Simulate_hash_length_extension_attack/blob/master/code3.PNG)
這樣就能實現出hash length extension attack了。 

