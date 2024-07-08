# Preços médio de combustíveis

## _Informações de coleta dos dados obtidos acessando <https://precos.petrobras.com.br/>_

**SHELL**
~~~ shell
$: scrapy crawl pcbrg #GASOLINA
$: scrapy crawl pcbrd #DIESEL
$: scrapy crawl pcbrglp #GÁS DE COZINHA (GLP)
~~~ 

~~~ shell
$: scrapy crawl pcbrg
~~~
**_retorno_**
~~~ json
[
    {
        "uf": "br",
        "combustivel":
        "gasolina",
        "porcentagens":
        {
            "preco_medio_final": 5.86, "distribuicao_revenda": 17.2, "custo_etanol_anidro": 12.6, "imposto_estadual": 23.4, "impostos_federais": 11.8, "parcela_petrobras": 35.0
        },
        "data": "2024-07-08T19:13:49.697322-03:00",
        "periodo_coleta": "23/06/2024 a 29/06/2024",
        "url": "https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/gasolina/br"
    },

]
~~~


