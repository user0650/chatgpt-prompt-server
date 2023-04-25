# chatgpt-prompt-server

### env
```
python 3.9.13
chrome
```

### install
```
pip install -r requirements.txt
```

### run
```
python server.py
```

### test
```
curl http://localhost:5000/
```
now you will see:
```
Hello, World!
```

### api
```
1.从详情页提取商品信息，生成prompt，总结该商品的优缺点
http://localhost:5000/page
METHOD -> POST/GET
DATA -> {"url", "a page url"}
```

```
2.根据关键词搜索，并选取前10个结果提取详细信息，生成prompt，总结最值得推荐的商品
http://localhost:5000/search
METHOD -> POST/GET
DATA -> {"keyword", "a search keyword"}
```

```
3.从详情页提取商品信息，生成prompt，生成关于这个商品的直播文案
http://localhost:5000/generate
METHOD -> POST/GET
DATA -> {"url", "a page url"}
```

### todo
```
What do you want? Tell me.
```
