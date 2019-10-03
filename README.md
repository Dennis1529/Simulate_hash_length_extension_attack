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

理想題目設計:
給你一個md5py.py檔案、hash(secret+message1)、md5的block size、和message2(append)，再給出一個數位簽章hash(secret+message1+padding+message2)，請你偽造這個數位簽章，並且算出你第一次所修改的鏈接變量和。
send格式為” 你的偽造簽章,鏈接變量和”。server會先比對這個數位簽章，若相同再比對鏈接變量和，若鏈接變量和也相同便會噴出flag。

原始程式碼:
![image](https://github.com/Dennis1529/Simulate_hash_length_extension_attack/blob/master/code1.PNG)

