/**
 * Makes a connection to the Redis Server and displays messaages on
 * error and connect events
 */
import { createClient, print } from 'redis';
import { promisify } from 'util'

// create a redis client
const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// sets a value for the key schoolName
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

// logs the value for the key passed as argument

const getAsync = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }   
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');