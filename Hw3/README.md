# 作業三：二項式定價模型法 (Binomial Options Pricing Model)

老師給的題目為以下敘述：

A non-dividend-paying stock is selling for $160.

u = 1.5; d = 0.5; r = 18.232% per period

Hence p = (R − d)/(u − d) = 0.7.

Consider a European call on this stock with X = 150 and n = 3.

What is the call/put value? Or what is the PV of the expected payoff at expiration? (by backward induction).

---
我們這個程式主要輸入的資料有：
* 股票(標的)價格 S
* 履約價(執行價格) X
* 到期期數 n
* 無風險利率 r
* 上升因子 u 、 下降因子 d

中間的過程使用 BOPM，由最後期選擇權的價格依序往前推，以求得現今選擇權價格的方式(backward induction)。

而輸出是現今該股票(標的)的選擇權價格，包括買權與賣權。

## 學習歷程
[選擇權的二項式定價法](https://wiki.mbalib.com/zh-tw/%E4%BA%8C%E9%A1%B9%E6%9C%9F%E6%9D%83%E5%AE%9A%E4%BB%B7%E6%A8%A1%E5%9E%8B) ([BOPM](https://en.wikipedia.org/wiki/Binomial_options_pricing_model), Binomial Options Pricing Model) 與 [B-S期權定價模型](https://wiki.mbalib.com/zh-tw/Black-Scholes%E6%9C%9F%E6%9D%83%E5%AE%9A%E4%BB%B7%E6%A8%A1%E5%9E%8B)([Black-Scholes Option Pricing Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)） 同為期權的訂價模型，只是前者的推導過程較後者簡單許多，而且前者其實是後者的近似，BOPM 用的是離散時間，B-S Model 是用連續的，故 BOPM 取極限會得到 B-S Model，他們之間還有許多關係，可參考[呂育道教授-BOPM and Black-Scholes Model](https://www.csie.ntu.edu.tw/~lyuu/finance1/2010/20100324.pdf) <br />

關於本次作業，最重要的部分就是 BOPM 的結構搭配 backward induction 來算出現在價格，


## 程式流程圖
以下為[`Hw3.ipynb`](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw3/Hw3.ipynb)的流程圖：<br />

![hw3_flowchart](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw3/hw3_flowchart.png)
