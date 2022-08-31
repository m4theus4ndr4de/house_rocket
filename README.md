<img src="real_state_market.jpg" alt="logo" style="zoom:100%;" />

<h1>House Rocket</h1>

    <p>This is a fictional project for studying purposes. The company, business context and the insights are not real. 
        The dataset used in this project is from Kaggle and it is available <a href="https://www.kaggle.com/datasets/harlfoxem/housesalesprediction" target="_blank">there</a>.</p>

<h2>1. Description of the Business Problem</h2>

    <p>The House Rocket is a real state company. They work buying houses for a good price and selling selling them later after some time. 
        The company has a dataset that contains information about a lot of houses available to be bought. 
        The data scientist from House Rocket should help the CEO answering two questions and creating two tool to help understanding the dataset</p>

    <h3>The questions to be answered:</h3>
        <p>Which houses should the House Rocket CEO buy and at what price?
            The source code can be found <a href="https://github.com/m4theus4ndr4de/house_rocket/blob/main/house_rocket_app.py" target="_blank">here</a>
             and the dashboard is available <a href="https://house-rocket-app-ma.herokuapp.com/" target="_blank">here</a>.
        </p>
        <p>When is the best time to sell them and what would be the selling price?</p>

    <h3>The tools to be created:</h3>
        <p>An interactive dashboard in which it is possible to filter the data according to the CEO requirements and explore more about it.</p>
        <p>Crate a few insights about the dataset telling if they are true or false.</p>

<h2>2. Dataset Attributes</h2>
    <p>Information about the atrributes can be found <a href="https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885" target="_blank">here</a>.</p>


    <table style="width:100%">
        <tr><th>Attribute</th><th>Description</th></tr>
        <tr><td>id</td><td>Unique ID for each home sold</td></tr>
        <tr><td>date</td><td>Date of the home sale</td></tr>
        <tr><td>price</td><td>Price of each home sold</td></tr>
        <tr><td>bedrooms</td><td>Number of bedrooms</td></tr>
        <tr><td>bathrooms</td><td>Number of bathrooms, where .5 accounts for a room with a toilet but no shower</td></tr>
        <tr><td>sqft_living</td><td>Square footage of the apartments interior living space</td></tr>
        <tr><td>sqft_lot</td><td>Square footage of the land space</td></tr>
        <tr><td>floors</td><td>Number of floors</td></tr>
        <tr><td>waterfront</td><td>A dummy variable for whether the apartment was overlooking the waterfront or not</td></tr>
        <tr><td>view</td><td>An index from 0 to 4 of how good the view of the property was</td></tr>
        <tr><td>condition</td><td>An index from 1 to 5 on the condition of the apartment</td></tr>
        <tr><td>grade</td><td>An index from 1 to 13, where 1-3 falls short of building construction and design, 
                                                           7 has an average level of construction and design, and 
                                                           11-13 have a high quality level of construction and design</td></tr>
        <tr><td>sqft_above</td><td>The square footage of the interior housing space that is above ground level</td></tr>
        <tr><td>sqft_basement</td><td>The square footage of the interior housing space that is below ground level</td></tr>
        <tr><td>yr_built</td><td>The year the house was initially built</td></tr>
        <tr><td>yr_renovated</td><td>The year of the house's last renovation</td></tr>
        <tr><td>zipcode</td><td>What zipcode area the house is in</td></tr>
        <tr><td>lat</td><td>Lattitude of the house</td></tr>
        <tr><td>long</td><td>Longitude of the house</td></tr>
        <tr><td>sqft_living15</td><td>The square footage of interior housing living space for the nearest 15 neighbors</td></tr>
        <tr><td>sqft_lot15</td><td>The square footage of the land lots of the nearest 15 neighbors</td></tr>
      </table>
<!--
# 3. Premissas do Negócio

Quais premissas foram adotadas para este projeto:

- As seguintes premissas foram consideradas para esse projeto:
- Os valores iguais a zero em **yr_renovated** são casas que nunca foram reformadas.
- O valor igual a 33 na coluna **bathroom** foi considerada um erro e por isso foi delatada das análises
- A coluna **price** significa o preço que a casa foi / será comprada pela empresa House Rocket
- Valores duplicados em ID foram removidos e considerados somente a compra mais recente
- A localidade e a condição do imóvel foram características decisivas na compra ou não do imóvel
- A estação do ano foi a característica decisiva para a época da venda do imóvel



# 4. Estratégia de solução

Quais foram as etapas para solucionar o problema de negócio:

1. Coleta de dados via Kaggle
2. Entendimento de negócio
3. Tratamento de dados 

- ​	Tranformação de variaveis 
- ​	Limpeza 
- ​	Entendimento

4. Exploração de dados

[link para app no Heroku](https://house-rocket-project.herokuapp.com/)


5. Responder problemas do negócio

6. Resultados para o negócio

7. Conclusão

# 5. Top Insights

Insights mais relevantes para o projeto:

Imóveis renovados recentemente são 35% mais caros

**Falso**: Imóveis antigos e atuais possuem uma faixa de preço equivalente.

Imóveis em más condições, mas com uma boa vista são 10% mais caros.

**Falso**: Imóveis em más condições e com vista ruim são mais caros.

Crescimento do preço mês após mês em 2014 é de 10%.

**Falso**: O preço dos imóveis são mais caros entre o mês 3 e 6.



# 6. Tradução para o negócio

O as análises das hipóteses dizem sobre o negócio

| Hipótese                                                     | Resultado  | Tradução para negócio                                        |
| ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| **H1** -Imóveis com vista para a água são em média 30% mais caros | Verdadeira | Investir em imóveis com vista para água                      |
| **H2** - Imóveis com data de construção menor que 1955 são em média 50% mais baratos | Falsa      | Investir em imóveis independente da data de construção       |
| **H3** - Imóveis sem porão com maior área total são 40% mais caros | Verdadeira | Investir em imóveis sem porão                                |
| **H4** - Imóveis que nunca foram reformados são em média 20% mais baratos | Verdadeira | Investir em imóveis não reformados e reformá-los para venda  |
| **H5** - Imóveis em más condições, mas com boa vista são 10% mais caros | Falsa      | Não investir em imóveis em más condições                     |
| **H6** - Imóveis antigos e não renovados são 40% mais baratos | Verdadeira | Investir em imóveis antigos e não renovados e reformalos para venda |
| **H7** - Imóveis com mais banheiros são em média 5% mais caros | Falsa      | Investir em imóveis de 3-5 banheiros                         |
| **H8** - Imóveis renovados recentemente são 35% mais caros   | Falsa      | Investir em imóveis independente da reforma                  |
| **H9** - O crescimento do preço dos imóveis mês após mês no ano de 2014 é de 10% | Falsa      | Investir em imóveis nos meses de menor custo                 |
| **H10** - Imóveis com 3 banheiros tem um crescimento mês após mês de 15% | Falsa      | Investir em imóveis nos meses de menor custo                 |

O valor total de lucro (lucro = preço de compra - preço de venda) dos imóveis é de: **22.623.548,20**



# 7. Conclusão

O objetivo final desse projeto era responder a duas questões principais:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

Os objetivos foram alcançados.  Os imóveis foram agrupados por região (zipcode). Considerando o preço do imóvel e a condição (1 - 5)  foi calculado a mediana do preço. Imóveis abaixo do preço da mediana e com melhores condições foram sugeridos para compra (Total de 151 imóveis). Os imóveis aptos para compra foram agrupados pela localidade e a estação do ano. A mediana foi calculada e imóveis com preço abaixo da mediana teve um acréscimo de 10% em seu valor, enquanto imóveis com preço acima da mediana teve um acréscimo de 30% acima do seu valor.  O melhor momento da venda dos imóveis é na primavera, uma vez que o preço é maior nessa época. 

Como próximo passo, seria interessante a análise de quais apartamentos deveriam sofrer reformas, uma vez que imóveis antigos e não reformados são mais baratos, enquanto imóveis renovados recentemente são mais caros.  Também é de interesse prever a valorização do imóvel, pois pode permitir reter a venda da habitação até esta estar mais valorizada no mercado. 
//-->
