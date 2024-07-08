import scrapy
import pytz
from typing import Any
from datetime import datetime
from scrapy.http import Response
class PCBRGLP(scrapy.Spider):
    name = 'pcbrglp'
    COMBUSTIVEL = str('glp')
    custom_settings = {
        'FEEDS' :{
    'glp.json':{
        'format':'json',
        'encoding':'utf8',
        'overwrite':True,
        }
    }
    }
    start_urls = [
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/br',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/am',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/ce',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/es',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/ma',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/mg',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/sp',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/rj',
        f'https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/{COMBUSTIVEL}/rs',
        
        ]
    UFS = ['br','am','ce','es','ma','mg','sp','rj','rs']
    TIMEZONE = pytz.timezone('America/Sao_Paulo')
    CURRENT_DATE =datetime.now(tz=TIMEZONE).isoformat()
    def parse(self, response: Response, **kwargs: Any) -> Any:
        for i in range(len(self.start_urls)):
            if(self.start_urls[i] == response.url):
                uf = self.UFS[i]
                preco_medio_final = response.xpath('//*[@id="ultimoslide"]/div[1]/p/text()').get()
                distribuicao_revenda = response.xpath('///*[@id="quadrobrancofinal"]/div/div[1]/div/p[3]/span/text()').get()
                icms = response.xpath('//*[@id="quadrobrancofinal"]/div/div[2]/div/p[3]/span/text()').get()
                impostos_federais = response.xpath('//*[@id="quadrobrancofinal"]/div/div[3]/div/p[3]/span/text()').get()
                parcela_petrobras = response.xpath('//*[@id="quadrobrancofinal"]/div/div[4]/div/p[3]/span/text()').get()
                periodo_coleta = response.xpath('//*[@id="ultimoslide"]/div[4]/div[2]/span[2]/text()').get()
                
            
                yield {
                        'uf':uf,
                        'combustivel':self.COMBUSTIVEL,
                        'porcentagens':{
                            'preco_medio_final':self.float_parse(preco_medio_final),
                            'distribuicao_revenda':self.float_parse(distribuicao_revenda),
                            'icms':self.float_parse(icms),
    
                            'impostos_federais':self.float_parse(impostos_federais),
                            'parcela_petrobras':self.float_parse(parcela_petrobras),
                        },
                        'data':self.CURRENT_DATE,
                        'periodo_coleta':periodo_coleta,
                        'url':response.url
                    }

            

    def float_parse(self,value=str):
        return float(value.replace(',','.'))

