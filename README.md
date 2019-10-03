# Job-recommendation-project
此為作品-工作對對碰 工作推薦部分
因word2vec model檔案太大 所以沒有上傳
訓練用的語料庫為維基文檔 zhwiki-20190501-pages-articles.xml.bz2

# Word2Vec model訓練
在下維基文檔後 依序執行

1.抓取維基文章.py

2.簡體轉繁體.py

3.文章斷詞斷字(含去標點,自傳,維基文章皆適用)py

4.word2vec模型訓練.py

即產生Word2Vec將model 3個檔案丟進'''smart_recommend'''資料夾即完成訓練步驟

# 網頁呈現

## installation

### frontend
先在`root`根目錄，有出現`package.json`檔案的地方安裝依賴檔`node_modules`

安裝前端套件
``` javascript
npm install
```
### backend
再到`server`資料夾，有出現`package.json`檔案的地方安裝依賴檔`node_modules`

安裝後端套件
``` javascript
npm install
```

## env 
環境設定檔也要用好,要轉換env檔名,或者建立`.env`檔案

### frontend
在根目錄轉換成`.env`的檔名
``` javascript
cp .env.example .env
```

### backend
在`server`資料夾轉換成`.env`的檔名
``` javascript
cp .env.example .env
```

## usage 

這個需要架起`前端server`和`後端server`

### frontend
在根目錄啟動app
``` javascript
npm start
```

### backend
在`server`資料夾啟動後端app服務
``` javascript
npm run dev
```
### 資料夾移動
將'''smart_recommend'''資料夾放入'''server'''資料夾中

之後在網址連結打[localhost:8080](http://localhost:8080)便能看到內容

