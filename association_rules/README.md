### (shell) pyspark --driver-memory 10g


### lift
| | antecedent                                    |    consequent                               |     confidence  | lift|
|:------------  |:------------|:------------|:------------|:------------|
|0|            Dairy Free Greek Yogurt Strawberry |         Dairy Free Greek Yogurt Blueberry   |  0.492777 | 2593.758705|
|1|            Dairy Free Greek Yogurt Blueberry  |     Dairy Free Greek Yogurt Strawberry      |  0.528399 | 2593.758705|
|2|         Grassfed Whole Milk Strawberry Yogurt |Organic Strawberry Grassfed Whole Milk Yogurt|  0.495298 | 2127.363901|
|3| Organic Strawberry Grassfed Whole Milk Yogurt |       Grassfed Whole Milk Strawberry Yogurt |  0.443820 | 2127.363901|
|4|      Organic Cashew Nondairy Blueberry Yogurt |  Organic Nondairy Strawberry Cashew Yogurt  |  0.616129 | 2061.488198|


### confidence
$$
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mi>c</mi>
  <mi>o</mi>
  <mi>n</mi>
  <mi>f</mi>
  <mi>i</mi>
  <mi>d</mi>
  <mi>e</mi>
  <mi>n</mi>
  <mi>c</mi>
  <mi>e</mi>
  <mo stretchy="false">(</mo>
  <mi>A</mi>
  <mo stretchy="false">&#x2192;<!-- → --></mo>
  <mi>B</mi>
  <mo stretchy="false">)</mo>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <mi>P</mi>
      <mo stretchy="false">(</mo>
      <mi>A</mi>
      <mo>,</mo>
      <mi>B</mi>
      <mo stretchy="false">)</mo>
    </mrow>
    <mrow>
      <mi>P</mi>
      <mo stretchy="false">(</mo>
      <mi>A</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </mfrac>
</math>
$$

| |  antecedent                                                       |    consequent                                        | confidence |   lift     |
|:------------  |:------------|:------------|:------------|:------------|
|0| Oh My Yog! Organic Wild Quebec Blueberry Cream Top Yogurt & Fruit | oh My Yog! Pacific Coast Strawberry Trilayer Yogurt  |   0.661383 | 707.942415 |
|1|                Grain Free Turkey Canned Cat Food                  | Grain Free Chicken Formula Cat Food                  |   0.645418 |1087.476896 |
|2|       Organic Cottage Cheese Blueberry Acai Chia                  | Organic Strawberry Grassfed Whole Milk Yogurt        |   0.616210 |1618.940833 |
|3|         Organic Cashew Nondairy Blueberry Yogurt                  | Organic Nondairy Strawberry Cashew Yogurt            |   0.616129 |2061.488198 |
|4|                Grain Free Turkey Canned Cat Food                  | Grain Free Turkey & Salmon Formula Cat Food          |   0.615538 |1208.210718 |

