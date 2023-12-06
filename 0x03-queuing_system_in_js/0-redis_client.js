/**
 * Makes a connection to the Redis Server and displays messaages on
 * error and connect events
 */
import { createClient } from 'redis';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));