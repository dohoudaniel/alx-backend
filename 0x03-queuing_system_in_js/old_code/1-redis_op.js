import { print, createClient } from 'redis';

const cli = createClient();

cli.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

cli.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
	cli.set(schoolName, value, print);
}
function displaySchoolValue(schoolName) {
	cli.get(schoolName, (error, value) => {
		if (error) {
			console.error(error);
		} else {
			console.log(value);
		}
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

