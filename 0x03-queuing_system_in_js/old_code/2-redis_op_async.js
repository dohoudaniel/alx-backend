import { print, createClient } from 'redis';

import { promisify } from 'util';

const cli = createClient();

cli.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

cli.on('connect', () => console.log('Redis client connected to the server'));

const set = promisify(cli.set).bind(cli);
const get = promisify(cli.get).bind(cli);

async function setNewSchool(schoolName, value) {
	const val = await set(schoolName, value);
	console.log(`Reply: ${val}`);
}
async function displaySchoolValue(schoolName) {
	const val = await get(schoolName);
	console.log(val);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

