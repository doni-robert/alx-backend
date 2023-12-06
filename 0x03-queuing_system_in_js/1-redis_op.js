/**
 * Makes a connection to the Redis Server and displays messaages on
 * error and connect events
 */
import { createClient } from 'redis';
import { print } from 'redis';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// sets i Redis the value for the key 'schoolName'
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

// logs the value for the key passed as argument
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(err);
        }
        console.log(reply)
    });
    
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');