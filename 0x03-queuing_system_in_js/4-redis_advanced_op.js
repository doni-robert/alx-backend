/**
 * Redis server that stores a hash value
 */
import { createClient, print } from 'redis';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const hashKey = 'HolbertonSchools';
const fieldValues = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
};

for (const field in fieldValues) {
    client.hset(hashKey, field, fieldValues[field], print);
}

client.hgetall(hashKey, (err, reply) => {
    if (err) {
        console.error(err);
    }
    console.log(reply)
});