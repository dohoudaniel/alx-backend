import { print, createClient } from 'redis';

const cli = createClient();

cli.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

cli.on('connect', () => console.log('Redis client connected to the server'));

const data = {
	'Portland': 50, 'Seattle': 80, 'New York': 20,
	'Bogota': 20, 'Cali': 40, 'Paris': 2
}
for (const key in data) {
	cli.hset("HolbertonSchools", key, data[key], print);
}
cli.hgetall('HolbertonSchools', (error, value) => {
	if (error) {
		console.error(error);
	} else {
		console.log(value);
	}
});
