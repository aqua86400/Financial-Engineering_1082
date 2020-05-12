# 作業五：使用 Hull-White model 模擬短期利率，並代入 GBM 模擬股價再計算選擇權價格

## 學習歷程

這次作業與前兩次類似，都是要計算選擇權定價(先前使用了 BOPM 與 B-S model)。

>老師給的題目為：<br />
HW5 Option Pricing with Hull White Model <br />
1.透過 Monte Carlo method，對 Hull White Model 模擬 Short Rate。<br />
2.將 Short Rate 帶入 Geometric Brownian Motion，r 換成 r(t) 模擬股價。<br />
3.自訂選擇權履約價，對每一條 path 計算出到期日時的 PayOff，
並對所有 Path 的 PayOff 進行期望值計算，並折現回 t=0 的時間點以計算出 Call Price & Put Price。

關於 Hull-White model 的使用，老師建議我們可以使`QuantLib`套件，裡面有寫好的財務模型函式，並給了我們一個相關參考網站：
[Hull White Term Structure Simulations with QuantLib Python](http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html)




而輸出有：**買權**及**賣權**價格。



## 程式流程圖
以下為[`Hw5.ipynb`](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw5/Hw5.ipynb)的流程圖：<br />

![HW5_flowchart](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw5/Hw5_flowchart.png)
