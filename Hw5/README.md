# 作業五：使用 Hull-White model 計算選擇權價格

## 學習歷程

這次作業與前兩次類似，都是要計算選擇權定價(先前使用了 BOPM 與 B-S model)。

>老師給的題目為：<br />
HW5 Option Pricing with Hull White Model <br />
1.透過 Monte Carlo method，對 Hull White Model 模擬 Short Rate。<br />
2.將 Short Rate 帶入 Geometric Brownian Motion，r 換成 r(t) 模擬股價。<br />
3.自訂選擇權履約價，對每一條 path 計算出到期日時的 PayOff，
並對所有 Path 的 PayOff 進行期望值計算，並折現回 t=0 的時間點以計算出 Call Price & Put Price。

一、[Hull-White model](https://zh.wikipedia.org/wiki/%E8%B5%AB%E7%88%BE%E6%87%B7%E7%89%B9%E6%A8%A1%E5%9E%8B) <br />
為一利率模型，此模型假設短期利率服從隨機微分方程式：
<img src="https://render.githubusercontent.com/render/math?math=dr = (\theta(t)-ar)dt%2B\sigma dW"> <br />
其中有：
<img src="https://render.githubusercontent.com/render/math?math=\theta(t) = \dfrac{\partial f(0,t)}{\partial t}%2B af(0,t)%2B\dfrac{\sigma^2}{2a}(1-e^{-2at})">

關於 Hull-White model 的使用，老師建議我們可以使`QuantLib`套件，裡面有寫好的財務模型函式，並給了我們一個相關參考網站：
[Hull White Term Structure Simulations with QuantLib Python](http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html)


二、[Geometric Brownian Motion(GBM)](https://zh.wikipedia.org/wiki/%E5%87%A0%E4%BD%95%E5%B8%83%E6%9C%97%E8%BF%90%E5%8A%A8)<br />
是一種連續隨機過程，也叫做指數布朗運動，其隨機變量的對數遵循布朗運動，而此隨機過程會滿足：
<img src="https://render.githubusercontent.com/render/math?math=dS_t = \mu S_tdt%2B\sigma S_tdW_t"> <br />
其中<img src="https://render.githubusercontent.com/render/math?math=W_{t}"> 是一個維納過程(Wiener process), 或是布朗運動，而 <img src="https://render.githubusercontent.com/render/math?math=\mu"> ('百分比drift') 和 <img src="https://render.githubusercontent.com/render/math?math=\sigma">  ('百分比volatility')則是常量。

關於GBM，老師有提供一個[範例程式](https://colab.research.google.com/drive/1LL_m1UO_U2oHDMQhBDPjhUBANDpVhev7)當作模擬參考。



## 程式流程圖
以下為[`Hw5.ipynb`](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw5/Hw5.ipynb)的流程圖：<br />

![HW5_flowchart](https://github.com/aqua86400/Financial_Engineering/blob/master/Hw5/Hw5_flowchart.png)
