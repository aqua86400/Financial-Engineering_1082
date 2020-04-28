# 作業四：使用 B-S formula 計算選擇權價格

## 學習歷程

這次作業與上一次類似，都是要計算選擇權定價，與上次使用**BOPM**不同的是，這次使用了**Black-Scholes formula**來計算。

由於有固定的解析解當作公式，所以這次作業相對簡單，就是把公式寫成程式碼來計算。

輸入的參數主要有：S(**股價**)、X(**履約價**)、r(**無風險利率**)、sigma(**波動度**)、tau(**持有期間**)

次要有：div(股利發放)，在代入公式計算時，需要將股價(S)-股利折現值，再帶入公式計算。


而輸出有：**買權**及**賣權**價格。



## 程式流程圖
以下為[`Hw4.ipynb`](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw4/Hw4.ipynb)的流程圖：<br />

![hw4_flowchart](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw4/hw4_flowchart.png)
