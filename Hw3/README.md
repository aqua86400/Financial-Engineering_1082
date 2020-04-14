# 作業三：選擇權的二項式定價法 (Binomial Options Pricing Model)

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

輸出是現今該股票(標的)的選擇權價格，包括買權與賣權。

## 學習歷程

## 程式流程圖
以下為[`Hw3.ipynb`](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw3/Hw3.ipynb)的流程圖：<br />

![hw3_flowchart](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw3/hw3_flowchart.png)
