# 債券報價中的 YTM、Spot Rate、Forward Rate

## 學習歷程
一、 這次的作業對非財務相關的我挺困難的......除了看老師的投影片([1](https://docs.google.com/presentation/d/e/2PACX-1vT0uWPmTezKky8GLD_fkmfuJjXCLRuVkQWNuHmeogeMpY21cbwQurn7CsaVWRZDSZcZTvXjjpvY4lwE/pub?start=false&loop=false&delayms=3000&slide=id.p)、[2](https://docs.google.com/presentation/d/e/2PACX-1vSVL0BfN9ddvwhYgAX3PDQzzy864wCQflg9G1-1J7g-t7Rw8bXg1iicVBmgN0HSarVZSFs35Pxv1gA3/pub?start=false&loop=false&delayms=3000&slide=id.p))和相關連結，還有去旁聽一門課([財務演算法](https://github.com/andydong1209/NTU_FinAlgo))，剛好也有提到YTM、Spot Rate與Forward Rate，不過還不是很了解，因此還有求助一位朋友也是修課同學。

二、到期收益率(Yield to Maturity,YTM)：

一項債券的內部報酬率(Internal Rate of Return)，如果 PV是現值，CF_i 是第i期的現金流，n是總期數，則即期利率y有以下方程式：
<img src="https://render.githubusercontent.com/render/math?math=PV = \sum_{i=1}^n\dfrac{CF_i}{(1 %2By)^i}">

我使用了Python的`sympy`套件來求y，由於他會把所有的的解包括實數、虛數算出來，而這邊的YTM是要正的實數，所以我有另外建一個判別一個數字是正實數與否的函數。

二、即期利率(Spot Rate,SR)：

零息債券(Zero-Coupon Bond)的到期收益率就是它的即期利率。
如果今天是一個有配息的債券，我們可以把它切割成總期數個數(n)個的零息債券來看，然後去算最後一期的折現率也就是這邊的SR(n)，所以要先在市場上找到其他年期是小於總年期的零息債的YTM當作前面的SR(i)才能計算。

三、遠期利率

