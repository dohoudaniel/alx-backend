import { createClient } from 'redis';
import express from 'express';
import { promisify } from 'redis';

const listProducts = [
 {'Id': 1, 'name': 'Suitcase 250', 'price': 50, 'stock': 4},
 {'Id': 2, 'name': 'Suitcase 450', 'price': 100, 'stock': 10}
 {'Id': 3, 'name': 'Suitcase 650', 'price': 350, 'stock': 2}
	B
 {'Id': 4, 'name': 'Suitcase 1050', 'price': 550, 'stock': 5}
]
const cli = createClient();
const set = promisify(cli.set).bind(cli);
const get = promisify(cli.get).bind(cli);
const convert = (obj) => {
	return {
	 'itemId': obj.Id,
	 'itemName': obj.name,
	 'price': obj.price,
	 'initialAvailableQuantity': obj.stock
	}
}

function getItemById(id){
	for (const pro of listProducts) {
		if (pro.Id === id) {
			return convert(pro);
		}
	}
}

function reserveStockById(itemId, stock) {
  return set(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId) {
  const stock = await get(`item.${itemId}`);
  if (stock === null) {
	  return 0;
  }
  return stock;
}

const app = express();
const PORT = 1245;

app.get('/list_products', (_, res) => {
  res.json(listProducts.map(convert));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length > 0) {
    const stock = await getCurrentReservedStockById(itemId);
    item.currentQuantity = item.initialAvailableQuantity - stock;
    return res.json(item);
  }
  return res.json({ status: 'Product not found' });
});


app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length === 0) {
    return res.json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  if (stock >= item.initialAvailableQuantity) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, Number(stock) + 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

function clearRedisStock() {
  return Promise.all(listProducts.map((item) => SET(`item.${item.Id}`, 0)));
}

app.listen(1245, async () => {
  await clearRedisStock();
  console.log('API available on localhost via port 1245');
});
