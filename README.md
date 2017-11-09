# 找程序外包的工具
聚合外包平台的工具。

## 运行
1. 安装依赖:`pip install -i https://mirrors.aliyun.com/pypi/simple/ Scrapy` 用的阿里的镜像安装。注1
1. `cd outsource`
1. 爬数据: `scrapy crawl waibo -o res.json -s FEED_EXPORT_ENCODING=utf-8`
1. 打开 res.json 查看结果。

## 数据格式
* 标题
* 类型: 网站，后台，APP，小程序，其他
* 价格
* 状态
* 平台：码市,开源中国众包 等
* 简单介绍
* 详情地址

## 资源
* [码市](https://mart.coding.net/) coding.net
* [开源中国众包](https://zb.oschina.net/projects) oschina
* [CSTO 外包平台](http://www.csto.com/project/list) CSDN
* [码客帮](https://www.make8.com/market)
* [外包通缉令](http://waibao.io/projects) [干货集中营](http://gank.io/)

## 待探究
* [快码](https://www.kuai.ma/)
* [齿轮](https://chilunyc.com/) 一体化产品解决方案提供商。

## 帮助
* `scrapy shell "地址"` 交互式的看页面结构

## 注
1. 如果报 [Command “python setup.py egg_info” failed with error code 1 in ''](https://stackoverflow.com/questions/46719114/command-python-setup-py-egg-info-failed-with-error-code-1-in) 可以通过安装 `pip3 install incremental` 来解决。