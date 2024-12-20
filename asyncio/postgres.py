import asyncpg
import asyncio
from random import sample

host='192.168.1.177'
port=5432
user='postgres'
database='products'
password='ZtC36wLn1P0Z7asQ'

import asyncpg
import asyncio
from typing import List, Tuple, Union
from random import sample
from random import randint, sample
 
def load_common_words() -> List[str]:
    with open('/Users/davidhunt/research/learning/asyncio/common_words.txt') as common_words:
        return common_words.readlines()
def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, ]]]:
    return [(words[index].replace('\n',''),) for index in sample(range(100), 100)]
 
def gen_products(common_words: List[str],
                 brand_id_start: int,
                 brand_id_end: int,
                 products_to_create: int) -> List[Tuple[str, int]]:
    products = []
    for _ in range(products_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products
 
 
def gen_skus(product_id_start: int,
             product_id_end: int,
             skus_to_create: int) -> List[Tuple[int, int, int]]:
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus
 
 
async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)
 
 

async def main():
    words = load_common_words()
    connection = await asyncpg.connect(host='192.168.1.177',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='ZtC36wLn1P0Z7asQ')
    product_tuples = gen_products(words,
                                  brand_id_start=105,
                                  brand_id_end=204,
                                  products_to_create=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
                                 product_tuples)
 
    sku_tuples = gen_skus(product_id_start=3,
                          product_id_end=1000,
                          skus_to_create=100000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
                                 sku_tuples)
 
    await connection.close()

asyncio.run(main())